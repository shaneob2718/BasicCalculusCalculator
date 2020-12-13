# A derivative calculator for real valued functions 
import sys
import os 
import time 
import math

def menu(): 
	print('Welcome to my Calculus Calculator!') 
	mm_choice=input('Press c to use the calculator \nPress q to quit \n')  
	if mm_choice=="c" and "C": 
		print(' ')
		calculator()   
	elif mm_choice== "q" and "Q": 
		print('Goodbye! \n')
		time.sleep(1)
		sys.exit() # This raises an exception so exception handlers have to be specific 
	else: 
		menu() 

def calculator(): 
	flg1 = 1 
	while flg1 == 1: 
		print('Would you like to differentiate or integrate?')
		choice=input('(Press d to differentiate and i to integrate) \n')
		if choice == 'd': 
			flg1 = 0
			derv_calc() 
		elif choice == 'i': 
			flg1 = 0
			inte_calc() 
		else: 
			print("Invalid option \n") 
			flg1=1 
	
##############################################

# Make into a class ? 
def derv_calc():
	flg2 = 0 
	derv_term_num = 0
	derv_a_suff = ''
	global derv_terms
	derv_terms = [] 

	try: # Handles exception raised when non-char value is inputted as variable 
		var=input('Enter the  variable you are integrating with respect to: \n') 
		if ord(var) <= 122 and ord(var) >= 65: # Restricts variable names to letters
			pass 
		else: 
			print("Invalid input, must be one alphabetical character \n") 
			derv_calc() 
	except TypeError: 
		print("Invalid input, must be one alphabetical character \n") 
		derv_calc() 

	while flg2 == 0: 

		if derv_term_num == 1: # Determines the suffix with the given a-value 
			derv_a_suff = 'st'
		elif derv_term_num == 2: 
			derv_a_suff = 'nd' 
		elif derv_term_num == 3: 
			derv_a_suff = 'rd' 
		else: 
			derv_a_suff='th'

		const=int(input('Enter the ' + str(derv_term_num) + derv_a_suff + ' a-value: \n')) 
		expo=int(input('Enter the exponent of the variable: \n')) 
		derv(const, var, expo) 

		ynflg=0 
		while ynflg==0: 
			yn = input('More terms? (y/n)\n') 
			if yn == 'y': 
				derv_term_num = derv_term_num + 1 # Counts how many terms there are added to the list 
				flg2 = 0 
				ynflg=1
			elif yn == 'n':
				sorted(derv_terms) # needs to be sorted by degree 
				print('\n') 
				print('The derivative of your function is:')
				for i in range(len(derv_terms)-1): 
					print(derv_terms[i] + " + ", end ="")   # Prints out the terms on one line 
				print(derv_terms[derv_term_num]) 

				print("\n")
				entflag=0
				while entflag==0: # This block waits for the user to press enter before continuing 
					enter = input("(Press enter to go back to the menu) \n")
					if enter == "": 
						entflag=1
						ynflg=1
						menu() 
					else: 
						ynflg=1
						entflag=0
			else: 
				print("Invalid input \n") 
				ynflg=0 

def derv(const, var, expo): 
	diff=expo-1 
	if diff == 1: 
		actd = str(expo*const) + str(var) # actd being the actual derivative, str casts the variables to a string to be printed normally 
		derv_terms.append(actd)
	elif diff == 0: 
		actd = str(expo*const)
		derv_terms.append(actd)
	else: 
		actd = str(expo*const) + str(var) + '^' + str(expo-1)
		derv_terms.append(actd) 

#################################################

def inte_calc(): 
	flg3 = 0 
	inte_term_num = 0 
	global inte_terms
	inte_terms = []
	inte_a_suff = ''

	try: # Handles exception raised when non-char value is inputted as variable 
		var=input('Enter the  variable you are integrating with respect to: \n') 
		if ord(var) <= 122 and ord(var) >= 65: # Restricts variable names to letters
			pass 
		else: 
			print("Invalid input, must be one alphabetical character \n") 
			inte_calc() 
	except TypeError: 
		print("Invalid input, must be one alphabetical character \n") 
		inte_calc() 

	while flg3 == 0:

		if inte_term_num == 1: # Determines the suffix with the given a-value 
			inte_a_suff = 'st'
		elif inte_term_num == 2: 
			inte_a_suff = 'nd' 
		elif inte_term_num == 3: 
			inte_a_suff = 'rd' 
		else: 
			inte_a_suff='th' 

		const=int(input('Enter the ' + str(inte_term_num) + str(inte_a_suff) + ' a-value: \n')) 
		expo=int(input('Enter the exponent of the variable: \n')) 
		integ(const, var, expo) 

		ynflg2=0
		while ynflg2 ==0: 
			yn = input('More terms? (y/n) \n') 
			if yn == 'y': 
				inte_term_num = inte_term_num + 1 
				flg3 = 0 
				ynflg2=1
			elif yn == 'n':
				sorted(inte_terms) 
				for i in range(len(inte_terms)-1): 
					print(inte_terms[i] + " + ", end ="")   # Prints out the terms on one line 
				print(inte_terms[inte_term_num] + ' +C') 
				
				print("\n")
				entflag=0
				while entflag==0: # This block waits for the user to press enter before continuing 
					enter = input("(Press enter to go back to the menu) \n")
					if enter == "": 
						entflag=1
						ynflg2=1
						menu() 
					else: 
						ynflg2=1
						entflag=0
			else: 
				print("Invalid input \n") 
				ynflg2=0

def integ(const, var, expo): 
	summ=expo+1 
	if summ == const: 
		act_int = str(var) + '^' + str(expo+1) 
		inte_terms.append(act_int) # Use modular division to simplify fractions 
	else: 
		denom=expo+1
		act_int = '(' + str(const) + str(var) + '^' + str(expo+1) + ')' + '/' + '(' + str(denom) + ')' 
		inte_terms.append(act_int)

menu()