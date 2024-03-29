import pygame


class Cell:
    rect = None

    def __init__(self, value, row, column, screen, cell_size):
        self.value = value
        self.row = row
        self.col = column
        self.screen = screen
        self.cell_size = cell_size
        self.sketched_value = 0
        self.locked = True if value != 0 else False

    def set_cell_value(self, value):
        if self.locked:
            return
        self.value = value
        self.sketched_value = 0
        self.locked = True

    def set_cell_reset(self, value):
        self.value = value
        self.sketched_value = 0

    def set_cell_sketched_value(self, value):
        if self.locked:
            return
        self.sketched_value = value

    def draw(self, selected):
        color = (0, 0, 0) if not selected else (196,245,255)

        x = self.col * self.cell_size
        y = self.row * self.cell_size
        rect = pygame.Rect(x, y, self.cell_size, self.cell_size)
        if selected:
            pygame.draw.rect(self.screen, color, rect, 0)
        else:
            pygame.draw.rect(self.screen, color, rect, 1)

        if self.value != 0:
            font = pygame.font.Font(None, 36)
            text = font.render(str(self.value), True, (0, 0, 0))
            text_rect = text.get_rect(center=rect.center)
            self.screen.blit(text, text_rect)
        elif self.value == 0 and self.sketched_value != 0:
            font = pygame.font.Font(None, 36)
            text = font.render(str(self.sketched_value), True, (128, 128, 128))
            text_rect = text.get_rect(center=rect.center)
            self.screen.blit(text, text_rect)
