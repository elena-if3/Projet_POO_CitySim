from tools.display import Display, MenuBuilder

class App():
    cities_list = []

    def main_menu() -> None:
        main_menu = (MenuBuilder.add_option("Create a city", lambda : print("Create a city"))
            .add_option("Show cities list", lambda : App.display_city_list(App.cities_list))
            .add_return(True)
            .build())
        while True:
            Display.clear_screen()
            Display.display_menu("CitySim")
            main_menu.show()

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