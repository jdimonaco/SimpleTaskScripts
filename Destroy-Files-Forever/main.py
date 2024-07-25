# This code is part of exercises from the Automate Everything with Python by Ardit Sulce.
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

from pathlib import Path

# Defining the root directory containing the CSV files
directory = Path('destination')

# Iterate over all CSV files in the directory
for csv_file in directory.glob('*.csv'):
    # Open each file in binary write mode and immediately close it to clear the content
    with open(csv_file, 'wb'):
        pass
    # Delete the empty file
    csv_file.unlink()
