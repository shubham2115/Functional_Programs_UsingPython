import math

class NationalWeatherService :

    @staticmethod
    def windChillTemp(t,v):
        w = 35.74 + (0.6215 * t) + ( (0.4275 * t) - 35.75 ) * (v ** 0.16)
        print("Effective wind chill temperature : ",w)

#variable
flag = True

while(flag == True):
    try:
        t = float(input("Enter the temperature in fahrenheit : "))
        if (t>50):
            raise ValueError
            flag = True

        v = float(input("Enter the speed in miles per hour : "))
        if(v>120 or v<3):
            raise OverflowError
            flag =True

        NationalWeatherService.windChillTemp(t,v)
        flag = False

    except ValueError :
        print("##Invalid input## \n Please enter the temperature below 50")

    except OverflowError :
        print("##Invalid Input## \n Please enter the speed between 3 to 120 miles per hour")