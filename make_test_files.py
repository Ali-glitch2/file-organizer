from pathlib import Path

folder=Path("test_downloads")
folder.mkdir(exist_ok=True)

names = ["photo.jpg", "logo.png", "cv.pdf", "notes.txt", "movie.mp4",
         "backup.zip", "script.py", "data.xlsx", "mystery.xyz"]


for name in names:
    (folder/name).write_text("test")

print(f"Test files created in '{folder}' folder.")