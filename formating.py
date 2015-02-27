#!/usr/bin/env python
# encoding=utf-8

# spravuje formatovanie vstupnych suborov
# otazok a typov ktore su spravovavane, poskytuje
# funkcie pre zobrazenia a ziskavanie tychto formatov

from formating_templates import get_string, get_boolean, get_select,get_multiselect,get_note,get_text,get_password


# zacne nacitavanie zo suboru
def get_from_file(name_of_file):
	try:
		f = open(name_of_file,'r')
		l = get_templates(f)	
		f.close()
		return l
	except NameError:
		print "Wrong file name\n"
		return {}


# nacitava otazku z file descriptoru
def get_templates(FILE):
	result = {}
	line = FILE.readline()
	# ignoruj prazdne riadky
	while line != "":
		# zaciatok vzoru
		if line[0] == '<':
			# meno vzoru
			caption = line[1:][:-2]
			# nacitanie vzoru
			result.update( {caption:get_template(FILE)} )
		line = FILE.readline()	
	return result

def get_template(FILE):
	try:
		# type
		a = FILE.readline()	
		TYPE = a.split(":")[1][:-1]
	except IndexError:
		raise RuntimeError("Wrong format of the template file:\n{}\n".format(FILE) )	
		# ak riadok nejde rozdelit je chyba vo formate

	TYPE = TYPE.lower()
	if (TYPE == "string"):
		return get_string(FILE)
	if (TYPE == "boolean"):
		return get_boolean(FILE)
	if (TYPE == "select"):
		return get_select(FILE)
	if (TYPE == "multiselect"):
		return get_multiselect(FILE)
	if (TYPE == "note"):
		return get_note(FILE)
	if (TYPE == "text"):
		return get_text(FILE)
	if (TYPE == "password"):
		return get_password(FILE)
	raise RuntimeError("Wrong format of the template file:\n{}\n".format(FILE) + "Was expecting type of a template, got: `{}`".format(TYPE) )


