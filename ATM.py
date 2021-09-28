class Atm(object):
     def __init__(self,type,money):
          self.type = type,
          self.money = money

     def CashWithdrawl(self):
         print("Cash is been Widhdrawed")

     def Balance(self):
         print("Your Balance is 2000")
     

     


TwoThousand= Atm("note",2000) 

print(TwoThousand.CashWithdrawl())




