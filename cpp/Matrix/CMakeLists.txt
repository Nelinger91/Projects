cmake_minimum_required(VERSION 3.6)
project(Matrix)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES Matrix.hpp Complex.h Complex.cpp GenericMatrixDriver.cpp)
add_executable(Matrix ${SOURCE_FILES})