# vi: spell spl=en

clean :
	make -C elements
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

