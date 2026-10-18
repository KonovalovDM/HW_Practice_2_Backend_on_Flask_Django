import asyncio
import time


async def api_call_1():
    """Имитация первого API-запроса — задержка 2 секунды."""
    print(f"[{time.strftime('%H:%M:%S')}] api_call_1: запрос отправлен")
    await asyncio.sleep(2)
    print(f"[{time.strftime('%H:%M:%S')}] api_call_1: ответ получен")
    return {"service": "api_1", "status": "ok", "data": "users"}


async def api_call_2():
    """Имитация второго API-запроса — задержка 1 секунда."""
    print(f"[{time.strftime('%H:%M:%S')}] api_call_2: запрос отправлен")
    await asyncio.sleep(1)
    print(f"[{time.strftime('%H:%M:%S')}] api_call_2: ответ получен")
    return {"service": "api_2", "status": "ok", "data": "orders"}


async def main():
    start = time.perf_counter()

    # Создаём задачи — обе стартуют одновременно
    task1 = asyncio.create_task(api_call_1())
    task2 = asyncio.create_task(api_call_2())

    # Ждём завершения обеих и собираем результаты
    result1 = await task1
    result2 = await task2

    elapsed = time.perf_counter() - start
    print(f"\nВремя выполнения: {elapsed:.2f} сек")
    print(f"Результат 1: {result1}")
    print(f"Результат 2: {result2}")


if __name__ == "__main__":
    asyncio.run(main())
