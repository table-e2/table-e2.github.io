while :
do
	python3 test2.py > newData.txt
	sort --key 2 --numeric-sort --reverse newData.txt > currentData.txt
	sleep 600
done
