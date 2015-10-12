f_name=raw_input("Enter a filename: ") # words.txt
try:
    f_hand=open(f_name)
except:
    print "Invalid Filename"
    exit()

for l in f_hand:
    l=l.rstrip()
    l=l.upper()
    print l
f_hand.close()
