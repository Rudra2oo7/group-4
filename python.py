'''name = input("hello, whats your name? ").title().strip()
first, last = name.split(" ")

print(f"shut up {first}") 


x = float(input("x = "))
y = float(input("y = "))
#for format print (f"{x+y:,}")
print (f"{x/y:.2f}")
'''
'''
def main():
		
	name = input("what is your name? ")
	hello(name)
	
def hello(to):
	print ("shut up", to)
	
main()

ans = input("what is the password: ")
def main (ans):
	if "khul jaa sim sim" in ans :
		return "unlocked"
	else:
		return "intruder"

password = main(ans)
print(password)
'''

'''x = int(input("what is x? "))
y = int(input("what is y? "))
if x < y:
	a = y - x
	
else:
	a = x - y
print("the positive difference of the two numbers is", a)
'''

'''
def evenodd():
	x = int(input("pick a number "))
	if boo(x):
		print("even")
	else:
		print('odd')

def boo(n):		
	return n%2==0
	
		
evenodd()
'''
'''
---------------------------------------------------------------code for backup security system ----------------------------------------------------------------------------------------------------
'''
import time
a=0
b=0
def main():
	global a
	global b
	x = input("please enter the backup password to obtain the password: ")
	if x == "security":
		print("the password is rudra122907")
		exit()
	else:
		a= a+1
		if a == 3:
			print("locked!!... try again later in", 5+b,"seconds")
			time.sleep(5+b)
			b= b+10
			a=0
			main()
		print("incorrect!... please try again.",    3-a,"attempts left")
		
	
while a <=3:
	main()
	

'''
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
		
		
	

