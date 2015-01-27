#!/usr/bin/env python
# encoding=utf-8

from conf_module import conf_start

print 40*'='
CONF=conf_start()		
CONF.make_front_end("template")			
CONF.ask_question( "bananas" )						
answer = CONF.get_answer( "bananas" )
if answer:
	CONF.msg("Ano banany su dobre")
	CONF.show()
else:
	CONF.warn("Ne ne!")
CONF.stop()
print 40*'='
print answer

