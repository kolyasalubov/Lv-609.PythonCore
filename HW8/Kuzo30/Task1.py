import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()

screen = pygame.display.set_mode([626, 278])

pygame.display.set_caption('Fly')

clock = pygame.time.Clock()

pygame.display.update()

background_position = [0, 0]

background_image = pygame.image.load("C:/MyStorage/Git/Lv-609.PythonCore/HW8/Kuzo30/imags/background.jpg").convert()
player_image = pygame.image.load("C:/MyStorage/Git/Lv-609.PythonCore/HW8/Kuzo30/imags/player.jpg").convert()

player_image.set_colorkey((15,161,251))

done = False

while not done:
    screen.blit(background_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]

    screen.blit(player_image, [x, y])

    pygame.display.flip()

    clock.tick(60)
    # print(clock.get_fps())

pygame.quit()
