def function_doubleasterix(**keywordargs):

    print("The KEYS in the kwargs dicionary are -", keywordargs.keys())
    print("The VALUES in the kwargs dicionary are -", keywordargs.values())

    print("--The key value assignment in the 'keywordargs' dictionary are as follows--")
    for key, value in keywordargs.items():
        print ("%s == %s" %(key, value))
#No exemplo acima, keywordargs está associado a um dicionário como no programa abaixo.

function_doubleasterix(SNo001 ='Alex', SNo002 ='Tom')