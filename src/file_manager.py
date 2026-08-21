import shutil
from pathlib import Path


def move_file(source_file, destination_folder):

    source = Path(source_file)

    destination_directory = Path(
        destination_folder
    )

    destination_directory.mkdir(
        parents=True,
        exist_ok=True
    )

    destination = (
        destination_directory / source.name
    )

    # Remove old file if it already exists
    if destination.exists():
        destination.unlink()

    shutil.move(
        str(source),
        str(destination)
    )

    return str(destination)