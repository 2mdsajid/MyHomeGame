global p
p=[]
def clear():
	import os
	os.system( 'clear' )

def r1():
	print("This is my room")
	p.append("bal")
	inside()
	
def r2():
	print("This is the TV room ")
	p.append("bal")
	inside()
		
def r3():		
	print("This is freezer room")
	p.appwnd("bal")
	inside()

def c_r3():
	print("\nyou're near freezer room")
	dd = input("Direction > ")
	if dd == "w":
		r3()
	elif dd=="f" or dd == "s":
		p.append("mid")
		con()
	elif dd =="b" or dd == "n":
		d_bal()
	elif dd == "q":
	 	print("Thanks for visiting ! ")
	 	exit()
	else:
		c_r3()

def d_bal():
	print("\nyou're at balcony")
	db =input("Direction > ") 
	if db == "r" or db == "e":
		r1()
	elif db == "l" or db == "w":
		r2()
	elif db == "f" or db == "s":
		c_r3()
	elif db == "q":
	 	print("Thanks for visiting ! ")
	 	exit()
	else:
		d_bal()



def m_r1():
	 print("this is kitchen room")
	 p.append("mid")
	 inside()
	 		 
def m_r2():
	print("upstairs for terrace")
	p.append("mid")
	inside()

def d_mid():
	 print("\nYou're at the midbay")
	 dm =input("Direction > ") 
	 if dm == "l" or dm == "w":
	 	m_r1()
	 elif dm == "r" or dm == "e" :
	 	m_r2()
	 elif dm =="b" or dm == "n":
	 	c_r3()
	 elif dm == "s":
	 	c_er5()
	 elif dm== "q":
	 	print("Thanks for visiting ! ")
	 	exit()
	 else:
	 	print("Can't go !")
	 	d_mid()


def e_r1():
	print("this is Oil shop")
	p.append("ent")
	inside()
	
def e_r2():
	print("This is Gas shop")
	p.append("ent")
	inside()
	
def e_r3():
	print("This is store room ")
	p.append("es")
	inside()
	
def e_r4():
	print("This is too store room")
	p.append("es")
	inside()
		
def e_r5():
	print("This is gues room")
	p.append("eg")
	inside()


def c_er5():
	print("\nyou're near guest room")
	d5 =input("Direction > ")
	if d5 == "r" or d5 == "s" : 
		e_r5()
	elif d5 =="b" or d5 == "w":
		c_er3()
	elif d5 == "l" or d5 == "n":
		p.append("mid")
		con()
	elif d5 == "q":
	 	print("Thanks for visiting ! ")
	 	exit()
	else:
		print("Can't go !")
		c_er5()

def c_er3():
	 print("\nyou're near store room")
	 d3 =input("Direction > ")
	 if d3 == "l" or d3 == "s":
	 	e_r3()
	 elif d3 == "r" or d3 == "n" :
	 	e_r3()
	 elif d3 == "f" or d3 == "e" :
	 	c_er5()
	 elif d3 =="b" or d3 == "w":
	 	d_ent()
	 elif d3 == "q":
	 	print("Thanks for visiting ! ")
	 	exit()
	 else:
	 	print("Can't go !")
	 	c_er3()
	 	
def d_ent():
	 print("\nYou're at the entrance !")
	 de =input("Direction > ") 
	 if de == "l"or de == "s" :
	 	e_r1()
	 elif de == "r" or de == "n" :
	 	e_r2()
	 elif de == "f" or de == "e":
	 	c_er3()
	 elif de == "q":
	 	print("Thanks for visiting ! ")
	 	exit()
	 else:
	 	print("Can't go !")
	 	d_ent()



	 	
	


def inside():
	while True:
		d1 = input("\nDirection> ")
		if not d1 == "b":
			print("Sorry ! You're inside a room ")
			continue
		else:
			if p[-1] == "bal":					
				d_bal()
			elif p[-1] == "mid":
				d_mid()
			elif p[-1] == "ent":
				d_ent()
			elif p[-1] == "eg":
				c_er5()
			elif p[-1] == "es":
				c_er3()
			
				
def con():
	if p[-1] == "bal":					
		d_bal()
	elif p[-1] == "mid":
		d_mid()
	elif p[-1] == "ent":
		d_ent()

def init():
	s = input("Starting Location > ")
	clear()
	if s.lower() =="balcony":
		d_bal()
	elif s.lower() == "midbay":
		d_mid()
	elif s.lower() =="entrance":
		d_ent()
	elif s == "q":
		print("Thanks ! ")
		exit()
		
		
def start():
	print("Welcome to My Home !")
	print("""You can use the keys like
f - foreward
b - back
n - north
s - south
e - east
w - west
	
There are 10 rooms. you can start your game at either of 
these three places 
a) Entrance
b) Midbay
c) Balcony

you can press "q" anytime to quit.
Have a nice day !

(ps : if you're inside a room, first you need to go back 
 and then only you can go somewhere else )
	""" )
	init()
start()	
		