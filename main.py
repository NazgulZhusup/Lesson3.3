import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир")

icon = pygame.image.load("img/2689911.png").convert()
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 85

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

target_x_change = 0.3  # Скорость движения цели по горизонтали
target_y_change = 0.3  # Скорость движения цели по вертикали

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

score = 0  # Подсчет очков

font = pygame.font.Font(None, 36)


def show_score():
    text = font.render("Очки: " + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))


running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                score += 1  # Увеличиваем счет
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Перемещение цели
    target_x += target_x_change
    target_y += target_y_change

    # Отскок от краев экрана
    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        target_x_change = -target_x_change
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        target_y_change = -target_y_change

    screen.blit(target_img, (target_x, target_y))
    show_score()

    pygame.display.update()

pygame.quit()
