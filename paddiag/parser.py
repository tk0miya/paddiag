#!/usr/bin/python

import sys
import ast
from itertools import izip_longest


class Transformer(ast.NodeTransformer):
    symbols = {
        ast.And: 'and',
        ast.Or: 'or',
        ast.Add: '+',
        ast.Sub: '-',
        ast.Mult: '*',
        ast.Div: '/',
        ast.Mod: '%',
        ast.Pow: '**',
        ast.LShift: '<<',
        ast.RShift: '>>',
        ast.BitOr: '|',
        ast.BitXor: '^',
        ast.BitAnd: '&',
        ast.FloorDiv: '//',
        ast.Eq: '==',
        ast.NotEq: '!=',
        ast.Lt: '<',
        ast.LtE: '<=',
        ast.Gt: '>',
        ast.GtE: '>=',
        ast.Is: 'is',
        ast.IsNot: 'is not',
        ast.In: 'in',
        ast.NotIn: 'not in',
        ast.Invert: '~',
        ast.Not: 'not',
        ast.UAdd: '+',
        ast.USub: '-',
        ast.Pass: 'pass',
        ast.Break: 'break',
        ast.Continue: 'continue',
        ast.Ellipsis: '...',
    }

    # Module(stmt* body)
    # Interactive(stmt* body)
    # Expression(expr body)

    # Suite(stmt* body)

    # FunctionDef(identifier name, arguments args,
    #             stmt* body, expr* decorator_list)

    # ClassDef(identifier name, expr* bases, stmt* body, expr *decorator_list)

    # Return(expr? value)
    def visit_Return(self, node):
        self.generic_visit(node)
        return ["return %s" % join(node.value)]

    # Delete(expr* targets)
    def visit_Delete(self, node):
        self.generic_visit(node)
        return ["del %s" % join(node.targets)]

    # Assign(expr* targets, expr value)
    def visit_Assign(self, node):
        self.generic_visit(node)
        return ["%s = %s" % (join(node.targets), join(node.value))]

    # AugAssign(expr target, operator op, expr value)
    def visit_AugAssign(self, node):
        self.generic_visit(node)
        return ["%s %s= %s" % (join(node.target), join(node.op), join(node.value))]

    # Print(expr? dest, expr* values, bool nl)
    def visit_Print(self, node):
        self.generic_visit(node)
        return ["print %s" % join(node.values)]

    # For(expr target, expr iter, stmt* body, stmt* orelse)

    # While(expr test, stmt* body, stmt* orelse)

    # If(expr test, stmt* body, stmt* orelse)

    # With(expr context_expr, expr? optional_vars, stmt* body)

    # Raise(expr? type, expr? inst, expr? tback)
    def visit_Raise(self, node):
        self.generic_visit(node)
        args = filter(None, [join(node.type), join(node.inst), join(node.tback)])
        return ["raise %s" % join(args)]

    # TryExcept(stmt* body, excepthandler* handlers, stmt* orelse)

    # TryFinally(stmt* body, stmt* finalbody)

    # Assert(expr test, expr? msg)
    def visit_Assert(self, node):
        self.generic_visit(node)
        args = filter(None, [join(node.test), join(node.msg)])
        return ["assert %s" % join(args)]

    # Import(alias* names)
    def visit_Import(self, node):
        self.generic_visit(node)
        return ["import %s" % join(node.names)]

    # ImportFrom(identifier module, alias* names, int? level)
    def visit_ImportFrom(self, node):
        self.generic_visit(node)
        return ["from %s import %s" % (node.module, join(node.names))]

    # Exec(expr body, expr? globals, expr? locals)
    def visit_Exec(self, node):
        self.generic_visit(node)
        return ["exec(%s)" % join(node.body)]

    # Global(identifier* names)
    def visit_Global(self, node):
        self.generic_visit(node)
        return ["global %s" % join(node.names)]

    # Expr(expr value)
    def visit_Expr(self, node):
        self.generic_visit(node)
        return node.value

    # BoolOp(boolop op, expr* values)
    def visit_BoolOp(self, node):
        self.generic_visit(node)
        return ["%s %s %s" % (node.values[0], join(node.op), node.values[1])]

    # BinOp(expr left, operator op, expr right)
    def visit_BinOp(self, node):
        self.generic_visit(node)
        return ["%s %s %s" % (join(node.left), join(node.op), join(node.right))]

    # UnaryOp(unaryop op, expr operand)
    def visit_UnaryOp(self, node):
        self.generic_visit(node)
        return ["%s %s" % (join(node.op), join(node.operand))]

    # Lambda(arguments args, expr body)
    def visit_Lambda(self, node):
        self.generic_visit(node)
        return ["lambda %s: %s" % (join(node.args), join(node.body))]

    # IfExp(expr test, expr body, expr orelse)
    def visit_IfExp(self, node):
        self.generic_visit(node)
        return ast.If(node.test, node.body, node.orelse)

    # Dict(expr* keys, expr* values)
    def visit_Dict(self, node):
        self.generic_visit(node)
        args = ("%s: %s" % (key, value) for key, value
                in zip(node.keys, node.values))
        return ["{%s}" % join(args)]

    # ListComp(expr elt, comprehension* generators)
    def visit_ListComp(self, node):
        self.generic_visit(node)
        args = (join(node.elt),
                " ".join("for %s" % gen for gen in node.generators))
        return ["[%s %s]" % args]

    # GeneratorExp(expr elt, comprehension* generators)
    def visit_GeneratorExp(self, node):
        self.generic_visit(node)
        args = (join(node.elt),
                " ".join("for %s" % gen for gen in node.generators))
        return ["(%s %s)" % args]

    # Yield(expr? value)
    def visit_Yield(self, node):
        self.generic_visit(node)
        if node.value:
            return ["yield %s" % join(node.value)]
        else:
            return ["yield"]

    # Compare(expr left, cmpop* ops, expr* comparators)
    def visit_Compare(self, node):
        self.generic_visit(node)
        args = ("%s %s" % pair for pair in zip(node.ops, node.comparators))
        return ["%s %s" % (join(node.left), " ".join(args))]

    # Call(expr func, expr* args, keyword* keywords,
    #      expr? starargs, expr? kwargs)
    def visit_Call(self, node):
        self.generic_visit(node)
        args = (node.args + node.keywords)
        if node.starargs:
            args.append("*%s" % join(node.starargs))
        if node.kwargs:
            args.append("**%s" % join(node.kwargs))

        return ["%s(%s)" % (join(node.func), join(args))]

    # Repr(expr value)

    # Num(object n) -- a number as a PyObject.
    def visit_Num(self, node):
        return [repr(node.n)]

    # Str(string s) -- need to specify raw, unicode, etc?
    def visit_Str(self, node):
        return [repr(node.s)]

    # Attribute(expr value, identifier attr, expr_context ctx)
    def visit_Attribute(self, node):
        self.generic_visit(node)
        return ["%s.%s" % (join(node.value), node.attr)]

    # Subscript(expr value, slice slice, expr_context ctx)
    def visit_Subscript(self, node):
        self.generic_visit(node)
        return ["%s[%s]" % (join(node.value), join(node.slice))]

    # Name(identifier id, expr_context ctx)
    def visit_Name(self, node):
        return [node.id]

    # List(expr* elts, expr_context ctx)
    def visit_List(self, node):
        self.generic_visit(node)
        return ["[%s]" % join(node.elts)]

    # Tuple(expr* elts, expr_context ctx)
    def visit_Tuple(self, node):
        self.generic_visit(node)
        if len(node.elts) == 1:
            return ["(%s,)" % join(node.elts)]
        else:
            return ["(%s)" % join(node.elts)]

    # Slice(expr? lower, expr? upper, expr? step)
    def visit_Slice(self, node):
        self.generic_visit(node)
        if node.step:
            return ["%s:%s:%s" % (join(node.lower) or '',
                                  join(node.upper) or '',
                                  join(node.step) or '')]
        elif node.upper:
            return ["%s:%s" % (join(node.lower) or '',
                               join(node.upper) or '')]
        else:
            return [join(node.lower)]

    # ExtSlice(slice* dims)
    def visit_ExtSlice(self, node):
        self.generic_visit(node)
        return [join(node.dims)]

    # Index(expr value)
    def visit_Index(self, node):
        self.generic_visit(node)
        return [join(node.value)]

    # comprehension = (expr target, expr iter, expr* ifs)
    def visit_comprehension(self, node):
        self.generic_visit(node)
        if node.ifs:
            args = (join(node.target), join(node.iter),
                    " ".join("if %s" % cond for cond in node.ifs))
            return ["%s in %s %s" % args]
        else:
            args = (join(node.target), join(node.iter))
            return ["%s in %s" % args]

    # excepthandler = ExceptHandler(expr? type, expr? name, stmt* body)

    # arguments = (expr* args, identifier? vararg,
    #              identifier? kwarg, expr* defaults)
    def visit_arguments(self, node):
        def to_arg(name, default):
            if default is None:
                return name
            else:
                return "%s=%s" % (name, default)

        self.generic_visit(node)
        args = node.args
        rargs = [to_arg(arg, default) for arg, default in izip_longest(reversed(node.args), node.defaults)]

        args = list(reversed(rargs))
        if node.vararg:
            args.append("*%s" % node.vararg)
        if node.kwarg:
            args.append("**%s" % node.kwarg)

        return [join(args)]

    # keyword = (identifier arg, expr value)
    def visit_keyword(self, node):
        self.generic_visit(node)
        return ["%s=%s" % (node.arg, join(node.value))]

    # alias = (identifier name, identifier? asname)
    def visit_alias(self, node):
        self.generic_visit(node)
        if node.asname:
            return ["%s as %s" % (node.name, node.asname)]
        else:
            return [node.name]

    def visit(self, node):
        if node.__class__ in self.symbols:
            return [self.symbols[node.__class__]]
        else:
            return super(Transformer, self).visit(node)


def parse(text):
    tree = ast.parse(text)
    return Transformer().visit(tree)


def join(node):
    if node is None:
        return None
    else:
        return ", ".join(node)


def main():
    tree = parse(open(sys.argv[0]).read())

    for node in tree:
        print node

if __name__ == '__main__':
    main()
