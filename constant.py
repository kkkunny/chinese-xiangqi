# -*- coding: utf-8 -*-
# 常量

ORIGINAL_WINDOWS_SIZE = (710, 800)  # 原窗口尺寸
SIZE_TIME = 1/2  # 窗口放大倍数
WINDOWS_SIZE = (int(ORIGINAL_WINDOWS_SIZE[0]*SIZE_TIME), int(ORIGINAL_WINDOWS_SIZE[1]*SIZE_TIME))  # 窗口尺寸
EDGE_DISTANCE = int(40 * SIZE_TIME)  # 边界尺寸
PIECE_INFOS = {  # 棋子信息
    "name": {  # 两方棋子名 红：黑
        "帅": "将",
        "仕": "士",
        "相": "象",
        "馬": "马",
        "車": "车",
        "炮": "砲",
        "兵": "卒"
    },
    "FEN": {
        "帅": "K",
        "仕": "A",
        "相": "B",
        "馬": "N",
        "車": "R",
        "炮": "C",
        "兵": "P",
        "将": "k",
        "士": "a",
        "象": "b",
        "马": "n",
        "车": "r",
        "砲": "c",
        "卒": "p",
        "红": "w",
        "黑": "b"
    }
}
PIECE_IMAGE_PATH = "./resources/pieces.png"  # 棋子图片位置
PIECE_SIZE = (86, 86)  # 每颗棋子的大小
PIECE_BOARD_IMAGE_PATH = "./resources/棋子.png"  # 棋子背景图片
HEADERS = {  # 网络请求头
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0"
}