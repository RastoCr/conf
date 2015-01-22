#!/usr/bin/env python
# encoding=utf-8

# vytvory front_end a posktuje funkcie pre
# posielanie a ziskavanie dat z neho

def get_front_end():
	return dialog()

#virtualna trieda
class front_end:
	def __init__(self):
		pass
	def send(self,msg):
		pass
	def get(self, msg):
		pass

class dialog(front_end):
	def __init__(self):
		front_end.__init__(self)

	def send(self, msg):
		print msg

	def get(self, msg):
		return raw_input(msg)


#TODO zvysne front_endy
