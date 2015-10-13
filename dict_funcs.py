new_dict=dict()
dict2={}
new_dict["test"]=5
dict2["car"]="bmw"
print dict2
print new_dict
new_dict["test"]+=1
print new_dict
print "ship" in dict2
print dict2.get("rolls royce","not found")
print dict2.get("rolls royce",0)
#same as
if "rolls royce" in dict2:
    print dict2["rolls royce"]
else:
    print "not found"
