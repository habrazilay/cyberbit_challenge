import os
import zipfile

# create an array of lowercase letters
letters = [chr(i) for i in range(ord('a'), ord('z')+1)]

# create txt files for each letter
for letter in letters:
    with open(f"{letter}.txt", "w") as f:
        f.write(letter)

# check if all txt files were created
for letter in letters:
    if not os.path.exists(f"{letter}.txt"):
        print(f"Error: {letter}.txt not found.")
        exit(1)

# get the VERSION environment variable
version = os.environ.get("VERSION", "1.0.0")

# create zip files for each letter
for letter in letters:
    with zipfile.ZipFile(f"{letter}_{version}.zip", mode='w') as z:
        z.write(f"{letter}.txt")

# check if all zip files were created
for letter in letters:
    if not os.path.exists(f"{letter}_{version}.zip"):
        print(f"Error: {letter}_{version}.zip not found.")
        exit(1)

print("All txt and zip files were created successfully.")
