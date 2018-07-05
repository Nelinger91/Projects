cmake_minimum_required(VERSION 3.6)
project(Chess)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES GamePiece.cpp GamePiece.h chess.cpp chess.h Pawn.cpp Pawn.h Queen.cpp
        Queen.h King.cpp King.h Rook.cpp Rook.h Bishop.cpp Bishop.h Knight.cpp Knight.h emptyPiece.cpp emptyPiece.h)
add_executable(Chess ${SOURCE_FILES})