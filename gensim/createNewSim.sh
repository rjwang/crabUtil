#!bin/sh

logo=$1

cp FullSim_SAVE_cfg.py FullSim_${logo}_cfg.py
sed -i "s/SAVE/$logo/g" FullSim_${logo}_cfg.py

