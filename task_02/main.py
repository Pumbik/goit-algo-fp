import turtle
import math

def draw_pythagoras_tree(t, branch_len, level):
    """
    Рекурсивна функція для малювання фрактала.
    
    Аргументи:
    t -- об'єкт черепашки (turtle)
    branch_len -- довжина гілки
    level -- поточний рівень рекурсії (глибина)
    """
    
    # 1. Базовий випадок
    if level == 0:
        return

    if level < 3:
        t.color("green")
    else:
        t.color("brown")
        
    t.pensize(level)

    # 2. стовбур
    t.forward(branch_len)

    # 3. розгалуження  (градус 45)
    angle = 45 
    
    # Коефіцієнт math.sqrt(2)/2 ≈ 0.707 - класичний для дерева Піфагора
    reduction_factor = math.sqrt(2) / 2

    # 4. Права гілка
    t.right(angle)
    draw_pythagoras_tree(t, branch_len * reduction_factor, level - 1)

    # 5. Ліва гілка  (90 градусів від поточного)
    t.left(angle * 2)
    draw_pythagoras_tree(t, branch_len * reduction_factor, level - 1)

    # 6. Повернення назад
    t.right(angle)
    
    # Відновлюємо колір
    if level < 3:
        t.color("green")
    else:
        t.color("brown")
        
    # Повертаємося в початок гілки
    t.backward(branch_len)

def main():
    try:
        user_input = input("Введіть рівень рекурсії (рекомендовано 6-10): ")
        recursion_level = int(user_input)
        if recursion_level < 0:
            print("Рівень має бути додатним числом.")
            return
    except ValueError:
        print("Будь ласка, введіть ціле число.")
        return

    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title(f"Дерево Піфагора (Рівень {recursion_level})")

    t = turtle.Turtle()
    t.speed(0)      # 0 - це максимальна швидкість
    t.left(90)      # Повертаємо черепашку головою вгору
    t.up()          # Піднімаємо перо
    t.goto(0, -200) # Переміщуємо в низ екрану
    t.down()        # Опускаємо перо

    print("Починаю малювати...")
    
    # Запуск рекурсії.
    draw_pythagoras_tree(t, 100, recursion_level)

    print("Готово! Клікніть по вікну, щоб закрити.")
    screen.exitonclick()

if __name__ == "__main__":
    main()