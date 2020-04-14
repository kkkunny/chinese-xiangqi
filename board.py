# -*- coding: utf-8 -*-
# 棋盘
import re
import pandas as pd


def make_board(fen):
    """生成棋盘, fen:FEN棋盘编码"""
    infos = re.findall("(.+) (.{1}) - - 0 (\d{1})", fen)[0]  # 正则获得棋盘信息
    board_infos = infos[0]  # 获得棋盘FEN
    faction = infos[1]  # 获得当前轮到的阵营
    rounds = int(infos[2])  # 获得局数
    board_infos_list = board_infos.split("/")  # 切分棋盘
    board = pd.DataFrame([[False for j in range(9)] for i in range(10)])  # 生成全为False的棋盘
    row = 0  # 初始化棋盘行数
    for board_info in board_infos_list:  # 遍历每一行的棋盘
        col = 0  # 初始化棋盘列数
        for piece in board_info:  # 遍历一行中的每一个棋子
            if piece == "9":  # 一行为空
                pass
            elif piece in [str(num + 1) for num in range(8)]:  # 空格
                num = int(piece)  # 将空格字符串转换为整型
                col += num  # 跳过空格
            else:  # 棋子
                board.iloc[row, col] = piece
                col += 1  # 列数增加
        row += 1  # 行数增加
    return board, faction, rounds


def make_fen(board, round, faction):
    """生成FENb编码棋盘, board:棋盘, round局数:, faction:当前应该走棋的阵营"""
    # 判断阵营
    if faction in ("红", "黑"):
        pass
    else:
        faction = "红" if faction else "黑"
    FEN = ""  # FEN编码的棋盘
    for row in range(10):
        num = 0  # 空格
        for col in range(9):
            piece = board.iloc[row, col]  # 获得棋盘没电上的物体
            if piece:
                if num != 0:
                    FEN += str(num)
                num = 0  # 还原空格数量
                FEN += piece
            else:  # 空格
                num += 1
        if num != 0:
            FEN += str(num)
        if row != 9:
            FEN += "/"
    FEN += " {} - - 0 {}".format(faction, round)
    return FEN