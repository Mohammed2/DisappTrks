from OSUT3Analysis.Configuration.configurationOptions import *
from DisappTrks.StandardAnalysis.addLifetimeReweighting import *
from DisappTrks.TriggerAnalysis.miniAODSamples_80X import *

config_file = "protoConfig_2016_cfg.py"

# 28629.903 = B (6108.362) + C (2963.704) + D (4485.279) + E (4243.920) + F (3177.925) + G (7650.713)
intLumi = 28629.903

InputCondorArguments = {'request_memory': '2048MB', 'request_cpus': '1'}

datasetsData = [
    'SingleMu_2016B',
    'SingleMu_2016C',
    'SingleMu_2016D',
    'SingleMu_2016E',
    'SingleMu_2016F',
    'SingleMu_2016G',
]

datasetsBkg = [
    'WJetsToLNu',
]

datasetsSig = [
    'AMSB_chargino_100GeV_10cm_80X',
    'AMSB_chargino_100GeV_100cm_80X',
    'AMSB_chargino_100GeV_1000cm_80X',
    'AMSB_chargino_100GeV_10000cm_80X',

    'AMSB_chargino_200GeV_10cm_80X',
    'AMSB_chargino_200GeV_100cm_80X',
    'AMSB_chargino_200GeV_1000cm_80X',
    'AMSB_chargino_200GeV_10000cm_80X',

    'AMSB_chargino_300GeV_10cm_80X',
    'AMSB_chargino_300GeV_100cm_80X',
    'AMSB_chargino_300GeV_1000cm_80X',
    'AMSB_chargino_300GeV_10000cm_80X',

    'AMSB_chargino_400GeV_10cm_80X',
    'AMSB_chargino_400GeV_100cm_80X',
    'AMSB_chargino_400GeV_1000cm_80X',
    'AMSB_chargino_400GeV_10000cm_80X',

    'AMSB_chargino_500GeV_10cm_80X',
    'AMSB_chargino_500GeV_100cm_80X',
    'AMSB_chargino_500GeV_1000cm_80X',
    'AMSB_chargino_500GeV_10000cm_80X',

    'AMSB_chargino_600GeV_10cm_80X',
    'AMSB_chargino_600GeV_100cm_80X',
    'AMSB_chargino_600GeV_1000cm_80X',
    'AMSB_chargino_600GeV_10000cm_80X',

    'AMSB_chargino_700GeV_10cm_80X',
    'AMSB_chargino_700GeV_100cm_80X',
    'AMSB_chargino_700GeV_1000cm_80X',
    'AMSB_chargino_700GeV_10000cm_80X',
]

datasetsSigShort = copy.deepcopy(datasetsSig)

datasetsSigVeryShort = [
    'AMSB_chargino_500GeV_10cm_80X',
    'AMSB_chargino_500GeV_100cm_80X',
    'AMSB_chargino_500GeV_1000cm_80X',
    'AMSB_chargino_500GeV_10000cm_80X',
]

addLifetimeReweighting (datasetsSig)

datasets = datasetsBkg + datasetsData
#datasets = datasetsSigShort
