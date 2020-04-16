# -*- coding: utf-8 -*-
# 移动路径
from board import *
from constant import *


class Move(object):
    """获得移动路径"""
    def get_path(self, selected, fen):
        """获取可移动路径, selected:被选中的棋子, fen:棋盘FEN编码"""
        board, faction, round = make_board(fen)  # 获得棋盘, 当前轮到的阵营, 局数
        type, pos = selected
        can_moves = []
        if type in ("兵", "卒"):  # 兵
            if faction == "红":  # 红方
                if selected[1][0] >= 5:  # 自家国界
                    can_moves = [(pos[0]-1, pos[1])]
                else:  # 对方国界
                    can_moves = [(pos[0]-1, pos[1]),
                                 (pos[0], pos[1]+1),
                                 (pos[0], pos[1]-1)]
            elif faction == "黑":  # 黑方
                if selected[1][0] <= 4:  # 自家国界
                    can_moves = [(pos[0] + 1, pos[1])]
                else:  # 对方国界
                    can_moves = [(pos[0]+1, pos[1]),
                                 (pos[0], pos[1]+1),
                                 (pos[0], pos[1]-1)]
        elif type in ("帅", "将"):
            # 普通移动
            can_moves = [(pos[0] + 1, pos[1]),
                         (pos[0] - 1, pos[1]),
                         (pos[0], pos[1] + 1),
                         (pos[0], pos[1] - 1)]
            # 飞将
            col_piece_list = []
            for row in range(10):  # 得到将/帅所处那一列的所有棋子
                if board.iloc[row, pos[1]]:
                    col_piece_list.append((board.iloc[row, pos[1]], (row, pos[1])))  # (棋子类型, (棋子位置))
            # 判断是否可以飞将
            index = col_piece_list.index((type, pos))  # 得到本棋子的索引
            if (index+1) < len(col_piece_list):
                if col_piece_list[index+1][0] in ("帅", "将"):
                    can_moves.append(col_piece_list[index+1][1])
            elif (index-1) > -1:
                if col_piece_list[index - 1][0] in ("帅", "将"):
                    can_moves.append(col_piece_list[index - 1][1])
        elif type in ("仕", "士"):
            can_moves = [(pos[0] + 1, pos[1] + 1),
                         (pos[0] + 1, pos[1] - 1),
                         (pos[0] - 1, pos[1] + 1),
                         (pos[0] - 1, pos[1] - 1)]
        elif type in ("相", "象"):
            can_moves = [(pos[0] + 2, pos[1] + 2),
                         (pos[0] + 2, pos[1] - 2),
                         (pos[0] - 2, pos[1] + 2),
                         (pos[0] - 2, pos[1] - 2)]
        elif type in ("馬", "马"):
            can_moves = [(pos[0] + 1, pos[1] + 2),
                         (pos[0] + 1, pos[1] - 2),
                         (pos[0] - 1, pos[1] + 2),
                         (pos[0] - 1, pos[1] - 2),
                         (pos[0] + 2, pos[1] + 1),
                         (pos[0] + 2, pos[1] - 1),
                         (pos[0] - 2, pos[1] + 1),
                         (pos[0] - 2, pos[1] - 1)]
        elif type in ("車", "车"):
            # 行
            split_tuple = [0, -1]  # 切分位置
            rows_list = []
            rows_can_move = []
            for row in range(10):
                rows_list.append(board.iloc[row, pos[1]])
                rows_can_move.append((row, pos[1]))
            for num in range(len(rows_list)):
                if rows_list[num]:  # 若存在棋子
                    if num < pos[0]:  # 位置高于车的位置
                        split_tuple[0] = num
                    elif num > pos[0] and split_tuple[1] == -1:  # 位置低于车的位置
                        split_tuple[1] = num
            if split_tuple[1] != -1:
                split_tuple[1] += 1
            rows_can_move = rows_can_move[split_tuple[0]:split_tuple[1]]
            can_moves += rows_can_move
            # 列
            split_tuple = [0, -1]  # 切分位置
            colmns_list = []
            colmns_can_move = []
            for colmns in range(9):
                colmns_list.append(board.iloc[pos[0], colmns])
                colmns_can_move.append((pos[0], colmns))
            for num in range(len(colmns_list)):
                if colmns_list[num]:  # 若存在棋子
                    if num < pos[1]:  # 位置左于车的位置
                        split_tuple[0] = num
                    elif num > pos[1] and split_tuple[1] == -1:  # 位置右于车的位置
                        split_tuple[1] = num
            if split_tuple[1] != -1:
                split_tuple[1] += 1
            colmns_can_move = colmns_can_move[split_tuple[0]:split_tuple[1]]
            can_moves += colmns_can_move
        elif type in ("炮", "砲"):
            # 行
            split_tuple = [0, -1]  # 切分位置
            rows_list = []
            rows_can_move = []
            pieces_list = []  # 该列存在的棋子的位置
            for row in range(10):
                rows_list.append(board.iloc[row, pos[1]])
                rows_can_move.append((row, pos[1]))
                if board.iloc[row, pos[1]]:
                    pieces_list.append((row, pos[1]))
            for num in range(len(rows_list)):
                if rows_list[num]:  # 若存在棋子
                    if num < pos[0]:  # 位置高于车的位置
                        split_tuple[0] = num
                    elif num > pos[0] and split_tuple[1] == -1:  # 位置低于车的位置
                        split_tuple[1] = num
            rows_can_move = rows_can_move[split_tuple[0] + 1:split_tuple[1]]
            can_moves += rows_can_move
            # 找出与炮隔一个棋子的棋子
            piece_index = pieces_list.index(pos)
            if piece_index > 1:
                can_moves.append(pieces_list[piece_index - 2])
            if piece_index < len(pieces_list) - 2:
                can_moves.append(pieces_list[piece_index + 2])
            # 列
            split_tuple = [0, -1]  # 切分位置
            colmns_list = []
            colmns_can_move = []
            pieces_list = []  # 该行存在的棋子
            for colmns in range(9):
                colmns_list.append(board.iloc[pos[0], colmns])
                colmns_can_move.append((pos[0], colmns))
                if board.iloc[pos[0], colmns]:
                    pieces_list.append((pos[0], colmns))
            for num in range(len(colmns_list)):
                if colmns_list[num]:  # 若存在棋子
                    if num < pos[1]:  # 位置左于车的位置
                        split_tuple[0] = num
                    elif num > pos[1] and split_tuple[1] == -1:  # 位置右于车的位置
                        split_tuple[1] = num
            colmns_can_move = colmns_can_move[split_tuple[0] + 1:split_tuple[1]]
            can_moves += colmns_can_move
            # 找出与炮隔一个棋子的棋子
            piece_index = pieces_list.index(pos)
            if piece_index > 1:
                can_moves.append(pieces_list[piece_index - 2])
            if piece_index < len(pieces_list) - 2:
                can_moves.append(pieces_list[piece_index + 2])
        return self.can_move(selected, can_moves, faction, board)  # 过滤可移动位置列表

    def can_move(self, selected, can_moves, faction, board):
        """过滤可移动路径, selected:被选中的棋子, can_moves:能够移动的位置列表, faction:阵营轮次, board:棋盘"""
        can_move_path = []  # 能够移动的位置
        type, pos = selected
        for can_move in can_moves:
            if 0 <= can_move[1] < 9 and 0 <= can_move[0] < 10 and can_move != pos:  # 是否存在该位置
                # 范围限定
                if type in ("兵", "卒", "馬", "马", "車", "车", "炮", "砲"):
                    pass
                elif type in ("帅", "将"):
                    if (7 <= can_move[0] or can_move[0] <= 2) and 3 <= can_move[1] <= 5:  # 位于方框内
                        pass
                    else: continue
                elif type in ("仕", "士"):
                    if (7 <= can_move[0] and 3 <= can_move[1] <= 5) or (
                            can_move[0] <= 2 and 3 <= can_move[1] <= 5):  # 位于方框内
                        pass
                    else: continue
                elif type in ("相", "象"):
                    if (faction == "红" and 5 <= can_move[0]) or (faction == "黑" and can_move[0] <= 4):  # 位于己方国界
                        pass
                    else: continue
                # 移动的位置上存在己方棋子
                if board.iloc[can_move]:
                    piece_faction = self.get_piece_faction(board.iloc[can_move])   # 获得棋子所属阵营
                    if faction == piece_faction:
                        continue
                # 走法限定
                if type in ("相", "象"):  # 中间点存在棋子
                    middle_pos = ((pos[0] + can_move[0]) // 2, (pos[1] + can_move[1]) // 2)
                    if board.iloc[middle_pos]:
                        continue
                elif type in ("馬", "马"):  # 撇脚
                    x_middle = (pos[0] + can_move[0]) // 2
                    if x_middle in (pos[0], can_move[0]):
                        x_middle = pos[0]
                    y_middle = (pos[1] + can_move[1]) // 2
                    if y_middle in (pos[1], can_move[1]):
                        y_middle = pos[1]
                    if board.iloc[x_middle, y_middle]:
                        continue
                can_move_path.append(can_move)  # 增加可移动点
        return can_move_path

    def get_piece_faction(self, piece):
        """获得棋子所属的阵营, piece:棋子"""
        for key in PIECE_INFOS["name"]:
            if key == piece:
                return "红"
            elif PIECE_INFOS["name"][key] == piece:
                return "黑"