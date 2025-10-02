import os
from pathlib import Path
import zipfile

# Create base project directory
base_path = Path("Data_Science_Project")
folders = [
    base_path / "data",
    base_path / "notebooks",
    base_path / "src"
]

# Sample files and their contents
files = {
    base_path / "README.md": "# Data Science Project\n\nThis is a sample data science project structure.",
    base_path / "requirements.txt": "pandas\nnumpy\nscikit-learn\nmatplotlib\njupyter",
    base_path / "main.py": "# Main script\n\nprint('Welcome to the Data Science Project')",
    base_path / "notebooks" / "analysis.ipynb": '{"cells": [], "metadata": {}, "nbformat": 4, "nbformat_minor": 5}',
    base_path / "src" / "preprocessing.py": "# Data preprocessing functions\n\ndef clean_data(df):\n    return df.dropna()",
    base_path / "src" / "model.py": "# Model training functions\n\ndef train_model(X, y):\n    pass"
}

# Create directories
for folder in folders:
    folder.mkdir(parents=True, exist_ok=True)

# Create files
for file_path, content in files.items():
    with open(file_path, "w") as f:
        f.write(content)

# Create a zip archive of the project
zip_path = Path("Data_Science_Project.zip")
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
    for file_path in base_path.rglob("*"):
        zipf.write(file_path, file_path.relative_to(base_path.parent))

print("Project folder and ZIP file created successfully.")