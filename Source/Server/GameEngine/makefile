# vi: spell spl=en

all : .test

.test :
	python runalltests.py

.report :
	./galaxy.py create test
	./galaxy.py report test
	cat /tmp/Nation_3.txt

clean :
	make -C elements clean
	make -C reports  clean
	rm -rf *.pyc
	rm -rf *.pdf *.csv *.png
	rm -rf tags

tags :
	ctags -R .

map.png : map.csv map.r
	R --vanilla < map.r

map.csv : galaxy.py
	./galaxy.py create test
	./galaxy.py map    test


