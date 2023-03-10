To compute the program, you should tap on the terminal:
        ‘python3 Nsliding_puzzle.py ’
Then a message  will be displayed on the output screen asking you to choose the way of generating the start configuration of the problem.

You either write ‘random’ and then a random initial state will be generated or  ‘text_file’ then the n and the initial state will be read from the file start_config.txt which has this format:
8
7 4 3
0 1 5
8 2 6

n on the first line and then the initial state

After choosing the start configuration choice, a message  will be displayed asking you to choose which algorithm to use from the ones implemented.
You write 'BFS' or 'UCS' or 'A*_h1' or 'A*_h2' or 'Bi_BFS'
