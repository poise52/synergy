from datetime import datetime

def is_leap_year(year):
    """Определяет, является ли год високосным."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_day_of_week(day, month, year):
    """Определяет день недели для заданной даты."""
    date = datetime(year, month, day)
    days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    return days[date.weekday()]

def calculate_age(day, month, year):
    """Вычисляет возраст пользователя."""
    today = datetime.today()
    birthday_this_year = datetime(today.year, month, day)
    age = today.year - year
    if today < birthday_this_year:
        age -= 1
    return age

def print_number_as_stars(number):
    """Прорисовывает цифры числа звёздочками."""
    digits = {
        '0': [" *** ", "*   *", "*   *", "*   *", " *** "],
        '1': ["  *  ", " **  ", "  *  ", "  *  ", " *** "],
        '2': [" *** ", "    *", " *** ", "*    ", " *** "],
        '3': [" *** ", "    *", " *** ", "    *", " *** "],
        '4': ["*   *", "*   *", " *** ", "    *", "    *"],
        '5': [" *** ", "*    ", " *** ", "    *", " *** "],
        '6': [" *** ", "*    ", " *** ", "*   *", " *** "],
        '7': [" *** ", "    *", "    *", "    *", "    *"],
        '8': [" *** ", "*   *", " *** ", "*   *", " *** "],
        '9': [" *** ", "*   *", " *** ", "    *", " *** "],
    }
    lines = [""] * 5
    for digit in str(number):
        for i in range(5):
            lines[i] += digits[digit][i] + "  "
    for line in lines:
        print(line)

def print_birth_date(day, month, year):
    """Выводит дату рождения в формате дд мм гггг звёздочками."""
    print("Дата рождения в формате дд мм гггг:")
    print_number_as_stars(f"{day:02}{month:02}{year}")

# Основная программа
if __name__ == "__main__":
    # Запрашиваем дату рождения у пользователя
    day = int(input("Введите день вашего рождения (число): "))
    month = int(input("Введите месяц вашего рождения (число): "))
    year = int(input("Введите год вашего рождения (число): "))

    # День недели
    day_of_week = get_day_of_week(day, month, year)
    print(f"Вы родились в {day_of_week}.")

    # Високосный год или нет
    leap_year = is_leap_year(year)
    print(f"Ваш год рождения {'високосный' if leap_year else 'не високосный'}.")

    # Возраст пользователя
    age = calculate_age(day, month, year)
    print(f"Вам сейчас {age} лет.")

    # Вывод даты рождения звёздочками
    print_birth_date(day, month, year)