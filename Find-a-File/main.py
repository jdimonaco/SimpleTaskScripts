# This code is part of exercises from the Automate Everything with Python by Ardit Sulce
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

# Import the Path class from the pathlib module to handle filesystem paths
from pathlib import Path

# Creating a Path object for the current working directory
current_dir = Path('.')
# Set the search keyword for filenames
keyword = '14'

# Loop through all files and directories recursively
for item in current_dir.rglob("*"):
    # Verify if the current item is a file
    if item.is_file():
        # Check if the filename contains the specified keyword
        if keyword in item.stem:
            print(item.resolve())





