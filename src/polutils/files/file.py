import typing
import zipfile

def zip(name: str, files: list[str]) -> None:
    """Zip a given list of files into an archieve file."""
    zip_name = f"{name}.zip"
    
    with zipfile.ZipFile(zip_name, "w") as f:
        for file in files:
            f.write(file)

def extract(zipped_file: str) -> None:
    """Unzip an archieved file."""
    file = f"{zipped_file}.zip"

    with zipfile.ZipFile(file, "r") as f:
        f.extractall(zipped_file)

def compare(file1: str, file2: str) -> typing.Optional[bool]:
    """Compare two text files."""
    with open(file1, "r", encoding='utf-8') as f:
        contents1 = f.readlines()
    with open(file2, "r", encoding='utf-8') as f:
        contents2 = f.readlines()
    if contents1 == contents2:
        return True
    print("".join([f"Difference [{contents2.index(line) + 1}]: {line}" for line in contents2 if line not in contents1]))