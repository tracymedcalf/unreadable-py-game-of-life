from random import randint

def my_print(w, h, board):
    return game(w, h, [i for c, i in enumerate(board) if print(str(i) + '' if c % (w - 1) else '\n', end = '') or True],
            lambda indices, board : 1 if sum(board[i] for i in indices) > len(indices) // 2 else 0,
            lambda i : [i - w - 1, i - w, i - w + 1, i - 1, i, i + 1, i + w - 1, i + w, i + w + 1],
            lambda indices : [i for i in indices if i > -1 and i < len(board)])

def game(w, h, board, new, indices, san_indices):
    return my_print(w, h, [new(san_indices(indices(i)), board) for i in range(len(board))]) if input('q<enter> to quit ') != 'q' else None

(lambda w, h :my_print(w, h, [randint(0, 1) for i in range(w * h)]))(int(input('width? ')), int(input('height? ')))
