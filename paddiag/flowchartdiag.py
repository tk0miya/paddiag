#!/usr/bin/python

import sys
import ast
from uuid import uuid1
from parser import parse
from tempfile import NamedTemporaryFile
from blockdiag.command import BlockdiagApp


def write_node(fd, label, previous_node_id=[], shape='box', edge_label=''):
    node_id = uuid1()
    fd.write('  %s [shape="%s", label="%s"]\n' % (node_id, shape, label))
    for _ in previous_node_id:
        fd.write('  %s -> %s [label="%s"]\n' % (_, node_id, edge_label))

    return [node_id]


def write_if(fd, stmt, previous_node_id=[], edge_label=''):
    if_node_id = write_node(fd, "".join(stmt.test), previous_node_id, shape='diamond', edge_label=edge_label)
    last_node_id = write_stmt(fd, stmt.body, if_node_id, edge_label='Yes')
    last_node_id += write_stmt(fd, stmt.orelse, if_node_id, edge_label='No')
    return last_node_id


def write_while(fd, stmt, previous_node_id=[], edge_label=''):
    while_node_id = write_node(fd, "".join(stmt.test), previous_node_id, shape='diamond', edge_label=edge_label)
    last_node_id = write_stmt(fd, stmt.body, while_node_id)
    for _ in last_node_id:
        fd.write('  %s -> %s\n' % (_, while_node_id[0]))
    return while_node_id


def write_for(fd, stmt, previous_node_id=[], edge_label=''):
    label = "for %s in %s" % ("".join(stmt.target), "".join(stmt.iter))
    loopin_node_id = write_node(fd, label, previous_node_id, shape='flowchart.loopin', edge_label=edge_label)
    last_node_id = write_stmt(fd, stmt.body, loopin_node_id)
    loopout_node_id = write_node(fd, "next", last_node_id, shape='flowchart.loopout')
    return loopout_node_id


def write_stmt(fd, statements, previous_node_id=[], edge_label=''):
    for i, stmt in enumerate(statements):
        if i > 0:
            edge_label = ''

        if isinstance(stmt, str):
            previous_node_id = write_node(fd, stmt, previous_node_id, edge_label=edge_label)
        elif isinstance(stmt, ast.If):
            previous_node_id = write_if(fd, stmt, previous_node_id, edge_label=edge_label)
        elif isinstance(stmt, ast.While):
            previous_node_id = write_while(fd, stmt, previous_node_id, edge_label=edge_label)
        elif isinstance(stmt, ast.For):
            previous_node_id = write_for(fd, stmt, previous_node_id, edge_label=edge_label)

    return previous_node_id


def main():
    tree = parse(open(sys.argv[1]).read())
    tmpfile = NamedTemporaryFile(dir='.', delete=False)
    tmpfile.write("{\n")
    tmpfile.write("  orientation = portrait\n")
    tmpfile.write("  edge_layout = flowchart\n")
    tmpfile.write("  node_width = 256\n")

    write_stmt(tmpfile, tree.body)

    tmpfile.write("}\n")
    tmpfile.close()

    args = [tmpfile.name, '--no-transparency']
    BlockdiagApp().run(args)


if __name__ == '__main__':
    main()
