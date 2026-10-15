import os
import shutil

def clean_downloads():

    downloads = os.path.expanduser(
        "~/Downloads"
    )

    for file in os.listdir(downloads):

        path = os.path.join(
            downloads,
            file
        )

        if os.path.isfile(path):

            ext = os.path.splitext(file)[1]

            if ext:

                folder = os.path.join(
                    downloads,
                    ext[1:].upper()
                )

                os.makedirs(
                    folder,
                    exist_ok=True
                )

                shutil.move(
                    path,
                    os.path.join(
                        folder,
                        file
                    )
                )

    print("Downloads Cleaned!")