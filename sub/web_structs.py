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
The file contains two container-classes for the swc.
"""


import os


class Webdomain(object):

    def __init__(self):
        self.file_infos = None
        self.input_files = []  # files in input folder
        self.main_file = None


class Webfile(object):

    def __init__(self, file_path):
        self.file_path = os.path.splitext(file_path)[0]  # cuts the extention
        self.code = open(file_path, "r").read()
        self.main_func = None  # type: Node
        self.local_func = {}
        self.file_info = {}
        self.output = ""
