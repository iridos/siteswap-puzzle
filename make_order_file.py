import os

pieces_dir = "pieces/"
tiles = sorted(os.listdir(pieces_dir))

def parse_tile(filename):
    parts = filename.strip(".svg").split("_")
    in_val = parts[1][2:]
    out_val = parts[2][3:]
    return filename, in_val, out_val

tiles_parsed = [parse_tile(t) for t in tiles]
tiles_dict = {t[1]: [] for t in tiles_parsed}  # Dictionary für schnelle Suche

for tile in tiles_parsed:
    tiles_dict[tile[1]].append(tile)

sorted_tiles = []
remaining_tiles = set(tiles_parsed)  # Set für schnelles Entfernen

while remaining_tiles:
    if not sorted_tiles:
        current_tile = remaining_tiles.pop()  # Erstes Teil nehmen
    else:
        last_tile = sorted_tiles[-1]
        next_tiles = tiles_dict.get(last_tile[2], [])  # Schnelle Suche per Dict
        next_tiles = [t for t in next_tiles if t in remaining_tiles]  # Nur verfügbare
        if next_tiles:
            current_tile = next_tiles[0]
            remaining_tiles.remove(current_tile)
        else:
            sorted_tiles.append(("BREAK", "-", "-"))  # Neue Reihe starten
            if remaining_tiles:
                current_tile = remaining_tiles.pop()  # Neuen Startpunkt setzen
            else:
                break  # Falls nichts mehr übrig ist, beenden

    sorted_tiles.append(current_tile)

    # Fortschritt
    progress = (1 - len(remaining_tiles) / len(tiles_parsed)) * 100
    print(f"Fortschritt: {progress:.2f}% ({len(sorted_tiles)}/{len(tiles_parsed)})", end="\r")

# Ergebnis speichern
with open("puzzle_order.txt", "w") as f:
    for tile in sorted_tiles:
        if tile[0] == "BREAK":
            f.write("\n")
        else:
            f.write(tile[0] + "\n")

print("\nReihenfolge in puzzle_order.txt gespeichert!")

