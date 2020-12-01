file = open("wordlist.txt", "r")

outfile = ""

for line in range(1, 10):
        outfile += file.readline()
    
    
print(outfile)