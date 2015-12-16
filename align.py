#!/usr/bin/python

"""
it works well only the case that the gap score is negative.
"""
MATCH = 3
MISMATCH = -4
GAP = -5
#letter for traceback. match,mismatch:1 gap_x:2, gap_y:3, start:4
trc = {
    'match': 1,
    'gap_x': 2,
    'gap_y': 3,
    'start': 4
}

import sys
argvs = sys.argv


def match(a, b):
    if a == b:
        return MATCH
    else:
        return MISMATCH


def calc_alignment(x, y):
    """
    calculate smith-waterman algorithm between x and y.
    """
    # score matrix: score
    # traceback matrix: trace
    score = [[0 for j in range(len(y))] for i in range(len(x))]
    trace = [[0 for j in range(len(y))] for i in range(len(x))]
    bestend = [0, 0]
    bestscore = 0

    # calculate score matrix and traceback one
    # with dynamic programming
    for i in range(1, len(x)):
        for j in range(1, len(y)):
            # score renewal

            m = score[i-1][j-1]+match(x[i], y[j])
            gap_x = score[i-1][j] + GAP
            gap_y = score[i][j-1] + GAP
            renew = [m, gap_x, gap_y, 0]
            score[i][j] = max(renew)

            # bestscore renewal for the record of best alignment
            if bestscore < score[i][j]:
                bestscore = score[i][j]
                bestend = [i, j]

            if max(renew) == m:
                trace[i][j] = trc['match']

            elif max(renew) == gap_x:
                trace[i][j] = trc['gap_x']

            elif max(renew) == gap_y:
                trace[i][j] = trc['gap_y']

            elif max(renew) == 0:
                trace[i][j] = trc['start']

## traceback
    currentscore = bestscore
    alignment = []
    k = bestend[0]
    l = bestend[1]
    while currentscore > 0:
        alignment.insert(0, trace[i][j])
        if score[k][l] == 0:
            startpoint = [k, l]
            break
        else:
            if trace[k][l] == trc['match']:
                k = k-1
                l = l-1
            elif trace[i][j] == trc['gap_x']:
                k = k-1
            elif trace[i][j] == trc['gap_y']:
                l = l-1

    print("startpoint:"+str(startpoint))
    print("alignment:"+str(alignment))

    return alignment

if __name__ == "__main__":
    x = argvs[1]
    y = argvs[2]
    alignment = calc_alignment(x, y)
