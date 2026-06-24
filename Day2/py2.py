# Tuple -> Inmutabel
a = (2,34,32,64,86)
# print(a)

# sum , min , max , length , count , delete

# print(sum(a))
# print(min(a))
# print(max(a))
# print(len(a))
# print(a.count(100))
del a
# print(a) # Delete the Touple

# Mapping 

# Dictionary -> Key-value Pair

a = {
    "Name" : "Sharry",
    "Age" : 20,
    "Course" : "Btech",
    "Location" : "Rania"
}

print(a)

# get , keys , values , items , pop , clear , delete

print(a.get("Age"))
print(a.keys())
print(a.values())
print(a.items())
a.pop("Location")
print(a)
a.clear()
print(a)

del a

# Set 
# -> Mutable and Immutable
a = {23 , "S_GILL" , 68 , "Shamsher" , 67 , 23.2}
print(a)

# Add , update , pop , union , intersection , difference , clear , delete

a.add(11)
# a.update([1,2,3])
# print(a) 

b = {59,11,12,99}
c = a.union(b)
d = a.intersection(b)
print(a,b,c,d)

print(a.difference(b))

a.clear()
print(a)

del a