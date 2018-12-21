import unittest
import wys_parser
import lex_tokens
import wys_ast


class ParserStatementTests(unittest.TestCase):
    def parser_test(self, code, parser, expected):
        tokens = lex_tokens.token_lex(code)
        result = parser(tokens, 0)
        self.assertNotEqual(None, result)
        self.assertEqual(expected, result.value)

    def test_assign_stmt(self):
        self.parser_test('x = 1', wys_parser.stmt_list(), wys_ast.AssignStatement('x', wys_parser.IntAexp(1)))

    def test_print_stmt(self):
        self.parser_test('print x', wys_parser.stmt_list(), wys_ast.PrintStatement('x'))

    def test_input_stmt(self):
        self.parser_test('input x', wys_parser.stmt_list(), wys_ast.InputStatement('x'))
