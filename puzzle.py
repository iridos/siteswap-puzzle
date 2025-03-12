#!/usr/bin/python3
# siteswap-puzzle
# finds "puzzle-pieces", i.e. numbers that can become valid siteswaps when combined with other pieces
import itertools
import svgwrite

shorten = 4 # we shorten the siteswap arrows here by 4 making them causal
puzzlelength = 4
valid_numbers = [2, 4, 5, 6, 7, 8, 9, 10]  # Zahlen 2-10 ohne 3
nubs_per_piece=2

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
    filename = f"pieces/sw{''.join(map(str, piece_id))}_in{''.join(map(str, holes))}_out{''.join(map(str, fillers))}.svg"
    print(filename)
    dwg = svgwrite.Drawing(filename, profile='tiny', size=(xysize+40, xysize))
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

    x_start, y_top, y_bottom = 60, 80, 200  # Startpositionen anpassen
    spacing = 40  # Abstand zwischen den Zahlen
    for idx, num in enumerate(piece_id):
        x_pos = x_start + idx * spacing
        y_pos = y_top if idx % 2 == 0 else y_bottom  # Gerade nach oben, ungerade nach unten
        dwg.add(dwg.text(str(num), insert=(x_pos, y_pos), font_size=40, fill="blue"))
    dwg.save()

def calculate_pieces(puzzlelength, shorten, valid_numbers, nubs_per_piece):
  for piece in map(list, itertools.product(valid_numbers, repeat=4)):
    interface = list(piece)
    size=len(interface)
    # minus 4 to convert to causal
    # minus position to 
    for idx in range(0,size):
        # causal: minus number hands (4)
        # +idx: make the sswp start from index 0,
        # +1: count that we count positions from 1
        # 6,6,6,6 becomes 2,2,2,2 then +1+idx: 3,4,5,6
        interface[idx] += idx + 1 - shorten
        # we do not support arrows going backwards, so break
        if(interface[idx] <= 0 ):
            interface=[]
            break
        else:
         if(interface[idx] <= puzzlelength):
            # puzzle-internal positions as negative
            # -3,-4,5,6
            interface[idx] *= -1
         else:
            # start outgoing connection from future puzzle piece start
            # -3,-4,1,2
            interface[idx] -= puzzlelength
            if interface[idx]>puzzlelength: 
                interface=[]
                break 
    if len(set(interface)) < puzzlelength:  
        # remove duplikates (invlid siteswap)
        continue
    occupied = {abs(x) for x in interface if x < 0}
    free     = sorted(set(range(1, size + 1)) - occupied)
    fillers  = sorted(x for x in interface if x > 0)
    if len(fillers) != len(free):
        import sys 
        print("error: in and out does not match ", len(occupied) , len(free))
        sys.exit()
    if len(free) != nubs_per_piece:
        continue
    numberobjects = 0
    for add in piece:
        numberobjects = numberobjects + add
    numberobjects = numberobjects / len(piece)
    # with interface
    #output=f"piece: %-14s  free: %-14s nubs: %-14s iface: %-18s"
    #print(output % (piece,free,fillers,interface)) 
    # regular output
    output=f"n: %-3s objs: %-3s piece: %-14s free: %-14s nubs: %-14s"
    print(output % (len(free),numberobjects,piece,free,fillers)) 
    create_piece(piece,free,fillers,puzzlelength)



calculate_pieces(puzzlelength, shorten, valid_numbers, nubs_per_piece)

