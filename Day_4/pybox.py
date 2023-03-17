import pygame
import random

# 게임 창 크기 설정
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BLOCK_SIZE = 20

# 오목판 크기 설정
BOARD_WIDTH = 25
BOARD_HEIGHT = 25

# 게임창 초기화
pygame.init()
pygame.display.set_caption("Omok")
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()


# 오목판 그리기
def draw_board():
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            rect = pygame.Rect(x*BLOCK_SIZE, y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, (255, 255, 255), rect, 1)


# 돌 그리기
def draw_stone(x, y, color):
    rect = pygame.Rect(x*BLOCK_SIZE, y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
    pygame.draw.ellipse(screen, color, rect)


# 게임 루프
def game_loop():
    running = True
    board = [[0] * BOARD_HEIGHT for _ in range(BOARD_WIDTH)]
    turn = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # 좌클릭한 경우
                pos = pygame.mouse.get_pos()
                x = pos[0] // BLOCK_SIZE
                y = pos[1] // BLOCK_SIZE
                if board[x][y] == 0:
                    color = (0, 0, 0) if turn == 0 else (255, 255, 255)
                    draw_stone(x, y, color)
                    board[x][y] = turn + 1
                    turn = (turn + 1) % 2

        screen.fill((0, 0, 0))  # 배경화면을 하얀색으로 채우기
        draw_board()  # 오목판 그리기
        for x in range(BOARD_WIDTH):
            for y in range(BOARD_HEIGHT):
                if board[x][y] == 1:
                    draw_stone(x, y, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))  # 검은색 돌 그리기
                elif board[x][y] == 2:
                    draw_stone(x, y, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))  # 흰색 돌 그리기
        pygame.display.update()  # 화면 업데이트
        clock.tick(60)  # FPS 설정

    pygame.quit()

game_loop()