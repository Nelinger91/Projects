//
// Created by Amit Nelinger on 1/14/17.
//

#ifndef CHESS_BISHOP_H
#define CHESS_BISHOP_H


#include "GamePiece.h"

class Bishop: public GamePiece
{
public:

    /**
    * A constructor.
    * @param position sets the position of the Rook
    * @param color sets the color of this rook piece
    * @param code sets the code of the ascii representation
    */
    Bishop(const string, const string, const string);

    /** checks if this piece can move to the location of the dest piece
    * @param dest the gamepiece in the destenation.
    * @param board the current board in play
    * @return returns a string that implies whether
    * a move can be made (EAT, MOVE, ILLEGAL)
    */
    string isLegalMove(GamePiece*,vector<GamePiece*>);
};


#endif //CHESS_BISHOP_H
