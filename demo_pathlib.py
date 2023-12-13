from pathlib import Path

BASE_DIR = Path(__file__).parent
#print(BASE_DIR)
#print(repr(BASE_DIR))


def demo_cwd():
    cwd = Path.cwd()
    print()

def demo_dirs():
    users_path = Path("/User")
    print(users_path)
    print(users_path.is_dir())
    print(users_path.exists())

    print()

    #users_path = Path("/Users")

    #print(users_path.is_dir())
    #print(users_path.exists())

    #for path in users_path.iterdir():
    #    print(path)

    pics_fil_name = "pics"
    cats_pics_dir = BASE_DIR / pics_fil_name / "cats"
    print(cats_pics_dir)
    cats_pics_dir.mkdir(parents=True, exist_ok=True)

def demo_files():
    filepath = BASE_DIR / "file.txt"
    filepath.write_text("Hello Ilya\n")
    print(filepath.read_text())


if __name__ == '__main__':
    #demo_cwd()
    #demo_dirs()
    demo_files()