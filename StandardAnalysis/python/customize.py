import FWCore.ParameterSet.Config as cms
from DisappTrks.StandardAnalysis.utilities import *
from DisappTrks.StandardAnalysis.Triggers import *
import os

def customize (process, runPeriod):

    if runPeriod == "2015":
        process.PUScalingFactorProducer.PU     = cms.string (os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/pu_disappTrks_run2.root')
        process.PUScalingFactorProducer.target = cms.string ("data2015")

        process.ISRWeightProducer.weightFile = cms.string(os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/isrWeight_disappTrks_run2.root')
        process.ISRWeightProducer.weightHist = cms.string('SingleMu_2015D')
        process.ISRWeightProducer.pdgIds = cms.vint32(1000022, 1000024)

        process.TriggerWeightProducer.efficiencyFile = cms.string(os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/triggerEfficiencies_disappTrks_2015D.root')
        process.TriggerWeightProducer.dataset = cms.string('SingleMu_2015D')
        process.TriggerWeightProducer.target = cms.string('WJetsToLNu')
        process.TriggerWeightProducer.inclusiveMetTriggers = triggersMetInclusive
        moveVariableProducer (process, "TriggerWeightProducer")

        setMissingHitsCorrection (process, "2015")

    elif runPeriod == "2016BC":
        process.PUScalingFactorProducer.PU     = cms.string (os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/pu_disappTrks_run2.root')
        process.PUScalingFactorProducer.target = cms.string ("data2016_BC")

        process.ISRWeightProducer.weightFile = cms.string(os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/isrWeight_disappTrks_run2.root')
        process.ISRWeightProducer.weightHist = cms.string('SingleMu_2016')
        process.ISRWeightProducer.pdgIds = cms.vint32(1000022, 1000024)

        process.TriggerWeightProducer.efficiencyFile = cms.string(os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/triggerEfficiencies_disappTrks_run2.root')
        process.TriggerWeightProducer.dataset = cms.string('SingleMu_2016BC')
        process.TriggerWeightProducer.target = cms.string('WJetsToLNu')
        process.TriggerWeightProducer.inclusiveMetTriggers = triggersMetInclusive
        moveVariableProducer (process, "TriggerWeightProducer")

        setMissingHitsCorrection (process, "2016BC")

    elif runPeriod == "2016DEFGH":
        process.PUScalingFactorProducer.PU     = cms.string (os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/pu_disappTrks_run2.root')
        process.PUScalingFactorProducer.target = cms.string ("data2016_DEFGH")

        process.ISRWeightProducer.weightFile = cms.string(os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/isrWeight_disappTrks_run2.root')
        process.ISRWeightProducer.weightHist = cms.string('SingleMu_2016')
        process.ISRWeightProducer.pdgIds = cms.vint32(1000022, 1000024)

        process.TriggerWeightProducer.efficiencyFile = cms.string(os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/triggerEfficiencies_disappTrks_run2.root')
        process.TriggerWeightProducer.dataset = cms.string('SingleMu_2016DEFGH')
        process.TriggerWeightProducer.target = cms.string('WJetsToLNu')
        process.TriggerWeightProducer.inclusiveMetTriggers = triggersMetInclusive
        moveVariableProducer (process, "TriggerWeightProducer")

        setMissingHitsCorrection (process, "2016DEFGH")

    return process
