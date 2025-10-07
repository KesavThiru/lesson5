costprice = int(input("enter the costprice"))
sellprice = int(input("enter the sellprice"))
if sellprice > costprice:
    print("profit")
    p=sellprice-costprice
    print (p)
else :
    print("no profit")
