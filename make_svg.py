#! /usr/bin/env python3
import svgwrite

def create_piece(piece_id, holes, fillers, size=4):
    xysize= size*50
    dwg = svgwrite.Drawing(f'piece_{piece_id}.svg', profile='tiny', size=(xysize+80, xysize+80))
    
    # draw box. 
    dwg.add(dwg.rect(insert=(20, 10), size=(xysize,xysize), stroke='black', fill='none'))
    
    for i in range(size):
        y_pos = 10 + i * 50
        # Löcher (links)
        if i + 1 in holes:
            dwg.add(dwg.rect(  insert=(20,  y_pos + 15), size=(20,20), stroke='black', fill='white'))
        # Nupsies (rechts)
        if i + 1 in fillers:
            dwg.add(dwg.rect(  insert=(xysize+20, y_pos + 15), size=(20,20), stroke='black', fill='white'))
            dwg.add(dwg.circle(center=(200+30, y_pos + 25), r=10, stroke='black', fill='black'))
    
    dwg.save()

# Beispiel für ein Puzzleteil

options = [[1,2,3,4]]#,[1,3],[1,4],[2,3],[2,4],[3,4]]

for holes in options:
    for fillers in options:
        name = f"h{holes[0]}{holes[1]}n{fillers[0]}{fillers[1]}"
        #holes = [1, 2]  # Positions mit Löchern
        #fillers = [3, 4]  # Positions mit Nupsies
        create_piece(name, holes, fillers)

