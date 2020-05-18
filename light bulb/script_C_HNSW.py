#!/usr/bin/bash

#HNSWFLAT efsearch 128
./algo_a.80.sif 'database_1K.txt' 'queries_1K.txt' 10 '1K_RAND' -1 'groundtruth_D_FLAT_1K_RAND.txt' 'groundtruth_I_FLAT_1K_RAND.txt' 0.2


#HNSWFLAT efsearch 128
./algo_a.80.sif 'database_1K.txt' 'queries_1K.txt' 10 'v1_1K_RAND' 7 'groundtruth_D_FLAT_1K_RAND.txt' 'groundtruth_I_FLAT_1K_RAND.txt' 0.2  &
./algo_a.80.sif 'database_10K.txt' 'queries_10K.txt' 100 'v1_10K_RAND' 7 'groundtruth_D_FLAT_10K_RAND.txt' 'groundtruth_I_FLAT_10K_RAND.txt' 0.2  &
./algo_a.80.sif 'database_100K.txt' 'queries_100K.txt' 100 'v1_100K_RAND' 7 'groundtruth_D_FLAT_100K_RAND.txt' 'groundtruth_I_FLAT_100K_RAND.txt' 0.2  &
./algo_a.80.sif 'database_1M.txt' 'queries_1M.txt' 1000 'v1_1M_RAND' 7 'groundtruth_D_FLAT_1M_RAND.txt' 'groundtruth_I_FLAT_1M_RAND.txt' 0.2  &
./algo_a.80.sif 'database_10M.txt' 'queries_10M.txt' 1000 'v1_10M_RAND' 7 'groundtruth_D_FLAT_10M_RAND.txt' 'groundtruth_I_FLAT_10M_RAND.txt' 0.2  &
./algo_a.80.sif 'database_1K.txt' 'queries_1K.txt' 10 'v2_1K_RAND' 7 'groundtruth_D_FLAT_1K_RAND.txt' 'groundtruth_I_FLAT_1K_RAND.txt' 0.4  &
./algo_a.80.sif 'database_10K.txt' 'queries_10K.txt' 100 'v2_10K_RAND' 7 'groundtruth_D_FLAT_10K_RAND.txt' 'groundtruth_I_FLAT_10K_RAND.txt' 0.4  &
./algo_a.80.sif 'database_100K.txt' 'queries_100K.txt' 100 'v2_100K_RAND' 7 'groundtruth_D_FLAT_100K_RAND.txt' 'groundtruth_I_FLAT_100K_RAND.txt' 0.4  &
./algo_a.80.sif 'database_1M.txt' 'queries_1M.txt' 1000 'v2_1M_RAND' 7 'groundtruth_D_FLAT_1M_RAND.txt' 'groundtruth_I_FLAT_1M_RAND.txt' 0.4  &
./algo_a.80.sif 'database_10M.txt' 'queries_10M.txt' 1000 'v2_10M_RAND' 7 'groundtruth_D_FLAT_10M_RAND.txt' 'groundtruth_I_FLAT_10M_RAND.txt' 0.4  &
#./algo_a.69.sif 'database_100M.txt' 'queries_100M.txt' 10000 '100M_RAND' 4 'groundtruth_D_FLAT_100M_RAND.txt' 'groundtruth_I_FLAT_100M_RAND.txt' 0.2
