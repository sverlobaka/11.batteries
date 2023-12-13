import os
import sys
#from pprint import pprint

#print("__file__:", __file__)
BASE_DIR = os.path.dirname(__file__)
#print(BASE_DIR)

def demo_env():
    APP_STATE = os.getenv("APP_STATE")
    OTUS_COURS = os.getenv("OTUS_COURS")

    print("APP_STATE:", APP_STATE)
    print("OTUS_COURS:", OTUS_COURS)
    print(os.environ.get("OTUS_COURS"))
    #pprint(dir(os.environ))

def demo_sys_size():
    data = {}
    print(data)
    print(sys.argv)
    print(sys.getsizeof(data))

def demo_show_dir():
    print(os.getcwd())
    print(os.listdir())
    print(os.listdir("lc-venv"))
    print(os.path.isdir("lc-venv/bin"))

def demo_change_dir():
    print(os.getcwd())
    print("os.listdir()", os.listdir())
    idea_patch= os.path.join(BASE_DIR, ".idea")
    print(os.listdir("./.idea")) #после того как создали idea_patch, заменяем "./.idea" на idea_patch сам находит путь до файла
    os.chdir("lc-venv")
    print(os.getcwd())
    #print(os.listdir("./.idea")) #после того как создали idea_patch, заменяем "./.idea" на idea_patch
    print(idea_patch)
    cats_pics_path = os.path.join(BASE_DIR, "pics", "cats")
    print("cats_pics_path", cats_pics_path)
    my_cats_pic = os.path.join(cats_pics_path, "my-cats.jpg")
    print("my_cats_pic", my_cats_pic)

def demo_files():
    filename = "plan.txt"
    file_path = os.path.join(BASE_DIR, filename)
    print("file_path", file_path)
    print("exists?", os.path.exists(file_path))
    print("isfile?", os.path.isfile(file_path))

    with open(file_path, "w") as file:    #записываем файл
        file.write("Hello Ilya\n")

    if os.path.isfile(file_path):    #удаляем файл
        os.unlink(file_path)

    with open(file_path, "w") as file:
        file.write("Hello Ilya\n")

    with open(file_path, "a") as file:
        file.write("opana\n")
        file.writelines(["foo\n", "bar\n"])

  # with open(file_path, "r") as file:
    with open(file_path) as file:    # эта запись одинакова предыдущей
        #print(file.read())
        for line in file:    #генератором читаем по строчкам (если файл много весит, то он забъет всю ОЗУ)
            #print(line)    #выведет с еще одним переносом между строчек
            print(line, end="")   #выведет без доп.переноса


if __name__ == '__main__':
    #demo_env()
    #demo_sys_size()
    #demo_show_dir()
    #demo_change_dir()
    demo_files()