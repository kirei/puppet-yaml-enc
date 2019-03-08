SCRIPT=	yamlenc/yamlenc.py

all:

regress::
	-python $(SCRIPT) --conf regress/bad-re.yaml --debug regress
	-python $(SCRIPT) --conf regress/missing-attr.yaml --debug regress
	python $(SCRIPT) --conf regress/good.yaml --debug regress
