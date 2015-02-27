#!/usr/bin/env python
# encoding=utf-8

# spravuje formatovanie vstupnych suborov
# otazok ktore su spravovavane, poskytuje 
# funkcie pre zobrazenia a ziskavanie tychto formatov

class template:
	def __init__(self, DESC, LDESC):
		self.DESC    = DESC
		self.LDESC    = LDESC

	def printable(self):
		return "Description:{}\nLong description:{}".format(self.DESC, self.LDESC)	

class note(template):
	def __init__(self, DESC, LDESC):
		template.__init__(self, DESC, LDESC)

class text(template):
	def __init__(self, DESC, LDESC):
		template.__init__(self, DESC, LDESC)
		
class question(template):
	def __init__(self, DEFAULT, PRIORITY, DESC, LDESC):
		template.__init__(self, DESC, LDESC)
		self.DEFAULT  = DEFAULT
		self.PRIORITY = PRIORITY

	def ask(self):
		return self.DESC + "\n"

class password(question):
		def __init__(self, DEFAULT, PRIORITY, DESC, LDESC):
			question.__init__(self, DEFAULT, PRIORITY, DESC, LDESC)

class string(question):
		def __init__(self, DEFAULT, PRIORITY, DESC, LDESC):
			question.__init__(self, DEFAULT, PRIORITY, DESC, LDESC)

class select(question):
	def __init__(self, CHOICES, DEFAULT, PRIORITY, DESC, LDESC):
		question.__init__(self, DEFAULT, PRIORITY, DESC, LDESC)
		self.CHOICES = CHOICES

	def give_options(self):
		return str(self.CHOICES)

	def answer_parser(self, answer):
		if (answer in self.CHOICES):
			return answer
		raise RuntimeError("Answer is not among choices - Wrong input")
			

class multiselect(select):
	def __init__(self, CHOICES, DEFAULT, PRIORITY, DESC, LDESC):
		select.__init__(self,CHOICES, DEFAULT, PRIORITY, DESC, LDESC)

	def answer_parser(self, answers):
		for answer in answers:
			if (answer in self.CHOICES):
				pass
			else:
				raise RuntimeError("Answer is not among choices - Wrong input")
		return answers
		

class boolean(select):
	def __init__(self, DEFAULT, PRIORITY, DESC, LDESC):
		select.__init__(self, [True, False], DEFAULT, PRIORITY, DESC, LDESC)

	def answer_parser(self, answer):
		answer = answer.lower()
		if (answer == 'y' or answer == "yes" or answer == "true"):
			return True
		if (answer == 'n' or answer == "no" or answer == "false"):
			return  False
		raise RuntimeError("Wrong input")

def get_description(FILE):
	a = FILE.readline()
	DESC = a.split(":")[1]
	
	while True:
		a = FILE.readline()
		#koniec suboru
		if ( a == "" ):
			raise RuntimeError("Wrong format of the template file:\n{}\n".format(FILE) )
		# precitalo uz cely description a ide citat long
		if (a.split(":")[0] == "Long description"):
			break
		DESC = DESC + a
	DESC = DESC[:-1]
	try:
		LDESC = a.split(":")[1]
	except IndexError:
		raise RuntimeError("Wrong format of the template file:\n{}\n".format(FILE) )	
	while True:	
		a = FILE.readline()
		#koniec suboru
		if ( a == "" ):
			raise RuntimeError("Wrong format of the template file:\n{}\n".format(FILE) )	
		if (a == "</>\n"):
			break
		LDESC = LDESC + a
	LDESC = LDESC[:-1]
	return DESC, LDESC

def get_choices(FILE):
	a = FILE.readline()
	return a.split(":")[1][:-1].split("/ ")

def get_default(FILE):
	a = FILE.readline()
	return a.split(":")[1][:-1]

def get_priority(FILE):
	a = FILE.readline()
	return a.split(":")[1][:-1]
		
		
def get_boolean(FILE):
	DEF = get_default(FILE)
	PRIO = get_priority(FILE)
	DES, LDES = get_description(FILE)
	return boolean(DEF, PRIO, DES, LDES )

def get_select(FILE):
	CHOI = get_choices(FILE)
	DEF = get_default(FILE)
	PRIO = get_priority(FILE)
	DES, LDES = get_description(FILE)
	return select(CHOI, DEF, PRIO, DES, LDES )

def get_multiselect(FILE):
	CHOI = get_choices(FILE)
	DEF = get_default(FILE)
	PRIO = get_priority(FILE)
	DES, LDES = get_description(FILE)
	return multiselect(CHOI, DEF, PRIO, DES, LDES )

def get_note(FILE):
	DES, LDES = get_description(FILE)
	return note(DES, LDES)

def get_text(FILE):
	DES, LDES = get_description(FILE)
	return text(DES, LDES)

def get_password(FILE):
	DEF = get_default(FILE)
	PRIO = get_priority(FILE)
	DES, LDES = get_description(FILE)
	return password(DEF, PRIO, DES, LDES)

def get_string(FILE):
	DEF = get_default(FILE)
	PRIO = get_priority(FILE)
	DES, LDES = get_description(FILE)
	return string(DEF, PRIO, DES, LDES)

