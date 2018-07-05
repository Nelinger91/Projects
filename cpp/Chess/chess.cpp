//
// Created by Amit Nelinger on 1/1/17.
//
#define SIZE 64
#include "chess.h"

#include <iostream>
#define EAT "eat"
#define MOVE "move"
#define ILLEGAL "illegal"


/**
 * the function gets an index and returns a string representing its board position
 * @param i the index in the GamePiece vector
 * @return a string represention of the position in the board
 */
string getPositionFromIndex(int i) {
    string pos = "";
    int div = i / 8;
    int num = i % 8;
    if (num == 0)
    {
        pos += "A";
    }
    else if (num == 1)
    {
        pos += "B";
    } else if (num == 2)
    {
        pos += "C";
    }
    else if (num == 3)
    {
        pos += "D";
    }
    else if (num == 4)
    {
        pos += "E";
    }
    else if (num == 5)
    {
        pos += "F";
    }
    else if (num == 6)
    {
        pos += "G";
    }
    else if (num == 7)
    {
        pos += "H";
    }
    if (div == 0) {
        pos += "8";
    }
    else if (div == 1)
    {
        pos += "7";
    }
    else if (div == 2)
    {
        pos += "6";
    }
    else if (div == 3)
    {
        pos += "5";
    }
    else if (div == 4)
    {
        pos += "4";
    }
    else if (div == 5)
    {
        pos += "3";
    }
    else if (div == 6)
    {
        pos += "2";
    }
    else if (div == 7)
    {
        pos += "1";
    }

    return pos;
}


/**
 * makes sure thats the move is in good format
 * @param let1 first letter
 * @param let2 second letter
 * @param num1 first num
 * @param num2 second num
 * @return true if all nums are between 0 and 9, and the letters are A-H, false otherwise
 */
bool checkAscii(char let1, char let2, char num1, char num2)
{
    int a = int(let1);
    int b = int(let2);
    int c = int(num1);
    int d = int(num2);
    if (a < 65 || a > 90 || b < 65 || b > 90)
    {
        return false;
    }
    return !(c < 48 || c > 57 || d < 48 || d > 57);
}
/**
 * same as the name
 * @param str the position comprising of a big letter and then a number
 * @return the index of this position in the vecor of game pieces.
 */
int getIndexFromPosition(string& str)
{
    int letter = (int) str[0] - 65;
    int num = 8 - std::stoi(str.substr(1));
    return num * 8 + letter;
}

/**
 * checks if a curr player king is threatend
 * @param color the color of the player we want to check
 * @param game the current game
 * @return true if he's threatend, false otherwise.
 */
bool checkChess(string color,chess* game)
{
    vector<GamePiece*> board = game->getBoard();
    std::vector<GamePiece*>::iterator it;
    GamePiece* curr;
    GamePiece* king;
    string threatPos;
    for (it = board.begin(); it != board.end(); ++it)
    {
        curr = *it;
        if (curr->getColor() == color && curr->getCode() == "265A")
        {
            king = curr;
        }
    }

    //go and see if anyone poses a threat
    for (it = board.begin(); it != board.end(); ++it)
    {
        curr = *it;
        if (curr->isLegalMove(king,board) != ILLEGAL)
        {
            return true;
        }
    }
    return false;
}


/**
 * checks whether or not there is still a check if the king moved to a new position
 * @param color the king color
 * @param game the current game
 * @param kingIdx the king new index he can move to
 * @return true if there is a threat, false otherwise.
 */
bool checkAfterMove(string color, chess* game, int kingIdx)
{
    vector<GamePiece*> board = game->getBoard();
    chess* realGame = game;
    chess* tempGame = new chess();
    vector<GamePiece*> tempBoard;
    tempBoard = tempGame->getBoard();
    delete(tempBoard.at(kingIdx));
    GamePiece* king = new King(color, getPositionFromIndex(kingIdx), "265A");
    tempBoard.at(kingIdx) = king;
    GamePiece* curr;
    std::vector<GamePiece*>::iterator it;

    for (it = tempBoard.begin(); it != tempBoard.end(); ++it)
    {
        curr = *it;
        if (curr->isLegalMove(king,tempBoard) != ILLEGAL)
        {
            //delete(tempGame);
            return true;
        }
    }
    return false;
}

/**
 * returns true if there is a state of checkmate
 * @param color the color we want to check if he's posed in checkmate
 * @param game the current game
 * @param possibleWinner the name of the winner if there is a checkmate
 * @return true if there is a checkmate, false otherwise.
 */
bool checkMate(string color,chess* game, string possibleWinner)
{
    vector<GamePiece*> board = game->getBoard();
    std::vector<GamePiece*>::iterator it;
    GamePiece* curr;
    GamePiece* king;
    string threatPos;
    for (it = board.begin(); it != board.end(); ++it)
    {
        curr = *it;
        if (curr->getColor() == color && curr->getCode() == "265A")
        {
            king = curr;
        }
    }

    string pos = king->getPosition();
    int idx = getIndexFromPosition(pos);
    int newPositions[] = {idx+1,idx-1,idx+9,idx-9,idx+7,idx-7,idx+8,idx-8};
    for (int newCurrIdx: newPositions)
    {
        if (newCurrIdx <= 63 && newCurrIdx >= 0)
        {
            curr = board.at(newCurrIdx);
            if (curr->getColor() == "none")
            {
                if (!checkAfterMove(color, game, newCurrIdx))
                {
                    return false;
                }
            }
        }
    }
    game->printBoard();
    std::cout<< possibleWinner << " won!" << std::endl;
    return true;
}
/**
 * check the legality of the move, if it is legal makes the move.
 * otherwise returns false and does nothing
 * @param move the move the player wants to make
 * @param playerColor color of the player
 * @return true if move was legal, false otherwise.
 */
bool chess::movePiece(const string& move,const string& playerColor)
{
    int colorDir;
    string from, to;
    char fromLetter,toLetter,fromNum,toNum;
    //check if the format is ok.
    if (move.length() != 4)
    {
        return false;
    }
    else
    {
        from =move.substr(0,2);
        to = move.substr(2,3);
        fromLetter = from[0];
        fromNum = from[1];
        toLetter = to[0];
        toNum = to[1];
        if (!checkAscii(fromLetter, toLetter, fromNum, toNum))
        {
            return false;
        }
    }

    int startingPoint = getIndexFromPosition(from);
    int movingIdx = getIndexFromPosition(to);
    GamePiece* currPiece = this->currBoard[startingPoint];
    GamePiece* movingPoint = this->currBoard[movingIdx];

    if (currPiece->getColor() != playerColor)
    {
        return false;
    }

    string res = currPiece->isLegalMove(movingPoint, this->currBoard);
    if (res == MOVE)
    {
        //make the pawn a queen if he got to the end of the line
        if ((currPiece->getCode() == "265F" && currPiece->getColor() == "black" && movingIdx >= 56) ||
                (currPiece->getCode() == "265F" && currPiece->getColor() == "white" && movingIdx <= 7))
        {
            this->currBoard[startingPoint] = new emptyPiece("none", from, " ");
            delete(this->currBoard[movingIdx]);
            this->currBoard[movingIdx] = new Queen(currPiece->getColor(), to, "265B");
        }
        // make the move
        else
        {
            this->currBoard[startingPoint] = new emptyPiece("none", from, " ");
            delete(this->currBoard[movingIdx]);
            this->currBoard[movingIdx] = currPiece;
            this->currBoard[movingIdx]->setPosition(to);
        }
        return true;
    }
    else
    {
        return false;
    }
}



/**
 * get the current board.
 * @return the current board of the game.
 */
vector<GamePiece*> chess::getBoard()
{
    return this->currBoard;
}

/**
 * initalizer, creates gamePieces for the entire board
 * @param board the board we want to initalize
 */
void initializeBoard(vector<GamePiece*>* board)
{
    string position, code, color;
    for (int i = 0; i < SIZE; ++i)
    {
        if (i >= 16 && i <= 47)
        {
            position = getPositionFromIndex(i);
            code = " ";
            color = "none";
            board->at(i) = (new emptyPiece(color,position,code));
        }
        else
        {
            if (i == 0)
            {
                //rook black
                code = "265C";
                color = "black";
                position = "A8";
                board->at(i) = (new Rook(color,position,code));
            }
            if (i == 1)
            {
                //knight black
                code = "265E";
                color = "black";
                position = "B8";
                board->at(i) = (new Knight(color,position,code));
            }
            if (i == 2)
            {
                //bishop black
                code = "265D";
                color = "black";
                position = "C8";
                board->at(i) = (new Bishop(color,position,code));
            }
            if (i == 3)
            {
                //queen black
                code = "265B";
                color = "black";
                position = "D8";
                board->at(i) = (new Queen(color,position,code));
            }
            if (i == 4)
            {
                //king black
                code = "265A";
                color = "black";
                position = "E8";
                board->at(i) = (new King(color,position,code));
            }
            if (i == 5)
            {
                //bishop black
                code = "265D";
                color = "black";
                position = "F8";
                board->at(i) = (new Bishop(color,position,code));
            }
            if (i == 6)
            {
                //knight black
                code = "265E";
                color = "black";
                position = "G8";
                board->at(i) = (new Knight(color,position,code));
            }
            if (i == 7)
            {
                //rook black
                code = "265C";
                color = "black";
                position = "H8";
                board->at(i) = (new Rook(color,position,code));
            }
            if (i >= 8 && i <= 15)
            {
                position = getPositionFromIndex(i);
                code = "265F";
                color ="black";
                board->at(i) = (new Pawn(color,position,code));
            }
            if (i >=48 && i<= 55)
            {
                position = getPositionFromIndex(i);
                code = "265F";
                color = "white";
                board->at(i) = (new Pawn(color,position,code));
            }
            if (i == 56)
            {
                //rook white
                position = getPositionFromIndex(i);
                code = "265C";
                color = "white";
                board->at(i) = (new Rook(color,position,code));
            }
            if (i == 57)
            {
                // knight white
                position = getPositionFromIndex(i);
                code = "265E";
                color = "white";
                board->at(i) = (new Knight(color,position,code));
            }
            if (i == 58)
            {
                //bishop white
                position = getPositionFromIndex(i);
                code = "265D";
                color = "white";
                board->at(i) = (new Bishop(color,position,code));
            }
            if (i == 59)
            {
                //queen white
                position = getPositionFromIndex(i);
                code = "265B";
                color = "white";
                board->at(i) = (new Queen(color,position,code));

            }
            if (i == 60)
            {
                //king white
                position = getPositionFromIndex(i);
                code = "265A";
                color = "white";
                board->at(i) = (new King(color,position,code));
            }
            if (i == 61)
            {
                //bishop white
                position = getPositionFromIndex(i);
                code = "265D";
                color = "white";
                board->at(i) = (new Bishop(color,position,code));
            }
            if (i == 62)
            {
                //knight white
                position = getPositionFromIndex(i);
                code = "265E";
                color = "white";
                board->at(i) = (new Knight(color,position,code));
            }
            if (i == 63)
            {
                //rook white
                position = getPositionFromIndex(i);
                code = "265C";
                color = "white";
                board->at(i) = (new Rook(color,position,code));
            }
        }
    }
}

/**
 * prints the board.
 */
void chess::printBoard()
{
    vector<GamePiece*> board = currBoard;
    int counter = 0;
    std::cout<< "  ";
    std::cout<<"A";
    std::cout<<"B";
    std::cout<<"C";
    std::cout<<"D";
    std::cout<<"E";
    std::cout<<"F";
    std::cout<<"G";
    std::cout<<"H";
    std::cout<<std::endl;
    std::cout<<std::endl;


    for (GamePiece* piece:board)
    {
        if (counter % 8 == 0)
        {
            std::cout<< 8 - counter / 8  << " ";
        }
        piece->printPiece();
        counter++;
        if (counter % 8 == 0)
        {
            std::cout<<" "<< 9 - counter / 8;
            std::cout<<std::endl;
        }
    }

    std::cout<<std::endl;
    std::cout<< "  ";
    std::cout<<"A";
    std::cout<<"B";
    std::cout<<"C";
    std::cout<<"D";
    std::cout<<"E";
    std::cout<<"F";
    std::cout<<"G";
    std::cout<<"H";
    std::cout<<std::endl;
    std::cout<<std::endl;
}
/**
 * a constructor, calls the initalizeBoard function
 */
chess::chess()
{
    turn = "white";
    currBoard.resize(SIZE);
    initializeBoard(&currBoard);
}


/**
 *
 * @return 0 if everything is fine
 */
int main() {
    string player1,player2,move;
    string turn = "white";
    std::cout<<"Enter white player name:\n";
    std::getline(std::cin,player1);
    std::cout<<"Enter black player name:\n";
    std::getline(std::cin,player2);
    chess* game = new chess();
    while(true)
    {
        cout << "\033[2J";
        game->printBoard();
        if(checkChess("white", game))
        {
            if (checkMate("white", game, player2))
            {
                break;
            }
            else
            {
                std::cout<<"\33[37;41mCheck!\33[0m"<<std::endl;
            }
        }
        std::cout<<player1<< ": Please enter your move:"<<std::endl;
        std::getline(std::cin,move);
        while (!game->movePiece(move,turn))
        {
            std::cout<<"\33[37;41millegal move\33[0m"<<std::endl;
            std::getline(std::cin,move);
        }


        turn = "black";
        cout << "\033[2J";
        game->printBoard();
        if(checkChess("black", game))
        {
            if (checkMate("black", game, player1))
            {
                break;
            }
            else
            {
                std::cout<<"\33[37;41mCheck!\33[0m"<<std::endl;
            }
        }
        std::cout<<player2<< ": Please enter your move:"<<std::endl;
        std::getline(std::cin,move);
        while (!game->movePiece(move,turn))
        {
            std::cout<<"\33[37;41millegal move\33[0m"<<std::endl;
            std::getline(std::cin,move);
        }
        turn = "white";
    }
    return 0;

}
