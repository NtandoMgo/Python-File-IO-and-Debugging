#
#
#

def file_read(nameoffile):
    try:
        f = open(nameoffile,'r')
        fr = f.readlines()
        f.close()
        return fr[fr.index('START\n')+1:]
    except:
        print("Sorry, could not find file '{}'.".format(nameoffile))



def main():
    n = eval(input ("Enter word length:\n"))

    print ("Searching...")

    filename = input ("Enter file name:\n") # twelve.txt
    print ("Writing results...")

if __name__=="__main__":
    main()

