import os
import shutil

# Paths to delete
paths_to_delete = [
    "client.py",
    "server.py",
    os.path.join("secure_file_transfer_web", "templates", "static")
]

for path in paths_to_delete:
    if os.path.isfile(path):
        os.remove(path)
        print(f"Deleted file: {path}")
    elif os.path.isdir(path):
        shutil.rmtree(path)
        print(f"Deleted folder: {path}")
    else:
        print(f"Not found (already deleted or moved): {path}")
