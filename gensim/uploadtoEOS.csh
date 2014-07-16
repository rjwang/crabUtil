#!bin/csh

foreach ifile (*.root)
	echo $ifile
	eos cp $ifile /eos/cms/store/user/rewang/AODSIM/EFT_Wimps_8TeV/
end
