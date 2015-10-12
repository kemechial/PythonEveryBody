input_data = raw_input("Enter Email line: ")
start = input_data.find('@')
stop = input_data.find(" ", start)
host = input_data[start + 1:stop]
print host
