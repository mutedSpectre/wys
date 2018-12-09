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

def precedence(value_parser, precedence_levels, combine):
    def op_parser(precedence_level):
        return any_operator_in_list(precedence_level) ^ combine
    parser = value_parser * op_parser(precedence_levels[0])
    for precedence_level in precedence_levels[1:]:
        parser = parser * op_parser(precedence_level)
    return parser

def aexp():
    return precedence(aexp_term(),
                      aexp_precedence_levels,
                      process_binop)

def process_relop(parsed):
    ((left, op), right) = parsed
    return RelopBexp(op, left, right)

def bexp_relop():
    relops = ['<', '<=', '>', '>=', '=', '!=']
    return aexp() + any_operator_in_list(relops) + aexp() ^ process_relop

def bexp_not():
    return keyword('not') + Lazy(bexp_term) ^ (lambda parsed: NotBexp(parsed[1]))

def bexp_group():
    return keyword('(') + Lazy(bexp) + keyword(')') ^ process_group

def bexp_term():
    return bexp_not()    | \
           bexp_relop()  | \
           bexp_group()

bexp_precedence_levels = [
    ['and'],
    ['or'],
]

def process_logic(op):
    if op == 'and':
        return lambda 1, r: AndBexp(1, r)
    elif op == 'or':
        return lambda 1, r: OrBexp(1, r)
    else:
        raise RuntimeError('unknown logic operator: ', + op)

def bexp():
    return precedence(bexp_term(),
                      bexp_precedence_levels,
                      process_logic)