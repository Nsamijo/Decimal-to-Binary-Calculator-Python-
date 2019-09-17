DEFAULT_BASE = 2
binNum = ""
number = 0
proceed = False
Stop = False
response = ""
def begin():
    print("Binary Calculator: ")
    print("Enter Exit to exit the program")

def requestInput():
    return input("Please enter a decimal number: ")

def reverse(String):
    return String[::-1]

begin()
while not Stop:

    while proceed == False:
        response = requestInput()
        if not (response.isalpha()) and (response != ""):
            number = int(response)
            proceed = True
        elif response == "Exit":
            proceed = True
            Stop = True
    
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