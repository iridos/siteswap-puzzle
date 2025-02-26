#! /usr/bin/env python3
import svgwrite

def bezier_string(x, y):
    #return (f"m {x},{y+8} c 7,0 10,-8 18,-8 c 8,0 16,8 16,17 c 0,9 -8,17 -16,17 c -8,0 -11,-8 -18,-8")
    # the bit with the hole is 50 high. the hole itself is 34 high. the first point is 8 below the top point
    # so we first have to draw a vertical line from x,y to x,y+8+8, then we can do relative movements
    # carefully crafted bezier string that is a nubsie/hole
    return (f"M {x},{y} L {x},{y+8+8} c 7,0 10,-8 18,-8 c 8,0 16,8 16,17 c 0,9 -8,17 -16,17 c -8,0 -11,-8 -18,-8 l 0,16")

def bezier_string_or_line(x, y,bezier):
    # the bit with the hole is 50 high. the hole itself is 34 high. the first point is 8 below the top point
    # so we first have to draw a vertical line from x,y to x,y+8+8, then we can do relative movements
    if(bezier):
    # carefully crafted bezier string that is a nubsie/hole
        return (f"L {x},{y+8+8} c 7,0 10,-8 18,-8 c 8,0 16,8 16,17 c 0,9 -8,17 -16,17 c -8,0 -11,-8 -18,-8 l 0,16")
    else:
        # less carefully crafted line if there is no nubsie/hole there
        return (f"L {x},{y+8+8+34+8} ")


def create_piece(piece_id, holes, fillers, size=4):
    border=25
    xysize= size*50 + 2*border
    hole_height=50
    xsize=xysize
    ysize=xysize
    print(f'piece_{piece_id}.svg');
    dwg = svgwrite.Drawing(f'piece_{piece_id}.svg', profile='tiny', size=(xysize+40, xysize))
    # draw top of box starting from right going to 0,0
    #dwg.add(dwg.path(d=f"M {xsize},{0} L {0},{0} ", stroke='black'))
    puzzle_string=f"M {xsize},{0} L {0},{0} "
    # holes on the left, first we draw the border up to the first nubs
    # we are already at 0,0
    #dwg.add(dwg.path(d=f"L 0,{border}", stroke='black'))
    puzzle_string=f"{puzzle_string} L 0,{border}"
    for i in range(size):
        # holes left 
        # we have a border on top , then every hole has a height
        y_pos = i * hole_height + border
        x, y = 0, y_pos 
        #dwg.add(dwg.path(d=bezier_string_or_line(x, y,i+1 in holes), stroke='black', fill='white'))
        puzzle_string=f"{puzzle_string} {bezier_string_or_line(x, y,i+1 in holes)}"
    # fill vertical to bottom
    #dwg.add(dwg.path(d=f"M {x},{y+hole_height} L {x},{y_pos+hole_height+ border} ", stroke='black'))
    #puzzle_string=f"{puzzle_string} M {x},{y+hole_height} L {x},{y_pos+hole_height+ border} "
    puzzle_string=f"{puzzle_string} L {x},{y_pos+hole_height+ border} "
    # line at the bottom
    y=y_pos+hole_height+ border
    #dwg.add(dwg.path(d=f"M {x},{y} L {x+ysize},{y} ", stroke='black'))
    puzzle_string=f"{puzzle_string} L {x+ysize},{y} "
    # border from top to first nubs
    #dwg.add(dwg.path(d=f"M {xsize},0 L {xsize},{border}", stroke='black'))
    puzzle_string=f"{puzzle_string} M {xsize},0 L {xsize},{border}"
    # 2nd loop for nubsies
    for i in range(size):
        # Nupsies (right)
        # we have a border on top , then every hole has a height
        y_pos = i * hole_height + border
        x, y = 0, y_pos 
        x, y = ysize, y_pos 
        #dwg.add(dwg.path(d=bezier_string_or_line(x, y,i+1 in fillers), stroke='black', fill='white'))
        puzzle_string=f"{puzzle_string} {bezier_string_or_line(x, y,i+1 in fillers)}"
    # last bit from last nubs to bottom
    #dwg.add(dwg.path(d=f"M {xsize},{y+hole_height} L {xsize},{ysize}", stroke='black'))
    puzzle_string=f"{puzzle_string} M {xsize},{y+hole_height} L {xsize},{ysize} Z"
    dwg.add(dwg.path(id=f"holes{holes[0]}{holes[1]}_fillers{fillers[0]}{fillers[1]}", d=puzzle_string,stroke='black',fill='#ccddcc',stroke_width=2))
    dwg.add(dwg.text("test",id="siteswap",insert=(100,20),font_size=20, color="blue"))
    dwg.save()

# all 4 holes/nubsies in one piece for testing
options = [[1,2,3,4]]
# all possible combinations of holes/pieces on one side
options = [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]


for holes in options:
    for fillers in options:
        name = f"h{holes[0]}{holes[1]}n{fillers[0]}{fillers[1]}"
        #holes = [1, 2]  # Positions with holes
        #fillers = [3, 4]  # Positions with nupsies
        create_piece(name, holes, fillers)

