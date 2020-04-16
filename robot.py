# -*- coding: utf-8 -*-
# 机器人
from constant import *
from requests import session
from re import findall


class Robot(object):
    """机器人"""
    def __init__(self, faction):
        """初始化, faction:阵营"""
        self.faction = faction
        self.session = session()  # 创建网络会话

    def spider(self, fen):
        """爬虫, fen:fen编码棋盘"""
        # 转换FEN为英文版
        fen_list = list(fen)
        for num in range(len(fen_list)):
            for key in PIECE_INFOS["FEN"]:
                if key == fen_list[num]:
                    fen_list[num] = PIECE_INFOS["FEN"][key]
        fen = "".join(fen_list)
        # 连接中国象棋API
        root_url = "http://www.chessdb.cn/chessdb.php?action="  # API地址
        url = root_url + "query" + "&board=" + fen  # 随机走法
        reponse = self.session.get(url=url, headers=HEADERS)
        if reponse.status_code == 200:
            move_text = reponse.text
            paths = findall("move:(\w)(\d)(\w)(\d)", move_text)[0] if findall("move:(\w)(\d)(\w)(\d)", move_text) else None
            if paths:
                alphas = "abcdefghi"
                path = []  # （以左下角为原点， 列索引， 行索引）
                for num in range(len(paths)):
                    if paths[num] in alphas:
                        path.append((alphas.find(paths[num]), 9-int(paths[num + 1])))
                return path
            else:  # API无最佳走法
                return None