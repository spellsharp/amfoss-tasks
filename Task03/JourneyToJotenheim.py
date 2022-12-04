t = int(input())
for i in range(t):
    n = int(input())
    a,b,c = input().split()
    x = int(a)
    y = int(b)
    z = int(c)

    if n==1:
        
        if x == 0:
            print("NO")
        elif x == 2:
            if y == 0:
                print("NO")
            else:
                print("YES")
        elif x == 3:
            if z == 0:
                print("NO")
            else:
                print("YES")
            
    if n==2:
        
        if y == 0:
            print("NO")
        
        elif y == 1:
            if x == 0:
                print("NO")
            else:
                print("YES")
        elif y == 3:
            if z == 0:
                print("NO")
            else:
                print("YES")
            
    if n==3:
        
        if z == 0:
            print("NO")

        elif z == 1:
            if x == 0:
                print("NO")
            else:
                print("YES")
        elif z == 2:
            if y == 0:
                print("NO")
            else:
                print("YES")
            