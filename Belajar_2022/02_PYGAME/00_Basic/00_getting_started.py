import pygame
import sys

pygame.init()

screen = pygame.display.set_mode([500, 500])
screen_rect = screen.get_rect()

platform = pygame.image.load("00_images/land.png")
platform_rect = platform.get_rect()
platform = pygame.transform.scale(platform, (2 * screen_rect.width, platform_rect.height))
platform_rect = platform.get_rect()
# platform_rect.x, platform_rect.y = 250-platform_rect.width/2, 500-platform_rect.height
platform_rect.midbottom = screen_rect.midbottom


def platform_move():
    platform_rect.x -= 5
    if platform_rect.centerx <= 0:
        platform_rect.left = screen_rect.left


bird = pygame.image.load("00_images/bird.png")
bird_rect = bird.get_rect()
bird_rect.center = screen_rect.center

pipe = pygame.Rect(0, 0, 0.15 * screen_rect.width, 0.4 * screen_rect.height)
pipe.topright = screen_rect.topright
pipe_head = pygame.Rect(0, 0, 1.2 * pipe.width, 0.1 * pipe.height)
pipe_head.midbottom = pipe.midbottom

pipe_2 = pygame.Rect(0, 0, 0.15 * screen_rect.width, 0.4 * screen_rect.height)
pipe_2.bottomright = screen_rect.bottomright
pipe_head_2 = pygame.Rect(0, 0, 1.2 * pipe.width, 0.1 * pipe.height)
pipe_head_2.midtop = pipe_2.midtop


def pipe_move():
    global bird_pass_pipe
    pipe.x -= 5
    pipe_2.x -= 5
    # pipe_head.x -= 5

    if pipe.right <= 0:
        pipe.left = screen_rect.right
        pipe_2.left = screen_rect.right
        bird_pass_pipe = False

    pipe_head.midbottom = pipe.midbottom
    pipe_head_2.midtop = pipe_2.midtop


bird_fly = False


def bird_move():
    global bird_fly

    if bird_fly:
        # print("Bird is flying")
        bird_rect.y -= 3
    else:
        # print("Bird is falling down")
        bird_rect.y += 1


bird_pass_pipe = False


def check_bird_point():
    global bird_pass_pipe, pipe, bird_rect, score, score_label, score_label_image

    if (bird_rect.centerx >= pipe.centerx) and not bird_pass_pipe:
        # print("got score")
        score += 1
        score_label_image = score_label.render(f"SCORE : {score}", True, (255, 255, 255))
        bird_pass_pipe = True


def check_bird_hit():
    global bird_rect, pipe, pipe_head, pipe_2, pipe_head_2, platform_rect, life, game_start, game_over

    collide_top_edge = bird_rect.y <= 0
    collide_pipe = bird_rect.colliderect(pipe) or bird_rect.colliderect(pipe_head)
    collide_pipe_2 = bird_rect.colliderect(pipe_2) or bird_rect.colliderect(pipe_head_2)
    collide_platform = bird_rect.colliderect(platform_rect)

    if collide_top_edge or collide_pipe or collide_pipe_2 or collide_platform:
        # print("Collision ...")
        # sys.exit()
        life -= 1
        game_start = False
        game_over = True


play_button = pygame.image.load("00_images/play_button.png")
play_button_rect = play_button.get_rect()
play_button = pygame.transform.scale(play_button,
                                     (int(0.1 * play_button_rect.width), int(0.1 * play_button_rect.height)))
play_button_rect = play_button.get_rect()
play_button_rect.center = screen_rect.center
play_button_rect.y += int(0.1 * screen_rect.height)

title_label = pygame.font.Font("00_fonts/BirdyGame.ttf", 40)
title_label_image = title_label.render("Flappy Bird", True, (255, 255, 255))
title_label_image_rect = title_label_image.get_rect()
title_label_image_rect.center = screen_rect.center
title_label_image_rect.y -= int(0.1 * screen_rect.height)

score = 0
score_label = pygame.font.Font("00_fonts/BirdyGame.ttf", 20)
score_label_image = score_label.render(str(f"SCORE : {score}"), True, (255, 255, 255))
score_label_image_rect = score_label_image.get_rect()
score_label_image_rect.topleft = screen_rect.topleft
score_label_image_rect.y += 10
score_label_image_rect.x += 10

game_over = False
game_over_label = pygame.font.Font("00_fonts/BirdyGame.ttf", 40)
game_over_label_image = game_over_label.render("GAME OVER", True, (255, 0, 0))
game_over_label_image_rect = title_label_image.get_rect()
game_over_label_image_rect.center = screen_rect.center
game_over_label_image_rect.y -= int(0.1 * screen_rect.height)

life = 1
hearts = []

heart = {
    "image": pygame.transform.scale(pygame.image.load("00_images/life.png"), (25, 25)),
    "rect": pygame.image.load("00_images/life.png").get_rect()
}
for i in range(life):
    hearts.append(heart)


def show_hearts():
    global hearts, screen, life
    x, counter, width = 10, 0, 0
    if life > 0:
        for heart in hearts:
            if counter == 0:
                width = heart["rect"].width

            heart["rect"].topright = screen_rect.topright
            heart["rect"].x -= x + (x + width) * counter
            heart["rect"].y += 10
            screen.blit(heart["image"], heart["rect"])
            counter += 1


game_start = False


def event_listener():
    global bird_fly
    global play_button_rect
    global game_start

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                bird_fly = True

        elif event.type == pygame.KEYUP:

            if event.key == pygame.K_SPACE:
                bird_fly = False

        elif event.type == pygame.MOUSEBUTTONDOWN:

            mouse_position = pygame.mouse.get_pos()

            if play_button_rect.collidepoint(mouse_position) and not game_start:
                game_start = True


while True:
    pygame.display.flip()  # draw - clear - draw dst.

    screen.fill([245, 66, 239])  # light purple

    screen.blit(score_label_image, score_label_image_rect)

    screen.blit(bird, bird_rect)

    pygame.draw.rect(screen, (60, 60, 60), pipe)
    pygame.draw.rect(screen, (60, 60, 60), pipe_head)
    pygame.draw.rect(screen, (60, 60, 60), pipe_2)
    pygame.draw.rect(screen, (60, 60, 60), pipe_head_2)

    screen.blit(platform, platform_rect)

    if game_start:
        bird_move()
        check_bird_point()
        check_bird_hit()

        pipe_move()
        platform_move()
    else:
        screen.blit(title_label_image, title_label_image_rect) if not game_over else screen.blit(game_over_label_image,
                                                                                                 game_over_label_image_rect)
        screen.blit(play_button, play_button_rect)

    show_hearts()

    pygame.time.Clock().tick(25)  # 25 frames in a second
    event_listener()
