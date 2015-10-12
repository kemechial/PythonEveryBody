lst = list()
try:
    f_hand = open("romeo.txt")
    for line in f_hand:
      line = line.rstrip()
      l_lst = line.split()
      for w in l_lst:
        if not w in lst:
            lst.append(w)
    f_hand.close()
except:
    print "Invalid Filename"

lst.sort()
print lst
