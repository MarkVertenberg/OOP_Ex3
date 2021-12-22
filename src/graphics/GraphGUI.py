import pygame
import sys
from Button import Button
from InputText import InputBox

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
    test_box = InputBox(0, 0, 200, 50, "Input Box Test")
    load_button = Button(WHITE, WIDTH / 5, HEIGHT / 5, WIDTH * 0.6, HEIGHT * 0.6, "Load Graph")
    while running:
        screen.fill(WHITE)
        load_button.draw(screen)
        test_box.draw(screen, 5)
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            test_box.handle_event(event)
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if load_button.is_over(pos):
                    print("The Load button is clicked!")
                    main_screen()
            if event.type == pygame.MOUSEMOTION:
                if load_button.is_over(pos):
                    load_button.text_color = GREEN
                else:
                    load_button.text_color = BLACK
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
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in list_buttons:
                    if button.is_over(pos):
                        print(button.text + " button is clicked!")
            if event.type == pygame.MOUSEMOTION:
                for button in list_buttons:
                    if button.is_over(pos):
                        button.color = SKY_BLUE
                        button.text_color = WHITE
                    else:
                        button.color = WHITE
                        button.text_color = BLACK
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
    load_button = Button(WHITE, WIDTH * 0.75, 0, WIDTH * 0.25, HEIGHT * (1 / 9.0), "Load Graph")
    save_button = Button(WHITE, WIDTH * 0.75, HEIGHT * (1 / 9.0), WIDTH * 0.25, HEIGHT * (1 / 9.0), "Save Graph")
    add_node_button = Button(WHITE, WIDTH * 0.75, (HEIGHT * (1 / 9.0)) * 2, WIDTH * 0.25, HEIGHT * (1 / 9.0), "Add Node")
    remove_node_button = Button(WHITE, WIDTH * 0.75, (HEIGHT * (1 / 9.0)) * 3, WIDTH * 0.25, HEIGHT * (1 / 9.0), "Remove Node")
    add_edge_button = Button(WHITE, WIDTH * 0.75, (HEIGHT * (1 / 9.0)) * 4, WIDTH * 0.25, HEIGHT * (1 / 9.0), "Add Edge")
    remove_edge_button = Button(WHITE, WIDTH * 0.75, (HEIGHT * (1 / 9.0)) * 5, WIDTH * 0.25, HEIGHT * (1 / 9.0), "Remove Edge")
    shortest_path_button = Button(WHITE, WIDTH * 0.75, (HEIGHT * (1 / 9.0)) * 6, WIDTH * 0.25, HEIGHT * (1 / 9.0), "Shortest Path")
    tsp_button = Button(WHITE, WIDTH * 0.75, (HEIGHT * (1 / 9.0)) * 7, WIDTH * 0.25, HEIGHT * (1 / 9.0), "TSP")
    center_point_button = Button(WHITE, WIDTH * 0.75, (HEIGHT * (1 / 9.0)) * 8, WIDTH * 0.25, HEIGHT * (1 / 9.0), "Center Node")
    return [load_button, save_button, add_node_button, remove_node_button, add_edge_button, remove_edge_button,
            shortest_path_button, tsp_button, center_point_button]


if __name__ == '__main__':
    start_screen()
