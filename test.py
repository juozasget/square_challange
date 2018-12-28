
# Def list
list = [2, 45, 1, 3, 4, 45, 5, 42, 46]

dict = {}
sum = 47

# Run list check
for item in list:

    key = sum - item
    if dict.get(str(key)):
        print("%s, %s" % (str(key), str(item)))
        # Delete dict item 
        dict.pop(str(key))
    else:
        dict[str(item)] = item
