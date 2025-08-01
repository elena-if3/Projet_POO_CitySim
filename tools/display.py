from .menu.menu_builder import MenuBuilder
from models.city import City
import os

class Display():

    DISPLAY_WIDTH = 60

    @classmethod
    def wait_input(cls):
        '''Procedure to use when waiting for the user to press a key to display some informations'''
        input("\nAppuyer sur ENTRER pour continuer…")

    @classmethod
    def clear_screen(cls) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

    @classmethod
    def display_menu(cls,title : str) -> None:
        print(f"{"="*Display.DISPLAY_WIDTH}")
        print(f"{title.upper().center(Display.DISPLAY_WIDTH)}")
        print(f"{"="*Display.DISPLAY_WIDTH}", end="\n\n")            

    @classmethod
    def display_city_info(city : City) -> None:
        pass


if __name__ == '__main__':
    Display.main_menu()