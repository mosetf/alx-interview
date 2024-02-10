#!/usr/bin/python3
"""N queens puzzle"""
import sys


def printSolution(board):
    """Prints the solution"""
    queens = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                queens.append([i, j])
    print(queens)



