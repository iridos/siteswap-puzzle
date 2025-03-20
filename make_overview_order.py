import svgwrite
import os

# Einstellungen
cols = 12
tile_width = 290
tile_height = 250
overlap = 40  # Korrigiert von 50 auf 40
pieces_dir = "pieces/"
output_file = "puzzle_ordered.svg"
order_file = "puzzle_order.txt"  # Datei mit der Reihenfolge

# Puzzleteile in Reihenfolge laden
with open(order_file, "r") as f:
    ordered_tiles = [line.strip() for line in f.readlines() if line.strip()]

# Berechnung der Gesamtgröße
rows = -(-len(ordered_tiles) // cols)  # Aufrunden für genug Zeilen
width = (cols - 1) * (tile_width - overlap) + tile_width
height = rows * tile_height

# SVG-Dokument erstellen
dwg = svgwrite.Drawing(output_file, profile="tiny", size=(width, height))

for idx, tile in enumerate(ordered_tiles):
    x = (idx % cols) * (tile_width - overlap)
    y = (idx // cols) * tile_height
    dwg.add(dwg.image(os.path.join(pieces_dir, tile), insert=(x, y), size=(tile_width, tile_height)))

dwg.save()
print(f"Geordnetes SVG gespeichert: {output_file}")
