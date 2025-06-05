import asyncio
import time 
async def task1():
    print("task Just started")
    await asyncio.sleep(3)
    print("task Just completed")
    return "Done"
    
async def task2():
    print("New task Just started")
    await asyncio.sleep(3)
    print("New task is Completed")
    return "Done"
    
async def main():
    start_time = time.time()
    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())
    
    r1 = await t1
    r2 = await t2
    print(f"Total time: {time.time() - start_time:.2f} seconds")
    
asyncio.run(main())
