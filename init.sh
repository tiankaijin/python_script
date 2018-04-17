lei=10p
res_name=fix
res_split=-
res_hou=.py
lei=10p
if [ $lei == $3 ]
then
	touch ${res_name}${res_split}$2${res_split}$1-10p${res_hou}
	echo "import matplotlib.pyplot as plt" > ${res_name}${res_split}$2${res_split}$1-10p${res_hou}
else
	touch ${res_name}${res_split}$2${res_split}$1-mp${res_hou}
	echo "import matplotlib.pyplot as plt" > ${res_name}${res_split}$2${res_split}$1-mp${res_hou}
fi

