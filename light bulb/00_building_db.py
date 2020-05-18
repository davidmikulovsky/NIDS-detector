#!/usr/bin/python

import time
import numpy as np
#import faiss
import os
import sys
import getopt

def main(sys):


    np.random.seed(1234)  # make reproducible

    m = len(sys)
    print("The script has the name %s" % (sys[0]))
    print("initiate: %s " % (sys[0]))
    print("Number of arguments: ", m, " arguments.")

    output_file_dataset = sys[1]
    #output_file_queries = sys[2]


    print("check of the arguments")
    for i in range(m):
        print("arguments: %s " % (sys[i]))



    n_db = int(sys[3])
    k = int(sys[4])
    d = int(sys[5])
    n_q = int(sys[6])


    a_v = np.random.choice([-1, 1], size=(int(n_db), int(d))).astype('float32')
    np.savetxt(output_file_dataset, a_v)
    # q_s = np.random.choice([-1, 1], size=(int(n_q), int(d))).astype('float32')
    # np.savetxt(output_file_queries, q_s)

    print("database built...")

    print(a_v)
    print(q_s)


    print("finish")



if __name__ == "__main__":
   main(sys.argv[0:])
