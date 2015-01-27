#!/usr/bin/env python
# encoding=utf-8

# spravuje formatovanie vstupnych suborov
# otazok ktore su spravovavane, poskytuje 
# funkcie pre zobrazenia a ziskavanie tychto formatov

class question:
	def __init__(self, TYPE, DEFAULT, PRIORITY, DESC, LDESC):
		self.TYPE     = TYPE
		self.DEFAULT  = DEFAULT
		self.PRIORITY = PRIORITY
		self.DESC    = DESC
		self.LDESC    = LDESC

	def printable(self):
		return "Type:{}\nDefault:{}\nPriority:{}\nDescription:{}\nLong description:{}".format(self.TYPE, self.DEFAULT, self.PRIORITY, self.DESC, self.LDESC)
	
	def ask(self):
		return self.DESC + "\n"

	#TODO rozne typy otazok
	def give_options(self):
		return ""

	#TODO zvysne typy
	def answer_parser(self, answer):
		if (self.TYPE.lower() == "boolean"):
			answer = answer.lower()
			if (answer == 'y' or answer == "yes" or answer == "true"):
				return True
			if (answer == 'n' or answer == "no" or answer == "false"):
				return  False
			raise RuntimeError("Wrong input")
			


def get_from_file(name_of_file):
	try:
		f = open(name_of_file,'r')
		l = get_questions(f)	
		f.close()
		return l
	except NameError:
		print "Wrong file name\n"
		return {}

def get_questions(FILE):
	result = {}
	line = FILE.readline()
	while line != "":
		if line[0] == '<':
			caption = line[1:][:-2]
			result.update( {caption:get_question(FILE)} )
		line = FILE.readline()	
	return result

#TODO nech to necykli ked niekto spravi zly format.
def get_question(FILE):
	a = FILE.readline()
	TYPE = a.split(":")[1][:-1]
	a = FILE.readline()
	DEFAULT = a.split(":")[1][:-1]
	a = FILE.readline()
	PRIORITY = a.split(":")[1][:-1]
	
	a = FILE.readline()	
	DESC = a.split(":")[1]
	while True:
		a = FILE.readline()	
		if (a.split(":")[0] == "Long description"):
			break
		DESC = DESC + a
	DESC = DESC[:-1]

	LDESC = a.split(":")[1]
	while True:	
		a = FILE.readline()	
		if (a == "</>\n"):
			break
		LDESC = LDESC + a
	LDESC = LDESC[:-1]
	return question(TYPE,DEFAULT,PRIORITY,DESC,LDESC)

