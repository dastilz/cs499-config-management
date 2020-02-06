# Import library for arguments (optional)
import sys

# Global files (will import files later, need to be global for proper scope in private functions)
addressesFile = None
salariesFile = None

# Global Maps
addressMap = {}
salaryMap = {}
joinMap = {}

# Global Sets
selectSet = []

# This function will reset reused globals to default value
def resetReusedGlobals():
    joinMap.clear()
    del selectSet[:]

# This function will parse given files and populate hash maps (dictionaries)
def parseFiles():
    addressesFile = open("personnel_addresses2.txt")
    salariesFile = open("personnel_salaries2.txt")    
    
    # Get map of name -> address from address folder
    for line in addressesFile:
        name, address = line.split('|')
        # Get rid of hanging new line character
        address = address.rstrip()
        addressMap[name] = address

    # Get map of name -> salary from salaries folder
    for line in salariesFile:
        name, salary = line.split('|')
        # Get rid of hanging new line character
        salary = salary.rstrip()
        salaryMap[name] = salary

# This function will find name associated to a salary based on given address and then print found names and salaries
def printSalariesByAddress(inp):
    # Iterate through address folder items and put matching substrings based on input into a set
    for name, address in addressMap.items():
        # Check matching substring by using 'in' operator and case sensitivity using 'lower' function
        if inp.lower() in address.lower():
            selectSet.append(name)
    
    # Iterate through set and map selected names to their associated salary
    for name in selectSet:
        joinMap[name] = salaryMap[name]
    
    # Iterate through join map and output items
    for name, salary in joinMap.items():
        output = "{} : {} ".format(name, salary)
        print(output)

# This main function will start when file is executed (not imported)
def main(argv):

    # If an argument is used as input, just output based on single argument
    if len(argv) == 2:
        inp = argv[1]
        parseFiles()
        printSalariesByAddress(inp)
    # Don't allow for over one argument
    elif len(argv) > 2:
        print('Too many arguments')
    # If there are no arguments, check for user input and loop until user inputs 'quit' or 'q'
    else:
        parseFiles()
        inp = ""
        print("This program will find name and salary associated to a given address")
        while inp.lower() != "quit" and inp.lower() != "q":
            # Prompt user input
            inp = raw_input("Enter address to search: ")
            printSalariesByAddress(inp)
            resetReusedGlobals()

# This is just fancy for saying execute when called (no need to worry for imports since this is not a class)
if __name__ == "__main__":
    main(sys.argv)
