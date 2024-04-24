import asyncio


# async def func():
#     print("Inside the function")
#     await asyncio.sleep(1)
#     print("Another statement")
#     await asyncio.sleep(1)
#     print("Async function")


# asyncio.run(func())


# ********Async event loop in python*********

# async def f1():
#     print("One")
#     await asyncio.sleep(1)
#     await f2()
#     print("four")
#     await asyncio.sleep(1)
#     print("five")
#     await asyncio.sleep(1)


# async def f2():
#     await asyncio.sleep(1)
#     print("two")
#     await asyncio.sleep(1)
#     print("three")


# asyncio.run(f1())



# **************actually making the code asynchronous 

# async def f1():
#     task = asyncio.create_task(f2())
#     print("One")
#     print("four")
#     await asyncio.sleep(1)
#     print("five")
#     await asyncio.sleep(1)


# async def f2():
#     print("two")
#     await asyncio.sleep(1)
#     print("three")


# asyncio.run(f1())


#******************I/O bound tasks using aysncio.sleep()

async def f1():
    print("f1 started")
    await asyncio.sleep(1)
    print("f1 ended")

async def f2():
    print("f2 started")
    await asyncio.sleep(1)
    print("f2 ended")


async def f3():
    print("f3 started")
    await asyncio.sleep(1)
    print("f3 ended")

async def main():
    L = await asyncio.gather(f1(), f2(), f3())
    print("Main ended")


asyncio.run(main())