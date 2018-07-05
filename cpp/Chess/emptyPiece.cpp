//
// Created by Amit Nelinger on 1/14/17.
//

#include "emptyPiece.h"
#define ILLEGAL "illegal"

emptyPiece::emptyPiece(const string color,const string pos,const string code)
{
    this->setColor(color);
    this->setPosition(pos);
    this->setCode(code);
}


string emptyPiece::isLegalMove(GamePiece* dest, vector<GamePiece*> board)
{
    return  ILLEGAL;
}