//
// Created by Amit Nelinger on 1/14/17.
//

#ifndef CHESS_ROOK_H
#define CHESS_ROOK_H


#include "GamePiece.h"


/*
 * the Rook class inherting from the GamePiece Class.
 */
class Rook : public GamePiece{
public:
    /**
    * A constructor.
    * @param position sets the position of the Rook
    * @param color sets the color of this rook piece
    * @param code sets the code of the ascii representation
    */
    Rook(const string, const string, const string);
    /**
    * checks if this piece can move to the location of the dest piece
    * @param dest the gamepiece in the destenation.
    * @param board the current board in play
    * @return returns a string that implies whether
    * a move can be made (EAT, MOVE, ILLEGAL)
    */
    string isLegalMove(GamePiece*,vector<GamePiece*>);
private:
    bool moveMade;
};


#endif //CHESS_ROOK_H
