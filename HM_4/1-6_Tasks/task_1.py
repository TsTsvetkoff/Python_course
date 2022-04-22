"""
1. Play with the sys and os modules. Try passing arguments to a python script, as well as
exploring your filesystem. Send me the resulting python programs.
"""
import os
import shutil


def os_testing(file_name):
    # We create a file with some content
    cwd = os.getcwd()
    print("PWD is " + cwd)
    with open(file_name,  'w') as fp:
        fp.write(f"{file_name} is created")

    with open (f"{cwd}/{file_name}", "r") as f:
        print(f.read())


os_testing('My_1st_file.csv')


def move_the_file():
    # Now we create a new my_dir
    cwd = os.getcwd()
    my_dir = "Destination_new_dir"
    path = os.path.join(cwd, my_dir)
    newly_created_dir_path = os.path.join(cwd, path)
    os.mkdir(path)
    print("Directory '% s' created" % my_dir)
    print(newly_created_dir_path)

    # Now we create a destination my_dir where we will move the newly created file
    shutil.move('C:\\Users\\tsvetoslav.tsvetkov\\PycharmProjects\\Python_course\\HM_4\\1-6_Tasks\\My_1st_file.csv',
                str(newly_created_dir_path))

    dir_list = os.listdir(os.chdir(str(newly_created_dir_path)))
    print(f"Prior the deletion the content of the newly created dir {my_dir} is {dir_list}: ")


move_the_file()


def delete_the_file():
    os.remove("C:\\Users\\tsvetoslav.tsvetkov\\PycharmProjects\\Python_course\\HM_4\\1-6_Tasks\\Destination_new_dir"
              "\\My_1st_file.csv")


delete_the_file()


