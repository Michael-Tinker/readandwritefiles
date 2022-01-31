def main():
    #Open a file named philosophers.txt
    infile = open("clients.txt", "r")

    #Read the file's contents    
    n=0
    #Print the data that was read into memory
    for client in infile:
        n+=1
        client = client.rstrip("\n")
        print(str(n) + ".", client)
        

    #Close the File
    infile.close()

main()