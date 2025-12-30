import asyncio
async def brew(name):
    print(f"Brewing {name}...")
    await asyncio.sleep(2)
    print(f"{name} brewed!")

async def main():
    await asyncio.gather(
        brew("Masala chai"),
        brew("Green chai"),
        brew("Black chai")
        )

asyncio.run(main())
