import pygame
import sys
from Button import Button
from InputBox import InputBox
from LittleWindow import LittleWindow

WIDTH = 1280
HEIGHT = 720
REFRESH_RATE = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
SKY_BLUE = (75, 118, 229)
LIGHT_YELLOW = (255, 253, 126)

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Graph GUI")
icon = pygame.image.load('images/graph_icon.jpg')
pygame.display.set_icon(icon)

running = True
clock = pygame.time.Clock()


def start_screen():
    global clock
    global running
    load_button = Button(WHITE, (WIDTH / 2) - 125, (HEIGHT / 2) - 15, 250, 75, "Load Graph")
    while running:
        screen.fill(WHITE)
        load_button.draw(screen)
        for event in pygame.event.get():
            load_button.handle_event(event, WHITE, WHITE, GREEN, BLACK)
            if load_button.is_clicked:
                main_screen()
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
        clock.tick(REFRESH_RATE)
    pygame.quit()
    sys.exit()


def main_screen():
    global clock
    global running
    list_buttons = create_buttons()
    while running:
        screen.fill(WHITE)
        show_graph(WIDTH * 0.75, HEIGHT)
        show_buttons(list_buttons)
        for event in pygame.event.get():
            for button in list_buttons:
                button.handle_event(event)
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
        clock.tick(REFRESH_RATE)
    pygame.quit()
    sys.exit()


def show_graph(width, height):
    global screen
    pygame.draw.rect(screen, BLACK, (0, 0, width, height), 5, 5)


def show_buttons(buttons):
    global screen
    for button in buttons:
        button.draw(screen, 5)


def create_buttons():
    remove_node_input_box = InputBox(10, 10, 200, 30, "Node key", text_size=16)
    remove = Button(WHITE, 220, 10, 80, 30, "Remove", text_size=16)
    remove_node_window = LittleWindow([remove_node_input_box], [remove])
    load_button = Button(WHITE, WIDTH * 0.75, 0, WIDTH * 0.25, HEIGHT * (1 / 9.0), "Load Graph", window=LittleWindow())
    save_button = Button(WHITE, WIDTH * 0.75, HEIGHT * (1 / 9.0), WIDTH * 0.25, HEIGHT * (1 / 9.0), "Save Graph", window=LittleWindow())
    add_node_button = Button(WHITE, WIDTH * 0.75, (HEIGHT * (1 / 9.0)) * 2, WIDTH * 0.25, HEIGHT * (1 / 9.0), "Add Node", window=LittleWindow())
    remove_node_button = Button(WHITE, WIDTH * 0.75, (HEIGHT * (1 / 9.0)) * 3, WIDTH * 0.25, HEIGHT * (1 / 9.0), "Remove Node", window=remove_node_window)
    add_edge_button = Button(WHITE, WIDTH * 0.75, (HEIGHT * (1 / 9.0)) * 4, WIDTH * 0.25, HEIGHT * (1 / 9.0), "Add Edge", window=LittleWindow())
    remove_edge_button = Button(WHITE, WIDTH * 0.75, (HEIGHT * (1 / 9.0)) * 5, WIDTH * 0.25, HEIGHT * (1 / 9.0), "Remove Edge", window=LittleWindow())
    shortest_path_button = Button(WHITE, WIDTH * 0.75, (HEIGHT * (1 / 9.0)) * 6, WIDTH * 0.25, HEIGHT * (1 / 9.0), "Shortest Path", window=LittleWindow())
    tsp_button = Button(WHITE, WIDTH * 0.75, (HEIGHT * (1 / 9.0)) * 7, WIDTH * 0.25, HEIGHT * (1 / 9.0), "TSP", window=LittleWindow())
    center_point_button = Button(WHITE, WIDTH * 0.75, (HEIGHT * (1 / 9.0)) * 8, WIDTH * 0.25, HEIGHT * (1 / 9.0), "Center Node", window=LittleWindow())
    return [load_button, save_button, add_node_button, remove_node_button, add_edge_button, remove_edge_button,
            shortest_path_button, tsp_button, center_point_button]


if __name__ == '__main__':
    start_screen()
