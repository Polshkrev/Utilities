from typing import Any, Callable, Protocol

import importlib

_registration: dict[str, Callable[..., Any]] = {}

def register(type: str, initializer: Callable[..., Any]) -> None:
    """Register a new class type."""
    _registration[type] = initializer

def unregister(type: str) -> None:
    """Unregister a class type."""
    _registration.pop(type, None)

def create(arguments: dict[str, Any]) -> Callable[..., Any]:
    """Create a class of a specific type, given a dictionary of arguments."""
    args_copy = arguments.copy()
    type = args_copy.pop("type")
    try:
        initializer = _registration[type]
        return initializer(**args_copy)
    except KeyError:
        raise ValueError(f"Unknown registration type {type}") from None

class Interface(Protocol):
    
    @staticmethod
    def initialize() -> None:
        """Initializes the interface."""

def _import_module(name: str) -> Interface:
    return importlib.import_module(name) #type: ignore

def load_modules(modules: list[str]) -> None:
    for module in modules:
        imported_module = _import_module(module)
        imported_module.initialize()