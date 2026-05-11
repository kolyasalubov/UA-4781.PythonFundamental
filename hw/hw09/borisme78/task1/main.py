'''
Завдання 1. Напишіть сценарій гри, який випадковим чином генерує число в діапазоні від
1 до 100 і пропонує користувачеві вгадати це число за 10 спроб.

Програма зчитує введені користувачем числа та запитує його,
чи вгадане число більше чи менше за введене
користувачем. Гра повинна тривати доти, доки користувач не використає 10 спроб і не вгадає
число. Якщо користувач вгадав число, програма виводить
повідомлення з поздоровленням, а якщо 10 спроб вичерпано, а користувач
не встиг вгадати число, то виводиться відповідне повідомлення.

(для виконання завдання потрібно імпортувати модуль random,

а з нього — функцію randint()) softserve
'''
import pygame
import random
# Початкові налаштування програми 
pygame.init()
width_display = 500
height_display = 500
screen = pygame.display.set_mode((width_display, height_display))
pygame.display.set_caption('Guess the number')
icon = pygame.image.load("hw9/task1/images/icon.png").convert_alpha()
pygame.display.set_icon(icon)
clock = pygame.time.Clock()


# Основні змінні та обєкти програми 
GREY = (200, 200, 200)
bg = pygame.image.load("hw9/task1/images/bg.jpg").convert() 
font = pygame.font.SysFont('Arial', 15)
guess_label = font.render("Guess the number between 1 and 100", True, (GREY))
input_label = font.render("Enter your guess: ", True, (GREY))
result_label = font.render("", True, (255, 255, 255))
number_to_guess = 21
user_text = ''
attempts = 10
user_text  = ""
active = False

input_rect = pygame.Rect(169, 139, 200, 40)

# Цикл створенння програми 
running = True
while running:
   
    

    screen.blit(bg, (0, 0))


    



    for event in pygame.event.get():
        # завершення програми при натисканні на хрестик
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        
        
        
        # обробка вводу користувача
        # Відображення введеного тексту користувача
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False

        
        # дозволяє користувачеві вводити текст за допомогою клавіатури
        if event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += event.unicode
        
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and active:
            if user_text.strip().isdigit():
                user_number = int(user_text)
                if user_number < number_to_guess:
                    result_label = font.render("Number is greater than your guess", True, (255, 255, 255))
                elif user_number > number_to_guess:
                    result_label = font.render("Number is less than your guess", True, (255, 255, 255))
                else:
                    result_label = font.render("Congratulations! You guessed the number!", True, (255, 255, 255))
            else:
                result_label = font.render("Please enter a valid number", True, (255, 255, 255))
            attempts -= 1
            if attempts == 0:
                result_label = font.render(f"Game Over! The number was {number_to_guess}", True, (255, 255, 255))
                active = False
            user_text = ""
       
       
    text_surface = font.render(user_text, True, (255, 255, 255))
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

    pygame.draw.rect(screen, GREY, input_rect, 2)

    screen.blit(guess_label, (50, 50))
    screen.blit(input_label, (50, 150))
    screen.blit(result_label, (50, 250))
    pygame.display.update()
    clock.tick(60)

