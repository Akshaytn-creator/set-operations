print("1:union of a set:")
print("2:intersection of a set:")
print("3:difference of a set:")
print("4:symmetric difference of a set:")
print("5:length of a set:")
print("6:clear of a set:")
print("7:pop of a set:")
print("8:subset of a set:")
print("9:disjoint of a set:")
print("10:update of a set:")
while True:
    choice=int(input("enter the choice:"))
    if choice==1:
        s1=set(input("enter the first value of a set:").split())
        s2=set(input("enter the second value of a set:").split())
        z=s1.union(s2)
        print(z)
    elif choice==2:
        s1=set(input("enter the first value of a set:").split())
        s2=set(input("enter the second value of a set:").split())
        z=s1.intersection(s2)
        print(z)
    elif choice==3:
        s1=set(input("enter the first value of a set:").split())
        s2=set(input("enter the second value of a set:").split())
        print(s1-s2)
        print(s2-s1)
    elif choice==4:
        s1=set(input("enter the first value of a set:"))
        s2=set(input("enter the second value of a set:"))
        z=s1.symmetric_difference(s2)
        print(z)
    elif choice==5:
        s1=set(input("enter the value of a set:"))
        print(len(s1))
    elif choice==6:
        s1=set(input("enter the value of a set:"))
        s1.clear()
        print(s1)
    elif choice==7:
        s1=set(input("enter the value of a set:").split())
        s1.pop()
        print(s1)
    elif choice==8:
        s1=set(input("enter the first value of a set:").split())
        s2=set(input("enter the second value of a set:").split())
        print(s1.issubset(s2))
    elif choice==9:
        s1=set(input("enter the first value of a set:").split())
        s2=set(input("enter the second value of a set:").split())
        z=s1.isdisjoint(s2)
        print(z)
    elif choice==10:
        s1=set(input("enter the first value of a set:"))
        s2=set(input("enter the second value of a set:"))
        z=s1.update(s2)
        print(z)
        print
        break
    else:
        print("invalid choice!!!")
        
    
    
    