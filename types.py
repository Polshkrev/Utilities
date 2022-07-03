from typing import Callable, Awaitable, Any

JSON = int | str | float | bool | None | dict[str, "JSON"] | list["JSON"]
JSONObject = dict[str, JSON]
JSONList = list[JSON]

ComposableFunction = Callable[..., Any]
AwaitableFunction = Awaitable[Any]