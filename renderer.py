
import pygame

WIDTH, HEIGHT = 800, 600


class Renderer:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.screen.fill((0, 0, 0))

    def render(self, x: float, y: float) -> None:
        pos_x = WIDTH / 2 + y
        pos_y = HEIGHT / 2 - x
        self.screen.set_at((int(pos_x), int(pos_y)), (100, 255, 0))
        pygame.display.update()


if __name__ == '__main__':
    r = Renderer()
    r.render()
