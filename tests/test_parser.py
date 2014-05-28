#!/usr/bin/python

import ast
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
    def test_Return(self):
        source = "return 1"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

    # Delete(expr* targets)
    def test_Delete(self):
        source = "del var"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

    # Assign(expr* targets, expr value)
    def test_Assign(self):
        source = "var = 1"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

    # AugAssign(expr target, operator op, expr value)
    def test_AugAssign(self):
        source = "var += 1"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        source = "var -= 1"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

    # Print(expr? dest, expr* values, bool nl)
    def test_Print(self):
        source = "print 1"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

    # For(expr target, expr iter, stmt* body, stmt* orelse)

    # While(expr test, stmt* body, stmt* orelse)

    # If(expr test, stmt* body, stmt* orelse)

    # With(expr context_expr, expr? optional_vars, stmt* body)

    # Raise(expr? type, expr? inst, expr? tback)
    def test_Raise(self):
        source = "raise Exception"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        source = "raise Exception, 'message'"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        source = "raise Exception, 'message', tback"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

    # TryExcept(stmt* body, excepthandler* handlers, stmt* orelse)

    # TryFinally(stmt* body, stmt* finalbody)

    # Assert(expr test, expr? msg)
    def test_Assert(self):
        source = "assert 1 == 1"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        source = "assert 1 == 1, 'ok'"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

    # Import(alias* names)
    def test_Import(self):
        source = "import sys"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        source = "import sys as var"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

    # ImportFrom(identifier module, alias* names, int? level)
    def test_ImportFrom(self):
        source = "from sys import path"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        source = "from sys import path as var"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

    # Exec(expr body, expr? globals, expr? locals)
    def test_Exec(self):
        source = "exec('1')"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

    # Global(identifier* names)
    def test_Global(self):
        source = "global var"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

    # Expr(expr value)
    def test_Expr(self):
        source = "1"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

    # Pass
    def test_Pass(self):
        source = "pass"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

    # Break
    def test_Break(self):
        source = "break"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

    # Continue
    def test_Continue(self):
        source = "continue"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

    # BoolOp(boolop op, expr* values)
    def test_BoolOp(self):
        source = "var and var or var"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

    # BinOp(expr left, operator op, expr right)
    def test_BinOp(self):
        # Add
        source = "1 + 1"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        # Sub
        source = "1 - 1"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        # Mult
        source = "1 * 1"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        # Div
        source = "1 / 1"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        # Mod
        source = "1 % 1"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        # Pow
        source = "1 ** 1"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        # LShift
        source = "1 << 1"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        # RShift
        source = "1 >> 1"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        # BitOr
        source = "1 | 1"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        # BitXor
        source = "1 ^ 1"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        # BitAnd
        source = "1 & 1"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        # FloorDiv
        source = "1 // 1"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

    # UnaryOp(unaryop op, expr operand)
    def test_UnaryOp(self):
        # Invert
        source = "~ var"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        # Not
        source = "not var"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        # UAdd
        source = "+ var"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        # USub
        source = "- var"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

    # Lambda(arguments args, expr body)
    def test_Lambda(self):
        source = "lambda x, y: x + y"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        source = "lambda x, y, *args, **kwargs: x + y"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        source = "lambda x, y=1, *args, **kwargs: x + y"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

    # IfExp(expr test, expr body, expr orelse)
    def test_IfExp(self):
        source = "1 if 2 else 3"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertIsInstance(ret.body[0], ast.If)
        self.assertEqual(ret.body[0].test, ["2"])
        self.assertEqual(ret.body[0].body, ["1"])
        self.assertEqual(ret.body[0].orelse, ["3"])

    # Dict(expr* keys, expr* values)
    def test_Dict(self):
        source = "{1: 2, '3': 4}"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

    # ListComp(expr elt, comprehension* generators)
    def test_ListComp(self):
        source = "[elem * 2 for elem in var]"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        source = "[elem * 2 for elem in var if cond]"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        source = "[elem * 2 for elem in var if cond if cond]"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        source = "[elem * 2 for elem in var for elem2 in var2]"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        source = "[elem * 2 for elem in var if cond for elem2 in var2 if cond]"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

    # GeneratorExp(expr elt, comprehension* generators)
    def test_GeneratorExp(self):
        source = "(elem * 2 for elem in var)"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

    # Yield(expr? value)
    def test_Yield(self):
        source = "yield"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        source = "yield 1"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

    # Compare(expr left, cmpop* ops, expr* comparators)
    def test_Compare(self):
        # Eq
        source = "1 == 1"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        # Eq (str)
        source = "name == 'Jiro'"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        # NotEq
        source = "1 != 1"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        # Lt
        source = "1 < 1"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        # LtE
        source = "1 <= 1"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        # Gt
        source = "1 > 1"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        # GtE
        source = "1 >= 1"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        # Is
        source = "1 is 1"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        # IsNot
        source = "1 is not 1"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        # In
        source = "1 in 1"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        # NotIn
        source = "1 not in 1"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

    # Call(expr func, expr* args, keyword* keywords,
    #      expr? starargs, expr? kwargs)
    def test_Call(self):
        source = "foo(1, 2)"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        source = "foo(1, 2, var1=3, var2=4, *args, **kwargs)"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

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
        # str
        source = "'Hello world'"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        # unicode
        source = "u'Hello world'"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

    # Attribute(expr value, identifier attr, expr_context ctx)
    def test_Attribute(self):
        source = "var.attr"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

    # Subscript(expr value, slice slice, expr_context ctx)
    def test_Subscript(self):
        # Ellipsis
        source = "var[...]"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        # Slice
        source = "var[1:2:3]"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        source = "var[1]"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        source = "var[:2]"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        source = "var[::3]"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        # ExtSlice
        source = "var[:2, :2]"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

        # Index
        source = "var[1]"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

    # Name(identifier id, expr_context ctx)
    def test_Name(self):
        source = "var1"
        ret = parse(source)
        self.assertEqual(len(ret.body), 1)
        self.assertEqual(ret.body[0], source)

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

    # excepthandler = ExceptHandler(expr? type, expr? name, stmt* body)


if __name__ == '__main__':
    unittest.main()
