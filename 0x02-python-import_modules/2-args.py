#!/usr/bin/python3

if __name__ == "__main__":
  
    """Print the number of and list of arguments."""
    import sys
    
    """removed the name of the script at index 0"""
    arg = (sys.argv) - 1  
    if arg == 0:
        print("0 arguments.")
    elif arg == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arg))
        """" printing args with their index """
    for i in range(arg):
        print("{} : {}".format(i+1, sys.argv[i+1]))
