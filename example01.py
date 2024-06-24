#!/usr/bin/python3


def network_check():
    # your code that checks on network metrics
    print("No current warnings or errors on network intercaces")

def snapshot_taker():
    # you write your contribution
    print("snapshot successful!")


# this is the "zach" function
def main():
    print("Welcome to python class for PowerFlex scripting")

    myvar = input("what is your name? ") # prompts from a STRING

    print(myvar)   # display the STRING

    myothervar = 42     # this is an INT
    mystringvar = "42"  # this is a STR
    myfloatvar = 4.2

    print(myothervar)


    ######### main always calls the functions that do our work
    snapshot_taker()

    network_check()





# call the function
if __name__ == "__main__":
    main()
