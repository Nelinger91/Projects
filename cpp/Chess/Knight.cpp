//
// Created by Amit Nelinger on 1/14/17.
//

#include "Knight.h"
#define MOVE "move"
#define ILLEGAL "illegal"
Knight::Knight(const string color,const string pos,const string code)
{
    this->setColor(color);
    this->setPosition(pos);
    this->setCode(code);
}

int getAbs(int num)
{
    if (num < 0)
    {
        return -1*num;
    }
    return num;
}


string Knight::isLegalMove(GamePiece* dest, vector<GamePiece*> board)
{
    string from = this->getPosition();
    string to = dest->getPosition();
    char fromLet = from[0];
    char toLet = to[0];
    char fromNum = from[1];
    char toNum = to[1];
    int letterGap = fromLet - toLet;
    int numGap = fromNum - toNum;
    if (getAbs(letterGap) + getAbs(numGap) == 3 && letterGap !=0 && letterGap !=3 && numGap != 0 && numGap != 3)
    {
        if (dest->getColor() != this->getColor())
        {
            return MOVE;
        }
    }
    else
    {
        return ILLEGAL;
    }
}