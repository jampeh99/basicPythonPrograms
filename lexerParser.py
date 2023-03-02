import ply.lex as lex
import ply.yacc as yacc

# Define tokens
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
)

# Define regular expressions for each token
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Define a regular expression for integers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule to track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Define a rule to ignore whitespace
t_ignore = ' \t'

# Define a rule to handle errors
def t_error(t):
    print(f"Invalid character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)

# Create the lexer
lexer = lex.lex()


# Parser

# Define grammar rules
def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_multiply(p):
    'term : term MULTIPLY factor'
    p[0] = p[1] * p[3]

def p_term_divide(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_number(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_paren(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

# Define a rule to handle syntax errors
def p_error(p):
    if p:
        print(f"Syntax error at token {p.type} ({p.value}) on line {p.lineno}")
    else:
        print("Syntax error at end of input")

# Create the parser
parser = yacc.yacc()


# Parsing input for the parser and lexer
input_expr = "2 * (3 + 4)"

# Tokenize the input expression
lexer.input(input_expr)
for tok in lexer:
    print(tok)

# Parse the input expression
result = parser.parse(input_expr)
print(result)