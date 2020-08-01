'''
lab1 nitay malka 304931801
this is the functions code
'''

'''
func 1 - take from user temperature in celsius and convert it to fahrenheit 
use the formula tempC = (5/9)*(tempF - 32)
tempF = 1.8tempC + 32
'''
def celsiusToFahrenheit(temp_c = 'WRONG'):
    #temp_c = 'WRONG'
    while temp_c.isdigit() == False:
        temp_c = input("Enter temperature in Celsius ")
        if temp_c.isdigit() == False:
            print("Sorry your input is not a number")
    temp_c = float(temp_c)
    temp_f = 1.8*temp_c + 32
    print("{} in Celsius equal to {} in fahrenheit".format(temp_c,temp_f))
