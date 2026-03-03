from src.menus.InitialMenu import InitialMenu

VERSION = "0.1.0"

def main():
    menu = InitialMenu(version=VERSION)
    menu.show()

if __name__ == "__main__":
    main()