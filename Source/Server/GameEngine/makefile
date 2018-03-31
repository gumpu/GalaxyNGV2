# vi: spell spl=en

all : .test

.test :
	python runalltests.py

.report :
	./bin/galaxy.py create test
	./bin/galaxy.py report test
	cat /tmp/Nation_3.txt

clean :
	make -C ngengine clean
	rm -rf *.pyc
	rm -rf *.pdf *.csv *.png
	rm -rf tags
	rm -rf map.png
	rm -rf map.csv

tags :
	ctags -R .

map.png : map.csv map.r
	R --vanilla < map.r

map.csv : ./bin/galaxy.py
	./bin/galaxy.py create test
	./bin/galaxy.py map    test


