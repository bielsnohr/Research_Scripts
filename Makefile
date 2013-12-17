# @name: /Users/Matt/Google Drive/Python_workspace/Scripts/Makefile
# @author: Matt
# @date: Dec 16, 2013
# @version: 0.1
# @description: A makefile for plotting the basis and bound orbitals produced
#	from stg1d_orbs.x
BAS = $(shell ls | grep bas[0-9] -c)
ORB = $(shell ls | grep orb -c)
orb_depend = $(wildcard bas*) $(wildcard orb*)

all: plot_show 

plot_show: orbitals
	python plot_bas.py 1 $(ORB) 1 $(BAS)

plot_save: orbitals 
	python plot_bas.py 1 $(ORB) 1 $(BAS) -s
	
orbitals: $(orb_depend) 
	#$(orb_depend)
	sh ORBS.SH	
	touch $@

clean:
	rm -f bas* orb* *.png orbitals