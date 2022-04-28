# #######기본 출력도구들
import sys
import pygame
from material import *
from pygame.locals import QUIT, KEYDOWN ,K_ESCAPE, K_UP, K_LEFT, K_RIGHT, K_DOWN
from math import sqrt
import random

class Block:
    def __init__(self, name):
        self.turn = 0
        self.type - BLOCKS[name]
        self.data = self.type[self.turn]
        self.size = int(sqrt(len(self.data)))
        self.X_position = (WIDTH - self.size)//2
        self.Y_position = 0

    def draw(self):
        for index in range(len(self.data)):
            X_position = index % self.size
            Y_position = index // self.size
            val = self.data[index]
            if ((0 <= Y_position + self.Y_position < HEIGHT) and
                (0 <= X_position + self.X_position < WIDTH) and
                (val != 'RED')):
                x_pos = 25 + (X_position + self.X_position) * 25
                y_pos = 25 + (Y_position + self.Y_position) * 25
                pygame.draw.rect(SURFACE, COLORS[val], (x_pos, y_pos, 24, 24))

    # 키 입력
    def left(self):
        self.X_position = self.X_position-1
    def right(self):
        self.X_position = self.X_position+1
    def down(self):
        self.Y_position = self.Y_position+1
    def up(self):
        self.turn = (self.turn+1)%4
        self.data = self.type[self.turn]

def get_block():
    name = random.choice(list(BLOCKS.keys()))
    block = Block(name)
    return block

# ######기본세팅 + 전역변수
pygame.init()
pygame.key.set_repeat(30, 30)
pygame.display.set_caption('TETRIS_PRACTICE') #<<<게임제목
SURFACE = pygame.display.set_mode((600,600)) #<<<화면 크기
FPSCLOCK = pygame.time.Clock() #프레임레이트 건들기
FPS = 15
WIDTH = 10 + 2
HEIGHT = 20 + 1
FIELD = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
BLOCK = None


# 메인함수 - 프로그램 시작후 가장 먼저 실행하는 함수
def main():
    global BLOCK
    SCORE = 0
    if BLOCK is None:
        BLOCK = get_block()

    smallfont = pygame.font.SysFont(None, 40)

    for Y_position in range(HEIGHT):
        for X_position in range(WIDTH):
            FIELD[Y_position][X_position] = 'BLACK' if X_position == 0 or X_position == WIDTH - 1 else 'GREEN'
    for index in range(WIDTH):
        FIELD[HEIGHT-1][index] = 'BLACK'


    # #카운트 테스트용
    # sysfont = pygame.font.SysFont(None, 20) #카운터_테스트용
    # counter = 0

    while True:
        key = None
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                key = event.key
                if key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        if key == K_UP:
            BLOCK.up()
        elif key == K_RIGHT:
            BLOCK.right()
        elif key == K_LEFT:
            BLOCK.left()
        elif key == K_DOWN:
            BLOCK.down()

        #맵 구성
        SURFACE.fill('WHITE')
        for Y_position in range(HEIGHT):
            for X_position in range(WIDTH):
                value = FIELD[Y_position][X_position]
                pygame.draw.rect(SURFACE, COLORS[value],
                                   (X_position*25 + 25, Y_position*25 + 25, 24, 24))
        BLOCK.draw()

        #점수표시
        SCORE_STR = str(SCORE).zfill(8)
        SCORE_IMAGE = smallfont.render(SCORE_STR, True, 'BLACK')
        SURFACE.blit(SCORE_IMAGE, (440, 30))

        #카운트 테스트용
        # counter = counter +1
        # count_txt = sysfont.render(f'count is {counter}',
        #                            True, GREEN)
        # SURFACE.blit(count_txt, (100, 100))

        pygame.display.update()
        FPSCLOCK.tick(FPS) #프레임 레이트 조절

if __name__ == '__main__':
    main()