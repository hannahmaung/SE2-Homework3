##Normal leap year program. 

#asks user to enter an input
year = int(input("Enter a year: "))

#Checks if the input is evenly divisibly by 4
if (year % 4) == 0:
    #checks if it is evenly divisible by 100
    if (year % 100) == 0:
        if (year % 400) == 0:
            ##checks if year is evenly divisible by 400
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")
    else:
        print(year, "is a leap year")
else:
    print(year, "is not a leap year")



