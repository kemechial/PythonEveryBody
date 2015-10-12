f_name=raw_input("Enter a filename: ") # mbox-short.txt
count=0
sum_spam=0
try:
    f_hand=open(f_name)
except:
    print "Invalid Filename"


for line in f_hand:
    if line.startswith("X-DSPAM-Confidence:"):
        count+=1
        start=line.find(":")
        num=float(line[start+1:].lstrip())
        sum_spam+=num
print  "Average spam confidence:",sum_spam/count

f_hand.close()
