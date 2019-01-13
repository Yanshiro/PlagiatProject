from pycparser import c_parser, c_ast
from pathlib import Path
import os
import re

parser = c_parser.CParser()
datafolder = "data/"
uploadfolder = "uploadfiles/"


def initializefile():
    createFiles("data/file1.txt")
    createFiles("data/file2.txt")
    c_file1 = getUploadedFile()[0]
    c_file2 = getUploadedFile()[1]
    f1 = open('data/file1.txt', 'a')
    f2 = open('data/file2.txt', 'a')
    copyCleanedFile(c_file1, f1)
    copyCleanedFile(c_file2, f2)


def createFiles(name):
    Path(name).touch()


def getUploadedFile():
    uploadedFiles = []
    for root, dirs, files in os.walk("uploadfiles"):
        for file in files:
            uploadedFiles.append(open(uploadfolder + "" + file, "r", encoding="utf-8"))
    return uploadedFiles


# TODO
# handle comments
def copyCleanedFile(fileinput, fileoutput):
    d = fileinput.readlines()
    fileinput.seek(0)
    for i in d:
        if not i.startswith("#include"):
            fileoutput.write(i)
    return fileoutput


def getAstList():
    c_files = []
    for root, dirs, files in os.walk("data"):
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


def compareScheme(ast1, ast2):
    arrayast1 = []
    arrayast1 = getScheme(ast1.ext[getIndexFctDef(ast1)].body.block_items, arrayast1)
    arrayast2 = []
    arrayast2 = getScheme(ast2.ext[getIndexFctDef(ast2)].body.block_items, arrayast2)
    if len(arrayast1) != len(arrayast2):
        return False
    for (i, j) in zip(arrayast2, arrayast1):
        if (i != j):
            return False
    return True


def getScheme(ast1, array):
    for i, c in enumerate(ast1):
        if (type(c) != c_ast.Decl):
                if(type(c) == c_ast.Assignment and type(ast1[i - 1]) == c_ast.Assignment):
                    continue
                else:
                    array.append(str(type(c)))
        if (hasattr(c, "stmt")):
            getScheme(c.stmt.block_items, array)
    return array


def getIndexFctDef(ast):
    i = 0
    while (type(ast.ext[i]) != c_ast.FuncDef):
        i += 1
    return i


def compareSignature(ast, ast2):
    function_decl = ast.ext[getIndexFctDef(ast)].decl
    for param_decl in function_decl.type.args.params:
        print('Type:')
        print(type(param_decl.type))
        param_decl.type.show(offset=6)
    return False


def similarityCalculator(ast1, ast2):
    if not (compareSignature(ast1, ast2)):
        return 0
    if (compare_asts(ast1, ast2)):
        return 1
    if (compareScheme(ast1, ast2)):
        return 2


def main():
    initializefile()
    c_file1 = getAstList()[0].read()
    c_file2 = getAstList()[1].read()
    ast1 = parser.parse(c_file1, filename='<none>')
    ast2 = parser.parse(c_file2, filename='<none>')
    print(compare_asts(ast1, ast2))#true si copie conforme ou identique au nom de variable pres
    print(compareScheme(ast1, ast2))#true si même schema


# TODO
# Signatures similarity
# SimilarityCalculator to improve
# view

if __name__ == "__main__":
    main()
