# @name: /Users/Matt/Google Drive/Python_workspace/Scripts/DARC/Makefile
# @author: Matt
# @date: Dec 17, 2013
# @version: 0.1
# @description: Recipes for compiling the DARC and Rmatrix source to create
#	relevant executables

# set the fortran compiler to be employed
FF=f95 -O2  -xtarget=native -m64 -xarch=sse4_2 -xmodel=medium -xlic_lib=sunperf

all: $(patsubst %.f, %.x, $(wildcard *.f))

clean:
	rm *.x

%.x: %.f
	$(FF) -o $@ $<