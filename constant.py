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
    "image": {  # 棋子图片路径
        "红": {
            "帅": "./resources/红帅.png",
            "仕": "./resources/红仕.png",
            "相": "./resources/红相.png",
            "馬": "./resources/红马.png",
            "車": "./resources/红车.png",
            "炮": "./resources/红炮.png",
            "兵": "./resources/红兵.png"
        },
        "黑": {
            "将": "./resources/黑将.png",
            "士": "./resources/黑士.png",
            "象": "./resources/黑象.png",
            "马": "./resources/黑马.png",
            "车": "./resources/黑车.png",
            "砲": "./resources/黑炮.png",
            "卒": "./resources/黑卒.png"
        }
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
PIECE_BOARD_IMAGE_PATH = "./resources/棋子.png"  # 棋子背景图片
HEADERS = {  # 网络请求头
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0"
}