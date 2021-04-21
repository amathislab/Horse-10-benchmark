# simple script to convert DLC meta data regarding splits into general format.

import deeplabcut, os
import pandas as pd

basepath='/home/alex/Hacking/Horse-10-benchmark'
Data=pd.read_hdf(os.path.join(basepath,'Horses-Byron-2019-05-08/training-datasets/iteration-0/UnaugmentedDataSet_HorsesMay8/CollectedData_Byron.h5'))

def GetWithinandacrossDomainTestindices(Data,trainIndices,testIndices):
    TrainHorses=set([fn.split(os.sep)[1] for fn in Data.index[trainIndices]])
    testIndices_withinDomain,testIndices_acrossDomain=[],[]
    for t in testIndices:
        if Data.index[t].split(os.sep)[1] in TrainHorses:
            testIndices_withinDomain.append(t)
        else:
            testIndices_acrossDomain.append(t)
    return testIndices_withinDomain,testIndices_acrossDomain

for shuffle in [1,2,3]:
    _, trainIndices, testIndices, _=deeplabcut.auxiliaryfunctions.read_pickle(os.path.join(basepath,'Horses-Byron-2019-05-08/training-datasets/iteration-0/UnaugmentedDataSet_HorsesMay8/Documentation_data-Horses_50shuffle'+str(shuffle)+'.pickle'))
    testIndices_withinDomain, testIndices_acrossDomain = GetWithinandacrossDomainTestindices(Data,trainIndices,testIndices)

    data=[Data.index[t] for t in [trainIndices,testIndices_withinDomain, testIndices_acrossDomain]]

    df = pd.DataFrame(
    data,
    index=["trainIndices","testIndices_withinDomain", "testIndices_acrossDomain"],
    ).T

    df.to_csv("TrainTestInfo_shuffle"+str(shuffle)+".csv")
