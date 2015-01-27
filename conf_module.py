#!/usr/bin/env python
# encoding=utf-8

# tento subor poskytuje celu funkcionalitu,
# vsetko co sa da spravit, sa da spravit odtialto

from communication import communicator
from front_end     import get_front_end

def conf_start():
	return conf_module()

class conf_module:
	def __init__(self):
		self.priority = 1
		
	def make_front_end(self, file_path):
		end = get_front_end()
		# cesta k suboru z otazkami
		self.comm = communicator(end, file_path)
		try:
			self.comm.load("save.p")
		except:
			pass		

	def ask_question(self, ID):
		self.comm.ask_question ( ID )

	def get_answer(self, ID):
		return self.comm.get_answer( ID )
		
	def msg(self, _msg):
		self.comm.add_to_buffer(_msg)

	def warn(self, _msg):
		self.comm.warn(_msg)
		

	def show(self):
		self.comm.show()

	
	def stop(self):
		self.comm.save("save.p") 
		# TODO exportacia novych odpovedi
		self.comm.stop()

	
