import asyncio
import time


async def api_call_1():
    """Имитация первого API-запроса — задержка 2 секунды."""
    print(f"[{time.strftime('%H:%M:%S')}] api_call_1: старт")
    await asyncio.sleep(2)
    print(f"[{time.strftime('%H:%M:%S')}] api_call_1: финиш")
    return {"service": "api_1", "status": "ok", "data": "users"}


async def api_call_2():
    """Имитация второго API-запроса — задержка 1 секунда."""
    print(f"[{time.strftime('%H:%M:%S')}] api_call_2: старт")
    await asyncio.sleep(1)
    print(f"[{time.strftime('%H:%M:%S')}] api_call_2: финиш")
    return {"service": "api_2", "status": "ok", "data": "orders"}


async def main():
    # Создаём задачи — обе стартуют одновременно
    task1 = asyncio.create_task(api_call_1(), name="api-1")
    task2 = asyncio.create_task(api_call_2(), name="api-2")

    # ----- 1. Проверка статуса сразу после создания -----
    print("Статусы сразу после create_task:")
    print(f"  task1.done() = {task1.done()}")   # False
    print(f"  task2.done() = {task2.done()}")   # False

    # Дадим event loop немного поработать
    await asyncio.sleep(0)
    print("Статусы после asyncio.sleep(0):")
    print(f"  task1.done() = {task1.done()}")   # всё ещё False
    print(f"  task2.done() = {task2.done()}")   # всё ещё False

    # ----- 2. Получаем результаты по мере завершения -----
    print("\nПолучаем результаты через as_completed():")
    for finished_task in asyncio.as_completed([task1, task2]):
        result = await finished_task
        print(f"  Готово: {result}")

    # ----- 3. Проверка статуса после завершения -----
    print("\nСтатусы после завершения:")
    print(f"  task1.done() = {task1.done()}")       # True
    print(f"  task2.done() = {task2.done()}")       # True
    print(f"  task1.cancelled() = {task1.cancelled()}")  # False
    print(f"  task1.result() = {task1.result()}")   # можно получить напрямую
    print(f"  task2.result() = {task2.result()}")


if __name__ == "__main__":
    asyncio.run(main())