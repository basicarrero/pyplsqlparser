import sys
import pandas as pd
from antlr4 import *
from pyPlSqlLexer import pyPlSqlLexer
from pyPlSqlParser import pyPlSqlParser
from pyPlSqlParserListener import pyPlSqlParserListener
from CaseChangingStream import CaseChangingStream


class myListener(pyPlSqlParserListener):

    def __init__(self):
        self.data = {
            'Funcion': [],
            'Argumentos': []
        }

    def getDF(self):
        return pd.DataFrame(self.data)

    def enterFunction_call(self, ctx:pyPlSqlParser.Function_specContext):
        payload = ctx.getPayload()
        funName = payload.children[0].getText()
        funArgs = payload.children[1].getText()[2:-2]
        self.data['Funcion'].append(funName)
        self.data['Argumentos'].append(funArgs)


def getPLSQLparser(input):
    casedInput = CaseChangingStream(input, True)
    lexer = pyPlSqlLexer(casedInput)
    stream = CommonTokenStream(lexer)
    return pyPlSqlParser(stream)


if __name__ == '__main__':
    stream = FileStream(sys.argv[1], encoding='utf-8')
    parser = getPLSQLparser(stream)
    tree = parser.sql_script()
    listener = myListener()
    ParseTreeWalker().walk(listener, tree)

    df = listener.getDF()
    print(df.to_string())
    print('\n============================================================\n')
    df = df.groupby('Funcion', as_index=False).agg({'Argumentos': 'nunique'})
    df.columns = ['Funcion', 'Llamadas']
    print(df.to_string())
