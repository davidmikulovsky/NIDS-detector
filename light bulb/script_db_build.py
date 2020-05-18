#!/usr/bin/python

import os
print("check from script")


print("initiate-building-db")

#s.system("python /00_building_database.py 'database_1K.txt' 'queries_1K.txt' n_db k d n_q")
os.system("python ./00_building_database.py 'database_1K.txt' 'queries_1K.txt' 1000 0 256 100")
os.system("python ./00_building_database.py 'database_10K.txt' 'queries_10K.txt' 10000 0 256 1000")
os.system("python ./00_building_database.py 'database_100K.txt' 'queries_100K.txt' 100000 0 256 10000")
os.system("python ./00_building_database.py 'database_1M.txt' 'queries_1M.txt' 1000000 0 256 10000")
os.system("python ./00_building_database.py 'database_10M.txt' 'queries_10M.txt' 10000000 0 256 100000")
os.system("python ./00_building_database.py 'database_100M.txt' 'queries_100M.txt' 100000000 0 256 100000")
os.system("python ./00_building_database.py 'database_1B.txt' 'queries_1B.txt' 1000000000 0 256 100000")

# os.system("python ./00_building_database.py 'database_100M_a.txt' 'queries_100M_a.txt' 20000000 0 256 20000")
# os.system("python ./00_building_database.py 'database_100M_b.txt' 'queries_100M_b.txt' 20000000 0 256 20000")
# os.system("python ./00_building_database.py 'database_100M_c.txt' 'queries_100M_c.txt' 20000000 0 256 20000")
# os.system("python ./00_building_database.py 'database_100M_d.txt' 'queries_100M_d.txt' 20000000 0 256 20000")
# os.system("python ./00_building_database.py 'database_100M_e.txt' 'queries_100M_e.txt' 20000000 0 256 20000")
