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
The file contains the ply lexer.
"""


import logging as log
import ply.lex as lex


class MyLexer(object):
    reserved = {
        "return": "RETURN",
        "def": "DEF",
        "if": "IF",
        "else": "ELSE",

        "for": "FOR",

        "true": "TRUE",
        "false": "FALSE",

        "readd": "READD",
        "write": "WRITE",

        # No Operation
        "nop": "NOP"
    }

    tokens = [
        # IDentifier, String, Multiline String("""), Int, float,
        'ID', 'STRING', 'MULTI_STRING', 'INT', 'FLOAT',
        # Operators (+,-,*,/,%,|,&,~,^,<<,>>, ||, &&, !, <, <=, >, >=, ==,
        # !=)
        'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD',
        'OR', 'AND', 'XOR', 'LSHIFT', 'RSHIFT',
        'LOR', 'LAND', 'LNOT',
        'LT', 'LE', 'GT', 'GE', 'EQ', 'NE',

        # Assignment
        'EQUALS',

        # Delimeters ( ) [ ] { } , . ; :
        'LPAREN', 'RPAREN',
        'LBRACKET', 'RBRACKET',
        'LBRACE', 'RBRACE',
        'COMMA',  'SEMI', 'COLON',  # 'PERIOD',
    ] + list(reserved.values())

    ##
    # Tokens

    # Operators
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_MOD = r'%'
    t_OR = r'\|'
    t_AND = r'&'
    t_XOR = r'\^'
    t_LSHIFT = r'<<'
    t_RSHIFT = r'>>'
    t_LOR = r'\|\|'
    t_LAND = r'&&'
    t_LNOT = r'!'
    t_LT = r'<'
    t_GT = r'>'
    t_LE = r'<='
    t_GE = r'>='
    t_EQ = r'=='
    t_NE = r'!='

    # Assignment operators
    t_EQUALS = r'='

    # Delimeters
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_LBRACKET = r'\['
    t_RBRACKET = r'\]'
    t_LBRACE = r'\{'
    t_RBRACE = r'\}'
    t_COMMA = r','
    # t_PERIOD = r'\.'
    t_SEMI = r';'
    t_COLON = r':'

    # Completely ignored characters
    t_ignore = ' \t\x0c'

    # Newlines
    def t_NEWLINE(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # Floating literal
    def t_FLOAT(self, t):
        r'((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?'
        t.value = float(t.value)
        return t

    # Integer literal
    def t_INT(self, t):
        r'\d+([uU]|[lL]|[uU][lL]|[lL][uU])?'
        # r'\d+'
        t.value = int(t.value)
        return t

    def t_ID(self, t):
        r'[A-Za-z_][\w_.]*'
        t.type = self.reserved.get(t.value, "ID")  # 2.Paam if not exist
        return t

    # String literal
    # t_STRING = r'\"([^\\\n]|(\\.))*?\"'
    def t_MULTI_STRING(self, t):
        r'\"\"\"(.|\n)*?\"\"\"'
        t.lexer.lineno += t.value.count('\n')
        return t

    def t_STRING(self, t):
        r'\"(.|\n)*?\"'
        t.lexer.lineno += t.value.count('\n')
        return t

    # Comments
    def t_COMMENT(self, t):
        r'/\*(.|\n)*?\*/'
        t.lexer.lineno += t.value.count('\n')

    # def t_MARKDOWN(self, t):

    def t_error(self, t):
        log.critical("Illegal character %s" % repr(t.value[0]))
        t.lexer.skip(1)

    def __init__(self, **kwargs):
        self.build(**kwargs)

    def build(self, **kwargs):
        self.lexer = lex.lex(object=self, **kwargs)

    def input(self, text):
        self.lexer.input(text)

    def token(self):
        self.last_token = self.lexer.token()
        return self.last_token

    # Only for testing
    def test(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok)
