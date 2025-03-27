"""
♔ (rey blanco) y ♚ (rey negro)
♕ (reina blanca) y ♛ (reina negra)
♖ (torre blanca) y ♜ (torre negra)
♗ (alfil blanco) y ♝ (alfil negro)
♘ (caballo blanco) y ♞ (caballo negro)
♙ (peón blanco) y ♟ (peón negro)
0 representa una casilla vacía
"""

chess_board = [
    ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'],
    ['♟', '♟', '♟', '♟', '♟', '♟','♟','♟'],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
    ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']
]

print(chess_board)

# Si movemos el caballo blanco '♘' a una de las dos posiciones posibles tenemos:

chess_board[7][1] = 0 # Casilla original del caballo blanco, que ahora estaría vacía.
chess_board[5][2] = '♘' # Nueva posición del caballo blanco.

print(chess_board)