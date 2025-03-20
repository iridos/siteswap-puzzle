import svgwrite
import os

# Einstellungen für das Raster
cols = 12   # Spaltenanzahl
rows = 36   # Zeilenanzahl
tile_size = 50  # Breite/Höhe eines Puzzleteils (anpassen!)
output_file = "puzzle_overview.svg"
pieces_dir = "pieces/"  # Verzeichnis mit den Puzzleteilen

# Puzzleteile sammeln (alphabetisch sortiert)
tiles = sorted(f for f in os.listdir(pieces_dir) if f.startswith("sw") and f.endswith(".svg"))

# SVG-Dokument erstellen
dwg = svgwrite.Drawing(output_file, profile="tiny", size=(cols * tile_size, rows * tile_size))

for idx, tile in enumerate(tiles):
    x = (idx % cols) * tile_size
    y = (idx // cols) * tile_size
    dwg.add(dwg.image(os.path.join(pieces_dir, tile), insert=(x, y), size=(tile_size, tile_size)))

dwg.save()
print(f"SVG mit {len(tiles)} Puzzleteilen als Raster gespeichert: {output_file}")

