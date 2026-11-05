
from pathlib import Path


def list_files(folder: Path) -> list[Path]:
    """
    Lists all files inside a directory.

    Args:
        folder: Directory to be scanned.

    Returns:
        A list containing the files found.
    """

    # Validate directory
    if not folder.exists():
        print(f"[ERROR] Folder not found: {folder}")
        return []

    if not folder.is_dir():
        print(f"[ERROR] Path is not a directory: {folder}")
        return []

    # Collect files
    files = []

    for item in folder.iterdir():
        if item.is_file():
            files.append(item)

    # Sort files alphabetically
    files.sort(key=lambda file: file.name.lower())

    return files

