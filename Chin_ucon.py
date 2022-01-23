def Chin_ucon():

    def ft2mi(ft):
        mi = round((ft*0.000189394), 3)
        print(str(ft) + "ft = " + str(mi) + 'mi')
    def ft2m(ft):
        m = round((ft*0.304800097536), 3)
        print(str(ft) + "ft = " + str(m) + 'm')
    def m2ft(m):
        ft = round((m*3.28084), 3)
        print(str(m) + "m = " + str(ft) + 'ft')
    def m2mi(m):
        mi = round((m*0.000621371), 3)
        print(str(m) + "m = " + str(mi) + 'mi')
    def sqft2acre(sqft):
        acre = round((sqft*43560), 3)
        print(str(sqft) + "ft2 = " + str(acre) + 'acre')
    def sq_m2acre(sq_m):
        acre = round((sq_m*4046.86), 3)
        print(str(sq_m) + "m2 = " + str(acre) + 'acre')
    def sq_mi2acre(sq_mi):
        acre = round((sq_mi*0.0015625), 3)
        print(str(sq_mi) + "mi2 = " + str(acre) + 'acre')
    def hect2acre(hect):
        acre = round((hect*0.404686), 3)
        print(str(hect) + "hectares = " + str(acre) + 'acre')


    print('Welcome to the unit converter')
    print('Choose the function you want to use')
    print('1. Feet to Miles')
    print('2. Feet to Meters')
    print('3. Meters to Feet')
    print('4. Meters to Miles')
    print('5. Square Feet to Acres')
    print('6. Square Meters to Acres')
    print('7. Square Miles to Acres')
    print('8. Hectares to Acres')


    while True:
        '''User defined input for the function that they want to call'''
        function = input("Choose from the functions above, between 1 and 8: ")
        try:
            function = int(function)
            if function not in range(1,9):
                print('Please enter a number between 1 and 8 (corresponding to above functions)')
                continue
        except:
            print("Invalid number")
            continue

        '''User defined input for the number that they want to convert'''
        number = input("Enter the value that you want to convert: ")
        try:
            number = int(number)
        except:
            print("Invalid number") 
            continue
        if number < 0:
            print('Please enter a positive number.')
            continue

        if function == 1:
            ft2mi(number)
        elif function == 2:
            ft2m(number)
        elif function == 3:
            m2ft(number)
        elif function == 4:
            m2mi(number)
        elif function == 5:
            sqft2acre(number)
        elif function == 6:
            sq_m2acre(number)
        elif function == 7:
            sq_mi2acre(number)    
        elif function == 8:
            hect2acre(number)

        resume_cmd = input("Enter any key to continue or press 'E' to Exit:" )
        resume_cmd = resume_cmd.upper()
        if resume_cmd == 'E':
            break
        else:
            continue
