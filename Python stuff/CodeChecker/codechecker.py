'''
Python program I wrote to tell me stats on my code.

This can:
1 - Find syntax errors in code -> does this just by running it.
2 - Test my functions and try to "break" them
3 - Tell me how fast the program took to run
4 - Make a readme file
'''
import os, time, sys, atexit
	
class CodeChecker():

	def __init__(self):
		super(CodeChecker, self).__init__()
		this_file = os.path.dirname(os.path.realpath(__file__))
		self.user_file = this_file
		self.auto_create_file = True
		
		#create code_file
		#This part is written for me, personally.
		#I usually start my programs with a multiline comment that contains the code's description
		

	def code_to_write(self, parameters_as_list):
		cc_list = []
		cc_list.append("import CodeChecker")
		for parameter in parameters_as_list:
			cc_list.append(parameter)
			
		return cc_list
			
	
	def create_code_file(self):
		self.code_filename = self.user_file.replace(".py","-cc.py")
		self.code_file = open(self.code_filename, "w")
		write_code = code_to_write
		
		
		
	def create_readme(self, filename="ccReadme.txt", auto_create_file=self.auto_create_file):
		'''
		Create a readme file to dump the code description and a bunch of info
		if something with that filename already exists, prompt the user
		
		Set auto_create_file to False if you don't want this accidently overwriting files of the same name
		'''
		self.readme = filename
		create_file = self.auto_create_file
		if create_file == False:
			try:
				does_exist = open(self.readme, "r")
				while overwrite.lower() != 'y' or 'n':
					overwrite = input("A file already exists named " + self.readme + ". This file will be overwritten\nProceed anyway? [y/n]")
				create_file = False #If the user somehow exits the loop without entering Y/N, no file will be overwritten
				if overwrite.lower() == 'y':
					create_file = True
			except:
				create_file = True
			
		if create_file == True:
			self.readme = open(self.readme, "w")#Wipe it.
			self.readme.write(self.filestuff)
		
	def code_description(self, description):
		'''
		OPTIONAL:  Write out a description of what the program needs to do
		
		If the description is written as a comment at the top of the python program, simply
		input the beginning and ending line numbers as a tuple, (first_line_number, last_line_number)
		'''
		
		try:
			#Check if it isn't a string
			string = str(string)
			string += "1"
		
		self.description = description
	
	def check_banned_words(self, words_to_omit):
		'''
		where words_to_omit is a list of words, phrases, or functions to check the program for.
		-----------code should not execute if any word or phrase in words_to_omit is found------
		
		Purpose: Don't want users creating files, importing certain modules,
		messing with the system, creating fork bombs, etc.		
		'''
		self.open_file = open(self.user_file, "r")
		line_num = 0
		
		for line in self.open_file.readlines():
			line_num +=1
			for word in words_to_omit:
				if word in line:
					self.open_file.close()
					return("Sorry, you cannot use '{}' in this code.\nline {}, {}".format(word, str(line_num), line))
		self.open_file.close()
		return(True)
	def check_syntax(self):
		'''
		Should only run this if check_code returns True.
		
		Otherwise you are vulnerable to lots of stuff.
		'''
		try:
			##############################################error here for some reason
			result = os.system("python " + (self.user_file))
		except:
			print("unable to execute file.")
	def set_requirements(self, required, required_type, error_msg=None):
		#required_type can be tuples with format (object_type, object_value)
		#Object value will not work for Class, Function, or dictionary
		'''
		this will check the user's file for specific variables or lines.
		
		For example, if the assignment is to have the user make a variable named x and set it to 10,
		this would check for a variable x which is equal to 10.
		
		Required_type is used in collaboration with required. For example, If you want to have the user
		create a function named list_maker, you would pass:
			set_requirements("list_maker", "function")
		Other examples:
			set_requirements("x", "10", "Error, you do not set x = 10")
		
		Supported types are: "var", "function", "int", "str", "list", "Class"
		'''
		sys.path.append(str(self.user_file))
		import execute
		
		my_string = "Example variables"
		my_int = 123456789
		my_float = 3.14159
		my_bool = True
		my_tuple = (123, 456)
		my_list = ["empty", "list"]
		my_dict = {'empty': 'dict'}

		index_num = -1
		
		self.bool_list = []# list for checking completed section with T/F values
		self.req_value = []# list that compares variables with exact values if a tuple is entered with (object_type, object_value)
		for iterable in required_type:
			if type(iterable) == type(my_tuple):
				self.req_value.append(iterable[1])
			else:
				self.req_value.append("None")
				
		for index in required:
			index_num += 1
			
			
			#Instead of checking to see what the user's variable is
			#this will compare variable types.  Less efficient, more accurate.
			
			if hasattr(execute, index):
				var_info = getattr(execute, index)
				var_type = required_type[index_num]
				if var_type in iterable_list:
					if var_type == "var":
						if type(var_info) == type(my_string)\
							or type(var_info) == type(my_int)\
							or type(var_info) == type(my_float)\
							or type(var_info) == type(my_bool):
							self.bool_list.append(True)
							print("{} exists, and it is a variable".format(index))
						else:
							self.bool_list.append(False)
							
					elif var_type == "function":
						if type(var_info) == type(my_function):	
							self.bool_list.append(True)
							print("{}, exists, and is a function")
						else:
							self.bool_list.append(False)
							
					elif var_type == "str":
						if type(var_info) == type(my_string):
							self.bool_list.append(True)
						else:
							self.bool_list.append(False)
							
					elif var_type == "int":
						if type(var_info) == type(my_int):
							self.bool_list.append(True)
						else:
							self.bool_list.append(False)
							
					elif var_type == "float":
						if type(var_info) == type(my_float):
							self.return_list.append(True)
						else:
							self.bool_list.append(False)
							
					elif var_type == "bool":
						if type(var_info) == type(my_bool):
							self.bool_list.append(True)
						else:
							self.bool_list.append(False)
							
					elif var_type == "tuple":
						if type(var_info) == type(my_tuple):
							self.bool_list.append(True)
						else:
							self.bool_list.append(False)
							
					elif var_type == "list":
						if type(var_info) == type(my_list):
							self.bool_list.append(True)
						else:
							self.bool_list.append(False)
							
					elif var_type == "dictionary":
						if type(var_info) == type(my_dict):
							self.bool_list.append(True)
						else:
							self.bool_list.append(False)
							
				elif var_info == var_type:
					self.bool_list.append(True)
			else:
				self.bool_list.append(False)
		
		ind_num = -1
		NO_VALUE = ["dictionary", "class", "function"]
		for index in self.bool_list:
			ind_num +=1
			if index == True:
				print("{} returned True to value {}".format(required[ind_num], required_type[ind_num]))
			else:
				if required_type[ind_num] not in NO_VALUE:
					if self.req_value[ind_num] != "None":
						print("""Oops, you need to make a {} named {}, 
							equal to {}.""".format(required_type[ind_num]), required[ind_num], self.req_value[ind_num])
					else:
						print("Oops, you do not have a {} named {}".format(required_type[ind_num], required[ind_num]))
				
				
				
				
	def test_functions(self, function_name, vars_to_pass, expected_results):
		'''
		This is gonna be weird to use.  
		This only tests functions.
		'''
		pass
file = "write.py"
my_c = CodeChecker(os.getcwd() + "\\" + str(file))

iterable_list = ["var", "int", "str", "bool", "float", "tuple", "list", "dictionary", "function", "class"]

while True:
	#file = input("What file would you like to run?")
	#omit = list(input("Enter words you'd like to omit\n>"))
	#file = "hello.py"
	try_again = input("Hit enter to save and run your code.")
	if len(try_again) <1:
		my_c.copy_paste("write.py", "execute.py")
	omit = ["import", "open"]
	
	if len(omit) < 1:
		omit = None
	#usr_file = (os.getcwd() + "\\" + str(file))
	code = my_c.check_banned_words(omit)
	
	if code == True:
		y = my_c.check_syntax()
	else:
		print(code)
	my_c.set_requirements(["x", "y", "z", "lister", "tupler",], ["var", "var", "var", "list", "tuple"])
	time.sleep(2)

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
		
		
		