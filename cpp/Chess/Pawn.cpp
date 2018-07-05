//
// Created by Amit Nelinger on 1/14/17.
//

#include "Pawn.h"
#define MOVE "move"
#define ILLEGAL "illegal"
#define EAT "eat"

Pawn::Pawn(const string color,const string pos,const string code)
{
    this->setColor(color);
    this->setPosition(pos);
    this->setCode(code);
    this->moveMade = false;
}

int getIdxFromPosition(string& str)
{
    int letter = (int) str[0] - 65;
    int num = 8 - std::stoi(str.substr(1));
    return num*8 + letter;
}

bool isClearPath(string from, string to,vector<GamePiece*> board,string color)
{
    int dir;
    if (color == "black")
    {
        dir = 1;
    }
    else{
        dir = -1;
    }
    int fromIdx = getIdxFromPosition(from);
    int toIdx = getIdxFromPosition(to);
    int temp = 0;
    if (dir == 1)
    {
        temp = min(fromIdx, toIdx);
    }
    else
    {
        temp = max(fromIdx, toIdx);
    }
    if (board.at(temp+(8*dir))->getCode() == " " && board.at(temp+(16*dir))->getCode() == " ")
    {
        return true;
    }
    else
    {
        return false;
    }
}

string Pawn::isLegalMove(GamePiece* dest, vector<GamePiece*> board)
{
    int colorDir;
    string from = this->getPosition();
    string to = dest->getPosition();
    char fromLet = from[0];
    char toLet = to[0];
    char fromNum = from[1];
    char toNum = to[1];
    int letterGap = fromLet - toLet;
    int numGap = fromNum - toNum;
    if (this->getColor() == "black")
    {
        colorDir = 1;
    }
    else
    {
        colorDir = -1;
    }

    if (numGap == 1 * colorDir)
    {
        if (letterGap == 0)
        {
            if (dest->getCode() == " ")
            {
                this->moveMade = true;
                return MOVE;
            }
            else
            {
                return ILLEGAL;
            }
        }
        else if ((letterGap == 1 || letterGap == -1) && dest->getColor()
                                                          != this->getColor() && dest->getColor() != "none")
        {
            this->moveMade = true;
            return MOVE;
        } else {
            return ILLEGAL;
        }
    }
    else if (numGap == 2 * colorDir && letterGap == 0 && !this->moveMade)
    {
        if (isClearPath(from, to, board,this->getColor()))
        {
            this->moveMade = true;
            return MOVE;
        }
        else
        {
            return ILLEGAL;
        }
    }
    else
    {
        return ILLEGAL;
    }
}
