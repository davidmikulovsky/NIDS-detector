#!/usr/bin/bash

./algo_a.91.sif 'database_10K.txt' 'queries_10K.txt' 100 'vA_10K_RAND' 9 'groundtruth_D_FLAT_10K_RAND.txt' 'groundtruth_I_FLAT_10K_RAND.txt' 0.2 'OPQ32_64,IVF256_HNSW32,PQ32' &
./algo_a.91.sif 'database_100K.txt' 'queries_100K.txt' 100 'vA_100K_RAND' 9 'groundtruth_D_FLAT_100K_RAND.txt' 'groundtruth_I_FLAT_100K_RAND.txt' 0.2 'OPQ32_64,IVF2048_HNSW32,PQ32' &
./algo_a.91.sif 'database_1M.txt' 'queries_1M.txt' 1000 'vA_1M_RAND' 9 'groundtruth_D_FLAT_1M_RAND.txt' 'groundtruth_I_FLAT_1M_RAND.txt' 0.2 'OPQ32_64,IVF16384_HNSW32,PQ32' &
./algo_a.91.sif 'database_10M.txt' 'queries_10M.txt' 1000 'vA_10M_RAND' 9 'groundtruth_D_FLAT_10M_RAND.txt' 'groundtruth_I_FLAT_10M_RAND.txt' 0.2 'OPQ32_64,IVF65536_HNSW32,PQ32' &
./algo_a.91.sif 'database_10K.txt' 'queries_10K.txt' 100 'vB_10K_RAND' 9 'groundtruth_D_FLAT_10K_RAND.txt' 'groundtruth_I_FLAT_10K_RAND.txt' 0.4 'OPQ32_64,IVF256_HNSW32,PQ32' &
./algo_a.91.sif 'database_100K.txt' 'queries_100K.txt' 100 'vB_100K_RAND' 9 'groundtruth_D_FLAT_100K_RAND.txt' 'groundtruth_I_FLAT_100K_RAND.txt' 0.4 'OPQ32_64,IVF2048_HNSW32,PQ32' &
./algo_a.91.sif 'database_1M.txt' 'queries_1M.txt' 1000 'vB_1M_RAND' 9 'groundtruth_D_FLAT_1M_RAND.txt' 'groundtruth_I_FLAT_1M_RAND.txt' 0.4 'OPQ32_64,IVF16384_HNSW32,PQ32' &
./algo_a.91.sif 'database_10M.txt' 'queries_10M.txt' 1000 'vB_10M_RAND' 9 'groundtruth_D_FLAT_10M_RAND.txt' 'groundtruth_I_FLAT_10M_RAND.txt' 0.4 'OPQ32_64,IVF65536_HNSW32,PQ32'


#./algo_a.69.sif 'database_100M.txt' 'queries_100M.txt' 10000 '100M_RAND' 4 'groundtruth_D_FLAT_100M_RAND.txt' 'groundtruth_I_FLAT_100M_RAND.txt' 0.2
