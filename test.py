import asyncio
import cleverbotfree

def chat():
    """Example code using cleverbotfree sync api."""
    with cleverbotfree.sync_playwright() as p_w:
        c_b = cleverbotfree.Cleverbot(p_w)
        while True:
            user_input = input("User: ")
            if user_input == 'quit':
                break
            bot = c_b.single_exchange(user_input)
            print('Cleverbot:', bot)
        c_b.close()

chat()


# async def async_chat():
#     """Example code using cleverbotfree async api."""
#     async with cleverbotfree.async_playwright() as p_w:
#         c_b = await cleverbotfree.CleverbotAsync(p_w)
#         while True:
#             user_input = input("User: ")
#             if user_input == 'quit':
#                 break
#             bot = await c_b.single_exchange(user_input)
#             print('Cleverbot:', bot)
#         await c_b.close()

# asyncio.run(async_chat())