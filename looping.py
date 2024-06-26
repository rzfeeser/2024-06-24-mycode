#!/usr/bin/python3

def main():

    # imagine we have some quantity of username:password combos within a dictionary
    creds = {"admin": "qwerty", "rzf": "openopen123", "testuser": "pa55w0rd", "adminEast": "password"}

    # run across login data and perform some operations on powerflex
    for x in creds:
        print(x)        # x is the "key"
        print(creds[x]) # this would produce the values
        print("----")

    # this returns 2 values; where x is the KEY and y is the VALUE
    for x, y in creds.items():
        print("The user", x, "has the password", y)

    # a list of hostnames pointing to powerflex servers
    powerflex_svrs = ['powerflex01', 'powerflex02', 'powerflex-east', 'powerflex-west']
    for pfs in powerflex_svrs:
        print("connecting to... ", pfs + ".acme.com")



if __name__ == "__main__":
    main()
