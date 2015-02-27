#!/usr/bin/env python
# encoding=utf-8

# vytvory front_end a posktuje funkcie pre
# posielanie a ziskavanie dat z neho

import sys
from front_end_selector import select
from dialog		import dialog


def get_front_end():
	end = select()
	if (end == "dialog"):
		return dialog()


#TODO zvysne front_endy
