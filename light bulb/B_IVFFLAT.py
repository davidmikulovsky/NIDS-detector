#!/usr/bin/python

import time
import numpy as np
import faiss
import os
import sys
import getopt



def main(sys):
    np.seterr(over='ignore')
    m = len(sys)
    print ("The script has the name %s" % (sys[0]))
    print("initiate: %s " % (sys[0]))
    print ("Number of arguments: ", m, " arguments.")


    input_file_dataset = sys[1]
    input_file_queries = sys[2]
    k = int(sys[3])
    var = sys[4]
    run = sys[5]
    ground_truth_D = sys[6]
    ground_truth_I = sys[7]
    error = float(sys[8])
    nlist = int(sys[9])       #number of clusters
    nprobe = int(sys[10])          #how many times repeat search

    print("check of the arguments")
    for i in range(m):
        print("arguments: %s " % (sys[i]))



    dataset = os.path.realpath(input_file_dataset)
    queryset = os.path.realpath(input_file_queries)
    groundtruth_D = os.path.realpath(ground_truth_D)
    groundtruth_I = os.path.realpath(ground_truth_I)
    #ground_truth = os.path.realpath(output_file_gt)

    a_vectors = np.loadtxt(dataset).astype(np.float32)
    query_set = np.loadtxt(queryset).astype(np.float32)
    GT_D = np.loadtxt(groundtruth_D).astype(np.float32)
    GT_I = np.loadtxt(groundtruth_I).astype(np.float32)

    n_db = len(a_vectors)
    d = len(a_vectors[0])  #dimension of database
    n_q = len(query_set)


    # nlist = int(len(a_vectors) / k)  #number of clusters
    # nprobe = int((k/2)+1)          #how many times repeat search


    print("check of dimensions")
    print("param n_db",  n_db)
    print("param d",  d)
    print("param k",  k)
    print("param n_q",  n_q)
    print("param nlist",  nlist)
    print("param nprobe",  nprobe)
    print("param error",  error)



    print("faiss ...")
    start1 = time.clock()
    quantizer = faiss.IndexFlatL2(d)   # build the index
    index = faiss.IndexIVFFlat(quantizer, d, nlist, faiss.METRIC_L2)
    assert not index.is_trained
    index.train(a_vectors)
    assert index.is_trained
    index.add( a_vectors)
    stop1 = time.clock()


    start2 = time.clock()
    index.nprobe = nprobe  # if set to nlist = same as brute force, part of autotuning performance - speed accuracy tradeoff
    D, I = index.search(query_set, k)     # actual search
    stop2 = time.clock()



    #run recall
    recall_i = recall_similar_match( GT_I, I)
    recall_d = recall_with_error( GT_D, D, error)

    stringname_D = 'D' + sys[0][1:7] + '_' + var +'.txt'
    stringname_I = 'I' + sys[0][1:7] + '_' + var +'.txt'
    np.savetxt(stringname_D, D)
    np.savetxt(stringname_I, I)

    time1 = stop1 - start1
    time2 = stop2 - start2
    #run, filename, index_time,  build_time, recall_D, recall_I, n_db, n_q, d, k
    print_time(run, sys[0], time1, time2, recall_d, recall_i, n_db, n_q, d, k, error)
    print("finish")

#------#

#helper functions

#------#

def print_time(run, filename, index_time, build_time, recall_D, recall_I, n_db, n_q, d, k , error):


    # print("finish (total cpu time): ", (time.clock() - start)/60)

    total_time = index_time  +  build_time
    speed =  int(n_db/ build_time)

    #instr = "'{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}'".format(softname, procversion, int(percent), exe, description, company, procurl)
    with open('outputfile.txt', 'a') as file:
        file.write( "{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} , {12} \n".format( run, filename, index_time, build_time, total_time, speed, recall_D, recall_I, n_db, n_q, d, k, error))


#recall function for values




#recall function for values
def recall_similar_match( GT_I, I):
    if len(I) != len(GT_I) or len(I[0]) != len(GT_I[0]):
        print("dimensions of ground truth are not equal to the result ")
        return "error"

    counter = 0
    for i in range(len(I)):
        for j in range(len(I[i])):
            # check each value in I and, if they are contained in the list of GT_I[i]
            # if not count error
            #print(" ", GT_I[i][j], I[i][j])
            if I[i][j] not in GT_I[i]:
                counter = counter + 1

    #print("wrong values found ", counter)
    dimension = len(GT_I) * len(GT_I[0])
    print("total values in gt_I vs. errors ", dimension, counter)

    rec = float(dimension) - float(counter)
    #print(" rec", rec)
    rec =  (rec/float(dimension))*100
    #print(" rec", rec)


    #print ("recall by correct index: ", recall)
    print ("recall by correct index: ", rec, " %")
    return rec




#recall function for values
def recall_with_error( GT_D, D, error):

    if len(D) != len(GT_D) or len(D[0]) != len(GT_D[0]):
        print("dimensions of ground truth are not equal to the result ")
        return "error"

    counter = 0

    sum1 = 0
    sum2 = 0
    for i in range(len(D)):

        sum1 = np.sum(D[i])
        sum2 = np.sum(GT_D[i])


        sum2 = sum2 * (1+error)
        #print(np.sqrt(sum1), np.sqrt(sum2))
        if sum1 > sum2:
            #print (sum (D[i]), sum ((GT_D[i] * (1 + error))))
            #print (sum1, sum2)
            counter = counter + 1

        sum1 = 0
        sum2 = 0

    dimension = len(D)* len(D[0])

    rows = len(D)

    recall = (((float(rows) - float(counter)) / float(rows) ) * 100)

    print ("total values in gt vs. errors ", rows, counter)

    print("Total recall for D {0}  \n".format(recall))


    return recall



if __name__ == "__main__":
   main(sys.argv[0:])
