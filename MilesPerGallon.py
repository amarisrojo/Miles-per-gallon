# Develop a sentinel-controlled-repetition script that 
# prompts the user to input the miles driven and gallons used for each tankful. 
# The script should calculate and display the miles per gallon obtained for each tankful.
# After processing all input information, the script should calculate and display the combined 
# miles per gallon obtained for all tankfuls (that is, total miles driven divided by total gallons used).

''' 
script: MilesPerGallon
action: calculates miles per gallon for each tankful, and total tankfuls
author: Amaris Rojo
date: 09/06/2024
'''

'''
action: calculate mpg for single tank input

input: takes arguments miles/gallon from main funtion input
output: none
return: rate of mpg per tank full

'''
#create function that calculates miles per gallon for individual tank
def calculate_mpg(miles, gallons):
    return miles / gallons if gallons != 0 else 0


'''
action: calculates the mpg overall total, ensures input is valid, calls on calculate_mpg funtion

input: miles driven, gallons used
output: prints the mpg for a single tank, prints overall mpg, displays error message 
return: none

'''
#define the main function 
def main():

#intialization phase
    sumMiles = 0
    sumGal = 0
    miles = 0
    gallons = 0
    inPut = 0  

#processing phase
#funtion for taking the input of miles driven and gallons used for each tankful(-1 to stop repetition)
#set variables to type float
#create sentinel-controlled-repetition script 
    while miles != -1: 
        miles = float(input("Please enter total amount of miles driven (Enter -1 to STOP): "))
        if miles == -1:
            continue
        gallons = float(input("Enter the total amount of gallons used: "))
        
        #call on function calculate_mpg to calculate for a single tank and display      
        mpg = calculate_mpg(miles, gallons)
        print("The miles/gallon for this tank is", mpg)

        #keep track of miles and gallons for total calculation
        sumMiles += miles
        sumGal += gallons

        #ensures that values are being entered 
        inPut += 1
        
#termination phase
#total average 
#responsible if -1 is only value entered
    if inPut > 0:
        average = sumMiles / sumGal
        print("The overall average miles/gallon was:", average)
    else:
        print('No value was entered')

#call main 
if __name__ == "__main__":
    main()

