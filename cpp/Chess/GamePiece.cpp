//
// Created by Amit Nelinger on 1/1/17.
//

#include "GamePiece.h"
#include <iostream>

#define  KING "265A"
#define  QUEEN "265B"
#define  ROOK "265C"
#define  BISHOP "265D"
#define  KNIGHT "265E"
#define  PAWN "265F"

void GamePiece::setColor(const string newColor)
{
    this->color = newColor;
}

void GamePiece::setCode(const string newCode)
{
    this->code = newCode;
}

void GamePiece::setType(const string newType)
{
    this->type = newType;
}

void GamePiece::setPosition(const string newPos)
{
    this->position = newPos;
}

GamePiece::GamePiece(string type,string color, string position)
{
    this->type = type;
    this->color = color;
    this->position = position;
}

string GamePiece::getType() { return this->type;}
string GamePiece::getColor() { return this->color;}
string GamePiece::getPosition() {return this->position;}
string GamePiece::getCode() {return this->code;}

string GamePiece::getPositionColor()
{
    int letter = (int) this->position[0] -64;
    int num = std::stoi(this->position.substr(1));
    if ((letter + num) % 2 == 0)
    {
        return "green";
    }
    else
    {
        return "blue";
    }
}


void GamePiece::printPiece()
{
    if (this->getColor() == "black")
    {
        if (this->getPositionColor() == "blue")
        {
            if (this->getCode() == ROOK)
            {
                std::cout<<"\33[30;46m\u265c\33[0m";
            }
            else if (this->getCode() == BISHOP)
            {
                std::cout<<"\33[30;46m\u265d\33[0m";
            }
            else if (this->getCode() == KNIGHT)
            {
                std::cout<<"\33[30;46m\u265e\33[0m";
            }
            else if (this->getCode() == QUEEN)
            {
                std::cout<<"\33[30;46m\u265b\33[0m";
            }
            else if (this->getCode() == KING)
            {
                std::cout<<"\33[30;46m\u265a\33[0m";
            }
            else if (this->getCode() == PAWN)
            {
                std::cout<<"\33[30;46m\u265f\33[0m";
            }
        }
        else
        {
            if (this->getCode() == ROOK)
            {
                std::cout<<"\33[30;42m\u265c\33[0m";
            }
            else if (this->getCode() == BISHOP)
            {
                std::cout<<"\33[30;42m\u265d\33[0m";
            }
            else if (this->getCode() == KNIGHT)
            {
                std::cout<<"\33[30;42m\u265e\33[0m";
            }
            else if (this->getCode() == QUEEN)
            {
                std::cout<<"\33[30;42m\u265b\33[0m";
            }
            else if (this->getCode() == KING)
            {
                std::cout<<"\33[30;42m\u265a\33[0m";
            }
            else if (this->getCode() == PAWN)
            {
                std::cout<<"\33[30;42m\u265f\33[0m";
            }
        }
    }
    else if (this->getColor() == "white")
    {
        if (this->getPositionColor() == "blue")
        {
            if (this->getCode() == ROOK)
            {
                std::cout<<"\33[37;46m\u265c\33[0m";
            }
            else if (this->getCode() == BISHOP)
            {
                std::cout<<"\33[37;46m\u265d\33[0m";
            }
            else if (this->getCode() == KNIGHT)
            {
                std::cout<<"\33[37;46m\u265e\33[0m";
            }
            else if (this->getCode() == QUEEN)
            {
                std::cout<<"\33[37;46m\u265b\33[0m";
            }
            else if (this->getCode() == KING)
            {
                std::cout<<"\33[37;46m\u265a\33[0m";
            }
            else if (this->getCode() == PAWN)
            {
                std::cout<<"\33[37;46m\u265f\33[0m";
            }
        }
        else
        {
            if (this->getCode() == ROOK)
            {
                std::cout<<"\33[37;42m\u265c\33[0m";
            }
            else if (this->getCode() == BISHOP)
            {
                std::cout<<"\33[37;42m\u265d\33[0m";
            }
            else if (this->getCode() == KNIGHT)
            {
                std::cout<<"\33[37;42m\u265e\33[0m";
            }
            else if (this->getCode() == QUEEN)
            {
                std::cout<<"\33[37;42m\u265b\33[0m";
            }
            else if (this->getCode() == KING)
            {
                std::cout<<"\33[37;42m\u265a\33[0m";
            }
            else if (this->getCode() == PAWN)
            {
                std::cout<<"\33[37;42m\u265f\33[0m";
            }
        }
    }
    else
    {
        if (this->getPositionColor() == "blue")
        {
            std::cout<<"\33[0;46m \33[0m";
        }
        else
        {
            std::cout<<"\33[0;42m \33[0m";
        }
    }
}


GamePiece::GamePiece()
{

}
