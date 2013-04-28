

.lint : gng.html
	xmllint gng.html


dummy.json : create_dummy_json_report.py
	python create_dummy_json_report.py > dummy.json

clean :
	rm -rf dummy.json
