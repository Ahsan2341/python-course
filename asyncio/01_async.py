import asyncio

async def brew_chai():
    print("Brewing chai...")
    await asyncio.sleep(2)
    print("Chai brewed!")

asyncio.run(brew_chai())