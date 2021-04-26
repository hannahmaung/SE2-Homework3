##Leap year program with error handling. Prints out error message
#if user enters something other than an integer(s).


while True:
    try:
        #prompts user to enter a year
        year = int(input("Enter a year: "))
        #checks if it is evenly divisible by 4
        if (year % 4) == 0:
            #checks if the year is divisible by 100
            if (year % 100) == 0:
                #checks if the leap year is divisible by 400
                if (year % 400) == 0:
                    print(year, "is a leap year")
                else:
                    print(year, "is not a leap year")
            else:
                print(year, "is a leap year")
        else:
            print(year, "is not a leap year")
            break
    ##prints our error message of user inputs something other than an integer
    except ValueError:
            print("Not a valid year, please try again!")


