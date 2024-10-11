import time
import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for count in range(5):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {count + 1} шар.')
    print(f'Силач {name} закончил соревнования')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Паша', 3))
    task2 = asyncio.create_task(start_strongman('Денис', 4))
    task3 = asyncio.create_task(start_strongman('Аполлон', 5))
    await task1
    await task2
    await task3


asyncio.run(start_tournament())
