# -*- coding: utf-8 -*-
# 图像处理
import pygame as pg
from constant import *


class Image(object):
    """图片类"""
    def __init__(self, windows):
        """初始化, windows:游戏主窗口"""
        self.windows = windows  # 游戏窗口
        self.piece_image = self.change_size(pg.image.load(PIECE_IMAGE_PATH))  # 棋子图片（整）
        self.piece_image_pos = {  # 棋子图片剪裁位置
            "黑": {
                "将": (0, 0, 86, 86),
                "士": (86, 0, 86, 86),
                "车": (172, 0, 86, 86),
                "马": (258, 0, 86, 86),
                "象": (344, 0, 86, 86),
                "砲": (430, 0, 86, 86),
                "卒": (516, 0, 86, 86)
            },
            "红": {
                "帅": (0, 86, 86, 86),
                "仕": (86, 86, 86, 86),
                "車": (172, 86, 86, 86),
                "馬": (258, 86, 86, 86),
                "相": (344, 86, 86, 86),
                "炮": (430, 86, 86, 86),
                "兵": (516, 86, 86, 86)
            },
            "棋子": (0, 172, 86, 86),
            "选中": (86, 172, 86, 86),
        }
        self.change_image_pos()

    def change_image_pos(self):
        """变更棋子剪裁位置以适应窗口倍数"""
        for key in self.piece_image_pos["黑"]:
            pos = self.piece_image_pos["黑"][key]
            self.piece_image_pos["黑"][key] = (int(pos[0]*SIZE_TIME), int(pos[1]*SIZE_TIME), int(pos[2]*SIZE_TIME), int(pos[3]*SIZE_TIME))
        for key in self.piece_image_pos["红"]:
            pos = self.piece_image_pos["红"][key]
            self.piece_image_pos["红"][key] = (int(pos[0]*SIZE_TIME), int(pos[1]*SIZE_TIME), int(pos[2]*SIZE_TIME), int(pos[3]*SIZE_TIME))
        pos = self.piece_image_pos["棋子"]
        self.piece_image_pos["棋子"] = (int(pos[0] * SIZE_TIME), int(pos[1] * SIZE_TIME), int(pos[2] * SIZE_TIME), int(pos[3] * SIZE_TIME))
        pos = self.piece_image_pos["选中"]
        self.piece_image_pos["选中"] = (int(pos[0] * SIZE_TIME), int(pos[1] * SIZE_TIME), int(pos[2] * SIZE_TIME), int(pos[3] * SIZE_TIME))

    def load(self, path, pos):
        """载入图片, path:图片路径, pos:图片放入窗口的位置"""
        image = pg.image.load(path)  # 载入图片
        image = self.change_size(image)  # 变更棋子大小
        self.windows.blit(image, (pos[0], pos[1]))

    def load_piece(self, chop_pos, pos):
        """载入棋子图片, path:图片路径, pos:图片放入窗口的位置"""
        self.windows.blit(self.piece_image, pos, self.piece_image_pos["棋子"])  # 显示棋子背景
        self.windows.blit(self.piece_image, pos, chop_pos)  # 显示棋子

    def load_bg(self, path, pos):
        """载入背景图片, path:图片路径, pos:图片放入窗口的位置"""
        image = pg.image.load(path)  # 载入图片
        image = pg.transform.scale(image, (WINDOWS_SIZE[0]+EDGE_DISTANCE*2, WINDOWS_SIZE[1]+EDGE_DISTANCE*2))  # 变更图片尺寸
        self.windows.blit(image, pos)

    def change_size(self, image):
        """变更图片大小以适应窗口倍数"""
        size = image.get_rect().size  # 获取图片大小
        image = pg.transform.scale(image, (int(size[0] * SIZE_TIME), int(size[1] * SIZE_TIME)))  # 变更图片尺寸
        return image