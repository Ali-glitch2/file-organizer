from pathlib import Path
import shutil

folder=Path("test_downloads")

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Archives": [".zip", ".rar", ".7z"],
    "Code": [".py", ".js", ".html"],
}



def get_category(extension):
    for c,e in CATEGORIES.items():
        if extension in e:
            return c
    return "Others"



def organize(folder):
    if not folder.exists():
        print(f"Folder '{folder}' does not exist.")
        return

    moved = 0
    skipped = 0

    for item in list(folder.iterdir()):
        if not item.is_file():
            continue

        category = get_category(item.suffix.lower())
        targetf=folder/category
        targetf.mkdir(exist_ok=True)
        target= targetf/item.name

        if target.exists():
            print(f"Skipped (already exists): {item.name}")
            skipped += 1
            continue

        shutil.move(str(item), str(target))

        print(f"Moved: {item.name} -> {category}/")
        moved += 1        
        
        
        print(f"\nDone. Moved: {moved}, Skipped: {skipped}")

    
def main():
    organize(folder)


if __name__ == "__main__":
    main()