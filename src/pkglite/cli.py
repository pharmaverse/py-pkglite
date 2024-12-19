from rich import print as rprint


def print_action(action: str, target: str) -> None:
    """
    Print a main action being performed.

    Args:
        action: The action being performed, for example, "Packing", "Unpacking".
        target: The target of the action, for example, package name.
    """
    rprint(f"[bold]{action}[/bold] [bold blue]{target}[/bold blue]")


def print_sub_action(action: str, path: str, path_type: str = "source") -> None:
    """
    Print a subordinate action being performed.

    Args:
        action: The sub-action being performed, for example, "Packing", "Unpacking".
        path: The file or directory path being processed.
        path_type: Type of path - "source" or "target". Default is "source".
    """
    color = "green" if path_type == "source" else "cyan"
    rprint(f"[dim]{action}[/dim] [{color}]{path}[/{color}]")


def print_success(message: str) -> None:
    """
    Print a success message with a checkmark.

    Args:
        message: The success message to print.
    """
    rprint(f"[bold green]✓[/bold green] {message}")


def print_warning(message: str) -> None:
    """
    Print a warning message with a warning symbol.

    Args:
        message: The warning message to print.
    """
    rprint(f"[bold yellow]⚠[/bold yellow] {message}")


def format_path(path: str, path_type: str = "target") -> str:
    """
    Format a path string with highlighting.

    Args:
        path: The path to format.
        path_type: Type of path - "source" or "target". Default is "target".

    Returns:
        The formatted path string with rich markup.
    """
    color = "green" if path_type == "source" else "cyan"
    return f"[{color}]{path}[/{color}]"


def format_count(count: int) -> str:
    """
    Format a count number with highlighting.

    Args:
        count: The number to format.

    Returns:
        The formatted number string with rich markup.
    """
    return f"[blue]{count}[/blue]"
