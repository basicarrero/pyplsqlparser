import sys
from antlr4 import *
from pyPlSqlLexer import pyPlSqlLexer
from pyPlSqlParser import pyPlSqlParser
from pyPlSqlParserListener import pyPlSqlParserListener
from CaseChangingStream import CaseChangingStream


class myListener(pyPlSqlParserListener):
    def enterFunction_call(self, ctx:pyPlSqlParser.Function_specContext):
        print('Llamada a función reconocida:\n\t', ctx.getText())


def getPLSQLparser(input):
    casedInput = CaseChangingStream(input, True)
    lexer = pyPlSqlLexer(casedInput)
    stream = CommonTokenStream(lexer)
    return pyPlSqlParser(stream)


if __name__ == '__main__':
    stream = FileStream(sys.argv[1], encoding='utf-8')
    parser = getPLSQLparser(stream)
    tree = parser.sql_script()
    ParseTreeWalker().walk(myListener(), tree)
