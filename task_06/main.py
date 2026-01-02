def greedy_algorithm(items, budget):
    """
    Жадібний алгоритм: вибирає страви з найкращим співвідношенням калорій до вартості.
    """
    # 1. Перетворюємо словник у список для зручності
    items_list = []
    for name, details in items.items():
        ratio = details["calories"] / details["cost"]
        items_list.append({
            "name": name,
            "cost": details["cost"],
            "calories": details["calories"],
            "ratio": ratio
        })

    # 2. Сортуємо список за спаданням ratio
    items_list.sort(key=lambda x: x["ratio"], reverse=True)

    total_calories = 0
    total_cost = 0
    chosen_items = []

    # 3. Набираємо їжу
    for item in items_list:
        if total_cost + item["cost"] <= budget:
            chosen_items.append(item["name"])
            total_cost += item["cost"]
            total_calories += item["calories"]

    return chosen_items, total_calories, total_cost


def dynamic_programming(items, budget):
    """
    Динамічне програмування: знаходить оптимальний набір для макс. калорійності.
    Підхід 0/1 Knapsack Problem.
    """
    # Підготовка даних: перетворюємо на списки для індексації
    item_names = list(items.keys())
    costs = [items[name]["cost"] for name in item_names]
    calories = [items[name]["calories"] for name in item_names]
    n = len(items)

    # 1. Створення таблиці DP (K)
    # K[i][w] буде зберігати макс. калорії для перших i предметів при бюджеті w
    K = [[0 for w in range(budget + 1)] for i in range(n + 1)]

    # 2. Заповнення таблиці
    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            cost = costs[i - 1]
            cal = calories[i - 1]

            if cost <= w:
                # Вибір: або беремо цей предмет (тоді додаємо його калорії до макс. знач. для залишку бюджету),
                # або не беремо (залишаємо значення з попереднього рядка)
                K[i][w] = max(cal + K[i - 1][w - cost], K[i - 1][w])
            else:
                # Предмет задорогий для поточного бюджету w
                K[i][w] = K[i - 1][w]

    # 3. Backtracking
    chosen_items = []
    w = budget
    for i in range(n, 0, -1):
        # Якщо значення відрізняється від того, що прямо над ним,
        # значить ми взяли цей предмет (i-1, бо індекси зміщені)
        if K[i][w] != K[i - 1][w]:
            item_name = item_names[i - 1]
            chosen_items.append(item_name)
            w -= costs[i - 1]

    # Повертаємо загальні калорії (остання клітинка таблиці) та список страв
    return chosen_items, K[n][budget]



if __name__ == "__main__":
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    test_budget = 100

    print(f"Бюджет: {test_budget}\n")

    # 1. Жадібний алгоритм
    greedy_items, greedy_cal, greedy_cost = greedy_algorithm(items, test_budget)
    print("--- Жадібний алгоритм ---")
    print(f"Обрані страви: {greedy_items}")
    print(f"Калорійність: {greedy_cal}")
    print(f"Витрачено: {greedy_cost}")

    print("\n" + "-"*30 + "\n")

    # 2. Динамічне програмування
    dp_items, dp_cal = dynamic_programming(items, test_budget)
    # Рахуємо вартість для виводу (хоча для алгоритму це не обов'язково повертати)
    dp_cost = sum(items[i]["cost"] for i in dp_items)
    
    print("--- Динамічне програмування ---")
    print(f"Обрані страви: {dp_items}")
    print(f"Калорійність: {dp_cal}")
    print(f"Витрачено: {dp_cost}")