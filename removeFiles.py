import os
import time
import shutil

path = input("Enter the path: ")


def delete_folder(folder_path):
    shutil.rmtree(folder_path)


def delete_file(file_path):
    os.remove(file_path)


if path == os.path.expanduser('~'):
    print(
        'Providing the home directory can cause major issues to your computer')
    raise SystemExit
else:
    if os.path.exists(path):
        for (root, dirs, files) in os.walk(path, topdown=True):
            # print('Root: ', root)
            # print('Dirs: ', dirs)
            # print('Files: ', files)
            # print('--------------------------------')
            if os.stat(root).st_ctime > time.time() - (60 * 60 * 24 * 0.5):
                delete_folder(root)
            else:
                for directory in dirs:
                    directory_location = os.path.join(root, directory)
                    if os.stat(directory_location).st_ctime > time.time() - (
                            60 * 60 * 24 * 0.5):
                        delete_folder(directory_location)
                for file in files:
                    file_location = os.path.join(root, file)
                    if os.stat(file_location).st_ctime > time.time() - (
                            60 * 60 * 24 * 0.5):
                        delete_file(file_location)
    else:
        print(path, "does not exist")
