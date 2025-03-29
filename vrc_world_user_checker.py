# VRChat Log  Formatting Tool
# The original code was created by sunasaji.
# Forked by CameIIian

# Changes from original code:
# 1. Remove unnecessary import statements
# 2. Fixing regular expressions used to retrieve user information
#    "Player" -> "Behaviour"
# 3. Display concise usage in case of error
# 4. Check the number of command line args
# 5. Adding input file date information to output files
# 6. Convert multiple log files in 1 batch

# TODO:
# - Improved method of "obtaining/determining the date" of the input log file, which is added to the formatted log file.

# imports
from sys import argv, exit
from re import search
from os.path import exists

# Format command line arguments
def getArgs():
    # error cases
    if len(argv) < 2:
        print('[NG] Too few arguments. Enter 1 log file you wish to convert after the conversion script')
        exit(1)
    
    # ok case
    return argv[1::]

# Main function to format data
def main(args):
    print("args: "+str(args))
    # Run until all files are formatted
    for loop in args:
        print("loop: "+loop)
        # Target files for the 1st argument
        path = loop

        # Don't run if file not found
        if not exists(path):
            print('[NG] {} is not found'.format(path))
            exit(1)

        # Determine output file name
        filename = "VRChat_usrlog.txt"
        if len(path) > 33:
            if path[12:32].isalpha() == False:
                filename = "VRChat_usrlog"+ str(path[12:32]) +".txt"
        
        # open output file
        output_file = open(filename, mode='a', encoding='utf-8', errors='ignore', buffering=1)

        # Start reading/writing files
        with open(path, mode='r' , encoding='utf-8',errors='ignore') as input_file:

            # Read 1 line at a time from the input file
            for line in input_file:

                # If logs of room entry or creation are found.
                match=search('([0-9\.]+ [0-9:]+).+Joining or Creating Room: (.+)',line)
                if match != None:
                    output_file.write(match.group(1) + " World: " + match.group(2) + "\n")
                
                # If logs of room leaving is found
                match=search('([0-9\.]+ [0-9:]+).+\[Behaviour\] Initialized PlayerAPI "(.+)" is remote',line)
                if match != None:
                    output_file.write(match.group(1) + "  User: " + match.group(2) + "\n")

        # Finish writing to output file
        output_file.close()
        print("[OK] Conversion End\n     Output file named: "+str(filename))

# Runs only when directly activated
if __name__ in '__main__':
    main(getArgs())
