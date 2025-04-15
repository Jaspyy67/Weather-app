
def get_city_input():
    while True:
        city = input("Enter the name of the city: ").strip()
        if city:
            return city
        print("Error: City name cannot be empty. Please try again.")
