test_string="I have bought a new car last week"
stuff=test_string.split()
print stuff
colors="my favorite colors are, blue, maroon, green, purple"
favorite=colors.split(",")
print favorite
for color in favorite:
    print "---"+color.strip()+"---"
