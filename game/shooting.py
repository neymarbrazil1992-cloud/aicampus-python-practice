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

# ============================================================
# 3. 화면 그리기 함수 
# ============================================================
def paint_entity(monitor, entity, x, y):
    # 이미지(entity)를 화면(monitor)의 (x,y)위치에 그린다 
    monitor.blit(entity,(x,y))
    
def get_contrast_color(bg_color):
    r,g,b = bg_color
    return(255-r, 255-g, 255-b) #배경색과 대비되는 글자샐 추출해서 반환 

#현재 점수를 화면의 왼쪽 아래에 출력한다 
def write_score(monitor, font, score, bg_color):
    text_color = get_contrast_color(bg_color)
    txt = font.render(f"파괴한 우주괴물 수 : {score}", True, text_color)
    paint_entity(monitor, txt, SCREEN_WIDTH * 0.05, SCREEN_HEIGHT * 0.9)
 
#남은 시간을  화면의 오른쪽 아래에 출력한다     
def write_time(monitor, font, remaining_time):
    txt = font.render(f"남은 시간 : {remaining_time}", True, WHITE)
    monitor.blit(txt, (SCREEN_WIDTH - 150, SCREEN_HEIGHT - 40))
    
def display_final_score(monitor, font, score):
    txt = font.render(f"게임종료   최종 점수 : {score}", True, RED)
    monitor.fill(BLACK)
    text_rect = txt.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    monitor.blit(txt, text_rect)
    pygame.display.update()
    pygame.time.delay(3000) #3초동안만 화면에 결과 보여줌 
    
# ============================================================
# 4. 리소스 로드  
# ============================================================
def load_resources():
    """이미지·폰트 리소스를 모두 불러와 딕셔너리로 반환한다."""
    resources = {
        "ship": pygame.image.load(resource_path("ship02.png")),
        "missile": pygame.image.load(resource_path("missile.png")),
        "monster_images": [resource_path(name) for name in MONSTER_IMAGE_FILES],
        "font_normal": pygame.font.Font(resource_path(FONT_NAME), FONT_SIZE_NORMAL),
        "font_large": pygame.font.Font(resource_path(FONT_NAME), FONT_SIZE_LARGE),
    }
    return resources

def spawn_monster(monster_image_files):
    """몬스터를 무작위 이미지·위치·속도로 새로 등장시킨다."""
    image_path = random.choice(monster_image_files)
    monster_surface = pygame.image.load(image_path)
    monster_size = monster_surface.get_rect().size
    monster_x = 0
    monster_y = random.randrange(0, int(SCREEN_WIDTH * MONSTER_SPAWN_HEIGHT_RATIO))
    monster_speed = random.randrange(MONSTER_SPEED_MIN, MONSTER_SPEED_MAX)
    return monster_surface, monster_size, monster_x, monster_y, monster_speed

# ============================================================
# 5. 메인 게임 루프 
# ============================================================
def play_game(monitor, resources):
    ship = resources["ship"]
    missile = resources["missile"]
    font_normal = resources["font_normal"]
    font_large = resources["font_large"]
    monster_image_files = resources["monster_images"]

    ship_size = ship.get_rect().size

    # 배경색은 게임 시작할 때 한 번 무작위로 정한다.
    bg_color = (
        random.randrange(0, 256),
        random.randrange(0, 256),
        random.randrange(0, 256),
    )

    # 우주선 초기 위치 및 이동량
    ship_x = SCREEN_WIDTH / 2
    ship_y = SCREEN_HEIGHT * 0.8
    dx, dy = 0, 0

    # 몬스터 초기화
    monster, monster_size, monster_x, monster_y, monster_speed = spawn_monster(monster_image_files)

    # 미사일 좌표 (None이면 발사 전 상태)
    missile_x, missile_y = None, None

    # 점수 및 타이머
    fire_count = 0
    start_time = time.time()
    clock = pygame.time.Clock()

    while True:
        # --- 5-1. 남은 시간 계산 ---
        elapsed_time = time.time() - start_time
        remaining_time = int(GAME_DURATION - elapsed_time)
        if remaining_time <= 0:
            display_final_score(monitor, font_large, fire_count)
            return fire_count

        clock.tick(FPS)
        monitor.fill(bg_color)

        # --- 5-2. 이벤트(키보드/마우스) 처리 ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -SHIP_SPEED
                elif event.key == pygame.K_RIGHT:
                    dx = SHIP_SPEED
                elif event.key == pygame.K_UP:
                    dy = -SHIP_SPEED
                elif event.key == pygame.K_DOWN:
                    dy = SHIP_SPEED
                elif event.key == pygame.K_SPACE:
                    if missile_x is None:  # 미사일이 발사 중이 아닐 때만 새로 발사
                        missile_x = ship_x + ship_size[0] / 2
                        missile_y = ship_y

            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN):
                    dx, dy = 0, 0

        # --- 5-3. 우주선 이동 (화면 하단 절반 안에서만 이동 가능) ---
        next_x = ship_x + dx
        next_y = ship_y + dy
        if 0 < next_x <= SCREEN_WIDTH - ship_size[0] and \
           SCREEN_HEIGHT / 2 < next_y <= SCREEN_HEIGHT - ship_size[1]:
            ship_x, ship_y = next_x, next_y
        paint_entity(monitor, ship, ship_x, ship_y)

        # --- 5-4. 몬스터 이동 ---
        monster_x += monster_speed
        if monster_x > SCREEN_WIDTH:
            monster, monster_size, monster_x, monster_y, monster_speed = spawn_monster(monster_image_files)
        paint_entity(monitor, monster, monster_x, monster_y)

        # --- 5-5. 미사일 이동 및 충돌 판정 ---
        if missile_x is not None:
            missile_y -= MISSILE_SPEED
            if missile_y < 0:
                missile_x, missile_y = None, None

        if missile_x is not None:
            paint_entity(monitor, missile, missile_x, missile_y)

            hit = (monster_x < missile_x < monster_x + monster_size[0]) and \
                  (monster_y < missile_y < monster_y + monster_size[1])
            if hit:
                fire_count += 1
                monster, monster_size, monster_x, monster_y, monster_speed = spawn_monster(monster_image_files)
                missile_x, missile_y = None, None

        # --- 5-6. 점수 / 시간 표시 ---
        write_score(monitor, font_normal, fire_count, bg_color)
        write_time(monitor, font_normal, remaining_time)

        pygame.display.update()   
    
    

# 6. 프로그램 메인 
def main():
    #pass  #바디 없는 인터페이스 
    pygame.init()
    
    monitor = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("우주괴물 무찌르기")
    
    resources = load_resources()
    
    play_gmae(monitor, resources)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()