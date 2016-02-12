#!/bin/sh
#SBATCH -p main                # partition (queue)
#SBATCH -N 19
#SBATCH --ntasks-per-node 15
#SBATCH -t 8-
#SBATCH --mem-per-cpu 3G
srun -l $HOME/Oriented_Coloring_Project/oriented_coloring.sh
