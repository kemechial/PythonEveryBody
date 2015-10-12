handle=open("mbox-short.txt")
count=0
for line in handle:
    line=line.rstrip()
    if not line.startswith("From "): continue
    words=line.split()
    count+=1
    print words[1]
print "There were", count, "lines in the file with From as the first word"
handle.close()
