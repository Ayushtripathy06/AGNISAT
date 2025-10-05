#temprature calculater 
tem = float(input("enter the temp "))
unit = input("enter the unit f,c,k,end ").lower()
while unit in ["f","c","k"]:
    print("valid unit")
    if "f" in unit:
        print((tem -32)*5/9,"in c")   
        print((tem -32)*5/9 + 273,"in k")
    elif "c" in unit:
        print (tem*9/5 + 32,"in f")
        print(tem +273,"in k")
    elif "k"in unit:
        print(tem - 273,"in c")
        print((tem - 273) * 9/5 + 32,"in f")
    else:
        print("ending")
    unit =input("enter the unit f,c,k,end ")
    


else:
    print("end")