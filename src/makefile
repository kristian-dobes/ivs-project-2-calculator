#-*- MakeFile-*-

EXECUTE=executables.py
MATHLIB=mathlibrary.py
DOC_DOX=Doxyfile
TEST=test.py
PROFILING=stddev.py

ZIP_FILE=xsynak03_xbalek02_xdobes22_xkralj12


all: init run profile
	
init:
	pip3 install -r requirements.txt
	pip3 freeze

pack: 
	mkdir -p ../../xsynak03_xbalek02_xdobes22_xkralj12/repo

	cp -r ../../repo ../../xsynak03_xbalek02_xdobes22_xkralj12
	cp -r ../../install ../../xsynak03_xbalek02_xdobes22_xkralj12
	cp -r ../../doc ../../xsynak03_xbalek02_xdobes22_xkralj12

	mv ../../xsynak03_xbalek02_xdobes22_xkralj12 ./
	zip -r $(ZIP_FILE).zip ./xsynak03_xbalek02_xdobes22_xkralj12
	rm -rf ./xsynak03_xbalek02_xdobes22_xkralj12


clean:


test:$(TEST)
	python3 -m unittest $(TEST)

doc : $(DOC_DOX)
	doxygen $(DOC_DOX)


run : $(EXECUTE)
	python3 $(EXECUTE)
	
profile:$(PROFILING)
	python3 $(PROFILING)


