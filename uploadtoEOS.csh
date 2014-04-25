#!bin/csh

foreach ifile (*.root)
	echo $ifile
	eos cp $ifile /eos/cms/store/user/rewang/dijet_HLTMu17v_HLTEle17CaloIdTCaloIsoVLTrkIdVLTrkIsoVLv/
end
