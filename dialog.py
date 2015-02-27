#!/usr/bin/env python
# encoding=utf-8

# vytvory front_end a posktuje funkcie pre
# posielanie a ziskavanie dat z neho

import sys

class dialog:
	def __init__(self):
		pass

	def send(self, msg):
		print msg

	def get(self, msg):
		return raw_input(msg)

	def flush(self):
		sys.stdout.flush()


