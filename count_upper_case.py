# count the number of upper case , lower case , vowels,digits , space , and special symobols from a given string

class String:
  def __init__(self,msg):
    self.uppercase=0
    self.lowercase=0
    self.vowel=0
    self.digit=0
    self.space=0
    self.specialsymbol=0
    self.msg=msg
    
  def count_uppercase(self):
    for i in self.msg:
      if i.isupper():
        self.uppercase=self.uppercase+1
  def count_lowercase(self):
    for i in self.msg:
      if i.islower():
        self.lowercase=self.lowercase+1
        
  def count_vowel(self):
    for i in self.msg:
      if i in ('a','e','i','o','u','A','E','I','O','U'):
        self.vowel=self.vowel+1
  def count_digit(self):
    for i in self.msg:
      if i.isdigit():
        self.digits=self.digits+1
  def count_space(self):
    for i in self.msg:
      if i.isspace():
        self.space=self.space+1
  def count_specialsymbol(self):
    for i in self.msg:
      if i.isalpha():
        pass
      elif i.isspace():
        pass
      elif i.isdigit():
        pass
      else:
        self.specialsymbol=self.specialsymbol+1
      
  def call_all(self):
    self.count_uppercase()
    self.count_lowercase()
    self.count_vowel()
    self.count_digit()
    self.count_space()
    self.count_specialsymbol()
  
  def printDetails(self):
    print('-'*20)
    print(f'uppercase = {self.uppercase}')
    print(f'lowercase = {self.lowercase}')
    print(f'vowel = {self.vowel}')
    print(f'digit = {self.digit}')
    print(f'space = {self.space}')
    print(f'specialsymbol = {self.specialsymbol}')

msg=input("Enter a string :- ") 
s1=String(msg)

s1.call_all()
s1.printDetails()