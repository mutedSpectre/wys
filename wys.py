#!/usr/bin/env python

import sys
import os
from wys_parser import *
from lex_tokens import *

def usage():
    sys.stderr.write('Usage: wys filename\n')
    sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()

    filename, file_extension = os.path.splitext(sys.argv[1])   #Extension check
    if file_extension != '.wys':
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
    prnt = {}
    if ast != 'print':
        ast.eval(env)
    else:
        ast.prnt(env, prnt)

    sys.stdout.write('Final variable values:\n')
    for name in prnt:
        sys.stdout.write('%s: %s\n' % (name, prnt[name]))
