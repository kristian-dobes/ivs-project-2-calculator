#-*- MakeFile-*-

EXECUTE=executables.py
MATHLIB=mathlibrary.py
DOC_DOX=qat.doxygen
TEST=test.py
PROFILING=stddev.py

ZIP_FILE=xsynak03_xbalek02_xdobes22_xkralj12


all: init run	
	
init:
	pip3 install -r requirements.txt
	pip3 freeze

# dont know if just pack or also make if dont exist
pack: #doc  #clean
	mkdir -p ../../xsynak03_xbalek02_xdobes22_xkralj12

	cp -r ../../repo ../../xsynak03_xbalek02_xdobes22_xkralj12
	cp -r ../../install ../../xsynak03_xbalek02_xdobes22_xkralj12
	cp -r ../../doc ../../xsynak03_xbalek02_xdobes22_xkralj12

	zip -r $(ZIP_FILE).zip ../../xsynak03_xbalek02_xdobes22_xkralj12
	rm -rf ../../xsynak03_xbalek02_xdobes22_xkralj12
	mv xsynak03_xbalek02_xdobes22_xkralj12.zip ../../



clean:
# dont know

test:$(TEST)
	python3 $(TEST)

doc : $(DOC_DOX)
	rm -rf ./doc
	doxygen $(MATHLIB)
	mkdir ./doc
	mv html/ ./doc
	mv latex/ ./doc

run : $(EXECUTE)
	python3 $(EXECUTE)
	
profile:$(PROFILING)
	python3 $(PROFILING)


