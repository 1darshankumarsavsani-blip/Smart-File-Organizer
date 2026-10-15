import hashlib
import os

def find_duplicates():

    hashes = {}

    for file in os.listdir():

        if os.path.isfile(file):

            with open(file, "rb") as f:

                file_hash = hashlib.md5(
                    f.read()
                ).hexdigest()

            if file_hash in hashes:

                print(
                    f"Duplicate Found: {file}"
                )

            else:
                hashes[file_hash] = file

    print("Duplicate Scan Complete!")
