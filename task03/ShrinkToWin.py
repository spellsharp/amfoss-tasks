#python3

userinp = input()
sum = 0
count = 0
while len(str(userinp))>1:
    for i in str(userinp):
        sum+= int(i)
    userinp = sum
    sum=0
    count+= 1
print(count)