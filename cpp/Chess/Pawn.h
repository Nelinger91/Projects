//
// Created by Amit Nelinger on 1/14/17.
//

#ifndef CHESS_PAWN_H
#define CHESS_PAWN_H


#include "GamePiece.h"

class Pawn: public GamePiece {
public:
    /**
    * A constructor.
    * @param position sets the position of the piece
    * @param color sets the color of this  piece
    * @param code sets the code of the ascii representation
    */
    Pawn(const string,const string, const string);

    /**
    * checks if this piece can move to the location of the dest piece
    * @param dest the gamepiece in the destenation.
    * @param board the current board in play
    * @return returns a string that implies whether
    * a move can be made (EAT, MOVE, ILLEGAL)
    */
    string isLegalMove(GamePiece*,vector<GamePiece*>);
    bool moveMade; /** true if a move has already been made */
};


#endif //CHESS_PAWN_H
