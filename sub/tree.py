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
The file contains a simple tree class for the swc.
"""


class Tree(object):

    def __init__(self, items={}, delimiter="/"):
        self.items = items  # tree with dicts
        self.delimiter = delimiter

    def __setitem__(self, key, value):
        path = key.split(self.delimiter)
        cur_dict = self.items
        for item in path[:-1]:
            if item not in cur_dict:
                cur_dict[item] = {}
            cur_dict = cur_dict[item]
        cur_dict[path[-1]] = value
        # self.items[key] = value

    def __contains__(self, item):
        path = item.split(self.delimiter)
        cur_dict = self.items
        for item in path:
            if item not in cur_dict:
                return False
            cur_dict = cur_dict[item]
        return True

    def __getitem__(self, key):
        if key.endswith(self.delimiter):
            key = key[:-1]
        path = key.split(self.delimiter)
        cur_dict = self.items
        last_dicts = []
        for item in path:
            last_dicts.append(self.items)
            cur_dict = cur_dict[item]
        if isinstance(cur_dict, dict):
            return Tree(items=cur_dict, delimiter=self.delimiter)
        return cur_dict

    def __iter__(self):
        key = self.items.iterkeys()
        return key

    def __str__(self):
        return "Tree: " + str(self.items)


def test():
    t = Tree()
    t["a/b"] = "halo"
    t["a/c"] = "halo 2"
    print t
    print t["a"]
    print "contains: " + str("a/c" in t)
    print "contains: " + str("a/x" in t)

if __name__ == "__main__":
    test()
