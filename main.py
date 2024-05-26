import pygame, sys

from src.events.keys import KeyPressed
from src.maps.map import Map
from src.ui.ath import ATH

max_lines = 7
max_cols = 10

pygame.init()
screen = pygame.display.set_mode((max_cols * 64, max_lines * 64 + ATH.ATH_HEIGHT))
# Initializing Color

pygame.display.set_caption("PY_PUZZLE RomainProjet31")
clock = pygame.time.Clock()
map_loader = Map()
ath = None


def start() -> ATH:
    map_loader.load_map(ATH.ATH_HEIGHT)
    return ATH(map_loader, screen.get_width(), screen.get_height())


def next() -> ATH:
    map_loader.next_map(ATH.ATH_HEIGHT)
    return ATH(map_loader, screen.get_width(), screen.get_height())


ath = start()
dt = 0
while True:
    KeyPressed.instance().key_pressed = None
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            KeyPressed.instance().key_pressed = event.key

        if (
            event.type == pygame.QUIT
            or KeyPressed.instance().key_pressed == pygame.K_ESCAPE
        ):
            pygame.quit()
            sys.exit()

    game_result = map_loader.game_result()
    if False == game_result:
        ath.flg_game_over = True
    elif True == game_result:
        ath.flg_game_won = True

    if ath.flg_game_won or ath.flg_game_over:
        ath.render(screen)
        if ath.flg_game_won:
            pygame.display.flip()
            pygame.time.wait(1500)
            if map_loader.has_next():
                ath = next()
            else:
                pygame.quit()
                sys.exit()
        elif ath.flg_game_over and KeyPressed.instance().key_pressed == pygame.K_r:
            ath = start()
    else:
        screen.fill("purple")
        map_loader.update(dt)
        ath.update()
        map_loader.render(screen)
        ath.render(screen)

    pygame.display.flip()
    dt = clock.tick(60)
