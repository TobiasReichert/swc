#!/usr/bin/python2
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
This is the main file for the swc
"""


import os
import sys
import argparse
import gc  # Garbage Collector
from shutil import copyfile
import logging as log

from sub.web_structs import Webdomain, Webfile
from sub.tree import Tree
from sub.visitor.collector import Collect
import sub.pl.lexer as Lex
import sub.pl.parser as Pars
import sub.pl.ast as AST
from sub.visitor.interpreter import Inter, Pass_Ex


def is_swc_dir(path):
    """
    checks if the given path has a "www"-folder and a "main.swc"-file in it
    """
    www_path = os.path.join(path, "www")
    main_file = os.path.join(path, "main.swc")
    return os.path.isdir(path) \
        and os.path.isdir(www_path) \
        and os.path.isfile(main_file)


def walk_through_dir(dir, ex_list, filelist):
    """
    collect all files in the given directory that
    have an extention in the ex_listand.
    mirror the dir in the given mirror_dir.
    """
    for root, subdirs, files in os.walk(dir):
        for file in files:
            file = os.path.join(root, file)
            ex = os.path.splitext(file)[1]
            if len(ex_list) == 0 or ex in ex_list:
                filelist.append(os.path.abspath(file))


def copy_folder_without(dir_src, dir_dst, ex_list = []):
    """
    Copy the src folder into the dst folder without the exlist files
    If the dest folder not exist it will create it
    """
    if not os.path.exists(dir_dst):
        os.makedirs(dir_dst)
    for root, subdirs, files in os.walk(dir_src):
        for folder in subdirs:
            # create each path in "in" in "out", too.
            dirpath = os.path.join(root, folder)
            rel_path = os.path.relpath(dirpath, dir_src)
            dirpath = os.path.join(dir_dst, rel_path)
            if not os.path.exists(dirpath):
                os.makedirs(dirpath)
        for file in files:
            ex = os.path.splitext(file)[1]
            if ex not in ex_list:
                file_src = os.path.join(root, file)
                rel_path = os.path.relpath(file_src, dir_src)
                file_dst = os.path.join(dir_dst, rel_path)
                copyfile(file_src, file_dst)


def parse_collect_webfile(webfile, is_main, verbose):
    """
    This function parses the text in to ast and
    collects the meta information
    """
    lex = Lex.MyLexer()
    parser = Pars.MyParser(lex, lex.tokens, errors=verbose)
    tree = parser.parse(webfile.code)
    if tree is None:
        log.critical("Error")
        sys.exit(-1)

    col = Collect(is_main)
    tree.welcome(col)
    webfile.main_func = col.main_func
    webfile.local_func = col.local_func
    webfile.file_info = col.file_info
    webfile.code = None  # for gc


def inter_web_domain(webdomain, debug, file_info, project_path):
    """
    This function interprets one .swc-file in the www-folder
    with the main file
    """
    for webfile in webdomain.input_files:
        log.info(">" + str(webfile.file_path))
        # join localfunc with mainfile funcs
        func = dict(webfile.local_func)
        func.update(webdomain.main_file.local_func)
        # make a AST tree with the file info
        file_info_tree = AST.Tree_Node(0)
        file_info_tree.set_tree(file_info)
        # make the rel_path for file_location
        rel_path = os.path.relpath(webfile.file_path,
                                   os.path.join(project_path, "www"))
        # Interprete
        inter = Inter(main_func=webdomain.main_file,
                      local_func=func,
                      file_func=webfile.main_func,
                      file_info_tree=file_info_tree,
                      debug=debug,
                      file_location=rel_path)
        # Save the output to write
        try:
            webfile.output = inter.start_main()
        except Pass_Ex:
            log.critical("In File: " + webfile.file_path)
            sys.exit(-1)

        webfile.local_func = None  # for gc
        webfile.main_func = None  # for gc


def change_output(webdomain, projekt_path, out_path):
    """
    function for arg -o
    """
    for webfile in webdomain.input_files:
        outfile = os.path.relpath(webfile.file_path,
                                  os.path.join(projekt_path, "www"))
        webfile.file_path = os.path.join(out_path, outfile)


def write_web_domain(webdomain, projekt_path):
    """
    writes a web files
    """
    for webfile in webdomain.input_files:
        outfile = webfile.file_path
        open(outfile, "w").write(webfile.output)


def main():
    ##
    # Args
    arg_p = argparse.ArgumentParser(
        description="####  Static Web Compiler  #####")
    arg_p.add_argument("-v", "--verbose",
                       help="Show parsing info(loglevel=info)",
                       action="store_true")
    arg_p.add_argument("-d", "--debug",
                       help="Show ALL the debug info(loglevel=debug)",
                       action="store_true")
    arg_p.add_argument("-c", "--clean",
                       help="Removes all *.html files", action="store_true")
    arg_p.add_argument("-o", "--output",
                       help="Spezifies an output Path", action="append")

    arg_p.add_argument("path", help="Path to the SWR Projekt")
    args = arg_p.parse_args()

    is_output = args.output is not None
    if is_output and len(args.output) > 1:
        log.critical("Error: too many output paths")
        sys.exit(-1)

    # logging
    logging_level = "WARNING"
    if args.verbose:
        logging_level = "INFO"
    if args.debug:
        logging_level = "DEBUG"

    log.basicConfig(format='[%(asctime)s] %(levelname)s: %(message)s',
                    datefmt='%I:%M:%S',
                    level=logging_level)

    ##
    # Path
    root_path = os.path.abspath(args.path)
    if not is_swc_dir(root_path):
        log.critical(str(root_path) + " is not a swc path")
        sys.exit(-1)
    www_dir = os.path.join(root_path, "www")

    ##
    # Clean
    if args.clean:
        delete_files = []
        walk_through_dir(www_dir, [".html"], delete_files)
        for file in delete_files:
            os.remove(file)
        log.info("Deleted " + str(len(delete_files)) + " files")

    ##
    # Copy
    if is_output:
        output = os.path.abspath(args.output[0])
        copy_folder_without(www_dir, output, [".swc"])
        log.info("Copyed src folder")

    ##
    # Open and read files
    log.info("Open and read files")
    files = []
    web_domain = Webdomain()
    walk_through_dir(www_dir, [".swc"], files)
    for file in files:
        webfile = Webfile(file)
        web_domain.input_files.append(webfile)
    web_domain.main_file = Webfile(os.path.join(root_path, "main.swc"))

    ##
    # parse / collect
    log.info("Parse and collect in AST")
    file_info_tree = Tree()
    for webfile in web_domain.input_files:
        parse_collect_webfile(webfile, False, args.debug)
        rel_path = os.path.relpath(webfile.file_path,
                                   www_dir)
        file_info_tree[rel_path] = webfile.file_info
    parse_collect_webfile(web_domain.main_file, True, args.debug)

    gc.collect()

    ##
    # interpret
    log.info("Interpret")
    inter_web_domain(web_domain, args.debug, file_info_tree, root_path)

    gc.collect()

    ##
    # Change outpath
    if is_output:
        change_output(web_domain, root_path, output)

    ##
    # write
    log.info("Write on Disk")
    write_web_domain(web_domain, root_path)
