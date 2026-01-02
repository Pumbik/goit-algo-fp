import random
import matplotlib.pyplot as plt

def get_analytical_probabilities():
    """
    Розраховує теоретичні імовірності для сум двох кубиків.
    Всього комбінацій: 6 * 6 = 36.
    """
    # Рахуємо кількість способів отримати кожну суму
    counts = {s: 0 for s in range(2, 13)}
    for d1 in range(1, 7):
        for d2 in range(1, 7):
            counts[d1 + d2] += 1
    
    # Переводимо у відсотки (імовірності)
    probabilities = {s: count / 36 for s, count in counts.items()}
    return probabilities

def monte_carlo_simulation(num_experiments):
    """
    Симулює кидання двох кубиків num_experiments разів.
    """
    # Лічильник для сум від 2 до 12
    sum_counts = {s: 0 for s in range(2, 13)}

    for _ in range(num_experiments):
        # Кидаємо два кубики
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2

        sum_counts[total] += 1

    # Обчислюємо імовірності
    simulated_probs = {s: count / num_experiments for s, count in sum_counts.items()}
    return simulated_probs


if __name__ == "__main__":
    # 1. кількість експериментів (чим більше, тим точніше)
    N = 1_000_000
    print(f"Запуск симуляції Монте-Карло на {N} кидків...")

    # 2. результати
    simulated = monte_carlo_simulation(N)
    analytical = get_analytical_probabilities()

    # 3. Виводимо таблицю результатів
    print("\n" + "="*55)
    print(f"{'Сума':<6} | {'Імовірність (Монте-Карло)':<25} | {'Імовірність (Теорія)':<20}")
    print("-" * 55)
    
    for s in range(2, 13):
        mc_val = simulated[s] * 100
        an_val = analytical[s] * 100
        # Виводимо у відсотках з точністю до двох знаків
        print(f"{s:<6} | {mc_val:.2f}% ({simulated[s]:.4f})      | {an_val:.2f}% ({analytical[s]:.4f})")
    
    print("="*55)

    # 4. Побудова графіка
    sums = list(range(2, 13))
    sim_values = [simulated[s] for s in sums]
    an_values = [analytical[s] for s in sums]

    plt.figure(figsize=(10, 6))
    
    # Малюємо теоретичні значення як лінію або точки
    plt.plot(sums, an_values, color='red', marker='o', linestyle='dashed', linewidth=2, label='Теоретична імовірність')
    
    # Малюємо результати симуляції як стовпчики
    plt.bar(sums, sim_values, color='skyblue', alpha=0.7, label='Монте-Карло')

    plt.xlabel('Сума на кубиках')
    plt.ylabel('Імовірність')
    plt.title(f'Імовірність випадіння сум (Monte Carlo: {N} спроб)')
    plt.xticks(sums)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.show()