#!/usr/bin/env python
'''
Mission points:

Each tier has 3 missions

Tier 1 (6 points):

- pacify mnoleg or ereshkigal
- poly trj and kill him
- complete a zig as soon after mission 8 as possible:
  - if you have a zig in D:
     - if you have enough gold, enter it asap on turn 9
     - if you don't have gold and have a zig in D and tomb will give you
     -   enough gold, do tomb and then zig on turn 10
  - if you don't have a zig in D:
    - you must enter pan on turn 9, and you must enter the first zig you see
    - that you can afford, and you must not leave pan before completing a
    - zig.

Tier 2 (4 points):
- get the slimy rune on turn 4 without worshipping jiyva at any point
- get the golden rune on turn 8 without worshipping kiku
- kill all hellpanlords

Tier 3 (2 points):
- complete mission one without dying
- get the slimy rune for your 2nd lair rune (any valid turn)
- think of a third mission!

Bonus Mission Points:

1stT*6 + 2ndT*4 + 3rdT*2

Player Points:
        
3*highest score, 2*min(second highest, 8), + sum(mission points)

Max score:
        
(3*18 + 2*9) + (3*6 + 3*4 + 3*2) = 72 + 36 = 108
'''
def character_points(a, b, c):
    assert a >= b >= c
    return (3 * a) + (2 * min(b, 9))

def mission_points(a, b, c):
    a, b, c = [n if n <= 3 else 3 for n in a, b, c]
    return (a * 6) + (b * 4) + (c * 2)

if __name__ == '__main__':
    import sys
    if sys.argv[1].startswith('character') and len(sys.argv) == 5:
        args = [int(n) for n in sys.argv[2:]]
        print character_points(*args)
    elif sys.argv[1].startswith('mission') and len(sys.argv) == 5:
        args = [int(n) for n in sys.argv[2:]]
        print mission_points(*args)
