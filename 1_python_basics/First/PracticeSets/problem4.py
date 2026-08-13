import os

path = "/"

try:
    files = os.listdir(path)
    print(f"Contents of directory '{path}':")
    for f in files:
        print("  ", f)
except Exception as e:
    print("Error while listing directory:", e)