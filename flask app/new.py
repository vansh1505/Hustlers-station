# inp = int(input("enter a number: "))
# i=1
def table():
    inp = int(input("enter a number: "))
    i=1
    while i<=10:
        out= inp*i
        i=i+1
        p=str(out)
        print(str(inp)+" X "+str(i-1)+" = "+p)

table()
while True:
    i2=input()
    if i2=="f":
        exit()
    else: 
        table()
