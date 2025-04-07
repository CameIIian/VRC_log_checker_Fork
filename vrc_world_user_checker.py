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
# 7. add yt-dlp info mode 
# 8. convert dir2dir mode
# 9. Improved method of "obtaining/determining the date" of the input log file, which is added to the formatted log file.

# TODO:
# - fix problem double data entry when a file with the same name exists.

# imports
from sys import argv, exit
from re import search
from glob import glob
from os import makedirs
from os.path import exists, isdir
import argparse as aps

# Format command line arguments
def getArgs():
    # error cases
    if len(argv) < 2:
        print('[NG] Too few arguments. Enter 1 log file you wish to convert after the conversion script')
        exit(1)
    
    # set Options
    parser=aps.ArgumentParser(description="")
    parser.add_argument("filenames", nargs='*')
    parser.add_argument("-v", "--video",     action="store_true", help="output video information to log")
    parser.add_argument("-r", "--directory", type=str, help="specify a directory instead of a file")
    parser.add_argument("-vr", "-rv",        type=str, help="specify -v and -r at the same time")

    # Analysis options
    args=parser.parse_args()

    count=1
    # Remove unneeded argv and process -r options
    if args.video == True:
        count+=1
    # activate 2 options
    if bool(args.vr) == True:
        args.video = True
        args.directory = args.vr
    # finding for files in a directory
    if bool(args.directory) == True:
        if not exists(args.directory):
            print('[NG] {}\\ is not found'.format(args.directory))
            exit(1)
        else:
            dirFiles = glob(str(args.directory).replace("\\","/").replace("./","").replace("/","")+'/output_log*.txt')

    # ok case
    if bool(args.directory) == False:
        return argv[count::], args.video
    else:
        return dirFiles, args.video

# Main function to format data
def main(filenames, vFlag):
    # if not find output dir, mkdir
    if isdir("output"):
        pass
    else:
        makedirs("output")

    # Run until all files are formatted
    for loop in filenames:
        # Target files for the 1st argument
        path = loop

        # Don't run if file not found
        if not exists(path):
            print('[NG] {} is not found'.format(path))
            exit(1)

        # Determine output file name        
        if search('([0-9\-]+\_[0-9\-]+)\.txt' ,path) != None:
            filename = "output/VRChat_usrlog"+ str(path[-24:-4]) +".txt"
        else:
            filename = "output/VRChat_usrlog.txt"

        # open output file
        output_file = open(filename, mode='a', encoding='utf-8', errors='ignore', buffering=1)

        # Start reading/writing files
        with open(path, mode='r' , encoding='utf-8',errors='ignore') as input_file:

            # Read 1 line at a time from the input file
            for line in input_file:

                # If logs of room entry or creation are found.
                match=search('([0-9\_]+ [0-9:]+).+Joining or Creating Room: (.+)',line)
                if match != None:
                    output_file.write(match.group(1) + " World: " + match.group(2) + "\n")
                
                # If logs of user coming is found.
                match=search('([0-9\.]+ [0-9:]+).+\[Behaviour\] Initialized PlayerAPI "(.+)" is remote',line)
                if match != None:
                    output_file.write(match.group(1) + "  User: " + match.group(2) + "\n")
                
                # If logs of searching video is found
                if vFlag == True:
                    match=search('([0-9\.]+ [0-9:]+).+\[Video Playback\] URL \'(.+)\' resolved to .+',line)
                    if match != None:
                        output_file.write(match.group(1) + " Video: " + match.group(2) + "\n")

        # Finish writing to output file
        output_file.close()
        print("[OK] Conversion End\n     Output file named: "+str(filename))

# Runs only when directly activated
if __name__ in '__main__':
    args, videoFlag=getArgs()
    main(args, videoFlag)
