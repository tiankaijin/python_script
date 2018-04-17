s=(0.2 0.4 1.0 1.2 2.0)
sta_num=(4 8 12 16 20)
file_name=arr
res_split=-
for n in ${sta_num[@]}
do
	rm data.txt
	rm data$n
	rm tmp
	for((i=0;i<${#s[@]};i++))
	do
		python r_fix_getdata.py aver$1-$n-${s[i]} $2 >> data.txt
		
	done
	python arrange_data.py data.txt > data$n
	echo -n "sta$n=" >> tmp
	echo -n `cat data$n` >>tmp
	cat tmp >> fix-r-$1-$2.py
	echo "" >> fix-r-$1-$2.py
done
