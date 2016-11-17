#!/usr/bin/env python

############################################################################################################
#########  LIST OF MINIAOD 2016 80X DATASETS  ##################################################################
############################################################################################################

dataset_names = {
    ############################################################################
    # MiniAOD stored on T3.
    ############################################################################

    ############################################################################
    # MiniAOD not stored on T3.
    ############################################################################

    'MET_2016B'       : "/MET/ahart-Run2016B-PromptReco-v2-DisappTrks-v6-c54ccc1822dfa6717a0025c44fd621af/USER",
    'MET_2016C'       : "/MET/ahart-Run2016C-PromptReco-v2-DisappTrks-v6-c54ccc1822dfa6717a0025c44fd621af/USER",
    'MET_2016D'       : "/MET/ahart-Run2016D-PromptReco-v2-DisappTrks-v6-c54ccc1822dfa6717a0025c44fd621af/USER",
    'MET_2016E'       : "/MET/ahart-Run2016E-PromptReco-v2-DisappTrks-v6-c54ccc1822dfa6717a0025c44fd621af/USER",
    'MET_2016F'       : "/MET/ahart-Run2016F-PromptReco-v1-DisappTrks-v6-c54ccc1822dfa6717a0025c44fd621af/USER",
    'MET_2016G'       : "/MET/bfrancis-Run2016G-PromptReco-v1-DisappTrks-v6-9b2edbeb3fa0a9ecef990a505ab27439/USER",

    'SingleEle_2016B' : "/SingleElectron/bfrancis-Run2016B-PromptReco-v2-DisappTrks-v6-136b6bd54d5297516ccc5e4597ba027d/USER",
    'SingleEle_2016C' : "/SingleElectron/bfrancis-Run2016C-PromptReco-v2-DisappTrks-v6-136b6bd54d5297516ccc5e4597ba027d/USER",
    'SingleEle_2016D' : "/SingleElectron/bfrancis-Run2016D-PromptReco-v2-DisappTrks-v6-136b6bd54d5297516ccc5e4597ba027d/USER",
    'SingleEle_2016E' : "/SingleElectron/bfrancis-Run2016E-PromptReco-v2-DisappTrks-v6-136b6bd54d5297516ccc5e4597ba027d/USER",
    'SingleEle_2016F' : "/SingleElectron/bfrancis-Run2016F-PromptReco-v1-DisappTrks-v6-136b6bd54d5297516ccc5e4597ba027d/USER",
    'SingleEle_2016G' : "/SingleElectron/bfrancis-Run201G-PromptReco-v1-DisappTrks-v6-136b6bd54d5297516ccc5e4597ba027d/USER",

    'SingleMu_2016B'  : "/SingleMuon/wulsin-Run2016B-PromptReco-v2-DisappTrks-v7-9400a0756dc17512d543a143a2bde30d/USER",
    'SingleMu_2016C'  : "/SingleMuon/wulsin-Run2016C-PromptReco-v2-DisappTrks-v7-9400a0756dc17512d543a143a2bde30d/USER",
    'SingleMu_2016D'  : "/SingleMuon/wulsin-Run2016D-PromptReco-v2-DisappTrks-v7-9400a0756dc17512d543a143a2bde30d/USER",
    'SingleMu_2016E'  : "/SingleMuon/wulsin-Run2016E-PromptReco-v2-DisappTrks-v7-9400a0756dc17512d543a143a2bde30d/USER",
    'SingleMu_2016F'  : "/SingleMuon/wulsin-Run2016F-PromptReco-v1-DisappTrks-v7-9400a0756dc17512d543a143a2bde30d/USER",
    'SingleMu_2016G'  : "/SingleMuon/wulsin-Run201G-PromptReco-v1-DisappTrks-v7-9400a0756dc17512d543a143a2bde30d/USER",

    'Tau_2016B'        :  "/Tau/ahart-Run2016B-PromptReco-v2-DisappTrks-v6-08dfac7d0c5e48045e9a5164b5e2f763/USER",
    'Tau_2016C'        :  "/Tau/ahart-Run2016C-PromptReco-v2-DisappTrks-v6-08dfac7d0c5e48045e9a5164b5e2f763/USER",
    'Tau_2016D'        :  ["/Tau/ahart-Run2016D-PromptReco-v2-DisappTrks-v6-08dfac7d0c5e48045e9a5164b5e2f763/USER", "/Tau/ahart-Run2016D-PromptReco-v2-DisappTrks-v6-cb3e0f46a2f7f32830a4152107df81ff/USER"],
    'Tau_2016E'        :  "/Tau/ahart-Run2016E-PromptReco-v2-DisappTrks-v6-08dfac7d0c5e48045e9a5164b5e2f763/USER",
    'Tau_2016F'        :  "/Tau/ahart-Run2016F-PromptReco-v1-DisappTrks-v6-08dfac7d0c5e48045e9a5164b5e2f763/USER",
    'Tau_2016G'        :  ["/Tau/ahart-Run201G-PromptReco-v1-DisappTrks-v6-08dfac7d0c5e48045e9a5164b5e2f763/USER", "/Tau/ahart-Run201G-PromptReco-v1-DisappTrks-v6-cb3e0f46a2f7f32830a4152107df81ff/USER"],

    'AMSB_chargino_100GeV_10cm_80X'    :  "/AMSB_chargino_M-100_CTau-10_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
    'AMSB_chargino_100GeV_100cm_80X'   :  "/AMSB_chargino_M-100_CTau-100_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
    'AMSB_chargino_100GeV_1000cm_80X'  :  "/AMSB_chargino_M-100_CTau-1000_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
    'AMSB_chargino_100GeV_10000cm_80X'  :  "/AMSB_chargino_M-100_CTau-10000_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",

    'AMSB_chargino_200GeV_10cm_80X'    :  "/AMSB_chargino_M-200_CTau-10_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
    'AMSB_chargino_200GeV_100cm_80X'   :  "/AMSB_chargino_M-200_CTau-100_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
    'AMSB_chargino_200GeV_1000cm_80X'  :  "/AMSB_chargino_M-200_CTau-1000_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
    'AMSB_chargino_200GeV_10000cm_80X'  :  "/AMSB_chargino_M-200_CTau-10000_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",

    'AMSB_chargino_300GeV_10cm_80X'    :  "/AMSB_chargino_M-300_CTau-10_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
    'AMSB_chargino_300GeV_100cm_80X'   :  "/AMSB_chargino_M-300_CTau-100_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
    'AMSB_chargino_300GeV_1000cm_80X'  :  "/AMSB_chargino_M-300_CTau-1000_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
    'AMSB_chargino_300GeV_10000cm_80X'  :  "/AMSB_chargino_M-300_CTau-10000_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",

    'AMSB_chargino_400GeV_10cm_80X'    :  "/AMSB_chargino_M-400_CTau-10_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
    'AMSB_chargino_400GeV_100cm_80X'   :  "/AMSB_chargino_M-400_CTau-100_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
    'AMSB_chargino_400GeV_1000cm_80X'  :  "/AMSB_chargino_M-400_CTau-1000_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
    'AMSB_chargino_400GeV_10000cm_80X'  :  "/AMSB_chargino_M-400_CTau-10000_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",

    'AMSB_chargino_500GeV_10cm_80X'    :  "/AMSB_chargino_M-500_CTau-10_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
    'AMSB_chargino_500GeV_100cm_80X'   :  "/AMSB_chargino_M-500_CTau-100_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
    'AMSB_chargino_500GeV_1000cm_80X'  :  "/AMSB_chargino_M-500_CTau-1000_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
    'AMSB_chargino_500GeV_10000cm_80X'  :  "/AMSB_chargino_M-500_CTau-10000_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",

    'AMSB_chargino_600GeV_10cm_80X'    :  "/AMSB_chargino_M-600_CTau-10_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
    'AMSB_chargino_600GeV_100cm_80X'   :  "/AMSB_chargino_M-600_CTau-100_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
    'AMSB_chargino_600GeV_1000cm_80X'  :  "/AMSB_chargino_M-600_CTau-1000_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
    'AMSB_chargino_600GeV_10000cm_80X'  :  "/AMSB_chargino_M-600_CTau-10000_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",

    'AMSB_chargino_700GeV_10cm_80X'    :  "/AMSB_chargino_M-700_CTau-10_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
    'AMSB_chargino_700GeV_100cm_80X'   :  "/AMSB_chargino_M-700_CTau-100_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
    'AMSB_chargino_700GeV_1000cm_80X'  :  "/AMSB_chargino_M-700_CTau-1000_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
    'AMSB_chargino_700GeV_10000cm_80X'  :  "/AMSB_chargino_M-700_CTau-10000_TuneZ2star_13TeV_pythia6/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_2016_miniAODv2_v1-v1/MINIAODSIM",
}

import re

new_dataset_names = {}
for dataset0 in dataset_names:
    if not re.match (r'AMSB_chargino_[^_]*GeV_[^_]*cm_.*', dataset0):
        continue
    mass = re.sub (r'AMSB_chargino_([^_]*)GeV_[^_]*cm_.*', r'\1', dataset0)
    ctau0 = float (re.sub (r'AMSB_chargino_[^_]*GeV_([^_]*)cm_.*', r'\1', dataset0))
    suffix = re.sub (r'AMSB_chargino_[^_]*GeV_[^_]*cm_(.*)', r'\1', dataset0)
    for i in range (2, 10):
        ctau = ctauP = 0.1 * i * ctau0
        if int (ctau) * 10 == int (ctau * 10):
            ctau = ctauP = str (int (ctau))
        else:
            ctau = ctauP = str (ctau)
            ctauP = re.sub (r'\.', r'p', ctau)
        dataset = 'AMSB_chargino_' + mass + 'GeV_' + ctauP + 'cm_' + suffix

        new_dataset_names[dataset] = dataset_names[dataset0]

dataset_names.update (new_dataset_names)
