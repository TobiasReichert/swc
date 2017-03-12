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
The file contains the ply parser.
"""


import logging as log

import ply.yacc as yacc
import ast as AST


class MyParser(object):

    ##
    # Precedence and associativity of operators
    ##
    precedence = (
        ('left', 'LOR'),
        ('left', 'LAND'),
        ('left', 'OR'),
        ('left', 'XOR'),
        ('left', 'AND'),
        ('left', 'EQ', 'NE'),
        ('left', 'GT', 'GE', 'LT', 'LE'),
        ('left', 'RSHIFT', 'LSHIFT'),
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE', 'MOD')
    )

    ##
    # starting symbol
    ##
    start = 'file'

    ##
    # root node / start symbol for file
    # body: wrap function
    ##
    def p_file(self, p):  # start symbol
        """file : functions
                | body"""
        p[0] = AST.File_Node(p.lineno(1))
        if isinstance(p[1], AST.Body_Node):  # body: wrap function
            p[0].add(AST.Function_Node(
                "entry", AST.Fun_Param_Node(p.lineno(1)), p[1], p.lineno(1)))
        else:
            p[0].extend(p[1])

    ##
    # returns a list of functions
    ##
    def p_functions(self, p):
        """functions : function
                     | functions function"""
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1]
            p[0].append(p[2])

    def p_funcall(self, p):
        """funcall : ID LPAREN funcall_params RPAREN"""
        result = AST.Funcall_Node(p[1], p[3], p.lineno(1))
        p[0] = result

    def p_funcall_params(self, p):  # [list]
        """funcall_params : empty
                          | expression
                          | funcall_params COMMA expression"""
        if len(p) == 4:  # params COMMA var
            p[0] = p[1].add(p[3])
            p[0] = p[1]
        elif p[1] is None:  # empty
            p[0] = AST.Funcall_Param_Node(p.lineno(1))
        else:  # var
            p[0] = AST.Funcall_Param_Node(p.lineno(1))
            p[0].add(p[1])

    def p_function(self, p):
        """function : DEF ID LPAREN fun_params RPAREN LBRACE body RBRACE"""
        p[0] = AST.Function_Node(p[2], p[4], p[7], p.lineno(1))

    def p_fun_params(self, p):  # [list]
        """fun_params : empty
                      | ID
                      | fun_pointer
                      | fun_params COMMA fun_pointer
                      | fun_params COMMA ID"""
        if len(p) == 4:  # params COMMA var
            p[0] = p[1].add(p[3])
            p[0] = p[1]
        elif p[1] is None:  # empty
            p[0] = AST.Fun_Param_Node(p.lineno(1))
        else:  # var
            p[0] = AST.Fun_Param_Node(p.lineno(1))
            p[0].add(p[1])

    def p_fun_pointer(self, p):
        """fun_pointer : ID LPAREN RPAREN"""
        p[0] = AST.Fun_Pointer(p[1], p.lineno(1))

    def p_body(self, p):  # semi in ex
        """body : ex
                | body ex"""
        if len(p) == 3:  # body ex
            p[0] = p[1]
            p[0].add(p[2])
        elif p[1] is None:  # empty
            p[0] = AST.Body_Node(p.lineno(1))
        else:  # ex
            p[0] = AST.Body_Node(p.lineno(1))
            p[0].add(p[1])

    def p_ex(self, p):  # a =
        """ex : assign SEMI
              | return SEMI
              | write SEMI
              | readd SEMI
              | funcall SEMI
              | readd_esc SEMI
              | nop SEMI
              | if
              | foreach
              | readd_esc"""
        # if -> no semi
        p[0] = p[1]

    def p_nop(self, p):
        """nop : NOP"""
        p[0] = AST.No_Operation_Node(p.lineno(1))

    def p_if(self, p):
        """if : IF LPAREN expression RPAREN LBRACE body RBRACE
              | IF LPAREN expression RPAREN LBRACE body RBRACE ELSE if
              | IF LPAREN expression RPAREN LBRACE body RBRACE ELSE LBRACE body RBRACE"""
        if len(p) == 8:
            else_body = None
        elif len(p) == 10:
            else_body = p[9]
        else:
            else_body = p[10]
        p[0] = AST.If_Node(p[3], p[6], else_body, p.lineno(1))

    def p_foreach(self, p):
        """foreach : FOR LPAREN var COLON value RPAREN LBRACE body RBRACE"""
        p[0] = AST.Foreach_Node(p[3], p[5], p[8], p.lineno(1))

    def p_return(self, p):
        """return : RETURN expression"""
        p[0] = AST.Return_Node(p[2], p.lineno(1))

    def p_write(self, p):
        """write : WRITE expression"""
        p[0] = AST.Write_Node(p[2], p.lineno(1))

    def p_readd(self, p):
        """readd : READD expression"""
        p[0] = AST.Readd_Node(p[2], p.lineno(1))

    def p_readd_esc(self, p):
        """readd_esc :  LT string GT"""
        p[0] = AST.Readd_Node(p[2], p.lineno(1))

    def p_readd_esc_parse(self, p):
        """readd_esc :  LT ID string GT"""
        p[0] = AST.Readd_Parse_Node(p[2], p[3], p.lineno(1))

    def p_assign(self, p):
        """assign : var EQUALS expression"""
        p[0] = AST.Assign_Node(p[1], p[3], p.lineno(1))

#
# ex
#

    def p_expression(self, p):
        """expression : value
                      | bool_ex
                      | op_ex"""
        p[0] = p[1]

    def p_bool_ex(self, p):
        """bool_ex : bool_value EQ bool_value
                   | bool_value NE bool_value
                   | bool_value LE bool_value
                   | bool_value GE bool_value
                   | bool_value LT bool_value
                   | bool_value GT bool_value
                   | bool_value LOR bool_value
                   | bool_value LAND bool_value"""
        p[0] = AST.Bool_Op_Node(p[1], p[2], p[3], p.lineno(1))

    def p_bool_ex_2(self, p):
        """bool_ex : LNOT bool_value
                   | LPAREN bool_ex RPAREN"""
        if len(p) == 3:
            p[0] = AST.Bool_Op_Node(p[2], p[1], None, p.lineno(1))
        else:
            p[0] = p[2]

    def p_bool_value(self, p):
        """bool_value : value
                                  | op_ex"""
        p[0] = p[1]

    def p_op_ex(self, p):
        """op_ex : value PLUS value
                 | value MINUS value
                 | value TIMES value
                 | value DIVIDE value
                 | value MOD value
                 | value LSHIFT value
                 | value RSHIFT value
                 | value OR value
                 | value AND value
                 | value XOR value

                 | value PLUS op_ex
                 | value MINUS op_ex
                 | value TIMES op_ex
                 | value DIVIDE op_ex
                 | value MOD op_ex
                 | value LSHIFT op_ex
                 | value RSHIFT op_ex
                 | value OR op_ex
                 | value AND op_ex
                 | value XOR op_ex"""
        p[0] = AST.Op_Ex_Node(p[1], p[2], p[3], p.lineno(1))

    def p_op_ex_2(self, p):
        """op_ex : LPAREN op_ex RPAREN"""
        p[0] = p[2]

#
# var / value
#
    def p_value(self, p):
        """value : var
                 | int
                 | float
                 | string
                 | bool
                 | funcall
                 | list
                 | array_get
                 | tree_get"""

        p[0] = p[1]

    def p_int(self, p):
        """int : INT"""
        p[0] = AST.Int_Node(p[1], p.lineno(1))

    def p_float(self, p):
        """float : FLOAT"""
        p[0] = AST.Float_Node(p[1], p.lineno(1))

    def p_string(self, p):
        """string : STRING"""
        p[0] = AST.String_Node(p[1][1:-1], p.lineno(1))

    def p_multi_string(self, p):
        """string : MULTI_STRING"""
        p[0] = AST.String_Node(p[1][3:-3], p.lineno(1))

    def p_bool_true(self, p):
        """bool : TRUE"""
        p[0] = AST.Bool_Node(True, p.lineno(1))

    def p_bool_false(self, p):
        """bool : FALSE"""
        p[0] = AST.Bool_Node(False, p.lineno(1))

    def p_list(self, p):
        """list : LBRACKET array RBRACKET"""
        p[0] = AST.Array_Node(p.lineno(1))
        p[0].extend(p[2])

    def p_array(self, p):
        """array : value
                 | array COMMA value"""
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1]
            p[0].append(p[3])

    def p_array_get(self, p):
        """array_get : ID LBRACKET INT RBRACKET"""
        p[0] = AST.Array_get_Node(p[1], p[3], p.lineno(1))

    def p_tree_get(self, p):
        """tree_get : ID LBRACKET string RBRACKET"""
        p[0] = AST.Tree_get_Node(p[1], p[3], p.lineno(1))

    def p_var(self, p):
        """var : ID"""
        p[0] = AST.Var_Node(p[1], p.lineno(1))

    def p_empty(self, p):
        """empty :"""
        p[0] = None

    def p_error(self, token):
        self.error = True
        if token is not None:
            log.critical("Line %s, illegal token %s" %
                         (token.lineno, token.value))
            log.critical(self.input.split("\n")[token.lineno - 1])
        else:
            log.critical('Unexpected end of input')

    def set_line(self, node, line):
        node.line = line
        """self.set_line(p[0],p.lineno(1))"""

    def __init__(self, lexer, tokens, errors=False):
        self.lexer = lexer
        self.tokens = tokens
        if errors:
            self.parser = yacc.yacc(module=self)
        else:
            self.parser = yacc.yacc(module=self, errorlog=yacc.NullLogger())
        self.error = False

    def parse(self, text):
        self.input = text
        result = self.parser.parse(text, lexer=self.lexer)
        if not self.error:
            return result
        else:
            return None
