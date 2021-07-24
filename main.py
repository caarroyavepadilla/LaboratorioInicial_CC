import sys
from antlr4 import *
import antlr4 as antlr4
from decafLexer import decafLexer
from decafListener import decafListener
from decafParser import decafParser
from decafVisitor import decafVisitor
from antlr4.tree.Trees import Trees

class DecafPrintListener(decafListener):
    pass
    # def enterProgram(self, ctx):
    #     print("Decaf: %s" % ctx.ID())

class MyDecafVisitor(decafVisitor):

    def visitProgram(self, ctx):
        print("program")

def main():
    program = open('test.txt', 'r+')
    text = program.read()
    program.close()
    text = antlr4.InputStream(text)
    lexer = decafLexer(text)
    stream = CommonTokenStream(lexer)
    parser = decafParser(stream)
    tree = parser.program()
    printer = DecafPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    print(Trees.toStringTree(tree, None, parser))

if __name__ == '__main__':
    main()