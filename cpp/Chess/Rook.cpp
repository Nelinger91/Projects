//
// Created by Amit Nelinger on 1/14/17.
//

#include "Rook.h"
#define MOVE "move"
#define ILLEGAL "illegal"
#define EAT "eat"
#define UP -8
#define DOWN 8
#define RIGHT 1
#define LEFT -1


Rook::Rook(const string color,const string pos,const string code)
{
    this->setColor(color);
    this->setPosition(pos);
    this->setCode(code);
    this->moveMade == false;
}

int getIdxFromPositionRook(string& str)
{
    int letter = (int) str[0] - 65;
    int num = 8 - std::stoi(str.substr(1));
    return num*8 + letter;
}


bool isClearPathRook(string from, string to, vector<GamePiece *> board, int jumps)
{
    int fromIdx = getIdxFromPositionRook(from);
    int toIdx = getIdxFromPositionRook(to);

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


/*
 *
 */
string Rook::isLegalMove(GamePiece* dest, vector<GamePiece*> board)
{
    string from = this->getPosition();
    string to = dest->getPosition();
    char fromLet = from[0];
    char toLet = to[0];
    char fromNum = from[1];
    char toNum = to[1];
    int letterGap = fromLet - toLet;
    int numGap = fromNum - toNum;

    if (!(letterGap == 0 || numGap == 0))
    {
        return ILLEGAL;
    }
    else
    {
        if (letterGap == 0)
        {
            if (numGap < 0)
            {
                if (isClearPathRook(from, to, board, UP))
                {
                    this->moveMade = true;
                    return MOVE;
                }
            }
            else if (numGap > 0)
            {
                if (isClearPathRook(from, to, board, DOWN))
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
        else
        {
            if (letterGap > 0)
            {
                if (isClearPathRook(from, to, board, LEFT))
                {
                    this->moveMade = true;
                    return MOVE;
                }
            }
            else
            {
                if (isClearPathRook(from, to, board, RIGHT))
                {
                    this->moveMade = true;
                    return MOVE;
                }
            }
        }
        return ILLEGAL;
    }


}