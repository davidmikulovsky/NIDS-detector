
# #!/usr/bin/python
#

import time
import numpy as np
import faiss
import os
import sys
import getopt





def print_time(run, run_i, filename, index_time, build_time, recall_a, recall_b, recall_c, n_db, n_q, d, k , error, step, var):


    # print("finish (total cpu time): ", (time.clock() - start)/60)

    total_time = index_time  +  build_time
    speed =  int(n_db/ build_time)

    #instr = "'{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}'".format(softname, procversion, int(percent), exe, description, company, procurl)
    with open('outputfile_new.txt', 'a') as file:
        file.write( "{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} , {12}, {13}, {14}, {15}, {16} \n".format( run, run_i, filename, index_time, build_time, total_time, speed, recall_a, recall_b, recall_c, n_db, n_q, d, k, error, step, var))


#recall function for values


def recall_exact_match( GT_I, I):
    if len(I) != len(GT_I) or len(I[0]) != len(GT_I[0]):
        print("dimensions of ground truth are not equal to the result ")
        return "error"

    counter = 0
    for i in range(len(I)):
        for j in range(len(I[i])):
            if I[i][j] != GT_I[i][j]:

                counter = counter + 1

    print("wrong values found ", counter)
    dimension = I.shape[0] * I.shape[1]
    print("total values in gt ", dimension)

    recall = ((dimension - counter) / dimension ) * 100

    print ("recall  ", recall)
    return recall

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





def A_FLAT(a_vectors, query_set, d, k):




    print("faiss ...")
    start1 = time.clock()

    index = faiss.IndexFlatL2(d)  # build the index
    index.add(a_vectors)  # add vectors to the index
    stop1 = time.clock()

    start2 = time.clock()
    D, I = index.search(query_set, k)  # actual search
    stop2 = time.clock()

    time1 = 0  # no index build
    stop2 = time.clock()
    # stop2 = time.process_time()
    time1 = stop1 - start1
    time2 = stop2 - start2
    # run, filename, index_time,  build_time, recall_D, recall_I, n_db, n_q, d, k

    return D, I, time1, time2

def main(sys):

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
    step = float(sys[8])


    print("check of the arguments")
    for i in range(m):
        print("arguments: %s " % (sys[i]))



    dataset = os.path.realpath(input_file_dataset)
    queryset = os.path.realpath(input_file_queries)
    #ground_truth = os.path.realpath(output_file_gt)

    a_vectors = np.loadtxt(dataset).astype(np.float32)
    query_set = np.loadtxt(queryset).astype(np.float32)

    n_db = len(a_vectors)
    d = len(a_vectors[0])  #dimension of database
    n_q = len(query_set)
    k = n_q
    error = step

    print("check of dimensions")
    print("param n_db",  n_db)
    print("param d",  d)
    print("param n_q",  n_q)

    step = 0
    GT_D, GT_I, time1, time2 = A_FLAT(a_vectors, query_set, d, k)
    print_time(run, 0, sys[0], time1, time2, 0, 0, 0, n_db, n_q, d, k, error, step, var)


    for i in range(int(run)):

        D, I, time1, time2 = A_FLAT(a_vectors, query_set, d, k)

        rec_a = recall_exact_match(GT_I, I)
        rec_b = recall_similar_match(GT_I, I)
        rec_c = recall_with_error(GT_D, D, error)


        print_time(run, i + 1, sys[0], time1, time2, rec_a, rec_b,rec_c, n_db, n_q, d, k, error, step, var )

        error = error + step

    stringname_D = ground_truth_D + var + '.txt'
    stringname_I = ground_truth_I + var + '.txt'
    np.savetxt(stringname_D, D)
    np.savetxt(stringname_I, I)




if __name__ == "__main__":
   main(sys.argv[0:])
