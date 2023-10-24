fname = input("Enter the name of the file: ")
if fname == "mbox.txt":   
    fhand = open("mbox.txt", "r")
    count = 0 
    for line in fhand:
        if line.startswith("From:"):
            line = line.rstrip()
            host = line.split('@')[1]
            print(host)
            count = count + 1

    print('Total %d hosts printed.' % count)
    fhand.close()

else:
    print("Write 'mbox.txt' as input.")