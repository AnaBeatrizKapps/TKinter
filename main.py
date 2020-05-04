import functions
def run(Wmethods,Wparameters,selection,pathFolder,pathKirby):
    path_file = functions.ImportFile()
    path_file.import_file(pathFolder)

    dices = functions.DiceVector()
    dices.Kirby()

    dicesMap = functions.DiceMap()
    dicesMap.transf_list()

    a = functions.AccountMethods()
    a.account_meth()

    MethClass = functions.MethodClass()
    MethClass.meth_class()

    similarity = functions.Similarity()
    similarity.calc_similarity(Wmethods,Wparameters,selection)

    f = functions.FileClass()
    f.file_class(pathKirby)
    f.groupParameters()