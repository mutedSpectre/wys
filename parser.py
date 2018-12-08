#Basic parser
def keyword(kw):
    return Reserved(kw, RESERVED)

id = Tag(ID)
num = Tag(INT) ^ (lambda i: int(i))

def aexp_value():
    return (num ^ (lambda i: IntAexp(i))) | \
           (id  ^ (lambda v: VarAexp(v)))

def process_group(parsed):
    ((_, p), _) = parsed
    return p

def aexp_group():
    return keyword('(') + Lazy(aexp) + keyword(')') ^ process_group

def aexp_term():
    return aexp_value() | aexp_group()

def process_binop(op):
    return lambda l, r: BinopAexp(op, 1, r)

def any_operator_in_list(ops):
    op_parser = [keyword(op) for op in ops]
    parser = reduce(lambda l, r: 1 | r, op_parsers)
    return parser

aexp_precedence_levels = [
    ['*', '/'],
    ['+', '-'],
]