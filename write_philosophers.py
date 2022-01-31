def main():
    outfile = open("philosophers.txt", "w")

    #Write the names of three philosophers to the file -
    # John Locke, David hume and Edmund Burke
    name1 = "John Locke"
    name2 = "David Hume"
    name3 = "Edmund Burke"

    outfile.write(name1 + "\n")
    outfile.write(name2 + "\n")
    outfile.write(name3 + "\n")

    #Close the File
    outfile.close()

main()