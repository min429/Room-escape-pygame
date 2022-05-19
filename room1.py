import pygame
from pygame.locals import *
import sys
from mainclass import *  # 객체 관리용 클래스
import python_racer
import room1
from main import *

while True:
    mousePosition = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        mousePressed = True
    else:
        mousePressed = False

    clock.tick(60)  # 60프레임 고정
    countframe = 0  # 무한반복 방지용 변수 다시 반복문에서 0으로 초기화

    if mousePressed:
        countframe = 1  # 화살표 클릭시 프레임 구현용 (무한반복 방지) 한번 클릭시 무조건 1으로 됨
        if control == 1:  # 객체 클릭할 때
            if once == 1:  # 처음 게임 시작시 나오는 어두운 화면
                if 765 <= mousePosition[0] <= 782:
                    if 405 <= mousePosition[1] <= 443:  # 스위치 클릭시
                        img.m_img.set_alpha(255)  # 1p 출력
                        fadeonce(1140, 720, oncebg, img.m_img, car1.m_img, car2.m_img)  # 1p와 객체들 출력
                        once, count, leftright = 2, 1, 0

            if count == 2:
                if 1020 <= mousePosition[0] <= 1125:
                    if 50 <= mousePosition[1] <= 200:  # 2번방에서 책 사진 클릭시
                        exec(open("python_racer.py", 'r', encoding="UTF-8").read())  # python_racer 실행

            if count == 1:
                if car_count == 1:
                    if car1.m_x <= mousePosition[0] <= car1.m_x + car1.m_size_x:
                        if car1.m_y <= mousePosition[1] <= car1.m_y + car1.m_size_y:  # 노란색 차 클릭시
                            car1.set_alpha(0)  # 노란색 차 투명화
                            big_car1.m_img.set_alpha(255)  # 큰 노란색차 시각화
                            small_blackbg.set_alpha(172)  # 전체화면 172만큼 반투명
                            car2.set_alpha(172)  # 나머지 객체들도 반투명 ex) 파란색차
                            x.set_alpha(255)  # x 버튼 시각화
                            car_count = 2  # 큰 노란색차 출력중일때로 넘어감
                            control = 0  # 다른 객체 클릭 못하게끔 (x버튼으로 탈출)

                if bluecar_count == 1:
                    if car2.m_x <= mousePosition[0] <= car2.m_x + car2.m_size_x:
                        if car2.m_y <= mousePosition[1] <= car2.m_y + car2.m_size_y:  # 파란색 차 클릭시
                            car2.set_alpha(0)  # 파란색 차 투명화
                            big_car2.m_img.set_alpha(255)  # 큰 파란색차 시각화
                            small_blackbg.set_alpha(172)  # 전체화면 172만큼 반투명
                            car1.set_alpha(172)  # 나머지 객체들도 반투명 ex) 노란색차
                            x.set_alpha(255)  # x 버튼 시각화
                            bluecar_count = 2  # 큰 파란색차 출력중일때로 넘어감
                            control = 0  # 다른 객체 클릭 못하게끔 (x버튼으로 탈출)

            if arrow_left.m_x <= mousePosition[0] <= arrow_left.m_x + arrow_left.m_size_x:
                if arrow_left.m_y <= mousePosition[1] <= arrow_left.m_y + arrow_left.m_size_y:
                    # (0, 250) <= 마우스 위치 <= (100, 350)
                    leftright = -1  # 왼쪽 화살표 클릭시
                    if count == 1: count = 4
                    elif count == 2: count = 1
                    elif count == 3: count = 2
                    elif count == 4: count = 3
                    ## 방 옮길때 count를 감소시키며 방을 왼쪽으로 옮김

            if arrow_right.m_x <= mousePosition[0] <= arrow_right.m_x + arrow_right.m_size_x:
                if arrow_right.m_y <= mousePosition[1] <= arrow_right.m_y + arrow_right.m_size_y:
                    # (700, 250) <= 위치 <= (1280, 350)
                    leftright = 1
                    if count == 1: count = 2
                    elif count == 2: count = 3
                    elif count == 3: count = 4
                    elif count == 4: count = 1
                    ## 방 옮길때 count를 증가시키며 방을 오른쪽으로 옮김

        # control이 0일때 (객체 확대 후 다시 돌아가는 코드)
        else:
            if car_count == 2:                                          # 큰 노란색 차 출력중일때
                if x.m_x < mousePosition[0] < x.m_x + x.m_size_x:
                    if x.m_y < mousePosition[1] < x.m_y + x.m_size_y:   # x 버튼 클릭시
                        car1.set_alpha(255)                             # 기존 객체들 시각화
                        car2.set_alpha(255)
                        big_car1.m_img.set_alpha(0)                     # 큰 노란색 차(클릭했던 객체) 투명화
                        small_blackbg.set_alpha(0)                      # 반투명했던 화면 다시 원래대로
                        x.set_alpha(0)                                  # x 버튼 투명화
                        car_count = 1                                   # 다시 원래 화면으로
                        control = 1                                     # 객체 클릭 가능한 상태로 되돌리기

            if bluecar_count == 2:
                if x.m_x < mousePosition[0] < x.m_x + x.m_size_x:
                    if x.m_y < mousePosition[1] < x.m_y + x.m_size_y:  # x 버튼 클릭시
                        car1.set_alpha(255)  # 기존 객체들 시각화
                        car2.set_alpha(255)
                        big_car2.m_img.set_alpha(0)  # 큰 파란색 차(클릭했던 객체) 투명화
                        small_blackbg.set_alpha(0)  # 반투명했던 화면 다시 원래대로
                        x.set_alpha(0)  # x 버튼 투명화
                        bluecar_count = 1  # 다시 원래 화면으로
                        control = 1  # 객체 클릭 가능한 상태로 되돌리기

    if once == 0:
        fade(1140, 720, blackbg, oncebg)  # 첫 실행시 검은 화면에서 1번 화면으로 나옴
        once = 1

    if count == 1:          # 1번 화면
        if leftright == -1:  # 1번 화면이고 왼쪽 화살표 클릭시
            if countframe == 1:  # countframe 0이면
                fade0(1140, 720, img2.m_img, img.m_img, car1.m_img, car2.m_img)
                leftright = 0
        elif leftright == 1:
            if countframe == 1:  # countframe 1이면
                fade0(1140, 720, img4.m_img, img.m_img, car1.m_img, car2.m_img)
                leftright = 0
        screen.blit(img.m_img, startpoint)
        screen.blit(inven.m_img, inven.m_location)  # 인벤토리 출력
        screen.blit(arrow_left.m_img, arrow_left.m_location)  # 왼쪽화살표 출력
        screen.blit(arrow_right.m_img, arrow_right.m_location)  # 오른쪽화살표 출력
        screen.blit(small_blackbg, (0, 0))
        screen.blit(car1.m_img, car1.m_location)
        screen.blit(big_car1.m_img, big_car1.m_location)
        screen.blit(big_car2.m_img, big_car2.m_location)
        screen.blit(car2.m_img, car2.m_location)
        screen.blit(x.m_img, x.m_location)
        pygame.display.update()  # display update
        countframe = 0  # 무한반복 방지용

    elif count == 2:        # 2번 화면
        if leftright == -1:
            if countframe == 1:
                fade(1140, 720, img3.m_img, img2.m_img)
                leftright = 0
        elif leftright == 1:
            if countframe == 1:
                # fade(1140, 720, img.m_img, img2.m_img)
                fade_in(1140, 720, img.m_img, img2.m_img, car1.m_img, car2.m_img)
                fade_out(1140, 720, img.m_img, img2.m_img)
                leftright = 0
        screen.blit(img2.m_img, startpoint)
        screen.blit(inven.m_img, inven.m_location)
        screen.blit(arrow_left.m_img, arrow_left.m_location)
        screen.blit(arrow_right.m_img, arrow_right.m_location)
        screen.blit(yaya.m_img, yaya.m_location)
        pygame.display.update()
        countframe = 0

    elif count == 3:        # 3번 화면
        if leftright == -1:
            if countframe == 1:
                fade(1140, 720, img4.m_img, img3.m_img)
                leftright = 0
        elif leftright == 1:
            if countframe == 1:
                fade(1140, 720, img2.m_img, img3.m_img)
                leftright = 0
        screen.blit(img3.m_img, startpoint)
        screen.blit(inven.m_img, inven.m_location)
        screen.blit(arrow_left.m_img, arrow_left.m_location)
        screen.blit(arrow_right.m_img, arrow_right.m_location)
        pygame.display.update()
        countframe = 0

    elif count == 4:        # 4번 화면
        if leftright == -1:
            if countframe == 1:
                fade_in(1140, 720, img.m_img, img4.m_img, car1.m_img, car2.m_img)
                fade_out(1140, 720, img.m_img, img4.m_img)
                leftright = 0
        elif leftright == 1:
            if countframe == 1:
                fade(1140, 720, img3.m_img, img4.m_img)
                leftright = 0
        screen.blit(img4.m_img, startpoint)
        screen.blit(inven.m_img, inven.m_location)
        screen.blit(arrow_left.m_img, arrow_left.m_location)
        screen.blit(arrow_right.m_img, arrow_right.m_location)
        pygame.display.update()
        countframe = 0

    for event in pygame.event.get():  # pygame 이벤트 실행
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN:  # 키 입력시
            if event.key == K_q:
                exec(open("python_racer.py", 'r', encoding="UTF-8").read())  # Q 누를시 pyracer 실행
            if event.key == K_ESCAPE:
                pygame.quit()  # esc 입력시 게임 종료
    print(control)
pygame.quit()
