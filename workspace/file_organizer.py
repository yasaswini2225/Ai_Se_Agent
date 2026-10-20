"""
DevPulse AI - Automated File Organizer Script
Categorizes files in a target directory into organized folders based on file extensions.
"""
import os
import shutil
from pathlib import Path

EXTENSIONS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".md", ".xlsx", ".pptx"],
    "Code": [".py", ".js", ".html", ".css", ".ts", ".json", ".sql"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".tar", ".gz", ".rar"]
}

def organize_directory(target_dir: str):
    base_path = Path(target_dir).resolve()
    print(f"📂 Scanning & Organizing Directory: {base_path}")
    
    if not base_path.exists():
        print("Directory does not exist. Creating sample files to demonstrate...")
        base_path.mkdir(parents=True, exist_ok=True)
        # Create sample files
        (base_path / "report.pdf").touch()
        (base_path / "photo.png").touch()
        (base_path / "script.py").touch()
        (base_path / "archive.zip").touch()
    
    stats = {category: 0 for category in EXTENSIONS}
    stats["Others"] = 0

    for item in base_path.iterdir():
        if item.is_file():
            ext = item.suffix.lower()
            placed = False
            for category, exts in EXTENSIONS.items():
                if ext in exts:
                    dest_folder = base_path / category
                    dest_folder.mkdir(exist_ok=True)
                    shutil.move(str(item), str(dest_folder / item.name))
                    stats[category] += 1
                    placed = True
                    break
            if not placed:
                dest_folder = base_path / "Others"
                dest_folder.mkdir(exist_ok=True)
                shutil.move(str(item), str(dest_folder / item.name))
                stats["Others"] += 1

    print("\n✅ File Organization Summary:")
    for cat, count in stats.items():
        if count > 0:
            print(f"  • {cat}: {count} files categorized")

if __name__ == "__main__":
    organize_directory("./sample_unorganized_files")
