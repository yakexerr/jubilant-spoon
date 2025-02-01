import filecmp
from pathlib import Path

file_dir = Path("files")

result = filecmp.cmp(
    file_dir/ 's.txt'
    , file_dir/ 't.txt')