
# !/usr/bin/python

import os
import numpy as np
import random
import sys


# recall function for values
def recall_exact_match(GT_I, I):
    if len(I) != len(GT_I) or len(I[0]) != len(GT_I[0]):
        print("dimensions of ground truth are not equal to the result ")
        return "error"

    counter = 0
    for i in range(len(I)):
        for j in range(len(I[i])):
            if I[i][j] != GT_I[i][j]:
                counter = counter + 1

    print("wrong values found ", counter)
    dimension = len(I) * len(I[1])
    print("total values in gt ", dimension)

    recall = ((float(dimension) - float(counter)) / float(dimension)) * 100

    print("recall  ", recall)
    return recall

def modify( queries, error):

    queries_modified = np.copy(queries)

    #indexes for the correct size of db
    m = len(queries_modified)
    n = len(queries_modified[0])



    corrupt = error * m * n
    print("multiply", error , m , n)
    print("corrupt",corrupt)
    print("data",m*n, m, n)


    buffer_matrix = np.ones([m,n])
    buffer_matrix = buffer_matrix*(-1)

    counter = 0

    print(m, n)
    while counter < corrupt:
        for i in range(m):

            index_j = random.choice(list(set(range(0, n))))
            buffer_matrix[i][index_j] = index_j
            # print(counter, corrupt)
            counter += 1
            if queries_modified[i][index_j] == 1:
                queries_modified[i][index_j] = -1
            else:
                queries_modified[i][index_j] = 1

    print("counter, corrupt", counter, corrupt)

    return queries_modified


# funtion to generate queries from db
def generate_queries(a_v, n_q, error):


    #indexes for the correct size of db
    m = len(a_v[0])
    n = len(a_v)


    queries = np.ones((n_q,m))
    #queries_modified = np.ones((n_q,m))

    random_int = set()
    print(n_q)



    #generate queries at random from existing database, n_q is number of queries
    for i in range(n_q):
        tmp = random.choice(list(set(range(0, n)) - set(random_int)))
        queries[i] = a_v[tmp] #np.insert(queries, a_v[tmp], axis=0)
        #queries_modified[i] = a_v[tmp] #np.insert(queries_modified, a_v[tmp], axis=0)
        random_int.add(tmp)


    k = len(queries)
    l = len(queries[0])
    print("dkfkdsfk", k,l)


    #
    #
    # buffer_matrix = np.ones([k,l])
    # buffer_matrix = buffer_matrix*(-1)
    #
    # counter = 0
    #
    #
    # while counter < corrupt:
    #     for i in range(k):
    #
    #         index_j = random.choice(list(set(range(0, l))))
    #         buffer_matrix[i][index_j] = index_j
    #         # print(counter, corrupt)
    #         counter += 1
    #
    #         if queries_modified[i][index_j] == 1:
    #             queries_modified[i][index_j] = -1
    #         else:
    #             queries_modified[i][index_j] = 1
    #
    # print("counter, corrupt", counter, corrupt)

    return queries

def main(sys):
    np.random.seed(1234)  # make reproducible

    m = len(sys)
    print("The script has the name %s" % (sys[0]))
    print("initiate: %s " % (sys[0]))
    print("Number of arguments: ", m, " arguments.")

    input_file_dataset = sys[1]
    output_file_queries = sys[2]
    err = float(sys[3])
    n_q = int(sys[4])
    var = sys[5]
    it = int(sys[6])

    dataset = os.path.realpath(input_file_dataset)
    a_vectors = np.loadtxt(dataset).astype(np.float32)

    print("check of the arguments")
    for i in range(m):
        print("arguments: %s " % (sys[i]))

    queries = generate_queries(a_vectors, n_q, err)

    error = err
    for i in range(it):


        queries_modified = modify(queries,error)
        rec = recall_exact_match(queries, queries_modified)

        name1 = "Q_MOD_" + str(i) + var   +"{:.2f}".format(error)+  "_" +  "{:.2f}".format(rec) +"_"  + output_file_queries


        np.savetxt(name1, queries_modified)
        error = error + err
    print("finish")


    name = "Q_" + var + output_file_queries
    np.savetxt(name, queries)


if __name__ == "__main__":
    main(sys.argv[0:])
