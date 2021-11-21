

test: \
	mypy \
	unittest 


mypy:
	mypy ygo_core tests
	

unittest:
	python -m unittest tests


