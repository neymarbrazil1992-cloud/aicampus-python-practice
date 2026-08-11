# -*- coding: utf-8 -*-
"""
shooting.py
- 우주괴물 무찌르기 (Space Shooting Game)
- pygame 기반 미니 게임 예제 (수업용)

[폴더 구조]
game/
 ├─ shooting.py ← 이 파일
 └─ resource/ ← 이미지·폰트 리소스 폴더
     ├─ NanumGothic.ttf
     ├─ ship02.png
     ├─ missile.png
     ├─ monster01.png
     ├─ monster02.png
     ├─ ...
     └─ monster10.png

실행 전 설치:
    pip install pygame

실행:
    python shooting.py
    (어느 폴더에서 실행하든 resource 폴더를 자동으로 찾습니다)
"""

import os
import sys
import random
import time

import pygame

# ============================================================
# 1. 경로 / 리소스 설정
# - __file__ 기준 절대경로를 사용해서, 실행 위치(cwd)에
# 상관없이 항상 resource 폴더를 정확히 찾도록 한다.
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESOURCE_DIR = os.path.join(BASE_DIR, "resource") #정적 파일 

def resource_path(filename):
    # resource 폴더 안에서 파일 경로를 지정하여 절대 경로로 사용 
    return os.path.join(RESOURCE_DIR, filename)

# ============================================================
# 2. 게임 설정값 (Config)
# - 값 조정이 필요할 때 이 구간만 보면 되도록 한 곳에 모은다.
# ============================================================

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700
FPS = 50
GAME_DURATION = 30

SHIP_SPEED = 5
MISSILE_SPEED = 10
MONSTER_SPEED_MIN = 1
MONSTER_SPEED_MAX = 5
MONSTER_SPAWN_HEIGHT_RATIO = 0.3

FONT_NAME = "NamumGothic.ttf"
FONT_SIZE_NORMAL = 20
FONT_SIZE_LARGE = 40

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

MONSTER_IMAGE_FILES = [f"monster{i:02d}.png" for i in range(1,11)]