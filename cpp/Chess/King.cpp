//
// Created by Amit Nelinger on 1/14/17.
//

#include "King.h"
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

King::King(const string color,const string pos,const string code)
{
    this->setColor(color);
    this->setPosition(pos);
    this->setCode(code);
    moveMade = false;
}

int getAbsValKing(int num)
{
    if (num < 0)
    {
        return num * -1;
    }
    return num;
}

int getIdxFromPositionKing(string& str)
{
    int letter = (int) str[0] - 65;
    int num = 8 - std::stoi(str.substr(1));
    return num*8 + letter;
}


bool isClearPathKing(string from, string to, vector<GamePiece *> board, int jumps)
{
    int fromIdx = getIdxFromPositionKing(from);
    int toIdx = getIdxFromPositionKing(to);

    if (board.at(toIdx)->getColor() != board.at(fromIdx)->getColor())
    {
        return true;
    }
    return false;
}

string King::isLegalMove(GamePiece* dest, vector<GamePiece*> board)
{
    string from = this->getPosition();
    string to = dest->getPosition();
    char fromLet = from[0];
    char toLet = to[0];
    char fromNum = from[1];
    char toNum = to[1];
    int letterGap = fromLet - toLet;
    int numGap = fromNum - toNum;


    if ((getAbsValKing(letterGap) + getAbsValKing(numGap) == 2 &&
            (getAbsValKing(letterGap) == 0 || getAbsValKing(numGap) == 0)) ||
            (getAbsValKing(letterGap) + getAbsValKing(numGap) > 3 ))
    {
        return ILLEGAL;
    }

    if (letterGap == 0)
    {
        if (numGap < 0)
        {
            if (isClearPathKing(from, to, board, UP))
            {
                this->moveMade = true;
                return MOVE;
            }
        }
        else if (numGap > 0)
        {
            if (isClearPathKing(from, to, board, DOWN))
            {
                this->moveMade = true;
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
            if (isClearPathKing(from, to, board, LEFT))
            {
                this->moveMade = true;
                return MOVE;
            }
        }
        else
        {
            if (isClearPathKing(from, to, board, RIGHT))
            {
                this->moveMade = true;
                return MOVE;
            }
        }
    }
    else
    {
        if (getAbsValKing(numGap) == getAbsValKing(letterGap))
        {
            if (numGap > 0 && letterGap > 0)
            {
                if (isClearPathKing(from, to, board, LEFTDOWNDIAG))
                {
                    this->moveMade = true;
                    return MOVE;
                }
            }
            else if (numGap > 0 && letterGap < 0)
            {
                if (isClearPathKing(from, to, board, RIGHTDOWNDIAG))
                {
                    this->moveMade = true;
                    return MOVE;
                }
            }
            else if (numGap < 0 && letterGap > 0)
            {
                if (isClearPathKing(from, to, board, LEFTUPDIAG))
                {
                    this->moveMade = true;
                    return MOVE;
                }
            }
            else if (numGap < 0 && letterGap < 0)
            {
                if (isClearPathKing(from, to, board, RIGHTUPDIAG))
                {
                    this->moveMade = true;
                    return MOVE;
                }
            }
        }
    }
    return ILLEGAL;}