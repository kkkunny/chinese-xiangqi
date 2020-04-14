# -*- coding: utf-8 -*-
# 图像处理
import pygame as pg
from constant import *


class Image(object):
    """图片类"""
    def __init__(self, windows):
        """初始化, windows:游戏主窗口"""
        self.windows = windows  # 游戏窗口

    def load(self, path, pos):
        """载入图片, path:图片路径, pos:图片放入窗口的位置"""
        image = pg.image.load(path)  # 载入图片
        size = image.get_rect().size  # 获取图片大小
        image = pg.transform.scale(image, (int(size[0]*SIZE_TIME), int(size[1]*SIZE_TIME)))  # 变更图片尺寸
        self.windows.blit(image, (pos[0], pos[1]))

    def load_piece(self, path, pos):
        """载入棋子图片, path:图片路径, pos:图片放入窗口的位置"""
        image = pg.image.load(path)  # 载入图片
        size = image.get_rect().size  # 获取图片大小
        image = pg.transform.scale(image, (int(size[0]*SIZE_TIME), int(size[1]*SIZE_TIME)))  # 变更图片尺寸
        self.load(PIECE_BOARD_IMAGE_PATH, pos)  # 载入棋子背景
        self.windows.blit(image, (pos[0], pos[1]))

    def load_bg(self, path, pos):
        """载入背景图片, path:图片路径, pos:图片放入窗口的位置"""
        image = pg.image.load(path)  # 载入图片
        image = pg.transform.scale(image, (WINDOWS_SIZE[0]+EDGE_DISTANCE*2, WINDOWS_SIZE[1]+EDGE_DISTANCE*2))  # 变更图片尺寸
        self.windows.blit(image, pos)