def is_queen (cu_ro):
    if  cu_ro == 0 or cu_ro == 7:
        return True

def coordinate_convertor(converting_row, converting_col):
    rows_coordinates = [8,7,6,5,4,3,2,1]
    columns_coordinate = ['a','b','c','d','e','f','g','h']
    return ''.join([columns_coordinate[converting_col],str(rows_coordinates[converting_row])])

rows = 8
cols = 8
b_coordinates = ''
w_coordinates = ''
matrix =[]

for _ in range(rows):
    matrix.append(input().strip().split(' '))
for row_index, row in enumerate(matrix):
    if 'b' in row:
        b_coordinates = (row_index,row.index('b'))
    elif 'w' in row:
        w_coordinates = (row_index, row.index('w'))

b_row, b_col = b_coordinates
w_row, w_col = w_coordinates
# delta_diagonal = ((1,1), (1,-1), (-1,-1), (-1,+1))
w_delta_row = -1
b_delta_row = 1
counter = 0
while True:

    cur_row = ''
    cur_col = ''
    cur_player = ''
    if counter % 2 == 0:
        cur_player = 'White'
        cur_row = w_row
        cur_col = w_col
        w_row += w_delta_row

    else:
        cur_player = 'Black'
        cur_row = b_row
        cur_col = b_col
        b_row += b_delta_row
    if cur_row == 7 and cur_player == 'Black':
        print(f"Game over! {cur_player} pawn is promoted to a queen at {coordinate_convertor(cur_row,cur_col)}.")
        break
    elif cur_row == 0 and cur_player == 'White':
        print(f"Game over! {cur_player} pawn is promoted to a queen at {coordinate_convertor(cur_row, cur_col)}.")
        break
    if abs(w_col - b_col) == 1:
        if cur_row == b_row:
            cur_row = w_row
            cur_col = w_col
            cur_player ='Black'
        else:
            cur_row = b_row
            cur_col = b_col
            cur_player = 'White'

        print(f'Game over! {cur_player} win, capture on {coordinate_convertor(cur_row, cur_col)}.')
        break

    counter +=1







