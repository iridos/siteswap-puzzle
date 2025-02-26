#! /usr/bin/env python3
import svgwrite

def bezier_string(x, y):
    y=y-14
    x=x-1
    return (f"M {x} {y+10} "  # Startpunkt
            f"C {x+5.78} {y+10}, {x+7.4} {y+8.3}, {x+10} {y+6.6} "
            f"C {x+12.9} {y+4.8}, {x+15.8} {y+3}, {x+18} {y+3} "
            f"C {x+26.7} {y+3}, {x+34} {y+10.1}, {x+34} {y+19} "
            f"C {x+34} {y+27.7}, {x+26.9} {y+35}, {x+18} {y+35} "
            f"C {x+15.8} {y+35}, {x+13.2} {y+33.2}, {x+10.5} {y+31.5} "
            f"C {x+7.8} {y+29.7}, {x+4.78} {y+28.1}, {x} {y+28}")



def create_piece(piece_id, holes, fillers, size=4):
    xysize= size*50
    print(f'piece_{piece_id}.svg');
    dwg = svgwrite.Drawing(f'piece_{piece_id}.svg', profile='tiny', size=(xysize+80, xysize+80))
    dwg.add(dwg.rect(insert=(0, 0), size=(xysize+80, xysize+80), fill='lightblue')) 
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

# Beispiel für ein Puzzleteil

options = [[1,2,3,4]]#,[1,3],[1,4],[2,3],[2,4],[3,4]]
options = [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

for holes in options:
    for fillers in options:
        name = f"h{holes[0]}{holes[1]}n{fillers[0]}{fillers[1]}"
        #holes = [1, 2]  # Positions mit Löchern
        #fillers = [3, 4]  # Positions mitNupsies
        create_piece(name, holes, fillers)

