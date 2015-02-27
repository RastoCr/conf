#!/usr/bin/env python
# encoding=utf-8

from conf_module import conf_start

print 40*'='
CONF=conf_start()		
CONF.make_front_end("template")			
CONF.ask_question( "t_bool" )						
answer = CONF.get_answer( "t_bool" )
if answer:
	CONF.msg("Ano banany su dobre")
	CONF.show()
else:
	CONF.warn("Ne ne!")

CONF.ask_question( "t_select" )
answer = CONF.get_answer( "t_select" )
CONF.msg(answer)
CONF.warn( "Toto bude drsne" )
CONF.show()
CONF.stop()
print 40*'='

