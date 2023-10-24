fname = input("Enter the name of the file: ")
try:
    f = open(fname)
    while True:
        line = f.readline().rstrip()
        
        if not line:
            f.close()
            break
        
        print(line.upper())

except:
    print("The file does not exist.")