import ply.lex as lex

frase_exemplo = """select ?nome ?desc where {
?s a dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en .
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000"""


tokens = (
    "LEFT_P",
    "RIGHT_P",
    "VARIABLE",
    "VALUE",
    "URI",
    "PUNCTUATION",
    "KEYWORD"
)


t_RIGHT_P = r"\}"
t_LEFT_P = r"\{"
t_VARIABLE = r"\?\w+"
t_VALUE = r"\d+|\"[^\"]*\"(?:@\w+)?"
t_URI = r"\w+:[\w\d]+"
t_PUNCTUATION = r"\."
t_KEYWORD = r"\w+"

t_ignore = " \t" #não é uma regex

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)
    

def t_error(t) :
    print(f"símbolo inválido na linha {t.lineno}: {t.value[0]}")

    t.lexer.skip(1)
    pass

lexer = lex.lex()

lexer.input(frase_exemplo)

while(r:= lexer.token()):
    print(r)