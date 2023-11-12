num=int(input("Enter '1' to convert from Celsius to Fahrenheit or '2' to convert from Fahrenheit to Celsius: "))

if num==1:
    celcius=float(input("Enter Celcius value: "))
    fahrenheit =(celcius*1.8)+32
    print("Farenheit= ",fahrenheit)

elif num==2:
    fahrenheit=float(input("Enter Farenheit value: "))
    celcius=(fahrenheit-32)/1.8
    print("Celcius= ",celcius)

else:
    print("Invalid operation entered")
    