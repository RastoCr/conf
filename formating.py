#!/usr/bin/env python
# encoding=utf-8

# spravuje formatovanie vstupnych suborov
# otazok ktore su spravovavane, poskytuje 
# funkcie pre zobrazenia a ziskavanie tychto formatov

#

# TODO: nacitavanie otazok zo suboru
def get_questions(FILE):
	return {"1":question("Mas rad UNIX?"),"2":question("Mas rad korytnacky?")}


class question:
	def __init__(self, QUESTION):
		self.QUESTION = QUESTION




