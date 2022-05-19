import pygame
from pygame.locals import *
import sys
from mainclass import *     # 객체 관리용 클래스
import time
import math
import python_racer
import room1

global fadespeed
fadespeed = 5
global control
control = 1
global inven
inven = objects("inven.png", (1140, 0), (140, 720))
# 인벤토리 객체 (140x720)


def fade_out(width, height, img_temp, img_temp2):  # fade-in, fade-out 사용용 함수
    fade = pygame.Surface((width, height))  # 어느 범위만큼 fade 할건지
    global fadespeed
    for alpha in range(255, 0, -fadespeed):
        fade.set_alpha(alpha)
        screen.blit(img_temp2, (0, 0))
        screen.blit(fade, (0, 0))
        screen.blit(inven.m_img, (1140, 0))
        pygame.display.update()
        pygame.time.delay(1)


def fade_in(width, height, img_temp, img_temp2, img_temp3, img_temp4):  # fade-in, fade-out 사용용 함수
    fade = pygame.Surface((width, height))  # 어느 범위만큼 fade 할건지
    global fadespeed
    for alpha in range(0, 255, fadespeed):  # alpha를 1씩 늘리며
        fade.set_alpha(alpha)  # 투명도 조절
        screen.blit(img_temp, (0, 0))
        screen.blit(img_temp3, (100, 100))  # 노란 차
        screen.blit(img_temp4, (400, 100))  # 파란 차
        screen.blit(fade, (0, 0))
        screen.blit(inven.m_img, (1140, 0))
        pygame.display.update()
        pygame.time.delay(1)


def fade0(width, height, img_temp, img_temp2, img_temp3, img_temp4):  # fade-in, fade-out 사용용 함수
    fade = pygame.Surface((width, height))  # 어느 범위만큼 fade 할건지
    global fadespeed
    for alpha in range(0, 255, fadespeed):  # alpha를 1씩 늘리며
        fade.set_alpha(alpha)  # 투명도 조절
        screen.blit(img_temp3, (100, 100))  # 노란 차
        screen.blit(img_temp4, (400, 100))  # 파란 차
        screen.blit(img_temp, (0, 0))
        screen.blit(fade, (0, 0))
        screen.blit(inven.m_img, (1140, 0))
        pygame.display.update()
        pygame.time.delay(1)

    for alpha in range(255, 0, -fadespeed):
        fade.set_alpha(alpha)
        screen.blit(img_temp2, (0, 0))
        screen.blit(img_temp3, (100, 100))
        screen.blit(img_temp4, (400, 100))  # 파란 차
        screen.blit(fade, (0, 0))
        screen.blit(inven.m_img, (1140, 0))
        pygame.display.update()
        pygame.time.delay(1)


def fade(width, height, img_temp, img_temp2):  # fade-in, fade-out 사용용 함수
    fade = pygame.Surface((width, height))  # 어느 범위만큼 fade 할건지
    global fadespeed
    for alpha in range(0, 255, fadespeed):  # alpha를 1씩 늘리며
        fade.set_alpha(alpha)  # 투명도 조절
        screen.blit(img_temp, (0, 0))
        screen.blit(fade, (0, 0))
        screen.blit(inven.m_img, (1140, 0))
        pygame.display.update()
        pygame.time.delay(1)

    for alpha in range(255, 0, -fadespeed):
        fade.set_alpha(alpha)
        screen.blit(img_temp2, (0, 0))
        screen.blit(fade, (0, 0))
        screen.blit(inven.m_img, (1140, 0))
        pygame.display.update()
        pygame.time.delay(1)


def fadeonce(width, height, img_temp, img_temp2, img_temp3, img_temp4):  # 맨 처음 불킬때 사용하는 페이드
    fade = pygame.Surface((width, height))  # 어느 범위만큼 fade 할건지
    global fadespeed

    for alpha in range(255, 0, -fadespeed * 50):
        fade.set_alpha(alpha)
        screen.blit(img_temp2, (0, 0))  # 1p
        screen.blit(img_temp3, (100, 100))  # 노란 차
        screen.blit(img_temp4, (400, 100))  # 파란 차
        screen.blit(fade, (0, 0))
        screen.blit(inven.m_img, (1140, 0))
        pygame.display.update()
        pygame.time.delay(1)

    for alpha in range(0, 199, fadespeed * 45):
        fade.set_alpha(alpha)  # 투명도 조절
        screen.blit(img_temp2, (0, 0))
        screen.blit(img_temp3, (100, 100))  # 노란 차
        screen.blit(img_temp4, (400, 100))  # 파란 차
        screen.blit(fade, (0, 0))
        screen.blit(inven.m_img, (1140, 0))
        pygame.display.update()
        pygame.time.delay(1)


# 배경 초기화
pygame.init()  # pygame 사용시 무조건 필요한 초기화 함수

size = (1280, 720)  # 게임 해상도 변수 (1280 x 720 고정)
screen = pygame.display.set_mode(size)  # 게임 해상도 설정
pygame.display.set_caption("Room Escape")  # 게임 상단바 이름

clock = pygame.time.Clock()  # 게임 프레임 단위 설정
background_color = (255, 255, 255)  # background용 color
screen.fill(background_color)

oncebg = pygame.image.load("oncebg.png")          # 맨 처음 어두운 화면
blackbg = pygame.image.load("black.png")  # 검은색 화면
small_blackbg = pygame.image.load("black.png")    # 검은화면
small_blackbg = pygame.transform.scale(small_blackbg, (1140, 720))
small_blackbg.set_alpha(0)


# 배경화면 객체화
img = objects("1p.png", (0, 0), size)  # 첫번째 이미지 로드
img2 = objects("2p.png", (0, 0), size)  # 두번째 이미지 로드
img3 = objects("3p.png", (0, 0), size)  # 세번째 이미지 로드
img4 = objects("4p.png", (0, 0), size)  # 네번째 이미지 로드

# 자동차 객체
car1 = objects("car20.png", (100, 100), (216, 96))  # 노란 차
car2 = objects("car10.png", (400, 100), (216, 96))  # 파란 차
big_car1 = objects("car20.png", (200, 200), (car2.m_size_x * 3, car1.m_size_y * 3))
big_car2 = objects("car10.png", (200, 200), (car2.m_size_x * 3, car1.m_size_y * 3))
big_car1.set_alpha(0)       # 객체 투명도 조절
big_car2.set_alpha(0)       # 0이 투명, 255가 원본

# 왼쪽 화살표 객체
arrow_left = objects("arrow.png", (0, 360 - 128 / 2), (128, 128))  # x는 0, y는 정중앙 (720반에서 화살표 크기의 반만큼 위에서)
arrow_left.initialize(128, 128, "arrow.png")  # arrow.png 불러오기
arrow_left.rotate(arrow_left.m_img, 180)  # 화살표를 180도 돌려줘야 왼쪽을 가리킴

# 오른쪽 화살표 객체
arrow_right = objects("arrow.png", (1140 - 128, 360 - 128 / 2), (128, 128))
arrow_right.initialize(128, 128, "arrow.png")  # arrow.png 불러오기

# 파이썬 책 객체
yaya = objects("board2.png", (1020, 50), (105, 150))

# x버튼 객체
x = objects("x.png", (1050, 25), (80, 80))
x.set_alpha(0)

# 화면 전환용 변수들
count = 0  # 시작 지점 설정 변수
startpoint = (0, 0)  # 시작좌표점 (0, 0) 으로 고정
countframe = 1  # 화살표 클릭시 프레임 구현용 (무한반복 방지)
leftright = 0   # 좌우 프레임 구현시 구분용 left=-1, right=1
once = 0        # 한번만 실행해야 하는 함수에 사용
car_count = 1   # 노란색 차 확대 1이면 작은거 출력 2면 큰거
bluecar_count = 1   # 파란색 차 기능은 위랑 같음


