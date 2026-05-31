import random

# ─────────────────────────────────────────
#  Функция для генерации одного уравнения
#  вида  a*x + b = c,  где x — целое число
# ─────────────────────────────────────────
def generate_equation():
    a = random.randint(-9, 9) or 1    # коэффициент при x (от -9 до 9, не 0)
    x = random.randint(-10, 10)       # целое решение, которое мы задаём заранее
    b = random.randint(-20, 20)       # свободный член

    c = a * x + b                     # вычисляем правую часть так, чтобы x было решением

    return a, b, c, x                 # возвращаем все части уравнения и ответ


# ─────────────────────────────────────────
#  Функция красивого вывода уравнения
# ─────────────────────────────────────────
def format_equation(a, b, c):
    # Обрабатываем знак b, чтобы уравнение выглядело аккуратно
    # Формируем часть с 'ax'
    if a == 1:
        ax_part = "x"
    elif a == -1:
        ax_part = "-x"
    else:
        ax_part = f"{a}x"

    # Формируем часть с 'b'
    if b > 0:
        b_part = f"+ {b}"
    elif b < 0:
        b_part = f"- {abs(b)}"
    else:
        b_part = ""              # если b == 0, не выводим его вовсе

    if b_part:
        return f"{ax_part} {b_part} = {c}"
    else:
        return f"{ax_part} = {c}"


# ─────────────────────────────────────────
#  Основная программа
# ─────────────────────────────────────────
def main():
    total_questions = 10   # количество задач
    correct = 0            # счётчик правильных ответов

    print("=" * 40)
    print("  Тренажёр: линейные уравнения")
    print("  Найдите x в каждом уравнении")
    print("=" * 40)
    print()

    for i in range(1, total_questions + 1):
        # Генерируем новое уравнение
        a, b, c, answer = generate_equation()
        equation = format_equation(a, b, c)

        print(f"Задача {i}/{total_questions}: {equation}")

        # Просим пользователя ввести ответ
        # Цикл повторяется, если введено не число
        while True:
            user_input = input("  Ваш ответ (x = ): ").strip()
            if user_input.lstrip("-").isdigit():   # проверяем, что введено целое число
                user_answer = int(user_input)
                break
            else:
                print("  ⚠ Введите целое число!")

        # Проверяем ответ
        if user_answer == answer:
            print("  ✅ Верно!\n")
            correct += 1
        else:
            print(f"  ❌ Неверно. Правильный ответ: x = {answer}\n")

    # ─────────────────────────────────────
    #  Итоговый результат
    # ─────────────────────────────────────
    print("=" * 40)
    print(f"  Результат: {correct} из {total_questions}")

    # Оценка в зависимости от результата
    if correct == total_questions:
        print("  🏆 Отлично! Все задачи решены верно!")
    elif correct >= 7:
        print("  👍 Хороший результат!")
    elif correct >= 4:
        print("  📚 Неплохо, но есть над чем поработать.")
    else:
        print("  💪 Не сдавайтесь, практикуйтесь больше!")

    print("=" * 40)


# Запускаем программу
if __name__ == "__main__":
    main()
