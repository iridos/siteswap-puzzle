#!/usr/bin/python3
# siteswap-puzzle
# finds "puzzle-pieces", i.e. numbers that can become valid siteswaps when combined with other pieces
import itertools


shorten = 4 # we shorten the siteswap arrows here by 4 making them causal
puzzlelength = 4
valid_numbers = [2, 4, 5, 6, 7, 8, 9, 10]  # Zahlen 2-10 ohne 3
nubs_per_piece=2

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


calculate_pieces(puzzlelength, shorten, valid_numbers, nubs_per_piece)

