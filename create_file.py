#!/usr/bin/python3

def main():
    """ create a file """

    # technique 01 - the original file object
    tabbed_folder = open("myfile.txt", "w")  # create a file object named tabbed_folder
    print("This line goes into the file", file=tabbed_folder) # place line in file object
    print("Second line", file=tabbed_folder)
    tabbed_folder.close() # don't forget to close your file!


    # techinque 02 - auto close by using "with"
    with open("myfile02.txt", "w") as glossy_folder:
        print("This line goes into the file", file=glossy_folder)
        glossy_folder.write("You can write into a file object with the write method\n") # no auto \n like print()
        # when indentation ends, the file is automatically CLOSED


if __name__ == "__main__":
    main()
