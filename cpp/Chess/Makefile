PP = g++
OBJECTS = Bishop.o chess.o GamePiece.o King.o Knight.o Pawn.o Queen.o Rook.o emptyPiece.o
#OBJECTS = *.o
TAR = ex2.tar
FILES = Bishop.h Bishop.cpp chess.cpp chess.h emptyPiece.h emptyPiece.cpp GamePiece.cpp GamePiece.h King.h King.cpp Knight.h Knight.cpp Pawn.cpp Pawn.h Queen.cpp Queen.h Rook.cpp Rook.h MakeFile
FLAGS = -c -std=c++11 -Wall -Wextra 


#exe

chess:	$(OBJECTS)
	$(PP) $(OBJECTS) -o chess


all: chess    


# Obj
emptyPiece.o: emptyPiece.cpp
	$(PP) $(FLAGS) emptyPiece.cpp -o emptyPiece.o
    
GamePiece.o: GamePiece.cpp
	$(PP) $(FLAGS) GamePiece.cpp -o GamePiece.o

King.o:	 King.cpp
	$(PP) $(FLAGS) King.cpp -o King.o

Knight.o: Knight.cpp
	$(PP) $(FLAGS) Knight.cpp -o Knight.o

Pawn.o:	 Pawn.cpp
	$(PP) $(FLAGS) Pawn.cpp -o Pawn.o

Queen.o: Queen.cpp
	$(PP) $(FLAGS) Queen.cpp -o Queen.o
    
Rook.o:	 Rook.cpp
	$(PP) $(FLAGS) Rook.cpp -o Rook.o

Bishop.o: Bishop.cpp
	$(PP) $(FLAGS) Bishop.cpp -o Bishop.o

chess.o: chess.cpp
	$(PP) $(FLAGS) chess.cpp -o chess.o

make:
	make all
	./chess
#clean

clean:
	-rm -f *.o chess

tar:
	tar cvf ${TAR} ${FILES}
