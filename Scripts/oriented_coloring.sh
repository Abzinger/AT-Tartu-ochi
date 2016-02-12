#!/bin/sh
echo 'Script oriented_coloring on node '`hostname`': procid='$SLURM_PROCID

echo Setting Gurobi licens file path to '~/Gurobi_Licenses/'`hostname`/gurobi.lic
export GRB_LICENSE_FILE=$HOME/Gurobi_Licenses/`hostname`/gurobi.lic

echo cd\'ing to '~/Oriented_Coloring_Project/Computation/procid-'$SLURM_PROCID
cd $HOME/Oriented_Coloring_Project/Computation/procid-$SLURM_PROCID

echo Executing python: python3 ../../Code/grid_IP_color_new.py tournaments `echo grid-* | sed 's/\.txt//'`
python3 ../../Code/grid_IP_color_new.py tournaments `echo grid-* | sed s/\.txt//`|| echo crash
#echo "No, not really, I'll just ls what's in this folder:"
#ls -hal
