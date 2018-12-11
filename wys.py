#!/usr/bin/env python

import sys
from parser import *
from lexer import *

def usage():
    sys.stderr.write('Usage: imp filename\n')
    sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
    filename = sys.argv[1]
    text = open(filename).read()
    tokens = token_lex(text)
    parse_result = wys_parse(tokens)
    if not parse_result:
        sys.stderr.write('Parse error!\n')
        sys.exit(1)
    ast = parse_result.value
    env = {}
    ast.eval(env)

    sys.stdout.write('Final variable values:\n')
    for name in env:
        sys.stdout.write('%s: %s\n' % (name, env[name]))
