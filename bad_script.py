
def main():
    print("bad script ONLY runs when it is called by name")
    print("good script")

# this is ONLY true if you invoke the script directly by name, i.e.: python3 bad_script.py

# this is FALSE if it is imported
if __name__ == "__main__":
    main()
