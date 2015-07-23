import numpy as np
import random
import pandas as pd

random_params = dict()
elements = dict()
num_elements = 0
num_functions = 16 # this is r
num_bands = 4 # this is b

def create_random_parameters():
    
    for i in range(num_functions):
        a = random.randint(1, num_elements)
        b = random.randint(1, num_elements)

        random_params[i] = [a, b]
        

    return

def read_meta_data(filename):
    global num_elements
    
    df = pd.read_csv(filename)
    col_names = list(df.columns)
    element_count = 0

    for col in col_names:
        elements[col] = element_count
        element_count = element_count + 1
    
##    for col in col_names:
##        col_levels = list(df[col].unique())
##        
##
##        for l in col_levels:
##            scoped_attrib_name = col + ":" + str(l)
##            if not scoped_attrib_name in elements:
##                elements[scoped_attrib_name] = element_count
##                element_count = element_count + 1

    num_elements = element_count

    return

def create_signature_matrix(filename):

    df = pd.read_csv(filename)

    num_cols = df.shape[0]

    num_rows = num_functions

    # signature matrix has num_function rows and num_records columns

    sig_mat = np.zeros((num_rows, num_cols))

    for i in range(num_rows):
        for j in range(num_cols):
            sig_mat[i,j] = 1e8 # a large number

    for index, doc in df.iterrows():
        
        for e in elements:
            r = elements[e]
            hash_values = generate_hash_values(r)
            #hash_values = verfiy_ur_example(r)
            

            if doc[e] == 1:
                for k in range(num_functions):
                    if hash_values[k] < sig_mat[k][index]:
                        sig_mat[k][index] = hash_values[k]
                      

    

    return sig_mat


def generate_hash_values(r):
    hash_values = list()

    for i in range(num_functions):
        a,b = random_params[i]
        hash_values.append((a + b*r) % num_elements)
    
    return hash_values

def verfiy_ur_example(r):
    hash_values = list()
    cv = [ [1,1], [1, 3]]
    for i in range(2):
        a,b = cv[i]
        hash_values.append((a + b*r) % num_elements)
    
    return hash_values

def min_hash():

    fp = "cvr_clean.csv"
    read_meta_data(fp)
    create_random_parameters()
    sig_mat = create_signature_matrix(fp)
    c = hash_sig_mat(sig_mat)

    return c

def hash_sig_mat(sig_mat):

    band_size = 4

    clusters = {i: dict() for i in range(band_size)}

    for index in range(num_bands):
        start_row = index * band_size
        end_row = start_row + band_size
        band = sig_mat[start_row : end_row, ]

        cb = clusters[index]

        doc_index = 0
        for doc in band.T:
            hv = hash(doc.tostring())

            if hv in cb:
                cb[hv].append(doc_index)
            else:
                cb[hv] = list()
                cb[hv].append(doc_index)
            doc_index = doc_index + 1    

    return clusters
