Year = int(input("Please Enter a Year to check it is leap Year or not : "))  
if (Year % 400 == 0):  
    print("%d is a leap Year."%Year)  
elif (Year % 100 == 0):  
    print("%d is not a leap Year."%Year)  
elif (Year % 4 == 0):  
    print("%d is a leap Year."%Year)  
else:  
    print("%d is not a leap Year."%Year)    
