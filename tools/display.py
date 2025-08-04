from .menu.menu_builder import MenuBuilder
from models.city import City, Housing, Leisure, Water, Electricity, Food
from models.citizen.profession import Profession
import os

class Display():

    DISPLAY_WIDTH = 75

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
    def display_city_info(cls, city : City) -> None:

        print(f"City Name : \033[1;96m{city.name}\033[0m".ljust(Display.DISPLAY_WIDTH//3), end="")
        print(f"Day(s): \033[1;96m{city.day}\033[0m".center(Display.DISPLAY_WIDTH//3), end="")
        print(f"Week Day : \033[1;96m{city.weekday}\033[0m".rjust(Display.DISPLAY_WIDTH//3),end = "\n\n")
        
        print(f"{(" - "*(Display.DISPLAY_WIDTH//4)).center(Display.DISPLAY_WIDTH)}",end="\n\n")

        print(f"Citizens : \033[1;{96 if len(city.citizens) < city.capacity else 91}m{len(city.citizens)}\033[0m/\033[1;{96 if len(city.citizens) < city.capacity else 91}m{city.capacity}\033[0m".center(Display.DISPLAY_WIDTH//2),end="")
        print(f"Facilities : \033[1;96m{len(city.facilities.items())}\033[0m".center(Display.DISPLAY_WIDTH//2))

        print(f"    • Homeless Citizen(s) : \033[1;96m{len(city.homeless_citizens)}\033[0m".center(Display.DISPLAY_WIDTH//2),end="")
        print(f"    • Housing : \033[1;96m{len(city.facilities[Housing])}\033[0m".center(Display.DISPLAY_WIDTH//2))

        print(f"    • Housed Citizen(s) : \033[1;96m{len(city.citizens) -len(city.homeless_citizens)}\033[0m".center(Display.DISPLAY_WIDTH//2),end="")
        print(f"    • Factory : \033[1;96m{len(city.facilities[Profession.FOOD_FACTORY.value])+len(city.facilities[Profession.POWER_PLANT.value])+len(city.facilities[Profession.WATER_SUPPLY_PLANT.value])}\033[0m".center(Display.DISPLAY_WIDTH//2))

        print(f"    • Happiness : \033[1;96m{city.happiness}\033[0m".ljust(Display.DISPLAY_WIDTH//2),end="")
        print(f"    • Leisure : \033[1;96m{len(city.facilities[Leisure])}\033[0m".center(Display.DISPLAY_WIDTH//2),end="\n\n")

        print(f"{(" - "*(Display.DISPLAY_WIDTH//4)).center(Display.DISPLAY_WIDTH)}",end="\n\n")

        print(f"Water : \033[1;96m{city.resources[Water].amount}\033[0m".ljust(Display.DISPLAY_WIDTH//3),end="")
        print(f"Electricity : \033[1;96m{city.resources[Electricity].amount}\033[0m".center(Display.DISPLAY_WIDTH//3),end="")
        print(f"Food : \033[1;96m{city.resources[Food].amount}\033[0m".center(Display.DISPLAY_WIDTH//3))

        print(f"\n{"="*Display.DISPLAY_WIDTH}", end="\n\n")

    @classmethod
    def input_int(cls, prompt, min : int = None, max : int = None):
        '''
        Return an int from the user or nothing if the input isnt valid.
        :param prompt(str): Message to display
        :param min(int, optional): Minimum value to accept:
        :param max(int, optional): Maximum value to accept:
        :return int: int from the user or nothing
        '''
        try :
            inputted_int = int(input(prompt))
            if min is not None and inputted_int < min:
                raise ValueError("Value must be higher than {}".format(min))
            if max is not None and inputted_int > max:
                raise ValueError("Value must be lower than {}".format(max))
        except ValueError:
            print("Incorrect input, please enter a valid number.")
        else:
            return inputted_int

if __name__ == '__main__':
    Display.main_menu()