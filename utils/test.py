import os
import ctypes

folder_path = os.path.join("..", ".usr")

if os.path.exists(folder_path):
    print("yes")
else:
    print("no")

FILE_ATTRIBUTE_NORMAL = 0x80
ctypes.windll.kernel32.SetFileAttributesW(folder_path, FILE_ATTRIBUTE_NORMAL)

if os.path.exists(folder_path):
    print("yes")
else:
    print("no")

folder_path = os.path.join("..", "usr")
print(folder_path)