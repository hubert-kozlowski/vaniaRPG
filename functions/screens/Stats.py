from functions.screens.menuScreen import menuScreen


def stats():
    print("Welcome to the stats!")
    choice = input("Press Enter to exit stats")
    if choice == "":
        menuScreen()