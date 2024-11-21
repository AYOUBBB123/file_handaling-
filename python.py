import logging
import os
from datetime import datetime
import shutil


logging.basicConfig(filename="file_handling_error.log", level=logging.ERROR)

def createfiles(filename="new_file", content="this is a new file",extension ="txt"):
    try:
        if os.path.exists(filename):
            print(f"Error: The file '{filename}.{extension}' already exists.")
            return
        else:
            filename = f"{filename}.{extension}"
            with open(filename, 'w') as f:
                f.write(content)
            print(f"The file '{filename}' was created successfully.")
    except Exception as e:
        logging.error(f"{datetime.now()} - Error creating {filename}: {e}")
        print(f"Error creating file: {e}")



def addcontent(filename="new_file", content="this is a new file",extension ="txt"):
    try:
            filename = f"{filename}.{extension}"
            with open(filename, 'a') as f:
                f.write(content)
                print(f"The contetn was add to  '{filename}'")
    except Exception as e:
        logging.error(f"{datetime.now()} - Error creating {filename}: {e}")
        print(f"Error creating file: {e}")



def list_files(directory="."):
    try:
        files = [entry for entry in os.listdir(directory) if os.path.isfile(os.path.join(directory, entry))]
        if files:
            if len(files) == 1:
                print(f"this the only file in this directory {files[0]}")
            else:
                print("Files in the directory:")
                for index,file in enumerate(files,start=1) :
                    print(f"{index}- {file}")
        else:
            print("No files found in the directory.")
    except FileNotFoundError:
        print(f"Error: The directory '{directory}' does not exist.")
        return False
    except PermissionError:
        print(f"Permission denied: Cannot access the directory '{directory}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def copyfiles(dirctory,source,extension,destination):
    try:
        os.chdir(dirctory)
        source =f"{source}.{extension}"
        shutil.copy(source, destination)
        print(f"File '{source}.{extension}' has been copied to '{destination}'.")
    except FileNotFoundError:
        print(f"Error: The source file '{source}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to access '{source}' or '{destination}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def deletefile(path,filename,extension):
    try:
        os.chdir(path)
        filename =f"{filename}.{extension}"
        os.remove(filename)
        print(f"File '{filename}.{extension}' has been deleted to .")
    except FileNotFoundError:
        print(f"Error: The source file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to access '{filename}' ")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    while True:
            try:
                op = int(input("Enter the number of the operation you want to do:\n1 - Create\n\n2 - add content\n \n3 - list of files\n \n4- copy file\n \n5- delete file\n"))
                match op:
                    case 1:
                        while True:
                            creat = input("If you want to create a file, type 'c'. Otherwise, type anything to quit: ").lower().strip()
                            if creat == "c":
                                name = input("Enter the file name with out the extension: ").strip().lower()
                                ex = input("Enter the file extension: ").strip()
                                cont = input("Enter the file content: ").strip()
                                createfiles(name, cont,ex)
                            else:
                                print("Exiting.")
                                break
                    case 2:
                        while True:
                            add = input("if u wanna add content or creat a file if does not exict type 'a' Otherwise, type anything to quit: ").strip().lower()
                            if add == "a":
                                print("here is the list of files u have ")
                                list_files()
                                name = input("Enter the file name with out the extension: ").strip()
                                ex = input("Enter the file extension: ").strip()
                                cont = input("Enter the file content: ").strip()
                                addcontent(name, cont,ex)
                            else:
                                print("Exiting.")
                                break
                    case 3:
                        one = input("if u want this directory press 'this' else click anything ").strip().lower()
                        if one.lower() == "this":
                            list_files()
                        else:
                            dir = input("enter the name of directory or the path ").strip()
                            list_files(dir)
                    case 4 :

                        dir = input("enter the name of directory or the path if u want to work in this file prss '.' ").strip().lower()
                        print("here is the list of files u have ")
                        list_files(dir)
                        file = input("enter file name u wanna copy without extension ").strip().lower()
                        ex = input("enter file extension ").strip().lower()
                        des = input("enter the file destination: ").strip().lower()
                        copyfiles(dir,file,ex,des)
                    case 5:
                        while True:
                            rm = input("if u wanna add content or creat a file if does not exict type 'r' Otherwise, type anything to quit: ").strip().lower()
                            if rm == "r":
                                path = input("enter dir path if u wanna here enter '.' ").strip().lower()
                                print("here is the list of files u have ")
                                list_files(path)
                                file = input("enter file name u wanna copy without extension ").strip().lower()
                                ex = input("enter file extension ").strip().lower()
                                deletefile(path,file,ex)
                            else:
                                print("Exiting.")
                                break
                    case _:
                        print("Invalid option. Exiting.")
            except ValueError as e:
                print(f"Invalid input: {e}")
                logging.error(f"{datetime.now()} - Invalid input: {e}")

            repeat = input("Do you want to perform another operation? (yes/no): ").strip().lower()
            if repeat not in ["yes", "y"]:
                print("Exiting program. Goodbye!")
                break
