#!/usr/bin/env python
# encoding=utf-8

from conf_module import conf_start

print 40*'='
CONF=conf_start("bla")		#vyvori configuracny modul a vrati ho ?iba ak je nutna konfiguracia?
CONF.make_front_end()		#vytvory front end
CONF.ask_question( "1" )	#spyta sa otazku
CONF.msg("Ahoj")		#prida hlasku do fronty
CONF.msg("Zdravim")
CONF.warn("Cele zle!")		#varuje uzivatela
CONF.show()			#zobrazi vsetky nahromadene spravy
answer = CONF.get_answer( "1" )	#vrati odpoved
CONF.stop()
print 40*'='
print answer

