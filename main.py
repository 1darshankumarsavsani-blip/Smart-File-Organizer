from organizer import organize_files
from duplicate_finder import find_duplicates
from downloads_cleaner import clean_downloads

while True:

    print("\n================================")
    print("      SMART FILE ORGANIZER")
    print("================================")
    print("1. Organize Files")
    print("2. Find Duplicate Files")
    print("3. Clean Downloads Folder")
    print("4. Exit")
    print("================================")

    choice = input("Enter Your Choice (1-4): ")

    if choice == "1":
        organize_files()

    elif choice == "2":
        find_duplicates()

    elif choice == "3":
        clean_downloads()

    elif choice == "4":
        print("Thank You For Using Smart File Organizer!")
        break

    else:
        print("Invalid Choice! Please Try Again.")

input("\nPress Enter To Exit...")