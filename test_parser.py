#!/usr/bin/python

import unittest
from parser import parse


class TransformerTestCase(unittest.TestCase):
    # Module(stmt* body)
    # Interactive(stmt* body)
    # Expression(expr body)

    # Suite(stmt* body)

    # FunctionDef(identifier name, arguments args,
    #             stmt* body, expr* decorator_list)

    # ClassDef(identifier name, expr* bases, stmt* body, expr *decorator_list)

    # Return(expr? value)

    # Delete(expr* targets)

    # Assign(expr* targets, expr value)

    # AugAssign(expr target, operator op, expr value)

    # Print(expr? dest, expr* values, bool nl)

    # For(expr target, expr iter, stmt* body, stmt* orelse)

    # While(expr test, stmt* body, stmt* orelse)

    # If(expr test, stmt* body, stmt* orelse)

    # With(expr context_expr, expr? optional_vars, stmt* body)

    # Raise(expr? type, expr? inst, expr? tback)

    # TryExcept(stmt* body, excepthandler* handlers, stmt* orelse)

    # TryFinally(stmt* body, stmt* finalbody)

    # Assert(expr test, expr? msg)

    # Import(alias* names)

    # ImportFrom(identifier module, alias* names, int? level)

    # Exec(expr body, expr? globals, expr? locals)

    # Global(identifier* names)

    # Expr(expr value)
    def test_Expr(self):
        source = "1"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

    # Pass

    # Break

    # Continue

    # BoolOp(boolop op, expr* values)

    # BinOp(expr left, operator op, expr right)

    # UnaryOp(unaryop op, expr operand)

    # Lambda(arguments args, expr body)

    # IfExp(expr test, expr body, expr orelse)

    # Dict(expr* keys, expr* values)
    def test_Dict(self):
        source = "{1: 2, '3': 4}"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

    # ListComp(expr elt, comprehension* generators)

    # GeneratorExp(expr elt, comprehension* generators)

    # Yield(expr? value)

    # Compare(expr left, cmpop* ops, expr* comparators)

    # Call(expr func, expr* args, keyword* keywords,
    #      expr? starargs, expr? kwargs)

    # Repr(expr value)

    # Num(object n) -- a number as a PyObject.
    def test_Num(self):
        source = "1"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        source = "1.1"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

    # Str(string s) -- need to specify raw, unicode, etc?
    def test_Str(self):
        source = "'Hello world'"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

    # Attribute(expr value, identifier attr, expr_context ctx)

    # Subscript(expr value, slice slice, expr_context ctx)

    # Name(identifier id, expr_context ctx)

    # List(expr* elts, expr_context ctx)
    def test_List(self):
        source = "[1, 2, '3']"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

    # Tuple(expr* elts, expr_context ctx)
    def test_Tuple(self):
        source = "(1, 2, '3')"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        source = "(1,)"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

    # Load

    # Store

    # Del

    # AugLoad

    # AugStore

    # Param

    # Ellipsis

    # Slice(expr? lower, expr? upper, expr? step)

    # ExtSlice(slice* dims)

    # Index(expr value)

    # And | Or

    # Add | Sub | Mult | Div | Mod | Pow | LShift
    #   | RShift | BitOr | BitXor | BitAnd | FloorDiv

    # Invert | Not | UAdd | USub

    # Eq | NotEq | Lt | LtE | Gt | GtE | Is | IsNot | In | NotIn

    # comprehension = (expr target, expr iter, expr* ifs)

    # excepthandler = ExceptHandler(expr? type, expr? name, stmt* body)

    # arguments = (expr* args, identifier? vararg,
    #              identifier? kwarg, expr* defaults)

    # keyword = (identifier arg, expr value)

    # alias = (identifier name, identifier? asname)


if __name__ == '__main__':
    unittest.main()
