import asyncio
# import typing
import typing

AwaitableFunction = typing.Awaitable[typing.Any]
# from utils.funcs.aliases import AwaitableFunction

async def run_sequence(*functions: AwaitableFunction) -> None:
    for function in functions:
        await function

async def run_parrell(*functions: AwaitableFunction) -> None:
    await asyncio.gather(*functions)