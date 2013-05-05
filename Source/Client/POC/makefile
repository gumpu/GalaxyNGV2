

.lint : gng.html dummy.json
	xmllint gng.html

.jsonlint :
	jsonlint -v dummy.json


dummy.json : create_dummy_json_report.py
	python create_dummy_json_report.py > dummy.json

clean :
	rm -rf dummy.json

coordtrans.pdf : coordtrans.svg
	inkscape --export-pdf=$@ $<

