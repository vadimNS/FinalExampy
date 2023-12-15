import matplotlib.pyplot as plt

def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    return fibonacci_sequence

def generate_primes(n):
    primes = []
    i = 2
    while len(primes) < n:
        is_prime = all(i % p != 0 for p in primes)
        if is_prime:
            primes.append(i)
        i += 1
    return primes

def generate_arithmetic(start, end, step, n):
    arithmetic_sequence = [start + i * step for i in range(n)]
    return arithmetic_sequence

def plot_sequence(sequence, sequence_type):
    plt.plot(sequence, marker='o')
    plt.title(f'{sequence_type} Sequence')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.show()

def main():
    print("Виберіть тип послідовності:")
    print("1. Фібоначчі")
    print("2. Прості числа")
    print("3. Арифметична")

    choice = input("Ваш вибір (1, 2 або 3): ")

    try:
        choice = int(choice)
        if choice not in [1, 2, 3]:
            raise ValueError("Введіть 1, 2 або 3.")
    except ValueError as e:
        print(f"Помилка: {e}")
        return

    n = int(input("Введіть довжину послідовності: "))
    start = int(input("Введіть початкове число: "))
    end = int(input("Введіть кінцеве число: "))

    if choice == 1:
        sequence = generate_fibonacci(n)
        sequence_type = "Фібоначчі"
    elif choice == 2:
        sequence = generate_primes(n)
        sequence_type = "Прості числа"
    else:
        step = int(input("Введіть крок арифметичної послідовності: "))
        sequence = generate_arithmetic(start, end, step, n)
        sequence_type = "Арифметична"

    filtered_sequence = [x for x in sequence if start <= x <= end]

    print(f"{sequence_type} Послідовність:")
    print(sequence)
    print(f"Послідовність у діапазоні [{start}, {end}]:")
    print(filtered_sequence)

    plot_sequence(sequence, sequence_type)

if __name__ == "__main__":
    main()
