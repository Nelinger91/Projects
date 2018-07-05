//
// Created by Amit Nelinger on 1/21/17.
//


#ifndef MATRIX_MATRIX_H
#define MATRIX_MATRIX_H
#include <vector>
#include <exception>
#include "Complex.h"

/*
 * The Matrix class
 * A generic matrix, can hold int/double/complex numbers.
 */
template <class T>
/**
 *
 * @tparam T ...
 */
class Matrix
{

private:
    std::vector<T> elems;
    int rowSize, colSize;
    int _getVectorIndex(unsigned int r, unsigned int c) const;

public:
    Matrix();
    Matrix(Matrix<T> && other);
    Matrix(const unsigned int rows, const unsigned int cols);
    Matrix(const Matrix<T>& matrix);
    Matrix(const unsigned int rows, const unsigned int cols, const std::vector<T>& cells);
    ~Matrix();
    Matrix<T>& operator=(const Matrix<T> &other);
    Matrix<T> operator+(const Matrix<T> &other) const;
    Matrix<T> operator-(const Matrix<T> &other) const;
    Matrix<T> operator*(const Matrix<T> &other) const;
    Matrix<T> trans() const;
    bool operator==(const Matrix<T> &other) const;
    bool operator!=(const Matrix<T> &other) const;
    T operator()(unsigned int row, unsigned int col) const;
    T& operator()(unsigned int row, unsigned int col);
    bool isSquareMatrix() const;
    template <class B>
    friend std::ostream& operator<<(std::ostream& o, const Matrix<T>& m);

    /**
     * gets the row size of the matrix
     * @return row size
     */
    int rows() const
    {
        return this->rowSize;
    }
    /**
     * gets the col size of matrix
     * @return col size
     */
    int cols() const
    {
        return this->colSize;
    }

    typedef typename std::vector<T>::const_iterator const_iterator;

    /**
     * this function returns a const iterator to the
     * begining of the matrix
     * @return same as every begin() in iterator
     */
    const_iterator begin()
    {
        return elems.begin();
    }

    /**
     * this function returns a const iterator to the
     * end of the matrix
     * @return same as every end() in iterator
     */
    const_iterator end()
    {
        return elems.end();
    }

    /**
     * class representing the out of bound index error
     */
    class indexError: public std::exception
    {
        virtual const char* what() const throw()
        {
            return "You're trying to reach an index out of bound.";
        }
    };

    /**
     * class representing the wrong dimensions index error
     */
    class dimError: public std::exception
    {
        virtual const char* what() const throw()
        {
            return "Dimensions don't fit.";
        }
    };
};

    /**
     * gets the index of the specific row and col
     * @tparam T .
     * @param r row index
     * @param c col index
     * @return the index in the vector.
     */
    template <class T>
    int Matrix<T>::_getVectorIndex(unsigned int r, unsigned int c) const
    {
        return (this->colSize * r) + c;
    }

    /**
     * defult constructor
     * @tparam T .
     */
    template  <class T>
    Matrix<T>::Matrix()
    {
        this->elems.push_back(T(0));
        this->rowSize = 1;
        this->colSize = 1;
    }

    /**
     * move constructor
     * @tparam T .
     * @param other the other matrix to be moved
     */
    template <class T>
    Matrix<T>::Matrix(Matrix<T> && other)
    {
        this->elems = std::move(other.elems);
        this->colSize = std::move(other.colSize);
        this->rowSize = std::move(other.rowSize);
    }

    /**
     * constructor. creates a matrix of size (row,cols) with default value
     * @tparam T .
     * @param rows num of rows
     * @param cols num of cols
     */
    template  <class T>
    Matrix<T>::Matrix(const unsigned int rows, const unsigned int cols)
    {
        rowSize = rows;
        colSize = cols;
        elems =  std::vector<T>(rows * cols, T(0));
    }

    /**
     * copy constructor
     * @tparam T .
     * @param matrix the matrix to be copied
     */
    template  <class T>
    Matrix<T>::Matrix(const Matrix<T>& matrix)
    {
        rowSize = matrix.rowSize;
        colSize = matrix.colSize;
        elems =  matrix.elems;
    }

    /**
     * semi-copy constructor with vector..
     * @tparam T .
     * @param rows num of rows of new matrix
     * @param cols num of cols in new matrix
     * @param cells the vector to be copied into new matrix
     */
    template  <class T>
    Matrix<T>::Matrix(const unsigned int rows, const unsigned int cols, const std::vector<T>& cells)
    {
        this->rowSize = rows;
        this->colSize = cols;
        this->elems =  cells;
    }

    /**
     * default deconstructor
     * @tparam T .
     */
    template <class T>
    Matrix<T>::~Matrix()
    {

    }

    /**
     *
     * @tparam T
     * @param other the right matrix
     * @return assigns the right matrix to the left
     */
    template <class T>
    Matrix<T>& Matrix<T>::operator=(const Matrix<T>& other)
    {
        this->rowSize = other.rowSize;
        this->colSize = other.colSize;
        this->elems = other.elems;
        return *this;
    }

    /**
     *
     * @tparam T .
     * @param other the right matrix
     * @return the added 2 matrices and
     */
    template <class T>
    Matrix<T> Matrix<T>::operator+(const Matrix<T> &other) const
    {
        if (this->rowSize != other.rowSize || this->colSize != other.colSize)
        {
            throw dimError();
        }
        Matrix<T> newMatrix = Matrix<T>(other.rowSize, other.colSize);
        typename std::vector<T>::const_iterator thisIt;
        thisIt = this->elems.begin();
        typename std::vector<T>::const_iterator otherIt;
        otherIt = other.elems.begin();
        typename std::vector<T>::iterator finalIt;
        finalIt = newMatrix.elems.begin();

        for ( ; thisIt != this->elems.end() ; thisIt++, otherIt++, finalIt++)
        {
            *finalIt = *thisIt + *otherIt;
        }
        return newMatrix;
    }

    /**
     *
     * @tparam T .
     * @param other the right matrix
     * @return the left matrix minus the right one.
     */
    template <class T>
    Matrix<T> Matrix<T>::operator-(const Matrix<T> &other) const
    {
        if (this->rowSize != other.rowSize || this->colSize != other.colSize)
        {
            throw dimError();
        }
        Matrix<T> newMatrix = Matrix<T>(other.rowSize, other.colSize);
        typename std::vector<T>::const_iterator thisIt;
        thisIt = this->elems.begin();
        typename std::vector<T>::const_iterator otherIt;
        otherIt = other.elems.begin();
        typename std::vector<T>::iterator finalIt;
        finalIt = newMatrix.elems.begin();

        for ( ; thisIt != this->elems.end() ; thisIt++, otherIt++, finalIt++)
        {
            *finalIt = *thisIt - *otherIt;
        }
        return newMatrix;
    }


    /**
     * .
     * @tparam T
     * @param other the right matrix
     * @return the multiplication of two matrices
     */
    template <class T>
    Matrix<T> Matrix<T>::operator*(const Matrix<T> &other) const
    {
        if (this->colSize != other.rowSize)
        {
            throw dimError();
        }
        Matrix<T> newMatrix = Matrix<T>(other.rowSize, other.colSize);
        int thisRow = this->rowSize;
        int thisCol = this->colSize;
        int otherCol = other.rowSize;
        for (int i = 0; i < thisRow ; ++i)
        {
            for (int j = 0; j < otherCol; ++j)
            {
                for (int k = 0; k < thisCol; ++k)
                {
                    newMatrix(i, j) += (*this)(i, k) * other(k, j);
                }
            }
        }
        return newMatrix;
    }

    /**
     * returns true if two matrices are the same
     * @tparam T
     * @param other the right matrix
     * @return true if matrices are the same
     */
    template <class T>
    bool Matrix<T>::operator==(const Matrix<T> &other) const
    {
        if (this->rowSize != other.rowSize || this->colSize != other.colSize)
        {
            return false;
        }
        typename std::vector<T>::const_iterator thisIt;
        thisIt = this->elems.begin();
        typename std::vector<T>::const_iterator otherIt;
        otherIt = other.elems.begin();
        for ( ; thisIt != this->elems.end(); thisIt++, otherIt++)
        {
            if (*thisIt != *otherIt)
            {
                return false;
            }
        }
        return true;
    }

    /**
     * false if matrices aren't the same
     * @tparam T .
     * @param other the right matrix
     * @return false if matrices aren't the same
     */
    template <class T>
    bool Matrix<T>::operator!=(const Matrix<T> &other) const
    {
        if (this->rowSize != other.rowSize || this->colSize != other.colSize)
        {
            return true;
        }
        typename std::vector<T>::const_iterator thisIt;
        thisIt = this->elems.begin();
        typename std::vector<T>::const_iterator otherIt;
        otherIt = other.elems.begin();
        for ( ; thisIt != this->elems.end(); thisIt++, otherIt++)
        {
            if (*thisIt != *otherIt)
            {
                return true;
            }
        }
        return false;
    }


    /**
     * .
     * @tparam T .
     * @param row the row index
     * @param col the col index
     * @return the value in that location
     */
    template <class T>
    T Matrix<T>::operator()(unsigned int row, unsigned int col) const
    {
        int index = this->_getVectorIndex(row, col);
        try
        {
            return this->elems.at(index);
        }
        catch (std::exception e)
        {
            throw indexError();
        }
    }

    /**
     *
     * @tparam T .
     * @param row the row index
     * @param col the col index
     * @return the value in that location
     */

    template <class T>
    T& Matrix<T>::operator()(unsigned int row, unsigned int col)
    {
        int index = this->_getVectorIndex(row, col);
        try
        {
            return this->elems.at(index);
        }
        catch (std::exception e)
        {
            throw indexError();
        }
    }

    /**
     * .
     * @tparam T
     * @return true if the matrix is of squared size
     */
    template <class T>
    bool Matrix<T>::isSquareMatrix() const
    {
        if (this->colSize == this->rowSize)
        {
            return true;
        }
        return false;
    }

    template <class B>
    std::ostream& operator<<(std::ostream& o, const Matrix<B>& m)
    {
        for (int i = 0; i < m.rows(); i++)
        {
            for (int j = 0; j < m.cols(); j++)
            {
                o << m(i, j) << "\t";
            }
            o << "\n";
        }
        return o;
    }

    /**
     * transposes the matrix
     * @tparam T .
     * @return the transposed matrix
     */
    template <class T>
    Matrix<T> Matrix<T>::trans() const
    {
        if (!(this->isSquareMatrix()))
        {
            throw dimError();
        }
        Matrix<T> newMatrix = Matrix(this->rowSize, this->colSize);
        for (int i = 0; i < this->rowSize; ++i)
        {
            for (int j = 0; j < this->colSize; ++j)
            {
                newMatrix(i, j) = (*this)(j, i);
            }
        }
        return newMatrix;
    }

    /**
     * creates a conjugate transpose
     * @return the conjugated transposed matrix
     */
    template <>
    Matrix<Complex> Matrix<Complex>::trans() const
    {
        if (!(this->isSquareMatrix()))
        {
            throw dimError();
        }
        Matrix<Complex> newMatrix = Matrix(this->rowSize, this->colSize);
        for (int i = 0; i < this->rowSize; ++i)
        {
            for (int j = 0; j < this->colSize; ++j)
            {
                newMatrix(i, j) = (*this)(i, j).conj();
            }
        }
        return newMatrix;
    }


#endif //MATRIX_MATRIX_H
