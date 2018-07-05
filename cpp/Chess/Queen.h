//
// Created by Amit Nelinger on 1/14/17.
//

#ifndef CHESS_QUEEN_H
#define CHESS_QUEEN_H


#include "GamePiece.h"

class Queen : public GamePiece {
public:
    /**
    * A constructor.
    * @param position sets the position of the piece
    * @param color sets the color of this  piece
    * @param code sets the code of the ascii representation
    */
    Queen(const string, const string, const string);
    /**
    * checks if this piece can move to the location of the dest piece
    * @param dest the gamepiece in the destenation.
    * @param board the current board in play
    * @return returns a string that implies whether
    * a move can be made (EAT, MOVE, ILLEGAL)
    */
    string isLegalMove(GamePiece*,vector<GamePiece*>);
};


#endif //CHESS_QUEEN_H
