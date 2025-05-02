import os
from pathlib import Path

from django.utils.text import slugify

ALLOWED_EXTENSIONS = ['.csv', '.doc', '.pdf', '.xlsx', '.py', '.txt']


def check_extension(filename):
   return Path(filename).suffix.lower() in ALLOWED_EXTENSIONS


def check_file_size(file, required_size=2):
   file_size = file.size / (1024 * 1024)

   if file_size > required_size:
       return False

   return True


def create_file_path(project_name: str, original_filename: str) -> str:
    ext = Path(original_filename).suffix.lower()
    name = Path(original_filename).stem
    safe_proj = slugify(project_name).replace(' ', '_')
    safe_name = slugify(name)
    return str(Path('documents') / safe_proj / f'{safe_name}{ext}')


def save_file(file_path, file_content):
   os.makedirs(os.path.dirname(file_path), exist_ok=True)
   with open(file_path, 'wb') as f:
       for chunk in file_content.chunks():
           f.write(chunk)

   return file_path


def delete_file(filepath: str) -> None:
    os.remove(os.path.relpath(filepath))
