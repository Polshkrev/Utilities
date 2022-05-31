def progress_bar(iteration: int, total: int, prefix: str, suffix: str, decimals: int = 2, length = 100, fill: str = "█") -> None:
    """Display a progress bar when a function runs."""
    percent = f"{100 * iteration / float(total):.{decimals}f}"
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + "-" * (length - filled_length)
    print(f"\r{prefix} |{bar}| {percent}% {suffix}", end="\r")
