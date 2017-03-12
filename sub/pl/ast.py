# -*- coding: utf-8 -*-

# :'######::'##:::::'##::'######::
# '##... ##: ##:'##: ##:'##... ##:
#  ##:::..:: ##: ##: ##: ##:::..::
# . ######:: ##: ##: ##: ##:::::::
# :..... ##: ##: ##: ##: ##:::::::
# '##::: ##: ##: ##: ##: ##::: ##:
# . ######::. ###. ###::. ######::
# :......::::...::...::::......:::

# Static Web Compiler [swc] The swc is a compiler for static webfiles.
# Copyright (C) 2017 Tobias Reichert

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
The file contains the abstract syntax tree
and a simple upper class for the visitor.
"""


from ..tree import Tree

##
# Oberklasse


class Node(object):

    def welcome(self, visitor):
        return visitor.visit(self)

    def __str__(self):
        result = "["
        for attribute in dir(self):
            if not attribute.startswith("_"):
                result += str(attribute) + ", "
        return self.__class__.__name__ + result + "]"
##


##
# root node


class File_Node(Node):

    def __init__(self, line):
        self.func_list = []
        self.line = line

    def add(self, func):
        self.func_list.append(func)

    def extend(self, funcs):
        self.func_list.extend(funcs)
#


class Function_Node(Node):

    def __init__(self, name, param, body, line):
        self.name = name
        self.param = param
        self.body = body
        self.line = line


class Fun_Param_Node(Node):

    def __init__(self, line):
        self.param_list = []
        self.line = line

    def add(self, param):
        self.param_list.append(param)


class Fun_Pointer(Node):

    def __init__(self, name, line):
        self.name = name
        self.line = line


class Funcall_Param_Node(Node):

    def __init__(self, line):
        self.param_list = []
        self.line = line

    def add(self, param):
        self.param_list.append(param)


class Funcall_Node(Node):

    def __init__(self, name, param, line):
        self.name = name
        self.param = param
        self.line = line


class Body_Node(Node):

    def __init__(self, line):
        self.ex_list = []
        self.line = line

    def add(self, ex):
        self.ex_list.append(ex)


class Return_Node(Node):

    def __init__(self, ex, line):
        self.ex = ex
        self.line = line


class Write_Node(Node):

    def __init__(self, ex, line):
        self.ex = ex
        self.line = line


class Readd_Node(Node):

    def __init__(self, ex, line):
        self.ex = ex
        self.line = line


class Readd_Parse_Node(Node):

    def __init__(self, parser, ex, line):
        self.parser = parser
        self.ex = ex
        self.line = line


class Assign_Node(Node):

    def __init__(self, name, value, line):
        self.name = name
        self.value = value
        self.line = line


class If_Node(Node):

    def __init__(self, bool_ex, body, else_body, line):
        self.bool_ex = bool_ex
        self.body = body
        self.else_body = else_body
        self.line = line


class Foreach_Node(Node):

    def __init__(self, var, var_list, body, line):
        self.var = var
        self.var_list = var_list
        self.body = body
        self.line = line


class No_Operation_Node(Node):

    def __init__(self, line):
        self.line = line
        pass


#
# ex
#


class Bool_Op_Node(Node):

    def __init__(self, first_bool, op, second_bool, line):
        self.first_bool = first_bool
        self.op = op
        self.second_bool = second_bool
        self.line = line


class Op_Ex_Node(Node):

    def __init__(self, first_value, op, second_value, line):
        self.first_value = first_value
        self.op = op
        self.second_value = second_value
        self.line = line

#
# var
#


class Var_Node(Node):

    def __init__(self, name, line):
        self.name = name
        self.line = line


class Array_Node(Node):

    def __init__(self, line):
        self.list = []
        self.line = line

    def add(self, value):
        self.list.append(value)

    def extend(self, value):
        self.list.extend(value)

    def __str__(self):
        result = "["
        first = True
        for node in self.list:
            if not first:
                result += ", "
            result += str(node)
            first = False
        result += "]"
        return result


class Array_get_Node(Node):

    def __init__(self, name, pos, line):
        self.name = name
        self.pos = pos
        self.line = line


class Tree_Node(Node):

    def __init__(self, line):
        self.tree = Tree()
        self.line = line

    def set_tree(self, tree):
        self.tree = tree

    def __setitem__(self, key, value):
        self.tree[key] = value

    def __contains__(self, item):
        return item in self.tree

    def __getitem__(self, key):
        return self.tree[key]


class Tree_get_Node(Node):

    def __init__(self, name, pos, line):
        self.name = name
        self.pos = pos
        self.line = line


class Int_Node(Node):

    def __init__(self, value, line):
        self.value = value
        self.line = line

    def __str__(self):
        return str(self.value)


class Float_Node(Node):

    def __init__(self, value, line):
        self.value = value
        self.line = line

    def __str__(self):
        return str(self.value)


class String_Node(Node):

    def __init__(self, value, line):
        self.value = value.replace(r"\n", "\n").replace(r"\t", "\t")
        self.line = line

    def __str__(self):
        return self.value


class Bool_Node(Node):

    def __init__(self, value, line):
        self.value = value
        self.line = line

    def __str__(self):
        return str(self.value)
