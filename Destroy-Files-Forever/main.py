# This code is part of exercises from the Automate Everything with Python by Ardit Sulce.
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

from pathlib import Path

root_dir = Path('destination')

for path in root_dir.glob("*.csv"):
  with open(path, 'wb') as file:
    file.write(b'')
  path.unlink()
