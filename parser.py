#!/usr/bin/python

import sys
import ast


class Transformer(ast.NodeTransformer):
    pass


def main():
    tree = ast.parse(open(sys.argv[0]).read())

    for node in Transformer().visit(tree).body:
        print node

if __name__ == '__main__':
    main()
