r=(0.0 0.2 0.4 0.6 0.8 1.0)
sta_num=(4 8 12 16 20)
file_name=arr
res_split=-
for n in ${sta_num[@]}
do
	rm data.txt
	rm data$n
	rm tmp
	for((i=0;i<${#r[@]};i++))
	do
		python s_fix_getdata.py aver${r[i]}-$n-$1 $2 >>data.txt
		
	done
	python arrange_data.py data.txt > data$n
	echo -n "sta$n=" >> tmp
	echo -n `cat data$n` >>tmp
	cat tmp >> fix-a-$1-$2.py
	echo "" >> fix-a-$1-$2.py
done

