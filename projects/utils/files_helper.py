from pathlib import Path
import os

ALLOWED_EXTENSIONS = ('.csv', '.doc', '.pdf', '.xlsx', '.py')
MAX_FILE_SIZE_MB = 2
MAX_FILE_SIZE_B = MAX_FILE_SIZE_MB * (1024 * 1024)


def validate_file_extension(file_name) -> bool:
    ext = Path(file_name).suffix.lower()

    if ext in ALLOWED_EXTENSIONS:
        return True
    return False


def validate_file_max_size(file) -> bool:
    if file.size <= MAX_FILE_SIZE_B:
        return True
    return False


def create_file_path(proj_name: str, file_name: str) -> str:
    return str(Path('documents') / proj_name / file_name)


def save_file_chunks(file, file_path: str) -> None:
    os.makedirs(os.path.dirname('documents'), exist_ok=True)

    with open(file_path, "wb") as file_:
        for chunk in file.chunks():
            file_.write(chunk)
