#! /usr/bin/env python3
import svgwrite

# carefully crafted bezier string that is a nubsie/hole
def bezier_string(x, y):
    y=y-14
    x=x-1
    return (f"m {x},{y+8} c 7,0 10,-8 18,-8 c 8,0 16,8 16,17 c 0,9 -8,17 -16,17 c -8,0 -11,-8 -18,-8")



def create_piece(piece_id, holes, fillers, size=4):
    # size is the number of hole
    # we take a pixel-size of 50 pixel per hole
    # we make the piece square for now, so xsize=ysize
    xysize= size*50
    print(f'piece_{piece_id}.svg');
    dwg = svgwrite.Drawing(f'piece_{piece_id}.svg', profile='tiny', size=(xysize+100, xysize+100))
    dwg.add(dwg.rect(insert=(0, 0), size=(xysize+100, xysize+100), fill='lightblue')) 
    # draw box. 
    dwg.add(dwg.rect(insert=(20, 10), size=(xysize,xysize), stroke='black', fill='white'))
    
    for i in range(size):
        y_pos = 10 + i * 50
        # Löcher (links)
        if i + 1 in holes:
            x, y = 20, y_pos + 20  # Beispielwerte
            dwg.add(dwg.path(d=bezier_string(x, y), stroke='black', fill='lightblue'))


        # Nupsies (rechts)
        if i + 1 in fillers:
            x, y = 220, y_pos + 20  # Beispielwerte
            dwg.add(dwg.path(d=bezier_string(x, y), stroke='black', fill='white'))
    dwg.save()

# all 4 holes/nubsies in one piece for testing
options = [[1,2,3,4]]]
# all possible combinations of holes/pieces on one side
options = [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]


for holes in options:
    for fillers in options:
        name = f"h{holes[0]}{holes[1]}n{fillers[0]}{fillers[1]}"
        #holes = [1, 2]  # Positions with holes
        #fillers = [3, 4]  # Positions with nupsies
        create_piece(name, holes, fillers)

