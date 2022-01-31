def main():
    #Open a file named philosophers.txt
    infile = open("philosophers.txt", "r")

    #Read the file's contents.
    #file_contents = infile.read()
    
    line1 = infile.readline().rstrip("\n")
    line2 = infile.readline().rstrip("\n")
    line3 = infile.readline().rstrip("\n")

    #Print the data that was read into memory
    #print(file_contents)

    print(line1)
    print(line2)
    print(line3)
    #Close the File
    infile.close()

#Call Main

def add_my_name():
    outfile = open("philosophers.txt", "a")

    myname = input("Enter your name to become a philosopher ")

    outfile.write(myname + "\n")

    #Close the File
    outfile.close()
main()
add_my_name()