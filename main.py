#!/usr/local/bin/python3

import time
import argparse
from parse import error_exit
from algo import solve_puzzle
from heuristics import manhattan_distance, hamming_distance, linear_conflict

if __name__ == '__main__':
    # Arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str, help='puzzle file')
    parser.add_argument('-g', '--greedy', action='store_true',
            help='greedy bonus')
    parser.add_argument('-u', '--ucs', action='store_true',
            help='uniform-cost bonus')
    parser.add_argument('-hr', '--heuristic', type=str, default='md',
            help='heuristic (md for manhattan_distance, \
                    hd for hamming_distance or lc for linear conflict)')
    parser.add_argument('-v', '--variant', type=int,
            help='coefficient for variant algorithm', default=1)
    args = parser.parse_args()

    # Arguments checking
    heuristics = {
            'md': manhattan_distance,
            'hd': hamming_distance,
            'lc': linear_conflict
    }
    error_exit('heuristic') if args.heuristic not in heuristics else 0
    error_exit('variant') if args.variant <= 0 else 0
    error_exit('bonus') if args.greedy and args.ucs else 0
    bonus = None
    if args.greedy:
        bonus = 'greedy'
    elif args.ucs:
        bonus = 'ucs'

    # Resolution
    start_time = time.time()
    solve_puzzle(args.file, args.variant, bonus=bonus, heuristic=heuristics[args.heuristic])
    print('Duration=', time.time() - start_time, 's')
