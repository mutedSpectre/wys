import unittest
import wys_parser
import lex_tokens
import wys_ast

class ParserStatementTests(unittest.TestCase):
    def parser_test(self, code, parser, expected):
        tokens = lex_tokens.token_lex(code)
        result = parser(tokens, 0)
        self.assertNotEquals(None, result)
        self.assertEquals(expected, result.value)

    def test_assign_stmt(self):
        self.parser_test('x = 1', wys_parser.stmt_list(), wys_ast.AssignStatement('x', wys_parser.IntAexp(1)))
