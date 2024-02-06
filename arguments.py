import argparse


## This our arg parser function. I stole the name from the professor's code :P
## It takes arguments from the command line using the argparse module
def demo():
    ## Parser is the assigned variable for our argument parser
    parser = argparse.ArgumentParser()

    ## This is where we declare the arguments we are collecting.
    ## File won't run if these aren't collected from the command prompt.
    parser.add_argument(help = 'Enter a string', dest = 'string',type = str)
    parser.add_argument(help = 'Enter an int', dest = 'int',type = int)
    parser.add_argument(help = 'Enter a float', dest = 'float',type = float)

    ## This is where we grab all of the args. I'm not sure what object 
    ## these are stored in. I just know the syntax for collecting them. 
    args = parser.parse_args()

    ## This grabs the inputs from the args object.
    dummyString = args.string
    dummyInt = args.int
    dummyFloat = args.float

    ## This prints the args. Also lets us know that the code is working.
    print('String: ', dummyString)
    print('Int: ', dummyInt)
    print('Float: ', dummyFloat)


## Only run the code here if the module is directly called
## If imported, it won't run demo.
if __name__ == '__main__':
    demo()

