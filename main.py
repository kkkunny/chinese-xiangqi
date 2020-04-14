# -*- coding: utf-8 -*-
from image import *
from move import *


class Main(object):
    """游戏主程序"""
    def __init__(self):
        """游戏初始化"""
        pg.init()  # pygame初始化
        pg.display.set_caption("中国象棋")  # 标题栏
        self.windows = pg.display.set_mode((WINDOWS_SIZE[0]+EDGE_DISTANCE*2, WINDOWS_SIZE[1]+EDGE_DISTANCE*2))  # 创建窗口
        self.image = Image(self.windows)  # 初始化图片处理对象
        self.player = True  # 玩家阵营
        self.start_game()  # 游戏初始化
        clock = pg.time.Clock()  # 游戏时钟
        self.round = 1  # 回合数
        while True:  # 游戏循环
            clock.tick(10)  # 锁帧60
            self.game()  # 正式游戏
            self.event()  # 调用用户交互
            pg.display.update()  # 刷新屏幕

    def start_game(self):
        """开始游戏"""
        # 建立棋盘每个位置的矩阵（中心点）
        pos_list = []
        for row in range(10):
            sed_pos_list = []
            for col in range(9):
                sed_pos_list.append((int((1 + row * 89) * SIZE_TIME), int((1 + col * 89) * SIZE_TIME)))
            pos_list.append(sed_pos_list)
        self.board_position = pd.DataFrame(pos_list)
        self.move_path = Move()  # 初始化获得可移动路径类
        # 初始棋盘
        self.fen = "车马象士将士象马车/9/1砲5砲1/卒1卒1卒1卒1卒/9/9/兵1兵1兵1兵1兵/1炮5炮1/9/車馬相仕帅仕相馬車 {} - - 0 1".format("红" if self.player else "黑")
        self.board, self.faction, self.round = make_board(self.fen)

        self.selected = ["", ()]  # 选中的棋子[棋子名, 位置[行, 列]]
        self.faction = True  # 阵营轮次 True:红棋 False:黑棋

    def game(self):
        """正式游戏"""
        # 将棋盘转变为FEN
        self.fen = make_fen(self.board, self.round, self.faction)
        self.cur_piece_poss = []  # 现有棋子的位置
        self.can_move = []  # 可移动坐标
        self.image.load_bg("./resources/bg.jpg", (0, 0))  # 背景
        self.image.load("./resources/棋盘.png", (EDGE_DISTANCE, EDGE_DISTANCE))  # 棋盘
        # 从棋盘中获得棋子信息
        for row in range(10):  # 行
            for col in range(9):  # 列
                if self.board.iloc[row, col]:  # 如果有棋子
                    self.display_piece(self.board.iloc[row, col], (row, col))  # 显示图片
                    self.cur_piece_poss.append((row, col))
        # 选中棋子的图片
        if self.selected[0]:
            self.image.load("./resources/selected.png", self.pos_to_position(self.selected[1]))
            self.get_move()  # 棋子移动
        # 判定输赢
        self.decide_win()

    def event(self):
        """交互"""
        event_list = pg.event.get()  # 获取事件
        for event in event_list:
            if event.type == pg.QUIT:  # 游戏退出事件
                self.quit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                # 选中棋子
                for pos in self.cur_piece_poss:  # 是否选中现有棋子
                    position = self.pos_to_position(pos)
                    if position[0] < mouse_pos[0] < position[0]+int(86*SIZE_TIME) and position[1] < mouse_pos[1] < position[1]+int(86*SIZE_TIME):
                        piece_faction = self.move_path.get_piece_faction(self.board.iloc[pos])
                        if (piece_faction == "红" and self.faction) or (piece_faction == "黑" and not self.faction):  # 阵营相同
                            self.selected = [self.board.iloc[pos], pos]
                if self.selected[0]:  # 有棋子被选中
                    if len(self.can_move) != 0:  # 能够移动
                        for pos in self.can_move:
                            position = self.pos_to_position(pos)
                            if position[0] < mouse_pos[0] < position[0]+int(86*SIZE_TIME) and position[1] < mouse_pos[1] < position[1]+int(86*SIZE_TIME):
                                self.move(self.selected, pos)  # 移动棋子
                                self.selected = ["", ()]  # 清空选中的棋子[棋子名, 位置[行, 列]]

    def get_move(self):
        """获得可移动棋子路径"""
        can_moves = self.move_path.get_path(self.selected, self.fen)
        for can_move in can_moves:
            self.image.load("./resources/selected.png", self.pos_to_position(can_move))
            self.can_move.append(can_move)

    def move(self, selected, pos):
        """移动棋子, selected:被选中的棋子, pos:位置"""
        self.board.iloc[selected[1]] = False  # 原始位置变为空
        self.board.iloc[pos] = selected[0]  # 移动位置变为棋子名
        if not self.faction & self.player:  # 轮次加1
            self.round += 1
        self.faction = not(self.faction)  # 轮到另一方阵营

    def pos_to_position(self, pos):
        """将矩阵点转换为像素点（左上角）, pos:矩阵点"""
        position = self.board_position.iloc[pos]
        position = (position[1]-int(43*SIZE_TIME)+EDGE_DISTANCE, position[0]-int(43*SIZE_TIME)+EDGE_DISTANCE)
        return position

    def game_win(self):
        """游戏胜利"""
        print("游戏胜利！！！！！")
        self.quit()

    def game_over(self):
        """游戏失败"""
        print("游戏失败！！！！！")
        self.quit()

    def quit(self):
        """游戏退出"""
        pg.quit()  # 退出pygame
        exit()

    def display_piece(self, name, pos):
        """在棋盘中显示棋子, name:棋子名, pos:位置"""
        for faction in PIECE_INFOS["image"]:
            for type in PIECE_INFOS["image"][faction]:
                if type == name:
                    self.image.load_piece(PIECE_INFOS["image"][faction][type], self.pos_to_position(pos))

    def decide_win(self):
        """判定输赢"""
        red_live = False  # 红方没有存活
        black_live = False  # 黑方没有存活
        for row in range(10):
            for col in range(9):
                if self.board.iloc[row, col]:
                    if self.board.iloc[row, col] == "帅":
                        red_live = True
                    elif self.board.iloc[row, col] == "将":
                        black_live = True
        if self.player:
            if red_live and not black_live:
                self.game_win()
            elif not red_live and black_live:
                self.game_over()
        else:
            if red_live and not black_live:
                self.game_over()
            elif not red_live and black_live:
                self.game_win()


if __name__ == '__main__':
    Main()