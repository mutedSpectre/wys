import unittest
import wys_parser
import lex_tokens

class ParserStatementTests(unittest.TestCase):
    def parser_test(self, code, parser, expected):
        tokens = lex_tokens.token_lex(code)
        result = parser(tokens, 0)
        self.assertNotEquals(None, result)
        self.assertEquals(expected, result.value)
