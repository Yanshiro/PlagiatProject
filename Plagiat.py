import os
import sys
from pathlib import Path

from pycparser import c_parser, c_ast

parser = c_parser.CParser()
datafolder = "data/"
uploadfolder = "uploadfiles/"
signature = "signature"
schema = "schema"
include = "#include"

def initializefile():
    for root, dirs, files in os.walk("data"):
        for file in files:
            os.remove(datafolder+file)
    createFiles(datafolder+"file1.txt")
    createFiles(datafolder+"file2.txt")
    c_file1 = getUploadedFile()[0]
    c_file2 = getUploadedFile()[1]
    f1 = open(datafolder+'file1.txt', 'a')
    f2 = open(datafolder+'file2.txt', 'a')
    copyCleanedFile(c_file1, f1)
    copyCleanedFile(c_file2, f2)


def createFiles(name):
    Path(name).touch()


def getUploadedFile():
    uploadedFiles = []
    for root, dirs, files in os.walk(uploadfolder):
        for file in files:
            uploadedFiles.append(open(uploadfolder + "" + file, "r", encoding="utf-8"))
    return uploadedFiles

def copyCleanedFile(fileinput, fileoutput):
    d = fileinput.readlines()
    fileinput.seek(0)
    for i in d:
        if not i.startswith(include):
            fileoutput.write(i)
    return fileoutput


def getAstList():
    c_files = []
    for root, dirs, files in os.walk(datafolder):
        for file in files:
            c_files.append(open(datafolder + "" + file, "r", encoding="utf-8"))
    return c_files


def compare_asts(ast1, ast2):
    if type(ast1) != type(ast2):
        return False
    if isinstance(ast1, tuple) and isinstance(ast2, tuple):
        if ast1[0] != ast2[0]:
            return False
        ast1 = ast1[1]
        ast2 = ast2[1]
        return compare_asts(ast1, ast2)
    for i, c1 in enumerate(ast1.children()):
        if compare_asts(c1, ast2.children()[i]) == False:
            return False
    return True


def getScheme(ast1, array):
    for i, c in enumerate(ast1):
        if (type(c) != c_ast.Decl and not (type(c)==c_ast.Assignment)):
            array.append(str(type(c)))
        if (hasattr(c, "stmt")):
            getScheme(c.stmt.block_items, array)
    return array


def getIndexFctDef(ast):
    i = 0
    while (type(ast.ext[i]) != c_ast.FuncDef):
        i += 1
    return i


def getSignature(ast):
    array = []
    function_decl = ast.ext[getIndexFctDef(ast)].decl
    for param_decl in function_decl.type.args.params:
        array.append(type(param_decl.type))
    return array


def compare(ast1, ast2, type):
    if (type == signature):
        array = getSignature(ast1)
        array2 = getSignature(ast2)
    else:
        array = []
        array2 = []
        array = getScheme(ast1.ext[getIndexFctDef(ast1)].body.block_items, array)
        array2 = getScheme(ast2.ext[getIndexFctDef(ast2)].body.block_items, array2)
    if len(array) != len(array2):
        return False
    for (i, j) in zip(array2, array):
        if (i != j):
            return False
    return True


def similarityCalculator(ast1, ast2):
    if not (compare(ast1, ast2, signature)):
        return 0
    if (compare_asts(ast1, ast2)):
        return 1
    if (compare(ast1, ast2, schema)):
        return 2
    else:
        return -1


def main():
    try:
        initializefile()
        c_file1 = getAstList()[0].read()
        c_file2 = getAstList()[1].read()
        ast1 = parser.parse(c_file1, filename='<none>')
        ast2 = parser.parse(c_file2, filename='<none>')
        sys.exit(similarityCalculator(ast1, ast2))
    except IndexError:
        sys.exit(-2)


if __name__ == "__main__":
    main()
