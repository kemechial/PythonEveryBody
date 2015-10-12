f_hand = open('input.txt', 'r')
count = 0
for line in f_hand:
    count += 1
    line=line.rstrip()
    if line.startswith('a'):
        print '-----found---- ',line
    else:
        print line
print 'number of lines', count
print 'reading the whole file:'
f_hand.close()
f_hand = open('input2.txt', 'r')
inp = f_hand.read()
len_inp=len(inp)
print 'number of characters',len(inp)
print "ord(inp[the last] (10 is new line)):",ord(inp[len_inp-1])
f_hand.close()
