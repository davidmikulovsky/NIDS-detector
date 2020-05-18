#!/usr/bin/bash


./algo_a.47.sif 'database_1K.txt' 'queries_1K.txt' 0 '1K_RAND' 2 'groundtruth_D_FLAT_1K_RAND.txt' 'groundtruth_I_FLAT_1K_RAND.txt' 0.2
./algo_a.53.sif 'database_10K.txt' 'queries_10K.txt' 100 '10K_RAND' 2 'groundtruth_D_FLAT_10K_RAND.txt' 'groundtruth_I_FLAT_10K_RAND.txt' 0.2
./algo_a.53.sif 'database_100K.txt' 'queries_100K.txt' 100 '100K_RAND' 2 'groundtruth_D_FLAT_100K_RAND.txt' 'groundtruth_I_FLAT_100K_RAND.txt' 0.2
./algo_a.53.sif 'database_1M.txt' 'queries_1M.txt' 1000 '1M_RAND' 2 'groundtruth_D_FLAT_1M_RAND.txt' 'groundtruth_I_FLAT_1M_RAND.txt' 0.2
./algo_a.53.sif 'database_10M.txt' 'queries_10M.txt' 1000 '10M_RAND' 2 'groundtruth_D_FLAT_10M_RAND.txt' 'groundtruth_I_FLAT_10M_RAND.txt' 0.2
./algo_a.53.sif 'database_100M.txt' 'queries_100M.txt' 10000 '100M_RAND' 2 'groundtruth_D_FLAT_100M_RAND.txt' 'groundtruth_I_FLAT_100M_RAND.txt' 0.2
