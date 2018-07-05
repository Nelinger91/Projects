
RUN = GenericMatrixDriver Matrix.hpp.gch

CC = g++
CFLAGS = -c -Wall -Wextra -Wvla -std=c++11

TAR = COPYFILE_DISABLE=1 tar cvf


# names of all the files to be used
FILES = ex3.tar Makefile Matrix.hpp
OFILES =  Complex.o

# make executable
make: GenericMatrixDriver Matrix
	./GenericMatrixDriver

GenericMatrixDriver: $(OFILES) GenericMatrixDriver.o
	$(CC) $(OFILES) GenericMatrixDriver.o -o GenericMatrixDriver

GenericMatrixDriver.o: $(OFILES) GenericMatrixDriver.cpp
	$(CC) $(CFLAGS) GenericMatrixDriver.cpp -o GenericMatrixDriver.o

# make object files
Matrix: Matrix.hpp Complex.h
	$(CC) $(CFLAGS) Matrix.hpp -o Matrix.hpp.gch


Complex.o: Complex.cpp
	$(CC) $(CFLAGS) Complex.cpp -o Complex.o


# clean o and executable files
clean:
	rm -f *.o $(RUN)

# make tar
tar:
	$(TAR) $(FILES)
