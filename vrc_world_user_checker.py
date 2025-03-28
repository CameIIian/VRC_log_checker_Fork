# VRChat Log  Formatting Tool
# The original code was created by sunasaji.
# Forked by Camellian

# Changes from original code
# 1. Remove unnecessary import statements
# 2. Fixing regular expressions used to retrieve user information
#    "Player" -> "Behaviour"

# imports
import sys
import re
from os.path import exists

# Main function to format data
def main():
    # Target files for the 1st argument
    path = sys.argv[1] 

    # Don't run if file not found
    if not exists(path):
        print('{} is not found'.format(path))
        return 
	
    # Determine output file name
    output_file = open("VRChat_usrlog.txt", mode='a', encoding='utf-8', errors='ignore', buffering=1)

    # Start reading/writing files
    with open(path, mode='r' , encoding='utf-8',errors='ignore') as input_file:

        # Read 1 line at a time from the input file
        for line in input_file:

            # If logs of room entry or creation are found.
            match=re.search('([0-9\.]+ [0-9:]+).+Joining or Creating Room: (.+)',line)
            if match != None:
                output_file.write(match.group(1) + " World: " + match.group(2) + "\n")
            
            # If logs of room leaving is found
            match=re.search('([0-9\.]+ [0-9:]+).+\[Behaviour\] Initialized PlayerAPI "(.+)" is remote',line)
            if match != None:
                output_file.write(match.group(1) + "  User: " + match.group(2) + "\n")

    # Finish writing to output file
    output_file.close()

# Runs only when directly activated
if __name__ in '__main__':
    main()
