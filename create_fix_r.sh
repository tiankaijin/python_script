fixed=r
arr=a
sh init.sh $1 ${fixed} $2
sh r_getdata.sh $1 $2
python write_finish.py $arr $2 $1 >> fix-$fixed-$1-$2.py
python fix-$fixed-$1-$2.py &
