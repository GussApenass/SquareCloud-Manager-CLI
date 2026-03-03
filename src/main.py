from src.menus.InitialMenu import InitialMenu

VERSION = "1.0.0"

def main():
    menu = InitialMenu(version=VERSION)
    menu.show()

if __name__ == "__main__":
    main()
