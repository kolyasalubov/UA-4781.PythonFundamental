import pygame
import sys
import pygame_gui
import random


WIDTH_DISPLAY = 600
HEIGHT_DISPLAY = 400

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY))
pygame.display.set_caption("Number Guessing Game")

clock = pygame.time.Clock()
MANAGER = pygame_gui.UIManager((WIDTH_DISPLAY, HEIGHT_DISPLAY))


text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((200, 200), (200, 50)),
                                                 manager=MANAGER, object_id="#main_text_entry")


def draw_text(text, size, x, y):
    font = pygame.font.SysFont("Calibri", size)
    img = font.render(text, True, BLACK)
    screen.blit(img, (x, y))


result = random.randint(1, 100)
attempts = 0
max_attempts = 10
message = "Guess a number between 1 and 100"
guess_tries = []

def process_guess(text):
    global attempts, message, result, guess_tries
    

    if not text.isdigit():
        message = "Enter a number between 1 and 100: "
        return

    guess = int(text)

    if not (1 <= guess <= 100):
        message = "Enter a number between 1 and 100: "
        return

    attempts += 1
    guess_tries.append(guess)

    if guess < result:
        message = f"the number {guess} is low!"
    elif guess > result:
        message = f"the number {guess} is high!"
    else:
        message = f"Congratulation! The number is: {result}"
        return

    if attempts >= max_attempts:
        message = f"Game over! The number was: {result}"

def random_game():
    global message

    while True:
        UI_REFRESH_RATE = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

     
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                if event.ui_object_id == "#main_text_entry":
                    process_guess(event.text)
                    text_input.set_text("")  

            MANAGER.process_events(event)

        MANAGER.update(UI_REFRESH_RATE)

      
        screen.fill(WHITE)

        draw_text("Number Guessing Game", 30, 120, 50)
        draw_text(message, 20, 120, 120)
        draw_text(f"Attempts: {attempts}/{max_attempts}", 20, 200, 160)

      
        tries_text = "Your previous attemps: " + ", ".join(map(str, guess_tries[-5:]))
        draw_text(tries_text, 20, 120, 320)

        MANAGER.draw_ui(screen)

        pygame.display.update()



random_game()
