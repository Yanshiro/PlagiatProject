from pycparser import c_parser, c_ast

parser = c_parser.CParser()

text = r"""
    typedef int Node, Hash;
    void HashPrint(Hash* hash, void (*PrintFunc)(char*, char*))
    {
        unsigned int i;
        if (hash == NULL || hash->heads == NULL)
            return;
        for (i = 0; i < hash->table_size; ++i)
        {
            Node* temp = hash->heads[i];
            while (temp != NULL)
            {
                PrintFunc(temp->entry->key, temp->entry->value);
                temp = temp->next;
            }
        }
    }
"""

text2 = r"""
    void counting_sort(int *tab, int taille)
{
  int i, min, max;
 
  min = max = tab[0];
  for(i=1; i < taille; i++) {
    if ( tab[i] < min ) {
      min = tab[i];
    } else  {
      max = tab[i];
    }
    
    min=3;
  }
}
"""


text3 = r"""
    void counng_sort(int *tableau, int n)
{
  int j, a, b;
   int l, m, n;

  a = b = tableau[0];
  for(j=1; j < n; j++) {
    if ( tableau[j]>a) {
      a = tableau[j];
    } else  {
      b = tableau[j];
    }
    a=3;
  }
}
"""

ast1 = parser.parse(text2, filename='<none>');
ast = parser.parse(text, filename='<none>');
ast2 = parser.parse(text3, filename='<none>');

#changement nom variable et fct pris en compte
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

def compareScheme(ast1,ast2):
    arrayast1 = []
    arrayast1 = getScheme(ast1.ext[getIndexFctDef(ast1)].body.block_items, arrayast1)
    arrayast2 = []
    arrayast2 = getScheme(ast2.ext[getIndexFctDef(ast2)].body.block_items, arrayast2)
    for (i,j) in zip(arrayast2,arrayast1):
        if(i!=j):
            return False
    return True

def getScheme(ast1,array):
    for i,c in enumerate(ast1):
        if(type(c)!=c_ast.Decl):
            array.append(str(type(c)))
        if (hasattr(c,"stmt")):
            getScheme(c.stmt.block_items,array)
    return array

def getIndexFctDef(ast):
    i = 0
    while(type(ast.ext[i])!=c_ast.FuncDef):
        i += 1
    return i

def compareSignature(ast,ast2):
    function_decl=ast.ext[getIndexFctDef(ast)].decl
    for param_decl in function_decl.type.args.params:
        print('Type:')
        print(type(param_decl.type))
        param_decl.type.show(offset=6)
    return False


def similarityCalculator(ast1,ast2):
    if not (compareSignature(ast1,ast2)):
        return 0
    if (compare_asts(ast1,ast2)):
        return 1
    if(compareScheme(ast1,ast2)):
        return 2

def main():
    # print(compare_asts(ast1, ast2))
    # print(compareScheme(ast1, ast2))
    # list = []
    # list = getScheme(ast.ext[getIndexFctDef(ast)].body.block_items, list)
    # for j in list:
    #     print(j)
    print("hello world")
    #TODO
    #Check condition
    #Check Assignement
    #Signatures similarity
    #SimilarityCalculator to improve

if __name__ == "__main__":
    main()


