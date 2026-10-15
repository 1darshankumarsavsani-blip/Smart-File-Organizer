import os
import shutil

def organize_files():

    categories = {
        "Images": [".jpg", ".png", ".jpeg"],
        "Videos": [".mp4", ".mkv"],
        "Documents": [".pdf", ".txt", ".docx"]
    }

    for file in os.listdir():

        if os.path.isfile(file):

            ext = os.path.splitext(file)[1].lower()

            for folder, exts in categories.items():

                if ext in exts:

                    os.makedirs(folder, exist_ok=True)

                    shutil.move(
                        file,
                        os.path.join(folder, file)
                    )

                    break

    print("Files Organized Successfully!")