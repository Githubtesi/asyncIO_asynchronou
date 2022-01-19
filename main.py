# -*- coding: utf-8 -*-
# Created by yoshiaki at 2022/01/20
import asyncio


async def main():
    task = asyncio.create_task(other_function())
    print("A")
    await asyncio.sleep(5)
    print("B")
    return_value = await task
    print(f"Return value was {return_value}")


async def other_function() -> int:
    print("1")
    await asyncio.sleep(2)
    print("2")
    return 10


asyncio.run(main())
