//
// Created by Amit Nelinger on 1/1/17.
//

#ifndef CHESS_BOARD_H
#define CHESS_BOARD_H

#include <vector>
#include "GamePiece.h"
#include "Pawn.h"
#include "King.h"
#include "Bishop.h"
#include "Queen.h"
#include "emptyPiece.h"
#include "Knight.h"
#include "Rook.h"


#include <string>

class chess {
public:
    /**
     * A constructor. Builds a new game
     */
    chess();
    /**
     * default destructor
     */
    ~chess();
    /**
     * this function is getting a move in the format of "A1A2" where
     * A can be any letter, and the numbers are between 1-8. and moves
     * the piece if the move is legal and possible
     * @param move string in the format of "A1A2"
     * @param playerColor a string representing the player color black/white.
     * @return true if the move is legal, and false otherwise.
     */
    bool movePiece(const string& move,const string& playerColor);
    /**
     * this function is printing the entire board
     */
    void printBoard();
    /**
     * returns the current board
     * @return the current board
     */
    vector<GamePiece*> getBoard();



private:
    vector<GamePiece*> currBoard; /** the curr board of the game*/
    string turn; /** black/white turn*/

};


#endif //CHESS_BOARD_H
