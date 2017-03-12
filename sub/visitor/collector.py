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
The file contains the collector.
It collects the first assignments
and save the values and keys in a dict.
"""


import sys

from ..pl import ast as AST


class Collect(object):  # (Visitor)

    def __init__(self, is_main):
        self.is_main = is_main  # bool
        self.main_func = None  # type: Node
        self.local_func = {}
        self.file_info = {}

###############

    def visit_file(self, node):
        for func in node.func_list:
            self.local_func[func.name] = func
            if self.is_main:
                if func.name == "main":
                    self.main_func = func
            else:
                if func.name == "entry":
                    self.main_func = func
        if self.main_func:
            self.main_func.welcome(self)
        else:
            print("Error: no main in file")
            sys.exit(-1)

    def visit_func(self, node):
        node.body.welcome(self)

    def visit_body(self, node):
        for ex in node.ex_list:
            if isinstance(ex, AST.Assign_Node):
                ex.welcome(self)
            else:
                break

    def visit_assign(self, node):
        if isinstance(node.value, AST.Int_Node) \
                or isinstance(node.value, AST.Float_Node) \
                or isinstance(node.value, AST.String_Node) \
                or isinstance(node.value, AST.Bool_Node):
            self.file_info[node.name.name] = node.value.welcome(self)

    def visit_int(self, node):
        return node.value

    def visit_float(self, node):
        return node.value

    def visit_string(self, node):
        return node.value

    def visit_bool(self, node):
        return node.value

###

    def visit(self, node):
        if isinstance(node, AST.File_Node):
            return self.visit_file(node)
        elif isinstance(node, AST.Function_Node):
            return self.visit_func(node)
        elif isinstance(node, AST.Body_Node):
            return self.visit_body(node)

        elif isinstance(node, AST.Assign_Node):
            return self.visit_assign(node)
# var
        elif isinstance(node, AST.Int_Node):
            return self.visit_int(node)
        elif isinstance(node, AST.Float_Node):
            return self.visit_float(node)
        elif isinstance(node, AST.String_Node):
            return self.visit_string(node)
        elif isinstance(node, AST.Bool_Node):
            return self.visit_bool(node)

        else:
            return None
