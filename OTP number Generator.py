'''PROJECT NUMBER 2'''

import random as r
a=set()
while True:
	t=int(input("WHAT IS YOUR TOTAL AND GET 25% DISCOUNT ON TOTAL BY ENTERING YOUR AMOUNT---"))
	d=int(input("PHONE NUMBER   "))
	b=str(d)
	if ((b not in a) and len(b)==10):
		print("NEW NUMBER DETECTED")
		a.add(b)
		c=r.randint(1,9999)
		print("one time password is here ",c)
		e=int(input("GIVE YOUR OTP---"))
		while True:
			if (e==c):
					n=.25*t
					m=t-n
					print("THE AMOUNT TO BE PAYED AFYTER DISCOUNT IS ",m)
					break
			elif(e!=c):
				print("invalid OTP")
				a.remove(b)
				break		
	elif((b in a)):
		print("NO OFFER")
		print("THE AMOUNT TO BE PAYED AFYTER DISCOUNT IS ",t)
	elif(d==000):
		 print("invalid number")
		 break
	elif(len(b)<10):
		print("invalid number")
	
	







