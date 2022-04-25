convertor_is_running = True

welcome_msg = """
Welcome to the converter.
Here you can convert miles <=> kilometers.
Available options are
1 = miles to kilometers
2 = kilometers to miles
3 = quit the converter
help = to see this details again
"""

print(welcome_msg)
while convertor_is_running:
    try:
        user_input = input("Please enter a option 1 - 3: ")
        if user_input == "help":
            print(welcome_msg)
        elif int(user_input) == 3:
            convertor_is_running = False
            print("Quitting....")

        if int(user_input) == 1:
            option_1 = True
            while option_1:
                try:
                    miles_2_km = input("Thank you for your valid option. Please input the wanted conversation  "
                                       "miles <=> km: ")
                    if '.' in miles_2_km:
                        miles_2_km = float(miles_2_km)
                        print(f"{miles_2_km} miles are {miles_2_km * 1.609344} kilometers")
                        option_1 = False
                    else:
                        miles_2_km = int(miles_2_km)
                        print(f"{miles_2_km} miles are {miles_2_km * 1.609344} kilometers")
                        option_1 = False
                except:
                    print("Please enter a value for conversion - float or integer")
                    option_1 = True
                    continue

        if int(user_input) == 2:
            option_2 = True
            while option_2:
                try:
                    km_2_miles = input("Thank you for your valid option. Please input the wanted conversation "
                                           "km <=> miles: ")
                    if '.' in km_2_miles:
                        km_2_miles = float(km_2_miles)
                        print(f"{km_2_miles} miles are {km_2_miles / 1.609344} kilometers")
                        option_2 = False
                    else:
                        km_2_miles = int(km_2_miles)
                        print(f"{km_2_miles} miles are {km_2_miles / 1.609344} kilometers")
                        option_2 = False

                except:
                    print("Please enter a value for conversion - float or integer")
                    option_2 = True
                    continue

    except:
        print("Please enter a valid option 1 - 3!")
        convertor_is_running = True
        continue
