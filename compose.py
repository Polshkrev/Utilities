import functools
from typing import Callable, Any

ComposableFunction = Callable[..., Any]

def compose(*functions: ComposableFunction) -> ComposableFunction:
    return functools.reduce(lambda f, g: lambda x: g(f(x)), functions)