import asyncio
import time


async def worker(worker_id, semaphore):
    """Корутина, которая запрашивает доступ к ресурсу через семафор."""
    async with semaphore:  # захватываем "слот" — максимум 2 одновременно
        print(f"[{time.strftime('%H:%M:%S')}] worker-{worker_id}: начал работу")
        await asyncio.sleep(2)  # имитация полезной работы
        print(f"[{time.strftime('%H:%M:%S')}] worker-{worker_id}: закончил")
    # здесь слот освобождён


async def main():
    semaphore = asyncio.Semaphore(2)  # максимум 2 задачи одновременно

    start = time.perf_counter()

    # Запускаем все 5 корутин одновременно
    tasks = [
        asyncio.create_task(worker(i, semaphore), name=f"worker-{i}")
        for i in range(1, 6)
    ]

    # Ждём завершения всех
    await asyncio.gather(*tasks)

    elapsed = time.perf_counter() - start
    print(f"\nВремя выполнения: {elapsed:.2f} сек")


if __name__ == "__main__":
    asyncio.run(main())