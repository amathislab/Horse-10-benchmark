# AM note for self: taken from fDLC. 

import deeplabcut, os
import pandas as pd

basepath='/home/alex/Hacking/Horse-10-benchmark'
Data=pd.read_hdf(os.path.join(basepath,'Horses-Byron-2019-05-08/training-datasets/iteration-0/UnaugmentedDataSet_HorsesMay8/CollectedData_Byron.h5'))

#loading scale data

#GT data:
Data=pd.read_hdf(os.path.join(projectpath,str(trainingsetfolder),'CollectedData_' + cfg["scorer"] + '.h5'),'df_with_missing')
Scale=pd.read_hdf('Horsescale.h5','df_with_missing')

# Model predictions
DataMachine = pd.read_hdf(resultsfilename,'df_with_missing')

def GetWithinandacrossDomainTestindices(Data,trainIndices,testIndices):
    TrainHorses=set([fn.split(os.sep)[1] for fn in Data.index[trainIndices]])
    testIndices_withinDomain,testIndices_acrossDomain=[],[]
    for t in testIndices:
        if Data.index[t].split(os.sep)[1] in TrainHorses:
            testIndices_withinDomain.append(t)
        else:
            testIndices_acrossDomain.append(t)
    return testIndices_withinDomain,testIndices_acrossDomain

def computedistances(cfg,Data,DataMachine,comparisonbodyparts,DLCscorer,trainIndices,testIndices,trainFraction,shuffle,full=False,Scale=None):
    ''' Computes distances betw DLC and users '''
    DataCombined = pd.concat([Data.T, DataMachine.T], axis=0).T
    if Scale is None:
        RMSE,RMSEpcutoff = pairwisedistances(DataCombined, cfg["scorer"], DLCscorer,cfg["pcutoff"],comparisonbodyparts)
    else:
        s=np.repeat(Scale.values,len(comparisonbodyparts),axis=1)
        RMSE,RMSEpcutoff = pairwisedistances(DataCombined, cfg["scorer"], DLCscorer,cfg["pcutoff"],comparisonbodyparts)
        RMSE,RMSEpcutoff=RMSE*1./s,RMSEpcutoff*1./s

    testerror = np.nanmean(RMSE.iloc[testIndices].values.flatten())
    trainerror = np.nanmean(RMSE.iloc[trainIndices].values.flatten())
    testerrorpcutoff = np.nanmean(RMSEpcutoff.iloc[testIndices].values.flatten())
    trainerrorpcutoff = np.nanmean(RMSEpcutoff.iloc[trainIndices].values.flatten())

    #results = [shuffle,np.round(trainerror,2),np.round(testerror,2),cfg["pcutoff"],np.round(trainerrorpcutoff,2), np.round(testerrorpcutoff,2)]
    print("Results", int(100 * trainFraction), shuffle, "train error:",np.round(trainerror,2), "pixels. Test error:", np.round(testerror,2)," pixels.")
    if full:
        return RMSE,RMSEpcutoff,trainerror,testerror,testerrorpcutoff,trainerrorpcutoff
    if full=='squeezed':
        return RMSE.iloc[testIndices].values.flatten(), RMSE.iloc[trainIndices].values.flatten(),trainerror,testerror,testerrorpcutoff,trainerrorpcutoff
    else:
        return trainerror,testerror,testerrorpcutoff,trainerrorpcutoff

#
RMSE, RMSEpcutoff,trainerror,testerror,testerrorpcutoff,trainerrorpcutoff=utils.computedistances(cfg,Data,DataMachine,comparisonbodyparts,DLCscorer,trainIndices,testIndices,trainFraction,shuffle,full=True,Scale=Scale)

testIndices_withinDomain,testIndices_acrossDomain=utils.GetWithinandacrossDomainTestindices(Data,trainIndices,testIndices)
DATA[shuffle][trainingsetindex][snapindex]['test_withinDomain']=np.nanmean(RMSE.iloc[testIndices_withinDomain].values.flatten())
DATA[shuffle][trainingsetindex][snapindex]['test_acrossDomain']=np.nanmean(RMSE.iloc[testIndices_acrossDomain].values.flatten())
DATA[shuffle][trainingsetindex][snapindex]['splitinfo']=[testIndices,trainIndices,testIndices_withinDomain,testIndices_acrossDomain]
DATA[shuffle][trainingsetindex][snapindex]['error_matrix']=RMSE
DATA[shuffle][trainingsetindex][snapindex]['error_matrix_pcutoff']=RMSEpcutoff
