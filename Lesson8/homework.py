
input1 = int(input("pick a number ")) 
input2 = int(input("pick a number ")) 
input3 = int(input("pick a number ")) 
input4 = int(input("pick a number ")) 
input5 = int(input("pick a number ")) 


set1 = set([])
set1.add(input1)
set1.add(input2)
set1.add(input3)
set1.add(input4)
set1.add(input5)

input6 = int(input("pick a number ")) 
input7 = int(input("pick a number ")) 
input8 = int(input("pick a number ")) 
input9 = int(input("pick a number ")) 
input10= int(input("pick a number ")) 


set2 = set([])
set2.add(input10)
set2.add(input7)
set2.add(input8)
set2.add(input9)
set2.add(input6)


print(set1.union(set2))

print(set1.intersection(set2))

print(set1.difference(set2))

print(set1.symmetric_difference(set2))
