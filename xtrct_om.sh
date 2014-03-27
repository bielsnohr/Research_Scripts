#!/bin/bash

# a list of the final levels for the transitions
# at the moment, this assumes the only transitions of interest are from ground
LIST='2 3 5 9 10'
now=$(date "+%Y_%m_%d")

for i in $LIST; do
	echo "1 -"$i > temp
	'xtrct.x' < temp 
	mv "xout" "om-1_"$i"-description-"$now".trns"
	echo "Done 1-->"$i
	echo "------------------------"
done

# alternatively, if you need specific transition, just write them out in a sequence
# like below

#echo '1 -2' > temp
#'xtrct.x' < temp 
#mv xout trans_1-2_om-luis.dat
#echo 'Done 1-->2'
#echo '------------------------'
