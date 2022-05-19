import pygame


class objects():
    def __init__(self, m_file, m_location, m_size=None):
        self.m_size = m_size
        self.m_size_x, self.m_size_y = self.m_size
        self.m_location = m_location
        self.m_x, self.m_y = self.m_location
        # m_degree = 0
        # self.m_img = None
        self.m_img = pygame.image.load(m_file)
        self.m_img = pygame.transform.scale(self.m_img, self.m_size)

    def size_trans(self, m_img, m_size_x, m_size_y):  # 비율조정
        self.m_img = pygame.transform.scale(m_img, (m_size_x, m_size_y))

    def rotate(self, m_img, m_degree):
        self.m_img = pygame.transform.rotate(m_img, m_degree)

    def initialize(self, size_x, size_y, img):
        self.m_size_x = size_x
        self.m_size_y = size_y
        self.m_size = (size_x, size_y)
        self.m_img = pygame.image.load(img)
        self.m_img = pygame.transform.scale(self.m_img, self.m_size)

    def self_locate(self, m_location):  # 객체 위치 변환
        self.m_location = m_location
        self.m_x, self.m_y = self.m_location

    def set_alpha(self, x):
        self.m_img.set_alpha(x)

    # def sound_add(num): #모션별 사운드추가

    # motion_sound.append(num)