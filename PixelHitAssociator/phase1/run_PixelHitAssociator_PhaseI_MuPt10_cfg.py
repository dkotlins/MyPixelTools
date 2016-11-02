# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: -s GEN,SIM,DIGI,L1,DIGI2RAW,RAW2DIGI,RECO --evt_type SingleMuPt10_cfi --conditions auto:phase1_2017_realistic --era Run2_2017 --geometry Extended2017new --fileout file:MuPt10_GENSIMRECO.root --python_filename=run_PixelHitAssociator_PhaseI_MuPt10_cfg.py -n 10 --runUnscheduled --no_exec
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('RECO',eras.Run2_2017)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2017newReco_cff')
process.load('Configuration.Geometry.GeometryExtended2017new_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic50ns13TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(
    allowUnscheduled = cms.untracked.bool(True)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('SingleMuPt10_cfi nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string(''),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('file:MuPt10_GENSIMRECO.root'),
    outputCommands = process.RECOSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2017_realistic', '')

process.generator = cms.EDProducer("FlatRandomPtGunProducer",
    AddAntiParticle = cms.bool(True),
    PGunParameters = cms.PSet(
        MaxEta = cms.double(2.5),
        MaxPhi = cms.double(3.14159265359),
        MaxPt = cms.double(10.01),
        MinEta = cms.double(-2.5),
        MinPhi = cms.double(-3.14159265359),
        MinPt = cms.double(9.99),
        PartID = cms.vint32(-13)
    ),
    Verbosity = cms.untracked.int32(0),
    firstRun = cms.untracked.uint32(1),
    psethack = cms.string('single mu pt 10')
)


# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.raw2digi_step = cms.Path(process.RawToDigi)
process.reconstruction_step = cms.Path(process.reconstruction)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.digitisation_step,process.L1simulation_step,process.digi2raw_step,process.raw2digi_step,process.reconstruction_step,process.endjob_step,process.RECOSIMoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 




# Code inserted here
# ----------------- PixelHitAssociator ----------------------

# Load new FPix Geometry (comment these out in original cmsDriver config on top)

# ### process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
# ###### process.load('Configuration.Geometry.GeometryRecoDB_cff')
# process.load('Geometry.CommonDetUnit.globalTrackingGeometryDB_cfi')
# process.load('RecoTracker.GeometryESProducer.TrackerRecoGeometryESProducer_cfi')
# process.load('Geometry.TrackerNumberingBuilder.trackerTopology_cfi')
# process.load('RecoMuon.DetLayers.muonDetLayerGeometry_cfi')
# process.load('Geometry.CaloEventSetup.CaloTopology_cfi')
# process.load('Geometry.CaloEventSetup.AlignedCaloGeometryDBReader_cfi')
# process.load('Geometry.CaloEventSetup.EcalTrigTowerConstituents_cfi')
# process.load('Geometry.EcalMapping.EcalMapping_cfi')
# process.load('Geometry.EcalMapping.EcalMappingRecord_cfi')
# process.load('Geometry.HcalCommonData.hcalDDDSimConstants_cfi')
# process.load('Geometry.HcalCommonData.hcalDDDRecConstants_cfi')
# process.load('Geometry.HcalEventSetup.hcalTopologyIdeal_cfi')
# process.load('Geometry.TrackerGeometryBuilder.idealForDigiTrackerGeometryDB_cff')
# process.load('Geometry.CSCGeometryBuilder.idealForDigiCscGeometryDB_cff')
# process.load('Geometry.DTGeometryBuilder.idealForDigiDtGeometryDB_cff')
# 
# ### process.load('Configuration.Geometry.GeometrySimDB_cff')
# process.load('GeometryReaders.XMLIdealGeometryESSource.cmsGeometryDB_cff')
# process.load('Geometry.MuonNumbering.muonNumberingInitialization_cfi')
# process.load('Geometry.TrackerNumberingBuilder.trackerNumberingGeometryDB_cfi')
# process.load('Geometry.HcalCommonData.hcalDDDSimConstants_cfi')

# NEW FPix Geom
#process.load('Configuration.Geometry.GeometryExtended2017NewFPixReco_cff')
#process.load('Configuration.Geometry.GeometrySimDB_cff')


#------------------------------------------
#  Options - can be given from command line
#------------------------------------------
import FWCore.ParameterSet.VarParsing as opts

opt = opts.VarParsing ('analysis')

opt.register('globalTag',          '',
	     opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.string,
	     'Global Tag, Default="" which uses auto:run2_data')

opt.register('useClustersOnTrack', True,
	     opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.bool,
	     'True: use RecHits of generalTracks, False: use siPixelRecHits')

opt.register('useTemplates',       True,
	     opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.bool,
	     'Only for On-track clusters! True: use Template reco, False: use Generic reco')

opt.register('saveRECO',           False,
	     opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.bool,
	     'Option to keep GEN-SIM-RECO')

opt.register('outputFileName',      '',
	     opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.string,
	     'Name of the histograms file')

opt.register('useLocalLASim',      False,
	     opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.bool,
	     'Test LA (SIM) conditions locally (prep/prod database or sqlite file')

opt.register('useLocalQuality',    False,
	     opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.bool,
	     'Test Quality conditions locally (prep/prod database or sqlite file')

opt.register('useLocalLA',         False,
	     opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.bool,
	     'Test LA (RECO) conditions locally (prep/prod database or sqlite file')

opt.register('useLocalGain',       False,
	     opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.bool,
	     'Test Gain conditions locally (prep/prod database or sqlite file')

opt.register('useLocalGenErr',     False,
	     opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.bool,
	     'Test GenError conditions locally (prep/prod database or sqlite file')

### Events to process: 'maxEvents' is already registered by the framework
opt.setDefault('maxEvents', 1000)

# Proceed with settings from command line
opt.parseArguments()

process.maxEvents.input = opt.maxEvents

# Configure PixelHitAssociator
process.load("DPGAnalysis-SiPixelTools.PixelHitAssociator.SiPixelRecHitsValid_cff")
if opt.useClustersOnTrack:
	process.pixRecHitsValid.useTracks = True
	#process.pixRecHitsValid.tracks="initialStepTracks" # first tracker step
	process.pixRecHitsValid.tracks="generalTracks"
	if opt.useTemplates:
		process.initialStepTracks.TTRHBuilder = 'WithAngleAndTemplate'
		if opt.outputFileName == '': opt.outputFileName = 'SimToRecHitHistos_TemplateReco_OnTrackHits.root'
	else:
		process.initialStepTracks.TTRHBuilder = 'WithTrackAngle'
		if opt.outputFileName == '': opt.outputFileName = 'SimToRecHitHistos_GenericReco_OnTrackHits.root'
else:
	process.pixRecHitsValid.useTracks = False
	#process.pixRecHitsValid.src="siPixelRecHitsPreSplitting"
	process.pixRecHitsValid.src="siPixelRecHits"
	if opt.outputFileName == '': opt.outputFileName = 'SimToRecHitHistos_GenericReco_siPixelRecHits.root'
process.pixRecHitsValid.outputFile = opt.outputFileName
process.pixRecHitsValid.verbose=False
#process.pixRecHitsValid.associatePixel = True
#process.pixRecHitsValid.associateStrip = False
#process.pixRecHitsValid.associateRecoTracks = False

# Print settings
print "Using options: "
if opt.globalTag == '':
    print "  globalTag (auto:phase1_2017_realistic) = "+str(process.GlobalTag.globaltag)
else:
    process.GlobalTag.globaltag = opt.globalTag
    print "  globalTag (manually chosen)            = "+str(process.GlobalTag.globaltag)
print "  useClustersOnTrack                     = "+str(opt.useClustersOnTrack)
print "  useTemplates                           = "+str(opt.useTemplates)
print "  saveRECO                               = "+str(opt.saveRECO)
print "  outputFileName                         = "+str(opt.outputFileName)
print "  maxEvents                              = "+str(opt.maxEvents)
print "  useLocalLASim                          = "+str(opt.useLocalLASim)
print "  useLocalQuality                        = "+str(opt.useLocalQuality)
print "  useLocalLA                             = "+str(opt.useLocalLA)
print "  useLocalGain                           = "+str(opt.useLocalGain)
print "  useLocalGenErr                         = "+str(opt.useLocalGenErr)

# Test Local DB conditions
# LA (SIM)
LASim_tag       = "SiPixelLorentzAngleSim_phase1_mc_v1"
#LASim_db        = 'sqlite_file:../../../../../DB/phase1/SiPixelLorentzAngleSim_phase1_mc_v1.db'
LASim_db        = 'frontier://FrontierPrep/CMS_CONDITIONS'
#LASim_db        = 'frontier://FrontierProd/CMS_CONDITIONS'

# Quality
Qua_tag         = 'SiPixelQuality_phase1_ideal'
#Qua_db          = 'sqlite_file:../../../../../DB/phase1/SiPixelQuality_phase1_ideal.db'
Qua_db          = 'frontier://FrontierPrep/CMS_CONDITIONS'
#Qua_db          = 'frontier://FrontierProd/CMS_CONDITIONS'

# LA (RECO)
LA_tag          = 'SiPixelLorentzAngle_phase1_mc_v1'
LA_Width_tag    = 'SiPixelLorentzAngle_phase1_mc_v1'
#LA_db           = 'sqlite_file:../../../../../DB/phase1/SiPixelLorentzAngle_phase1_mc_v1.db'
#LA_db           = 'frontier://FrontierPrep/CMS_CONDITIONS'
LA_db           = 'frontier://FrontierProd/CMS_CONDITIONS'
#LA_Width_db     = 'sqlite_file:../../../../../DB/phase1/SiPixelLorentzAngle_phase1_mc_v1.db'
#LA_Width_db     = 'frontier://FrontierPrep/CMS_CONDITIONS'
LA_Width_db     = 'frontier://FrontierProd/CMS_CONDITIONS'

# Gains
#Gain_tag        = 'SiPixelGainCalibration_phase1_mc_v1'
Gain_tag        = 'SiPixelGainCalibration_phase1_mc_v2'
#Gain_tag        = 'SiPixelGainCalibration_phase1_ideal'
#Gain_tag        = 'SiPixelGainCalibration_phase1_ideal_v2'
Gain_db         = 'sqlite_file:../../../../../DB/phase1/SiPixelGainCalibration_phase1_mc_v2.db'
#Gain_db         = 'sqlite_file:../../../../../DB/phase1/SiPixelGainCalibration_phase1_ideal_v2.db'
#Gain_db         = 'frontier://FrontierPrep/CMS_CONDITIONS'
#Gain_db         = 'frontier://FrontierProd/CMS_CONDITIONS'

# GenErrors
GenErr_tag      = 'SiPixelGenErrorDBObject_phase1_38T_mc_v1'
#GenErr_db       = 'sqlite_file:siPixelGenErrors38T.db'
#GenErr_db       = 'frontier://FrontierPrep/CMS_COND_PIXEL'
#GenErr_db       = 'frontier://FrontierPrep/CMS_CONDITIONS'
GenErr_db       = 'frontier://FrontierProd/CMS_CONDITIONS'

# Other statements
#process.mix.digitizers = cms.PSet(process.theDigitizersValid)
# modify digitizer parameters
#process.simSiPixelDigis.pixel.ThresholdInElectrons_BPix = 3500.0 
# disable dyn. ineff.
process.mix.digitizers.pixel.AddPixelInefficiencyFromPython = cms.bool(False)
#process.mix.digitizers.pixel.NumPixelBarrel = cms.int32(4)
#process.mix.digitizers.pixel.NumPixelEndcap = cms.int32(3)


#process.source = cms.Source("PoolSource", 
#  fileNames = cms.untracked.vstring(
#    'file:/afs/cern.ch/work/d/dkotlins/public//MC/mu_phase1/pt100_76/simhits/simHits1.root'
#  ),
#)

#process.MessageLogger = cms.Service("MessageLogger",
#    #debugModules = cms.untracked.vstring('Digitize'),
#    debugModules = cms.untracked.vstring('PixelDigitizer'),
#    destinations = cms.untracked.vstring('cout'),
#    #destinations = cms.untracked.vstring("log","cout"),
#    cout = cms.untracked.PSet(
#        threshold = cms.untracked.string('ERROR')
#    )
#    #log = cms.untracked.PSet(
#    #    threshold = cms.untracked.string('DEBUG')
#    #)
#)
process.MessageLogger.cerr.FwkReport.reportEvery = 10

#LA
if opt.useLocalLASim :
	process.LASimReader = cms.ESSource("PoolDBESSource",
		DBParameters = cms.PSet(
			messageLevel = cms.untracked.int32(0),
			authenticationPath = cms.untracked.string('')),
		toGet = cms.VPSet(cms.PSet(
			record = cms.string("SiPixelLorentzAngleSimRcd"),
			tag = cms.string(LASim_tag))),
		connect = cms.string(LASim_db))
	process.lasimprefer = cms.ESPrefer("PoolDBESSource","LASimReader")

# Quality
if opt.useLocalQuality :
	process.QualityReader = cms.ESSource("PoolDBESSource",
		DBParameters = cms.PSet(
			messageLevel = cms.untracked.int32(0),
			authenticationPath = cms.untracked.string('')),
		toGet = cms.VPSet(cms.PSet(
			record = cms.string('SiPixelQualityFromDbRcd'),
			tag = cms.string('SiPixelQuality_phase1_ideal'))),
		connect = cms.string(Qua_tag))
	process.es_prefer_QualityReader = cms.ESPrefer("PoolDBESSource","QualityReader")

# for reco
# LA 
if opt.useLocalLA :
	process.LAReader = cms.ESSource("PoolDBESSource",
		DBParameters = cms.PSet(
			messageLevel = cms.untracked.int32(0),
			authenticationPath = cms.untracked.string('')),
		toGet = cms.VPSet(cms.PSet(
			record = cms.string("SiPixelLorentzAngleRcd"),
			tag = cms.string(LA_tag))),
		connect = cms.string(LA_db))
	process.LAprefer = cms.ESPrefer("PoolDBESSource","LAReader")
	# now the forWidth LA
	process.LAWidthReader = cms.ESSource("PoolDBESSource",
		DBParameters = cms.PSet(
			messageLevel = cms.untracked.int32(0),
			authenticationPath = cms.untracked.string('')),
		toGet = cms.VPSet(cms.PSet(
			record = cms.string("SiPixelLorentzAngleRcd"),
			label = cms.untracked.string("forWidth"),
			tag = cms.string(LA_Width_tag))),
		connect = cms.string(LA_Width_db))
	process.LAWidthprefer = cms.ESPrefer("PoolDBESSource","LAWidthReader")

# Gain 
if opt.useLocalGain :
	process.GainsReader = cms.ESSource("PoolDBESSource",
		DBParameters = cms.PSet(
			messageLevel = cms.untracked.int32(0),
			authenticationPath = cms.untracked.string('')),
		toGet = cms.VPSet(cms.PSet(
			record = cms.string('SiPixelGainCalibrationOfflineRcd'),
			tag = cms.string(Gain_tag))),
		connect = cms.string(Gain_db))
	process.Gainprefer = cms.ESPrefer("PoolDBESSource","GainsReader")

# GenError
if opt.useLocalGenErr :
	process.GenErrReader = cms.ESSource("PoolDBESSource",
		DBParameters = cms.PSet(
			messageLevel = cms.untracked.int32(0),
			authenticationPath = cms.untracked.string('')),
		toGet = cms.VPSet(cms.PSet(
			record = cms.string('SiPixelGenErrorDBObjectRcd'),
			tag = cms.string(GenErr_tag))),
		connect = cms.string(GenErr_db))
	process.generrprefer = cms.ESPrefer("PoolDBESSource","GenErrReader")

#---------------------------
#  Path/Schedule
#---------------------------
process.pixRecHitsValid_step = cms.Path(process.pixRecHitsValid)

if not opt.saveRECO: process.schedule.remove(process.RECOSIMoutput_step)
process.schedule.remove(process.endjob_step)
process.schedule.remove(process.genfiltersummary_step)
process.schedule.append(process.pixRecHitsValid_step)

# ------------ End of PixelHitAssociator ------------------
# End ofinserted code




#do not add changes to your config after this point (unless you know what you are doing)
from FWCore.ParameterSet.Utilities import convertToUnscheduled
process=convertToUnscheduled(process)
from FWCore.ParameterSet.Utilities import cleanUnscheduled
process=cleanUnscheduled(process)


# Customisation from command line
