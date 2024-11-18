
list = [10,5,2,3,5,6,7,9,0,6]

sampleset = set(list)

print(type(sampleset))

print(set)

if 100 in sampleset:
    print("true")

else:
    print("false")

set1 = set([])
set1.add(12)
set1.add(20)
set1.add(50)
set1.add(0)
set1.add(10)

set1.remove(10)
#set1.remove(60)
set1.discard(60)


print(set1)



#set Operations
#1) Union
#2) Intersection
#3) Difference
#4) Symmetric Diffrence

a = {2,4,1,7}
b = {1,3,4,7,8}

print(a.union(b))
print(a|b)

print(a & b)

print(a.intersection(b))

print(a.difference(b))
print(a-b)

print(b.difference(a))

#SYmmetric diffrence is (union of sets - intersection of sets)
# removes comon terms
# a^b

print(a^b)
print(a.symmetric_difference(b))





