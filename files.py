import zipfile

def zip_files(name: str, files: list[str]) -> None:

    zip_name = f"{name}.zip"
    
    with zipfile.ZipFile(zip_name, "w") as f:
        for file in files:
            f.write(file)

def extract_zip_file(zipped_file: str) -> None:

    file = f"{zipped_file}.zip"

    with zipfile.ZipFile(file, "r") as f:
        f.extractall(zipped_file)