def get_day_of_week():
    days = {
        1: "Понеділок",
        2: "Вівторок",
        3: "Середа",
        4: "Четвер",
        5: "П'ятниця",
        6: "Субота",
        7: "Неділя"
    }

    try:
        number = int(input("Введіть номер дня тижня (1-7): "))
        
        if number in days:
            print(f"Це {days[number]}.")
        elif number >= 8 or number <= 0:
            print("Помилка: у тижні лише 7 днів. Введіть число від 1 до 7.")
            
    except ValueError:
        print("Помилка: ви ввели нечислові дані. Будь ласка, введіть цифру.")

get_day_of_week()