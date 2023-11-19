#%%
import chess
import chess.svg
from random import choice
from chess import Board, Move, PIECE_TYPES
import traceback
from flask import Flask, Response, request
import chess.pgn
import chess.engine
import time
import chess.polyglot
import subprocess
import pandas as pd
import webbrowser


class ChessAI():

    PV = {
        'pawn': 100,
        'knight': 320,
        'bishop': 330,
        'rook': 500,
        'queen': 950
    }

    DRAW_VALUE = 0
    
    def __init__(self, depth):
        self.depth = depth
        self.board = Board()
        self.legal_moves_san = [self.board.san(move) for move in self.board.legal_moves]

    @staticmethod
    def evaluate_board(board):
        scoring = {
            'p': -1,
            'n': -3,
            'b': -3,
            'r': -5,
            'q': -9,
            'k': 0,
            'P': 1,
            'N': 3,
            'B': 3,
            'R': 5,
            'Q': 9,
            'K': 0,
            }
        if board.is_checkmate():
            return float('-inf') if board.turn else float('inf')
        pieces = board.piece_map()
        score = sum(scoring[str(pieces[key])] for key in pieces)
        return score

    def ai_move(self, use_opening_book = False):
        start_time = time.time()
        reader = chess.polyglot.open_reader('baron30.bin')
        opening_move = reader.get(self.board)
        best_move = None
        if opening_move is not None:
            best_move = opening_move.move
            best_move = self.board.san(best_move)
            
        if best_move is None:
            df = ChessAI.minimax_root(self.board, self.depth, is_maximizing = self.board.turn)
            best_move = df.loc[0, 'move']
            print(df)
        print(f'best_move {best_move}')
        self.board.push_san(best_move)

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Time taken for the move: {elapsed_time} seconds")

    @staticmethod
    def minimax_root(board, depth, is_maximizing):
        moves_san = [str(board.san(move)) for move in board.legal_moves]
        df = pd.DataFrame(columns = ['move', 'score'])
        best_score = float('-inf')
        # print('swaggy moves:', moves_san)
        for move in moves_san:
            board.push_san(move)
            # print(f'swag_move: {move}')
            alpha = -1000
            beta = 1000
            final_score = ChessAI.minimax(board, depth, alpha, beta, is_maximizing)
            # print(f'final_score: {final_score}')
            board.pop()
            df.loc[len(df.index)] = [move, final_score]
            df = df.sort_values(by = 'score', ascending=False)
            if final_score > best_score:
                best_score = final_score
        df = df.sort_values(by = ['score', 'move'], ascending=False).reset_index(drop=True)
        df.to_csv(f'moves_{depth}.csv', index = False)
        return df

    @staticmethod
    def minimax(board, depth, alpha, beta, is_maximizing):
        if depth == 0 or board.is_game_over():
            return -ChessAI.evaluate_board(board)

        moves_san = [str(board.san(move)) for move in board.legal_moves]
        scores = []

        for move in moves_san:
            board.push_san(move)
            score = ChessAI.minimax(board, depth - 1, alpha, beta, not is_maximizing)
            scores.append(score)
            board.pop()
            if is_maximizing:
                alpha = max(alpha, score)
            else:
                beta = min(beta, score)
            if beta <= alpha:
                break
        if is_maximizing:
            return max(scores)
        else:
            return min(scores)

    def run_gui(self):
        app = Flask(__name__)
        @app.route("/")
        def main():
            ret = '<html><head>'
            ret += '<style>input {font-size: 20px; } button { font-size: 20px; }</style>'
            ret += '</head><body>'
            ret += '<img width=510 height=510 src="/board.svg?%f"></img></br></br>' % time.time()
            ret += '<form action="/new_game/" method="post"><button name="New Game" type="submit">New Game</button></form>'
            ret += '<form action="/undo/" method="post"><button name="Undo" type="submit">Undo Last Move</button></form>'
            # ret += '<form action="/move/"><input type="submit" value="Make Human Move:"><input name="move" type="text"></input></form>'
            ret += '<form action="/human_and_ai_move/"><input type="submit" value="human and ai move:"><input name="human_and_ai_move" type="text"></input></form>'
            # ret += '<form action="/dev/" method="post"><button name="ai move" type="submit">Make Ai Move</button></form>'
            # ret += '<form action="/engine/" method="post"><button name="Stockfish Move" type="submit">Make Stockfish Move</button></form>'
            return ret
        @app.route("/board.svg/")
        def board():
            return Response(chess.svg.board(board=self.board, size=700), mimetype='image/svg+xml')
        @app.route("/move/")
        def move():
            try:
                move = request.args.get('move', default="")
                board.push_san(move)
            except Exception:
                traceback.print_exc()
            return main()
        @app.route("/human_and_ai_move/")
        def human_and_ai_move():
            try:
                move = request.args.get('human_and_ai_move', default="")
                self.board.push_san(move)
                if move != "":
                    self.ai_move()
            except Exception:
                traceback.print_exc()
            result = self.board.result()
            print(result)
            return main()
        @app.route("/dev/", methods=['POST'])
        def dev():
            try:
                self.ai_move()
            except Exception:
                traceback.print_exc()
            return main()
        @app.route("/new_game/", methods=['POST'])
        def new_game():
            self.board.reset()
            return main()

        @app.route("/undo/", methods=['POST'])
        def undo():
            try:
                self.board.pop()
            except Exception:
                traceback.print_exc()
            return main()
        
        webbrowser.open('http://example.com')
        app.run()

chess_ai = ChessAI(depth = 3)
chess_ai.run_gui()




#%%

chess_ai.board.push_san('e4')
chess_ai.ai_move()
chess_ai.board

chess_ai.board.push_san('Nf3')
chess_ai.ai_move()
chess_ai.board

chess_ai.board.push_san('exd5')
chess_ai.ai_move()
chess_ai.board

chess_ai.board.push_san('d4')
chess_ai.ai_move()
chess_ai.board

chess_ai.board.push_san('c3')
chess_ai.ai_move()
chess_ai.board

chess_ai.board.push_san('h3')
chess_ai.ai_move()
chess_ai.board

# chess_ai.board.push_san('Be2')
# chess_ai.ai_move(use_opening_book = True)
# chess_ai.board

#%%

chess_ai.board.push_san('Be2')
chess_ai.ai_move(use_opening_book = True)
chess_ai.board


#%%

chess_ai.board.push_san('Re1')
chess_ai.ai_move(use_opening_book = False)
chess_ai.board

#%%

chess_ai.board.push_san('Nc3')
chess_ai.ai_move(use_opening_book = False)
chess_ai.board

#%%
chess_ai.board.push_san('Be2')
chess_ai.ai_move(use_opening_book = False)
chess_ai.board



#%%
swag_moves = ['Nf3', 'd4', 'h3', 'Bd3', 'd5', 'e5', 'e6']

for swag_move in swag_moves:
    chess_ai.board.push_san(swag_move)
    chess_ai.ai_move(use_opening_book = True)
    chess_ai.board


#%%
chess_ai.board.push_san('Nf3')
chess_ai.ai_move()
chess_ai.board
#%%
chess_ai.board.push_san('d4')
chess_ai.ai_move()
chess_ai.board
#%%
chess_ai.board.push_san('h3')
chess_ai.ai_move()
chess_ai.board
#%%
chess_ai.board.push_san('Bd3')
chess_ai.ai_move()
chess_ai.board
#%%
chess_ai.board.push_san('d5')
chess_ai.ai_move()
chess_ai.board
#%%
chess_ai.board.push_san('e5')
chess_ai.ai_move()
chess_ai.board
#%%
chess_ai.board.push_san('e6')
chess_ai.ai_move()
chess_ai.board
#%%
chess_ai.board.push_san('exd7')
chess_ai.ai_move()
chess_ai.board
#%%
chess_ai.board.push_san('Ne5')
chess_ai.ai_move()
chess_ai.board
#%%
chess_ai.board.push_san('Qf3')
chess_ai.ai_move()
chess_ai.board
#%%
chess_ai.board.push_san('Bxh6')
chess_ai.ai_move()
chess_ai.board
#%%
chess_ai.board.push_san('Bf4')
chess_ai.ai_move()
chess_ai.board
#%%
chess_ai.board.push_san('Bf4')
chess_ai.ai_move()
chess_ai.board
#%%
chess_ai.board.push_san('Nd2')
chess_ai.ai_move()
chess_ai.board
#%%
chess_ai.board.push_san('O-O')
chess_ai.ai_move()
chess_ai.board
#%%
chess_ai.board.push_san('O-O')
chess_ai.ai_move()
chess_ai.board
#%%
chess_ai.board.push_san('Rab1')
chess_ai.ai_move()
chess_ai.board
#%%
chess_ai.board.push_san('Bb5')
chess_ai.ai_move()
chess_ai.board
#%%
chess_ai.board.push_san('Bc4')
chess_ai.ai_move()
chess_ai.board
# chess_ai.board.push_san('Nf3')

# chess_ai.ai_move()


#################################################################################

# Searching Stockfish's Move    
# def stockfish():
#     engine = chess.engine.SimpleEngine.popen_uci(
#         "your_path/stockfish.exe")
#     move = engine.play(board, chess.engine.Limit(time=0.1))



#%%
