#Variable to store data into
DEFAULT_BASE = 2
binNum = ""
number = 0
proceed = False
Stop = False
response = ""
easterEgg = 0

#print the program name and instructions
def begin():
    print("Binary Calculator: ")
    print("Enter Exit to exit the program")
    print("Only decimal numbers are accepted")

#ask for user input and returns the user input
def requestInput():
    return input("Please enter a decimal number: ")

#reverse a string, used to reverse the binary number
def reverse(str):
    return str[::-1]

#defined a small easter egg
def surprise(int):
    if int == 3:
        print()
        print("Jeez put something that makes sense!")
        print()
    elif int == 5:
        print()
        print("It's free real estate!")
        print()
    elif int == 10:
        print()
        print("Wow, we have a badass over here!")
        print()
    elif int == 15:
        print()
        print("You do realise that you are wasting your own time right?")
        print()
    elif int > 15:
        print("Don't you have something else to do??")
    return

begin()
#continue endlessly until the user stops the program
while not Stop:
#loop till the user inputs a decimal number, user is also allowed to give no input
    while proceed == False:
        response = requestInput()
        if not (response.isalpha()) and (response != ""):
            number = int(response)
            proceed = True
        elif response == "Exit" or response == "exit":
            proceed = True
            Stop = True
        elif response == "":
            easterEgg = easterEgg + 1
            surprise(easterEgg)

#devide number by the base and keep going till the decimal number is 1 or 0. The answer is then printed in the terminal
    while number != 0:
        if number > 1:
            numDevided = number // DEFAULT_BASE
            left = number - (numDevided * DEFAULT_BASE)
            number = numDevided
        else:
            binNum += "1"
            number = 0
            proceed = False
            Stop = False
            print("In binary the decimal number, " + response + ", is " + reverse(binNum))
            response = ""
            binNum = ""
            break

        if left == 1:
            binNum += "1"
        elif left == 0:
            binNum += "0"