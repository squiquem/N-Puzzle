# N-Puzzle

ALgorithmic project: solving sliding puzzles
____

The goal of this project is to solve the N-puzzle ("taquin" in French) game using the A* search algorithm or one of its variants.
You start with a square board made up of N*N cells. One of these cells will be empty, the others will contain numbers, starting from 1, that will be unique in this instance of the puzzle.
Your search algorithm will have to find a valid sequence of moves in order to reach the final state, a.k.a the "snail solution", which depends on the size of the puzzle (Example below). While there will be no direct evaluation of its performance in this instance of the project, it has to have at least a vaguely reasonable perfomance : Taking a few second to solve a 3-puzzle is pushing it, ten seconds is unacceptable.
The only move one can do in the N-puzzle is to swap the empty cell with one of its neighbors (No diagonals, of course. Imagine you’re sliding a block with a number on it towards an empty space).

	1 2 3		 1  2  3  4		   1  2  3  4  5
	8   4		12 13 14  5		  16 17 18 19  6
	7 6 5		11    15  6		  15 24    20  7
				10  9  8  7		  14 23 22 21  8
								  13 12 11 10  9

## Generate puzzles

	python3 res_npuzzle-gen.py -h
____

## Help

	python3 main.py -h
____

## Run

	python3 main.py <puzzle>
____

## Return

The program returns:
- the path to the solution
- the number of nodes explored
- the time and size complexities
- the duration
____

If you have any questions or suggestions, feel free to send me an email at squiquem@student.42.fr
