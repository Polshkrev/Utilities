import time
from typing import Any, Optional
import colorama

Progressable = list[Any] | dict[Any, Any]
Interval = int | float

def progress_bar(target: Progressable, interval: Interval = 0.01, prefix: Optional[str] = None, suffix: Optional[str] = None, decimals: int = 2, length = 100, fill: str = "█", colour: str = colorama.Fore.WHITE) -> None:
    """Display a progress bar when a function runs."""
    def _bar(progress: int, total: int):
        percent = f"{100 * progress / float(total):.{decimals}f}"
        filled_length = int(length * progress // total)
        bar = fill * filled_length + "-" * (length - filled_length)
        print(colour + f"\r{prefix}|{bar}| {percent}% {suffix}", end="\r")
        try:
            if progress == total:
                print(colorama.Fore.GREEN + f"\r{prefix}|{bar}| {percent}% {suffix}", end="\r")
        except Exception as e:
                print(colorama.Fore.RED + f"\r{prefix}|{bar}| {percent}% {suffix}", end="\r")
                print(e)
    _bar(0, len(target))
    for index, _ in enumerate(target):
        time.sleep(interval)
        _bar(index + 1, len(target))
    print(colorama.Fore.RESET)