import functools
import typing

ComposableFunction = typing.Callable[..., typing.Any]
# from .aliases import ComposableFunction

def compose(*functions: ComposableFunction) -> ComposableFunction:
    """Ruduces composeable functions."""
    return functools.reduce(lambda f, g: lambda x: g(f(x)), functions)

def args(*arguments: str) -> list[str]:
    """Composes args to be used in the subprocess module."""
    return [arg for arg in arguments]