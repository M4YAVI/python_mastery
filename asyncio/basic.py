import asyncio

async def waiter():
    print("what do you want??")
    await asyncio.sleep(5)  # Pause for 5 second
    print("want more call me again")
    
asyncio.run(waiter())
