#!/usr/bin/env python3

from tree_sitter import Language, Parser

Language.build_library("build/tree-sitter-cpp.so", ["tree-sitter-cpp"])

CPP_LANGUAGE = Language("build/tree-sitter-cpp.so", "cpp")

parser = Parser()
parser.set_language(CPP_LANGUAGE)

# TODO