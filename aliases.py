import typing

JSON = int | str | float | bool | None | dict[str, "JSON"] | list["JSON"]
JSONObject = dict[str, JSON]
JSONList = list[JSON]

ComposableFunction = typing.Callable[..., typing.Any]
AwaitableFunction = typing.Awaitable[typing.Any]