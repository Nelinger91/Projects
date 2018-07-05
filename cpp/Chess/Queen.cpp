//
// Created by Amit Nelinger on 1/14/17.
//

#include "Queen.h"
#define MOVE "move"
#define ILLEGAL "illegal"
#define EAT "eat"
#define UP -8
#define DOWN 8
#define RIGHT 1
#define LEFT -1
#define RIGHTUPDIAG -7
#define LEFTUPDIAG  -9
#define RIGHTDOWNDIAG 9
#define LEFTDOWNDIAG 7


Queen::Queen(const string color,const string pos,const string code)
{
    this->setColor(color);
    this->setPosition(pos);
    this->setCode(code);
}

int getAbsVal(int num)
{
    if (num < 0)
    {
        return num * -1;
    }
    return num;
}

int getIdxFromPositionQueen(string& str)
{
    int letter = (int) str[0] - 65;
    int num = 8 - std::stoi(str.substr(1));
    return num*8 + letter;
}


bool isClearPathQueen(string from, string to, vector<GamePiece *> board, int jumps)
{
    int fromIdx = getIdxFromPositionQueen(from);
    int toIdx = getIdxFromPositionQueen(to);

    int pathLength = ((fromIdx - toIdx) / jumps) * -1;
    for (int i = 1; i <= pathLength; ++i)
    {
        if (i == pathLength)
        {
            if (board.at(fromIdx+(jumps*i))->getColor() == board.at(fromIdx)->getColor())
            {
                return false;
            }
        }
        else
        {
            if (board.at(fromIdx+(jumps*i))->getColor() != "none")
            {
                return false;
            }
        }
    }
    return true;
}



string Queen::isLegalMove(GamePiece* dest, vector<GamePiece*> board)
{
    string from = this->getPosition();
    string to = dest->getPosition();
    char fromLet = from[0];
    char toLet = to[0];
    char fromNum = from[1];
    char toNum = to[1];
    int letterGap = fromLet - toLet;
    int numGap = fromNum - toNum;

    if (letterGap == 0)
    {
        if (numGap < 0)
        {
            if (isClearPathQueen(from, to, board, UP))
            {
                return MOVE;
            }
        }
        else if (numGap > 0)
        {
            if (isClearPathQueen(from, to, board, DOWN))
            {
                return MOVE;
            }
        }
        else
        {
            return ILLEGAL;
        }
    }
    else if (numGap == 0)
    {
        if (letterGap > 0)
        {
            if (isClearPathQueen(from, to, board, LEFT))
            {
                return MOVE;
            }
        }
        else
        {
            if (isClearPathQueen(from, to, board, RIGHT))
            {
                return MOVE;
            }
        }
    }
    else
    {
        if (getAbsVal(numGap) == getAbsVal(letterGap))
        {
            if (numGap > 0 && letterGap > 0)
            {
                if (isClearPathQueen(from, to, board, LEFTDOWNDIAG))
                {
                    return MOVE;
                }
            }
            else if (numGap > 0 && letterGap < 0)
            {
                if (isClearPathQueen(from, to, board, RIGHTDOWNDIAG))
                {
                    return MOVE;
                }
            }
            else if (numGap < 0 && letterGap > 0)
            {
                if (isClearPathQueen(from, to, board, LEFTUPDIAG))
                {
                    return MOVE;
                }
            }
            else if (numGap < 0 && letterGap < 0)
            {
                if (isClearPathQueen(from, to, board, RIGHTUPDIAG))
                {
                    return MOVE;
                }
            }
        }
    }
    return ILLEGAL;
}