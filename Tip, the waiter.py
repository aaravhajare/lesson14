
def tip(bill , tip_per) :
    total = bill*(1 + 0.01*tip_per)
    total = round(total,2)
    print("please pay total" , total)

bill = int(input("enter bill"))
tip_per = int(input("enter tip cost"))

tip(bill,tip_per)