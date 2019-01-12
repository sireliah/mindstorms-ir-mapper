
import math
from typing import Tuple
import pygame

WIDTH, HEIGHT = 800, 800
WIDTH_HALF, HEIGHT_HALF = WIDTH / 2, HEIGHT / 2
ZOOM = 4


def translate(x: float, y: float, turned: float) -> Tuple[float, float]:
    turned = math.radians(-turned)
    new_x = x * math.cos(turned) - y * math.sin(turned)
    new_y = x * math.sin(turned) + y * math.cos(turned)
    return (new_x, new_y)


class Renderer:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.screen.fill((0, 0, 0))
        pygame.display.update()
        self.turned = 0

    def render(self, x: float, y: float, traveled: float, turned: float) -> None:
        print(f'Render x: {x}, y: {y}, traveled: {traveled}, turned: {turned}')
        (x, y) = translate(x, y, turned)
        pos_x = WIDTH_HALF + y * ZOOM
        pos_y = HEIGHT_HALF - x * ZOOM
        print('Will render: ', pos_x, pos_y)
        self.screen.set_at((int(pos_x), int(pos_y)), (100, 255, 0))

        fx, fy = 0, -40.0
        if self.turned != turned:
            (fx, fy) = translate(fx, fy, turned)
            pygame.draw.rect(
                self.screen,
                (0, 0, 0),
                [WIDTH_HALF-40, HEIGHT_HALF-40, 82, 82],
                0
            )
            pygame.display.update()

        pygame.draw.line(
            self.screen,
            (100, 255, 255),
            (WIDTH_HALF, HEIGHT_HALF), (WIDTH_HALF + fx, HEIGHT_HALF + fy),
            2
        )

        pygame.display.update()


if __name__ == '__main__':
    r = Renderer()
    r.render()
