pawns = {"b4", "c4", "d4", "e4", "f4", "g4", "e5"}

secure = []
for pawn in pawns:
    # split cell into rows and columns
    column = list(pawn)[0]
    row = list(pawn)[1]
    next_row = str(int(row) + 1)
    #use boundary condition for the edges of the bord
    if ord(column) < ord('h'):
        #get safe position diagonally
        safe = chr(ord(column) + 1) + next_row
        secure.append(safe)
    if ord(column) > ord('a'):
        safe = chr(ord(column) - 1) + next_row
        secure.append(safe)

# check how many pawns are safe
count = 0
for pawn in pawns:
    if pawn in set(secure):
        count += 1
print(set(secure))
print(count)