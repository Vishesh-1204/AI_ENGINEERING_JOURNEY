import asyncio
async def hello():
    print("Hello, World!")

asyncio.run(hello())

async def second():
    print("SECOND")
    await asyncio.sleep(2)
    print("SECOND DONE")

# asyncio.run(second())

async def third():
    print("THIRD")
    await asyncio.sleep(2)
    print("THIRD DONE")

# asyncio.run(third())

async def main():
    await asyncio.gather(second(), third())

asyncio.run(main())
