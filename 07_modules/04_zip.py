from pathlib import Path
from zipfile import ZipFile

# ejemplo 1
zip = ZipFile("file1.zip", "w")
for path in Path("c:\\code").rglob("*.*"):
    zip.write(path)
zip.close()

# ejemplo 2
with ZipFile("file2.zip", "w") as zip:
    for path in Path("c:\\code").rglob("*.*"):
        zip.write(path)
