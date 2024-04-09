class Bank:
  bankName="union bank of india"
  branch="Sidhi"
  
  #create account
  def __init__(self,username,pan,address):
    self.username=username
    self.pan=pan
    self.address=address
    self.balance=0.0
    print(f"{self.username} cong! your account create successfully")
  
  #create deposit
  def deposit(self,amount):
    self.balance=self.balance+amount
    print(f'{amount} deposited successfully ')
  #Withdraw amount
  def withdraw(self,amount):
    if amount<self.balance:
      self.balance=self.balance-amount
      print(f'{amount} withdraw successfully')
    else:
      print("Infficent fund.....")
      
  #ministatement 
  def ministatement(self):
    print(f'your current account balance is {self.balance}')
  
  
print(f'Welcome to {Bank.bankName},{Bank.branch}') 
username=input("please enter your username : ")
pan=input("enter pan card number : ")
address=input("enter your address :- ")
b=Bank(username,pan,address)

while True:
  print("Please select your any option")
  print('1.Deposit\n2.withdraw\n3.ministatement\n4.stop')
  option=int(input(''))
  
  if option==1:
    amount=float(input("Enter your deposit amount"))
    b.deposit(amount)
    
  if option==2:
    amount=float(input("Enter your withdraw amount"))
    b.withdraw(amount)
  
  if option==3:
    b.ministatement()
  
  if option==4:
    print("Thanks for useing this bank machine ")
    break