import lexer

RESERVED = 'RESERVED'
INT      = 'INT'
ID       = 'ID'

tokens_list = [
    (r'\=', RESERVED),
    (r'\+', RESERVED),
    (r'\-', RESERVED),
    (r'[0-9]+',   INT),
]

def token_lex(characters):
    return lexer.lex(characters, tokens_list)