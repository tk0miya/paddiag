#!bin/py

import os
import sys
import ast
from parser import parse
from blockdiag.imagedraw.svg import SVGImageDraw
from blockdiag.utils import Box, XY
from blockdiag.utils.fontmap import FontMap


PAGE_MARGIN = 32
NODE_WIDTH = 240
NODE_HEIGHT = 48
SPAN_WIDTH = 40
SPAN_HEIGHT = 24


def p(x, y):
    return XY(int(PAGE_MARGIN + NODE_WIDTH * x + SPAN_WIDTH * x),
              int(PAGE_MARGIN + NODE_HEIGHT * y + SPAN_HEIGHT * y))


def box(x, y, width=1, height=1):
    x, y = p(x, y)
    return Box(x, y,
               x + NODE_WIDTH * width + SPAN_WIDTH * (width - 1),
               y + NODE_HEIGHT * height + SPAN_HEIGHT * (height - 1))


class PADImageDraw(SVGImageDraw):
    def __init__(self, *args, **kwargs):
        super(PADImageDraw, self).__init__(*args, **kwargs)
        self.fontmap = FontMap()
        self.fontmap.set_default_font('/Library/Fonts/Hiragino Sans GB W3.otf')
        self.font = self.fontmap.find()

    def if_block(self, x, y, stmt):
        width, height = self.statement(x + 1, y, stmt.body)

        textbox = box(x, y, height=height + 0.25).shift(y=NODE_HEIGHT / 3)
        shape = (textbox.topleft, textbox.topright, textbox.right.shift(x=-32),
                 textbox.bottomright, textbox.bottomleft, textbox.topleft)
        self.line(shape, fill='black')
        self.textarea(textbox, "".join(stmt.test), self.font, fill='black')
        self.link(x, textbox.top.y)

        if stmt.orelse == []:
            height += 1
        else:
            w, h = self.statement(x + 1, y + height, stmt.orelse)
            width = max(width, w)
            height += h
            self.link(x, textbox.bottom.y)

        return (width + 1, height)

    def while_block(self, x, y, stmt):
        textbox = box(x, y)
        self.rectangle(textbox, outline='black', fill='white')
        self.textarea(textbox, "".join(stmt.test), self.font, fill='black')
        self.line((textbox.topleft.shift(x=12), textbox.bottomleft.shift(x=12)), fill='black')
        self.link(x, textbox.right.y)

        width, height = self.statement(x + 1, y, stmt.body)
        return (width + 1, height)

    def for_block(self, x, y, stmt):
        textbox = box(x, y)
        label = "for %s in %s" % ("".join(stmt.target), "".join(stmt.iter))
        self.rectangle(textbox, outline='black', fill='white')
        self.textarea(textbox, label, self.font, fill='black')
        self.line((textbox.topleft.shift(x=12), textbox.bottomleft.shift(x=12)), fill='black')
        self.link(x, textbox.right.y)

        width, height = self.statement(x + 1, y, stmt.body)
        return (width + 1, height)

    def render(self, tree):
        return self.statement(0, 0, tree.body)

    def statement(self, x, y, statements):
        height = 0
        width = 0
        for stmt in statements:
            if isinstance(stmt, str):
                w, h = self.process(x, y + height, stmt)
            elif isinstance(stmt, ast.If):
                w, h = self.if_block(x, y + height, stmt)
            elif isinstance(stmt, ast.While):
                w, h = self.while_block(x, y + height, stmt)
            elif isinstance(stmt, ast.For):
                w, h = self.for_block(x, y + height, stmt)
            else:
                w, h = (0, 0)

            height += h
            width = max(width, w)

        self.baseline(x, y, height)

        return (width, height)

    def process(self, x, y, text):
        textbox = box(x, y)
        self.rectangle(textbox, outline='black', fill='white')
        self.textarea(textbox, text, self.font, fill='black')

        return (1, 1)

    def baseline(self, x, y, height):
        start = box(x, y).shift(y=-SPAN_HEIGHT / 3)
        end = box(x, y + height - 1).shift(y=SPAN_HEIGHT / 3)
        self.line((start.topleft, end.bottomleft), fill='black')

    def link(self, x, py):
        start = XY(box(x, 0).right.x, py)
        end = XY(box(x + 1, 0).left.x, py)
        self.line((start, end), fill='black')


def main():
    tree = parse(open(sys.argv[1]).read())

    path = os.path.splitext(sys.argv[1])[0] + '.svg'
    drawer = PADImageDraw(path)
    width, height = drawer.render(tree)

    # reset canvas
    diagram = box(0, 0, width=width, height=height)
    drawer.set_canvas_size(diagram.bottomright.shift(PAGE_MARGIN, PAGE_MARGIN))
    drawer.render(tree)
    drawer.save(None, None, 'SVG')


if __name__ == '__main__':
    main()
