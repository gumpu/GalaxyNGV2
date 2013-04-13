# vi: spell spl=en

clean :
	rm -rf galaxy.db

galaxy.db : createdb.sql
	rm -rf galaxy.db
	sqlite3 galaxy.db < createdb.sql 

