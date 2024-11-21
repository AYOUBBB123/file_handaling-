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
            if not filename.strip():
                print("Error: File name cannot be empty.")
                return
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
        logging.error(f"{datetime.now()} - Error adding content top {filename}: {e}")
        print(f"Error creating file: {e}")
    except PermissionError as e:
        print(f"Permission denied: Cannot access the file '{filename}'.")
        logging.error(f"{datetime.now()} - Permission denied: cuze of  {filename}: {e}")




def list_files(directory="."):
    print("here is the list of files u have ")
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
    except FileNotFoundError as e:
        print(f"Error: The directory '{directory}' does not exist.")
        logging.error(f"{datetime.now()} - Error listing files in  {directory}: {e}")
        return False
    except PermissionError as e:
        print(f"Permission denied: Cannot access the directory '{directory}'.")
        logging.error(f"{datetime.now()} - Permission denied:  for  {directory}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        logging.error(f"{datetime.now()} - Error listing files in  {directory}: {e}")

def get_file_details():
    filename = input("Enter the file name without the extension: ")
    extension = input("Enter the file extension: ")
    return filename, extension

def copyfiles(dirctory,source,extension,destination):
    try:
        if not os.path.exists(dirctory):
            print(f"Error: The directory {dirctory} does not exist.")
            return
        os.chdir(dirctory)
        source =f"{source}.{extension}"
        if not os.path.exists(source):
            print(f"Error: The file '{source}' does not exist.")
            return
        shutil.copy(source, destination)
        print(f"File '{source}.{extension}' has been copied to '{destination}'.")
    except FileNotFoundError:
        print(f"Error: The source file '{source}' does not exist.")
    except PermissionError as e:
        print(f"Permission denied: Cannot access the file '{source}'.")
        logging.error(f"{datetime.now()} - Permission denied for {source}: {e}")
    except Exception as e:
        logging.error(f"{datetime.now()} - Unexpected error with {source}: {e}")
        print(f"An unexpected error occurred: {e}")


def deletefile(path,filename,extension="txt"):
    try:
        os.chdir(path)
        filename =f"{filename}.{extension}"
        if not os.path.exists(filename):
            print(f"Error: The file '{filename}' does not exist.")
            return
        os.remove(filename)
        print(f"File '{filename}.{extension}' has been deleted  .")
    except FileNotFoundError as e:
        print(f"Error: The source file '{filename}' does not exist.")
        logging.error(f"{datetime.now()} -not found {filename}: {e}")
    except PermissionError as e:
        print(f"Permission denied: Cannot access the file '{filename}'.")
        logging.error(f"{datetime.now()} - Permission denied for {filename}: {e}")
    except Exception as e:
        logging.error(f"{datetime.now()} - Unexpected error with {filename}: {e}")
        print(f"An unexpected error occurred: {e}")



def mergefile(path1,filename1,extension1,path2,filename2,extension2,path3,outputfile,extension3):
        try:
            file1_path = os.path.join(path1, f"{filename1}.{extension1}")

            file2_path = os.path.join(path2, f"{filename2}.{extension2}")

            output_path = os.path.join(path3, f"{outputfile}.{extension3}")

            with open(file1_path,'r') as f1:
                content1 = f1.read()
            os.chdir(path2)
            with open(file2_path,'r') as f2:
                content2 = f2.read()
            os.chdir(path3)
            with open(output_path,'w') as out:
                out.write(content1)
                out.write('\n')
                out.write(content2)
            print(f"Files '{filename1}' and '{filename2}' have been merged into '{outputfile}'.")
        except Exception as e:
            print(f"An error occurred: {e}")
            logging.error(f"{datetime.now()} - Unexpected error : {e}")
        except PermissionError as e:
            print(f"Permission denied: Cannot access the file .:{e}")
            logging.error(f"{datetime.now()} - Permission denied : {e}")





if __name__ == "__main__":
    while True:
            try:
                op = int(input("Enter the number of the operation you want to do:\n1 - Create\n\n2 - add content\n \n3 - list of files\n \n4- copy file\n \n5- delete file\n \n6- merge files \n"))
                match op:
                    case 1:
                        while True:
                            creat = input("If you want to create a file, type 'c'. Otherwise, type anything to quit: ").lower().strip()
                            if creat == "c":
                                name,ex = get_file_details()
                                cont = input("Enter the file content: ").strip()
                                createfiles(name, cont,ex)
                            else:
                                print("Exiting.")
                                break
                    case 2:
                        while True:
                            add = input("if u wanna add content or creat a file if does not exict type 'a' Otherwise, type anything to quit: ").strip().lower()
                            if add == "a":
                                list_files()
                                name,ex = get_file_details()
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
                            dir = os.path.abspath(input("Enter the directory path (default: current): ").strip() or '.')
                            list_files(dir)
                    case 4 :

                        dir = os.path.abspath(input("Enter the directory path (default: current): ").strip() or '.')
                        list_files(dir)
                        file,ex =get_file_details()
                        des = input("enter the file destination: ").strip().lower()
                        copyfiles(dir,file,ex,des)
                    case 5:
                        while True:
                            rm = input("if u wanna add content or creat a file if does not exict type 'r' Otherwise, type anything to quit: ").strip().lower()
                            if rm == "r":
                                path = os.path.abspath( input("Enter the directory path (default: current): ").strip() or '.')
                                list_files(path)
                                file,ex = get_file_details()
                                deletefile(path,file,ex)
                            else:
                                print("Exiting.")
                                break
                    case 6:
                        while True:
                            mr = input("if u wanna merge files type 'r' Otherwise, type anything to quit: ").strip().lower()
                            if mr == "r":
                                path1 = os.path.abspath( input("Enter the directory path of the first file (default: current): ").strip() or '.')
                                list_files(path1)
                                file1,ex1 = get_file_details()

                                path2 = os.path.abspath(input("Enter the directory path of the secend file (default: current): ").strip() or '.')
                                list_files(path2)
                                file2,ex2 = get_file_details()

                                path3 = os.path.abspath(input("Enter the directory path of the output file (default: current): ").strip() or '.')
                                list_files(path3)
                                file3, ex3 = get_file_details()

                                mergefile(path1,file1,ex1,path2,file2,ex2,path3,file3,ex3)
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
