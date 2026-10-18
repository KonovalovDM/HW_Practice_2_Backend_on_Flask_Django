import threading
import time


def long_task(name):
    """Блокирующая операция: спит и выводит результат."""
    print(f"[{time.strftime('%H:%M:%S')}] {name}: старт")
    time.sleep(2 if name == "task-1" else 1)
    print(f"[{time.strftime('%H:%M:%S')}] {name}: финиш")
    return f"{name} завершена"


def main():
    start = time.perf_counter()

    # Создаём потоки, передаём аргументы через args
    thread1 = threading.Thread(target=long_task, args=("task-1",), name="Thread-1")
    thread2 = threading.Thread(target=long_task, args=("task-2",), name="Thread-2")

    # Запускаем оба потока
    thread1.start()
    thread2.start()

    # Дожидаемся завершения обоих
    thread1.join()
    thread2.join()

    elapsed = time.perf_counter() - start
    print(f"\nВремя выполнения: {elapsed:.2f} сек")


if __name__ == "__main__":
    main()