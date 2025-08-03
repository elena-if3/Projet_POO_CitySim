from tools.display import Display, MenuBuilder
from tools.generator import Generator

class App():
    cities_list = []

    def main_menu() -> None:
        main_menu = (MenuBuilder.add_option("Create a city", lambda : App.create_city())
            .add_option("Show cities list", lambda : App.display_city_list(App.cities_list))
            .add_return(True)
            .build())
        while True:
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
            print("No cities found\n")
        print(f"{"="*Display.DISPLAY_WIDTH}",end="\n\n")
        entry = ""
        good_input = False
        while not good_input:
            if cities:
                try:
                    entry = int(input("\nVeuillez sélectionner une ville > "))
                    if 0 > entry or entry > len(cities):
                        raise IndexError
                except ValueError:
                    print("Please enter a number")
                except IndexError:
                    print("Please enter a number between 1 and " + str(len(cities)))
                else:
                    good_input = True
            else :
                Display.wait_input()
                good_input = True
        if entry:
            display_city(cities[entry])

if __name__ == "__main__":
    App.main_menu()