# This code is part of exercises from the Automate Everything with Python by Ardit Sulce.
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

# Import the Path class from the pathlib module for handling filesystem paths
from pathlib import Path


# Create a Path object representing the directory 'files'
root_dir = Path('files')

# nterate through the files and directories in 'root_dir'
file_paths = root_dir.iterdir()
print(Path.cwd())

# Iterate over each path object in the 'file_paths' iterator
for path in file_paths:
  # Create a new filename object by adding "new-" in front of the original name while keeping the original file extension unchanged.
  new_filename = "new-" + path.stem + path.suffix
  # Create a new Path object with the updated filename
  new_filepath = path.with_name(new_filename)
  print(new_filepath)
   # Rename the original file to the new file path
  path.rename(new_filepath)
  



