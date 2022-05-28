def progress_bar(initial_value: int, total: int) -> None:
    """Decorator to display a progress bar when a function runs."""
    percent = int(100 * (initial_value / float(total)))
    bar = "█" * percent + "-" * (100 - percent)
    print(f"\r|{bar}| {percent:.2f}%", end="\r")