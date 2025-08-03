from tools.display import Display, MenuBuilder, City
from tools.generator import Generator

class App():

    cities_list = []
    manage_city = True

    def toggle_manage_city():
        App.manage_city = not App.manage_city

    def main_menu() -> None:
        while True:
            MenuBuilder.reset_menu()
            main_menu = (MenuBuilder.add_option("Create a city", lambda : App.create_city())
                .add_option("Show cities list", lambda : App.display_city_list(App.cities_list))
                .add_return(True)
                .build())
            Display.clear_screen()
            Display.display_menu("CitySim")
            main_menu.show()

    def create_city():
        new_city = Generator.generate_city()
        App.cities_list.append(new_city)
        Display.clear_screen()
        Display.display_menu("NEW CITY")
        print(f"A new city named : {new_city.name} has been created")
        Display.wait_input()

    def display_city_list(cities : list['City'])-> None:
        Display.clear_screen()
        Display.display_menu("CitySim")
        if cities:
            for i, city in enumerate(cities):
                print(f"[\033[1;96m{i+1}\033[0m] - {city.name}")
        else:
            print("No cities found")
        print(f"\n{"="*Display.DISPLAY_WIDTH}",end="\n\n")
        entry = ""
        good_input = False
        while not good_input:
            if cities:
                try:
                    entry = int(input("\nVeuillez sélectionner une ville (0 to return) > "))
                    if 0 > entry or entry > len(cities):
                        raise IndexError
                except ValueError:
                    print("Please enter a number")
                except IndexError:
                    print("Please enter a number between 0 and " + str(len(cities)))
                else:
                    good_input = True
            else :
                Display.wait_input()
                good_input = True
        if entry:
            city_S = cities[entry - 1]
            App.display_city(cities[entry -1])
    
    def display_city(city : City) -> None :
        App.manage_city = True
        MenuBuilder.reset_menu()
        city_menu = (MenuBuilder.add_option("Add citizens [\033[1;33mNYI\033[0m]", lambda : None)
            .add_option("Add a building [\033[1;33mNYI\033[0m]", lambda : None)
            .add_option("Delete city [\033[1;33mNYI\033[0m]", lambda : None)
            .add_option("Live day(s) [\033[1;33mNYI\033[0m]", lambda : None)
            .add_return(False, lambda : App.toggle_manage_city())
            .build())
        while App.manage_city:
            Display.clear_screen()
            Display.display_menu(f"{city.name} : Infos")
            Display.display_city_info(city)
            city_menu.show()

if __name__ == "__main__":
    App.main_menu()