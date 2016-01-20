SCRIPT=	yamlenc.py

lint:
	pep8 --max-line-length=80 $(SCRIPT)
	pylint --reports=no $(SCRIPT)

regress::
	-python $(SCRIPT) --conf regress/bad-re.yaml --debug regress
	-python $(SCRIPT) --conf regress/missing-attr.yaml --debug regress
	python $(SCRIPT) --conf regress/good.yaml --debug regress
