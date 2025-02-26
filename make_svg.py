#! /usr/bin/env python3
import svgwrite

def create_piece(piece_id, holes, fillers, size=4):
    xysize= size*50
    print(f'piece_{piece_id}.svg');
    dwg = svgwrite.Drawing(f'piece_{piece_id}.svg', profile='tiny', size=(xysize+80, xysize+80))
    
    # draw box. 
    dwg.add(dwg.rect(insert=(20, 10), size=(xysize,xysize), stroke='black', fill='none'))
    
    for i in range(size):
        y_pos = 10 + i * 50
        # Löcher (links)
        if i + 1 in holes:
            x, y = 20, y_pos + 20  # Beispielwerte
            dwg.add(dwg.path(d=f"M {x} {y} "
                   "c 6.3 0.0 7.4 -1.7 10 -3.4 "
                   "c 2.9 -1.8 5.8 -3.6 8 -3.6 "
                   "c 8.7 0 16 7.1 16 16 "
                   "c 0 8.7 -7.1 16 -16 16 "
                   "c -2.2 0 -4.8 -1.8 -7.5 -3.5 "
                   "c -2.7 -1.8 -4.7 -3.4 -10 -3.5",  # Hier angepasst
                   stroke='black', fill='white'))
#  <path d="M 19.483844,30 C 25.783844,30 27.4,28.3 30,26.6 32.9,24.8 35.8,23 38,23 c 8.7,0 16,7.1 16,16 0,8.7 -7.1,16 -16,16 -2.2,0 -4.8,-1.8 -7.5,-3.5 C 27.8,49.7 24.783844,48.1 19.483844,48" fill="#ffffff" stroke="#000000"  />


        # Nupsies (rechts)
        if i + 1 in fillers:
            x, y = 220, y_pos + 20  # Beispielwerte
            dwg.add(dwg.path(d=f"M {x} {y} "
                   "c 6.3 0.0 7.4 -1.7 10 -3.4 "
                   "c 2.9 -1.8 5.8 -3.6 8 -3.6 "
                   "c 8.7 0 16 7.1 16 16 "
                   "c 0 8.7 -7.1 16 -16 16 "
                   "c -2.2 0 -4.8 -1.8 -7.5 -3.5 "
                   "c -2.7 -1.8 -4.7 -3.4 -10 -3.5",  # Hier angepasst
                   stroke='black', fill='white'))
    
    dwg.save()

# Beispiel für ein Puzzleteil

options = [[1,2,3,4]]#,[1,3],[1,4],[2,3],[2,4],[3,4]]

for holes in options:
    for fillers in options:
        name = f"h{holes[0]}{holes[1]}n{fillers[0]}{fillers[1]}"
        #holes = [1, 2]  # Positions mit Löchern
        #fillers = [3, 4]  # Positions mitNupsies
        create_piece(name, holes, fillers)

