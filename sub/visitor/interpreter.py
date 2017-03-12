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
The file contains the interpreter.
"""


import traceback
import logging as log
import collections
import importlib

from ..pl import ast as AST
from ..tree import Tree


class Interpreter_Error(Exception):

    def __init__(self, err_msg):
        self.err_msg = err_msg

    def __str__(self):
        return "Interpreter_Error: " + repr(self.err_msg)


class Pass_Ex(Exception):
    """
    Passes the Exeption to the main class
    """

    def __init__(self):
        pass


class Inter(object):  # (Visitor)

    def __init__(self, **kwargs):
        if "debug" in kwargs:
            self.debug = kwargs["debug"]
        else:
            self.debug = False

        if "file_location" in kwargs:
            self.file_location = kwargs["file_location"]
            if self.file_location.endswith("/"):
                self.file_location = self.file_location[:-1]
        if "webfile" in kwargs:
            webfile = kwargs["webfile"]
            self.main_func = webfile.main_func
            self.local_func = webfile.local_func
        elif ("main_func" in kwargs) and ("local_func" in kwargs):
            self.main_func = kwargs["main_func"]
            self.local_func = kwargs["local_func"]
            if ("file_func" in kwargs) and ("file_info_tree" in kwargs):
                self.file_func = kwargs["file_func"]
                self.file_info_tree = kwargs["file_info_tree"]

        else:
            raise Interpreter_Error("not enough params for Interpreter")
        self.local_var = {}
        self.return_value = None
        self.write_in_file = ""
        self.break_func = False

    def start_main(self):
        param = AST.Funcall_Param_Node(None)
        # funcall for input file entry
        param.add(self.file_func)
        param.add(self.file_info_tree)
        # funcall for main
        fc = AST.Funcall_Node("main", param, None)
        fc.welcome(self)
        return self.write_in_file
###############

    def visit_file(self, node):
        raise Interpreter_Error("Unexpected file node")

    def visit_func(self, node):
        if node.name not in self.local_func:
            raise Interpreter_Error("Unexpected func node")
        # node.param.welcome(self)
        node.body.welcome(self)
        return self.return_value

    def visit_fun_param(self, node):
        result = []
        for var in node.param_list:
            result.append(var)
        return result

    def visit_funcall_param(self, node):
        result = []
        for ex in node.param_list:
            if isinstance(ex, AST.Function_Node):
                result.append(ex)
            else:
                result.append(ex.welcome(self))

        return result

    def visit_funcall(self, node):
        fun = self.local_func.get(node.name)
        if not fun:
            raise Interpreter_Error("No function called: " + node.name)
        fun_params = fun.param.welcome(self)
        funcall_params = node.param.welcome(self)
        if not len(fun_params) == len(funcall_params):
            raise Interpreter_Error(
                "wrong count of params for function:/n" + node.name)

        # new inter for func
        new = Inter(local_func=self.local_func,
                    main_func=self.main_func, debug=self.debug,
                    file_location=self.file_location)
        for name, var in zip(fun_params, funcall_params):
            # if fun_params = Fun_pointer put fun in func
            if isinstance(name, AST.Fun_Pointer):
                new.local_func[name.name] = var
            else:
                new.local_var[name] = var
        fun.body.welcome(new)
        self.write_in_file += new.write_in_file
        return new.return_value

    def visit_body(self, node):
        for ex in node.ex_list:
            ex.welcome(self)
            if self.break_func:
                break

    def visit_return(self, node):
        self.return_value = node.ex.welcome(self)
        self.break_func = True

    def visit_write(self, node):
        self.write_in_file += str(node.ex.welcome(self))

    def readd(self, text):
        if self.return_value is None:
            self.return_value = ""
        elif not isinstance(self.return_value, basestring):
            raise Interpreter_Error("Return Value already taken")
        self.return_value += str(text) #.encode('utf-8').strip()

    def visit_readd(self, node):
        self.readd(node.ex.welcome(self))

    def visit_readd_parse(self, node):
        text = str(node.ex.welcome(self))
        if node.parser == "md":
            parser = "sub.parser.markdown"
        else:
            parser = "sub.parser." + node.parser
        my_module = importlib.import_module(parser)
        self.readd(my_module.parse(text))

    def visit_assign(self, node):
        self.local_var[node.name.name] = node.value.welcome(self)

    def visit_if(self, node):
        if node.bool_ex.welcome(self):  # is True:
            node.body.welcome(self)
        elif node.else_body is not None:
            node.else_body.welcome(self)

    def visit_foreach(self, node):
        # iterable = self.local_var[node.var_list.name]
        iterable = node.var_list.welcome(self)

        if not isinstance(iterable, collections.Iterable):
            raise Interpreter_Error(node.var_list.name
                                    + " not iterable. Type: "
                                    + str(type(iterable)))
        for var in iterable:
            self.local_var[node.var.name] = var
            node.body.welcome(self)

    def visit_no_operation(self, node):
        pass
#
# ex
#

    def visit_boolop(self, node):
        a = node.first_bool.welcome(self)
        b = node.second_bool.welcome(self)
        if a is None:
            raise Interpreter_Error("First op None None: " + str(node))
        if b is None:
            raise Interpreter_Error("Second op None None: " + str(node))

        if node.op == "==":
            return a == b
        elif node.op == "!=":
            return not a == b
        elif node.op == "<=":
            return a <= b
        elif node.op == ">=":
            return a >= b
        elif node.op == "<":
            return a < b
        elif node.op == ">":
            return a > b
        elif node.op == "||":
            return a or b
        elif node.op == "&&":
            return a and b
        else:
            raise NotImplementedError(node.op)

    def visit_opex(self, node):
        a = node.first_value.welcome(self)
        b = node.second_value.welcome(self)
        if a is None:
            raise Interpreter_Error("First op None None: " + str(node))
        if b is None:
            raise Interpreter_Error("Second op None None: " + str(node))

        if isinstance(a, basestring) or isinstance(b, basestring):
            a = str(a)
            b = str(b)

        if node.op == "+":
            return a + b
        elif node.op == "-":
            return a - b
        elif node.op == "*":
            return a * b
        elif node.op == "/":
            return a / b
        elif node.op == "%":
            return a % b
        elif node.op == "<<":
            return a << b
        elif node.op == ">>":
            return a >> b
        elif node.op == "|":
            return a | b
        elif node.op == "&":
            return a & b
        elif node.op == "^":
            return a ^ b
        else:
            raise NotImplementedError(node.op)

#
# var
#

    def visit_var(self, node):
        if node.name in self.local_var:
            return self.local_var[node.name]
        else:
            raise Interpreter_Error("'" + node.name + "' is not a Var")

    def visit_array(self, node):
        return node.list

    def visit_array_get(self, node):
        if node.name in self.local_var:
            var = self.local_var[node.name]
            if not isinstance(var, list):
                raise Interpreter_Error("'" + node.name + "' is not a List")
            return var[node.pos]
        else:
            raise Interpreter_Error("'" + node.name + "' is not a Var")

    def visit_tree(self, node):
        return node.tree

    def visit_tree_get(self, node):
        if node.name in self.local_var:
            var = self.local_var[node.name]
            if not isinstance(var, Tree):
                raise Interpreter_Error("'" + node.name + "' is not a Tree")

            pos = node.pos.welcome(self)
            if pos.startswith("./"):
                pos = pos.replace(".", self.file_location)
            return var[pos]  # TODO .. ./
        else:
            raise Interpreter_Error("'" + node.name + "' is not a Var")

    def visit_int(self, node):
        return node.value

    def visit_float(self, node):
        return node.value

    def visit_string(self, node):
        return node.value

    def visit_bool(self, node):
        return node.value


###############

    def visit(self, node):
        try:
            if isinstance(node, AST.File_Node):
                return self.visit_file(node)
            elif isinstance(node, AST.Function_Node):
                return self.visit_func(node)
            elif isinstance(node, AST.Fun_Param_Node):
                return self.visit_fun_param(node)
            elif isinstance(node, AST.Funcall_Param_Node):
                return self.visit_funcall_param(node)
            elif isinstance(node, AST.Funcall_Node):
                return self.visit_funcall(node)
            elif isinstance(node, AST.Body_Node):
                return self.visit_body(node)
            elif isinstance(node, AST.Return_Node):
                return self.visit_return(node)
            elif isinstance(node, AST.Write_Node):
                return self.visit_write(node)
            elif isinstance(node, AST.Readd_Node):
                return self.visit_readd(node)
            elif isinstance(node, AST.Readd_Parse_Node):
                return self.visit_readd_parse(node)
            elif isinstance(node, AST.Assign_Node):
                return self.visit_assign(node)
            elif isinstance(node, AST.If_Node):
                return self.visit_if(node)
            elif isinstance(node, AST.Foreach_Node):
                return self.visit_foreach(node)
            elif isinstance(node, AST.No_Operation_Node):
                return self.visit_no_operation(node)
    # ex
            elif isinstance(node, AST.Bool_Op_Node):
                return self.visit_boolop(node)
            elif isinstance(node, AST.Op_Ex_Node):
                return self.visit_opex(node)
    # var
            elif isinstance(node, AST.Var_Node):
                return self.visit_var(node)
            elif isinstance(node, AST.Array_Node):
                return self.visit_array(node)
            elif isinstance(node, AST.Array_get_Node):
                return self.visit_array_get(node)
            elif isinstance(node, AST.Tree_Node):
                return self.visit_tree(node)
            elif isinstance(node, AST.Tree_get_Node):
                return self.visit_tree_get(node)
            elif isinstance(node, AST.Int_Node):
                return self.visit_int(node)
            elif isinstance(node, AST.Float_Node):
                return self.visit_float(node)
            elif isinstance(node, AST.String_Node):
                return self.visit_string(node)
            elif isinstance(node, AST.Bool_Node):
                return self.visit_bool(node)

            else:
                raise NotImplementedError(str(node))

        except Pass_Ex:
            log.critical("\tOn line: " + str(node.line) + " On Node: " +
                         str(type(node).__name__))
            raise Pass_Ex()

        except Exception as e:
            if self.debug:
                traceback.print_exc()
            log.critical("Unexpected error: " + str(e)
                         + "\nOn Node: " + str(type(node).__name__)
                         + "\n\tOn line: " + str(node.line))
            raise Pass_Ex()
