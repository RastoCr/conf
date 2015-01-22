#!/usr/bin/env python
# encoding=utf-8

# Tento subor ma na starosti komunikaciu s front sendom

from formating import get_questions


class communicator():
	def __init__(self, end, file_path):
		# buffer hlasok pre zobrazenie
		self.buffer = []
		#front_end
		self.end = end
		# otazky vo forme ID:otazky
		self.questions = get_questions(file_path)
		# odpovede vo forme ID:odpoved
		self.answers   = {}


	# prida hlasku k zobrazeniu
	def add_to_buffer(self, msg):
		self.buffer.append(msg)

	# zobrazi vsetky hlasky
	def show(self):
		for msg in self.buffer:
			self.end.send(msg)
			self.buffer = self.buffer[1:]

	# varuje uzivatela (preskoci frontu hlasok)
	def warn(self, msg):
		self.end.send(msg)

	# ziska odpoved z otazky
	def get_answer(self, ID):
		return self.answers[ID]


	def ask_question(self, ID):
		#TODO neupdatovat ak uz je v zodpovedanych za ??podmienok??
		# napriklad uz bola zodpovedana, to sa moze lisit, zodpovedana
		# v behu tohto programu alebo pri predchadzajucej instalacii
		q = self.questions[ID]
		answer = self.end.get(q.QUESTION + "\n")
		self.answers.update({ID:answer})
	

	def stop(self):
		pass
		#TODO destroy front_end
		
