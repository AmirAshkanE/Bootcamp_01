print("----","\t","----","\t","----")
print(1**2,"\t",1**3,"\t",1**4)
print(1**2,"\t",1**3,"\t",1**4)
print(2**2,"\t",2**3,"\t",2**4)
print(3**2,"\t",3**3,"\t",3**4)
print(4**2,"\t",5**3,"\t",5**4)
print(6**2,"\t",6**3,"\t",6**4)
print(7**2,"\t",7**3,"\t",7**4)
print(8**2,"\t",8**3,"\t",8**4)



# Another way

for i in range(1,10):
    for j in range(2,5):
        print(i**j,end="\t")
    print("\n")   
        