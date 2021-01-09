# Урок 8: asyncio - конкурентность без потоков

import asyncio
import time


# async def создает корутину - функцию, которую можно ставить на паузу
async def download(name, seconds):
    print(f"начали {name}")
    # await asyncio.sleep имитирует ожидание сети.
    # В этот момент управление отдается другим корутинам
    await asyncio.sleep(seconds)
    print(f"закончили {name}")
    return f"данные {name}"


# Последовательно: время складывается
async def sequential():
    start = time.monotonic()
    await download("страницу 1", 1)
    await download("страницу 2", 1)
    await download("страницу 3", 1)
    print(f"последовательно: {time.monotonic() - start:.1f} сек")


# Конкурентно: gather запускает все сразу,
# общее время равно самой долгой задаче
async def concurrent():
    start = time.monotonic()
    results = await asyncio.gather(
        download("страницу 1", 1),
        download("страницу 2", 1),
        download("страницу 3", 1),
    )
    print(f"конкурентно: {time.monotonic() - start:.1f} сек")
    print(results)


# Важно понимать: asyncio не делает код параллельным.
# Работает по-прежнему один поток, но пока одна задача ЖДЕТ
# (сеть, диск, таймер), другая работает. Для тяжелых вычислений
# asyncio не поможет - там нужен multiprocessing
asyncio.run(sequential())
asyncio.run(concurrent())
