import os, subprocess, platform
import time

if input("Open File Explorer (y/n)? ").lower() == "y":
    os.system('cls')
    print("Opening File Explorer...")
    subprocess.Popen(['explorer', os.getcwd()])
    time.sleep(0.7)
def menu():
    os.system('cls')
    print(f"The current working directory is: '{os.getcwd()}'.")
    print("[1] Create a text file\n[2] Create a folder\n[3] Rename a file/folder\n[4] Delete a file\n[5] Delete a folder\n[6] Change cwd\n[7] List files")

    option = ""
    while option not in ["1","2","3","4","5","6","7"]:
            if option != "":
                print(f"'{option}' is not a valid option.")
            option = input("Choose an option (1-7): ")
    if option == "1":
        create_txt_file()
        return
    elif option == "2":
        create_folder()
        return
    elif option == "3":
        rename_file()
    elif option == "4":
        delete_file()
    elif option == "5":
        delete_folder()
    elif option == "6":
        change_cwd()
    elif option == "7":
        list_files()

def create_txt_file():
        os.system('cls')
        txt_file_name = input("Choose a name for your new text file: ")
        while os.path.exists(txt_file_name):
            print(f"{txt_file_name} already exists in this directory.")
            time.sleep(1.5)
            os.system('cls')
            txt_file_name = input("Choose a name for your new file: ")
        path = os.getcwd()
        new_file = os.path.join(path, txt_file_name)
        with open(new_file, "w") as file:
            pass
        os.system('cls')
        print(f"File was added to '{path}'.")
        time.sleep(1.5)
        menu()
        return

def create_folder():
    os.system('cls')
    folder_name = input("Choose a name for your new folder: ")
    while os.path.exists(folder_name):
        print(f"{folder_name} already exists in this directory.")
        time.sleep(1.5)
        os.system('cls')
        folder_name = input("Choose a name for your new folder: ")
    path = os.getcwd()
    new_folder = os.path.join(path,folder_name)
    os.mkdir(new_folder)
    os.system('cls')
    print(f"Folder was added to '{path}'.")
    time.sleep(1.5)
    menu()
    return

def rename_file():
    os.system('cls')
    file_name = input("Choose a file/folder to rename: ")
    while not os.path.exists(file_name):
        print("File not found.")
        time.sleep(0.7)
        os.system('cls')
        file_name = input("Choose a file/folder to rename: ")
    new_name = input("Choose a new name: ")
    os.rename(file_name,new_name)
    os.system('cls')
    print(f"Element was renamed to '{new_name}'.")
    time.sleep(1.5)
    menu()
    return

def delete_file():
    os.system('cls')
    file_to_delete = input("Choose a file to delete: ")
    while not os.path.exists(file_to_delete):
        print("File not found.")
        time.sleep(0.7)
        os.system('cls')
        file_to_delete = input("Choose a file to delete: ")
    while True:
        try:
            os.remove(file_to_delete)
        except:
            print("You can't delete folders here.")
            time.sleep(1.5)
            os.system('cls')
            file_to_delete = input("Choose a file to delete: ")
        else:
            break
    os.system('cls')
    print("File was deleted.")
    time.sleep(0.5)
    menu()
    return

def delete_folder():
    os.system('cls')
    folder_to_delete = input("Choose a folder to delete: ")
    while not os.path.exists(folder_to_delete):
        print("Folder not found.")
        time.sleep(0.7)
        os.system('cls')
        folder_to_delete = input("Choose a folder to delete: ")
    while True:
        try:
            os.rmdir(folder_to_delete)
        except:
            print("You can only delete folders here.")
            time.sleep(1.5)
            os.system('cls')
            folder_to_delete = input("Choose a folder to delete: ")
        else:
            break    
    os.system('cls')
    print("Folder was deleted.")
    time.sleep(1.5)
    menu()
    return

def change_cwd():
    os.system('cls')
    print(f"The current working directory is: '{os.getcwd()}'.")
    new_path_set = input("Change the cwd to: C:/")
    new_path = "C:/" + new_path_set
    while not os.path.exists(new_path):
        print("Directory not found.")
        time.sleep(0.7)
        os.system('cls')
        print(f"The current working directory is: '{os.getcwd()}'.")
        new_path_set = input("Change the cwd to: C:/")
        new_path = "C:/" + new_path_set
    os.chdir(new_path)
    os.system('cls')
    print(f"Cwd was changed to '{new_path}'.")
    time.sleep(1.5)
    menu()
    return

def list_files():
    os.system('cls')
    dirlist = os.listdir(os.getcwd())
    dirlist_length = len(dirlist)
    if dirlist_length > 0:
        counter = 1

        for i in dirlist:
            print(f"[{counter}] {i}")
            counter += 1

            time.sleep(0.001)
    else: 
        print("Directory is empty.")
    input("\nPress Enter...")
    menu()
    return  
menu()
