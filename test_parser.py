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

    def test_if_stmt(self):
        code = 'if 1 < 2 then x = 3 else x = 4 end'
        expected = wys_ast.IfStatement(wys_ast.RelopBexp('<', wys_ast.IntAexp(1), wys_ast.IntAexp(2)),
                                       wys_ast.AssignStatement('x', wys_ast.IntAexp(3)),
                                       wys_ast.AssignStatement('x', wys_ast.IntAexp(4)))
        self.parser_test(code, wys_parser.stmt_list(), expected)

    def test_while_stmt(self):
        code = 'while l < 2 { x = 3 }'
        expected = wys_ast.WhileStatement(wys_ast.RelopBexp('<', wys_ast.IntAexp(1), wys_ast.IntAexp(2)),
                                          wys_ast.AssignStatement('x', wys_ast.IntAexp(3)))
        self.parser_test(code, wys_parser.stmt_list(), expected)
