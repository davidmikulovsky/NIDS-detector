#!/usr/bin/python

import os
print("check from script")



#./algo_a.43.sif 'database_10K.txt' 'queries_10K.txt' k variance_in_namename


#os.system("python vi {value for value in variable}./algo_a.43.sif 'database_1K.txt' 'queries_1K.txt' 10 '1_KRAND' ")
os.system("python ./algo_a.43.sif 'database_10K.txt' 'queries_10K.txt' 100 '10KRAND' ")
os.system("python ./algo_a.43.sif 'database_100K.txt' 'queries_100K.txt' 100 '100KRAND' ")
os.system("python ./algo_a.43.sif 'database_1M.txt' 'queries_1M.txt' 1000 '1M_RAND' ")
os.system("python ./algo_a.43.sif 'database_10M.txt' 'queries_10M.txt' 1000 '10M_RAND' ")
#os.system("python ./algo_a.43.sif 'database_100M.txt' 'queries_100M.txt' 100 '10K' ")
