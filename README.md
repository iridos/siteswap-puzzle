After an idea from the passing signal group.

Siteswaps can be created by concatenating puzzle-pieces. This is some code to create such pieces as SVG. 
Puzzle pieces have the property, that they  encode incoming and outgoing throws as puzzle holes and puzzle noses. Which means throws that have to come in on one of the sites inside the puzzle piece and how far outgoing throws go.

The siteswaps are seen in their causal representation to shorten the throws so that more dependencies are fulfilled from within the puzzle piece. 

For now, this focuses on puzzle pieces that have 4 siteswap numbers on them. Of those.

Because the number of incoming/outgoing connections always has to be the same, translation between puzzle pieces with a different number of holes/noses is not possible.

Most pieces had two incoming/outgoing throws, so we further focus on those. 

single-step scripts:

* calculate_pieces.py

calculates puzzle pieces with 4 numbers on them. Output like:
`n: 2   objs: 5.25 piece: [4, 4, 6, 7]   free: [3, 4]         nubs: [1, 3] `
** n: the number of nubs/holes of the piece
objs: calculated number of objects juggled in this piece (pieces must fit circularly, then the average of those numbers will become a full number)
** piece: the siteswap numbers on that piece
** free: the positions of the holes on the piece 
** nubs: the positions of the nubs on the other side of the piece


* make_svg.py

creates the svg shapes of a piece. the possible placement of holes/nubsies is given via options:

** options = [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
these options create all shapes for a piece with 4 incoming/outgoing connections

== putting everything together ==

* puzzle.py

calculates pieces and svg shapes and creates one piece per result in pieces/

* make_order_file.py

creates an puzzle_order.txt file trying to fit most pieces together

* puzzle_order.txt 
here you can re-define an order to put the many piece-svg into one svg to group them all

* puzzle_ordered.svg

svg importing all pieces via <use> or <image>

* make_overview.py make_overview_order.py
create overview svg file (accorgin to puzzle_order.txt file)

* puzzle_overview.svg
final svg file
