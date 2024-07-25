# This code is part of exercises from the Automate Everything with Python by Ardit Sulce.
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

# Import the Path class from the pathlib module for handling filesystem paths
from pathlib import Path

# Create a Path object representing the directory 'files'
directory = Path('files')

# Print the current working directory
print(Path.cwd())

# Iterate through the files and directories in 'directory'
for file in directory.iterdir():
    # Create a new filename by prefixing "new-" to the original name while keeping the file extension unchanged
    new_name = "new-" + file.stem + file.suffix
    # Create a new Path object with the updated filename
    new_path = file.with_name(new_name)
    print(new_path)
    # Rename the original file to the new file path
    file.rename(new_path)

  



