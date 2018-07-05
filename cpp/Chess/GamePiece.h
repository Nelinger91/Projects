//
// Created by Amit Nelinger on 1/1/17.
//

#ifndef CHESS_GAMEPIECE_H
#define CHESS_GAMEPIECE_H

#include <string>
#include <vector>

using namespace std;



class GamePiece
{
public:
    /**
     * A general constructor
     */
    GamePiece();
    /**
     * Another  constructor that gets initial color, code and position
     * @param color the color of the piece
     * @param pos the position of the piece
     * @param type  the type of the piece
     */
    GamePiece(string,string,string);

    /**
     * the function returns the type
     * @return the type of the piece
     */
    string getType();
    /**
     * the function returns the color
     * @return the color of the piece
     */
    string getColor();
    /**
     * the function returns the pos
     * @return the pos of the piece
     */
    string getPosition();
    /**
     * the function returns the ascii code
     * @return the ascii code representing the piece
     */
    string getCode();
    /**
     * the function sets the color
     * @param color the color we want to set the piece to
     */
    void setColor(const string);
    /**
     * the function sets the type
     * @param type the type we want to set the piece to
     */
    void setType(const string);
    /**
     * the function sets the position
     * @param position the position we want to set the piece to
     */
    void setPosition(const string);
    /**
     * the function sets the code
     * @param code the code we want to set the piece to
     */
    void setCode(const string);
    /**
     * the function get the color of the board in the piece pos
     * @return color the color we of the board in which the piece stands
     */
    string getPositionColor();
    /**
     * prints the piece
     */
    void printPiece();
    /**
    *  a  pure virtual function that is implements by each specific piece
    * that checks if this piece can move to the location of the dest piece
    * @param dest the gamepiece in the destenation.
    * @param board the current board in play
    * @return returns a string that implies whether
    * a move can be made (EAT, MOVE, ILLEGAL)
    */
    virtual string isLegalMove(GamePiece*, vector<GamePiece*>) = 0;

private:
    string color; /** the color of the piece*/
    string type; /** the type of the piece*/
    string code; /** the ascii code representing the piece*/
    string position; /** the position of the piece*/


};


#endif //CHESS_GAMEPIECE_H
