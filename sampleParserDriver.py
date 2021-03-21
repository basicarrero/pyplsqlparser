import sys
from antlr4 import *
from pyPlSqlLexer import pyPlSqlLexer
from pyPlSqlParser import pyPlSqlParser
from pyPlSqlParserVisitor import pyPlSqlParserVisitor
from pyPlSqlParserListener import pyPlSqlParserListener
from CaseChangingStream import CaseChangingStream


class myVisitor(pyPlSqlParserVisitor):
    # TODO: Customice your visitor https://www.antlr.org/api/Java/org/antlr/v4/runtime/tree/ParseTreeVisitor.html
    def __init__(self):
        print('Not implemented yet')


class myListener(pyPlSqlParserListener):
    # TODO: Customice your listener https://github.com/antlr/antlr4/blob/master/doc/listeners.md
    def __init__(self):
        print('Not implemented yet')


def parseSql_script(input):
    casedInput = CaseChangingStream(input, True)
    lexer = pyPlSqlLexer(casedInput)
    stream = CommonTokenStream(lexer)
    parser = pyPlSqlParser(stream)
    return parser.sql_script()


if __name__ == '__main__':
    stream = FileStream(sys.argv[1], encoding='utf-8')
    # stream = InputStream('SELECT * from DUAL')

    tree = parseSql_script(stream)

    listener = myListener()
    ParseTreeWalker().walk(listener, tree)

    visitor = myVisitor()
    ast = visitor.visitSql_script(tree)
    print(repr(ast))
