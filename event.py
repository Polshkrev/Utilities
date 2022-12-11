import typing

_subscribers: dict[str, list[typing.Callable]] = dict()

def subscribe(event_type: str, function: typing.Callable) -> None:
    """Subscribes to an event."""
    if not event_type in _subscribers:
        _subscribers[event_type] = []
    _subscribers[event_type].append(function)

def post_event(event_type: str, data: typing.Any) -> None:
    """Posts an event with given data."""
    if not event_type in _subscribers:
        return
    for function in _subscribers[event_type]:
        function(data)