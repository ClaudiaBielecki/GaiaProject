#!bin/bash
File="download_links.txt"
listLinks=$(cat $File)
sim=(F I M)
view=(lsr0 lsr1 lsr2)
j=0
for i in $listLinks; do
	echo "downloading file number $j"
	wget $i
	mv download download.hdf5
	echo "reducing file"
	python reduceh5file.py
	v1=$((j%30)) 
        v2=$((v1/10))
	FileName="m12${sim[$((j/30))]}${view[$v2]}slice$((j%10))"
	mv data01.hdf5 $FileName
	echo "saved as $FileName"
	ls
	rm download.hdf5
	j=$((j+1))
done







