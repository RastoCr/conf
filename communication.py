#!/usr/bin/env python
# encoding=utf-8

# Tento subor ma na starosti komunikaciu s front sendom

from formating import get_from_file
import pickle


DIVIDER = ':'

class communicator():
	def __init__(self, end, file_path):
		# buffer hlasok pre zobrazenie
		self.buffer = []
		#front_end
		self.end = end
		# otazky vo forme ID:otazky
		self.questions = get_from_file(file_path)
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
			self.end.flush()

	# varuje uzivatela (preskoci frontu hlasok)
	def warn(self, msg):
		self.end.send(msg)
		self.end.flush()

	# ziska odpoved z otazky
	def get_answer(self, ID):
		return self.answers[ID]


	def ask_question(self, ID):
		#TODO neupdatovat ak uz je v zodpovedanych za ??podmienok??
		# napriklad uz bola zodpovedana, to sa moze lisit, zodpovedana
		# v behu tohto programu alebo pri predchadzajucej instalacii

		#najde otazku ktorej odpoved chceme
		q = self.questions[ID]	
		while True:
			try:
				text_answer = self.end.get( q.ask() + q.give_options() )
				answer = q.answer_parser(text_answer)
				self.answers.update({ID:answer})
				break
			except RuntimeError:
				self.warn("Wrong input, try again")

	#nacita odpovede zo suboru
	def load(self,file_path):
		ans = pickle.load ( open ( file_path, "rb" ) )
		self.answers.update ( ans )
		
	#ulozi odpovede
	def save(self,file_path):
		pickle.dump( self.answers, open( file_path, "wb" ) )
	

	def stop(self):
		pass
		#TODO destroy front_end
		
