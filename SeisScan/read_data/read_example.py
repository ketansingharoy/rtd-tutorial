import os
import json
import pickle

def read_example():
    """
    Description:
        Reads example data. This function returns Obspy.Stream, a list of reference_secondaries and a path to earth model.
    """

    #--- example data directory
    data_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
    data_dir = os.path.realpath(data_dir)

    #--- load data_file that contains obspy stream
    data_file = os.path.join(data_dir, "okl_wavefields-20160711-055516_allsta.p")
    st = pickle.load(open(data_file, "rb"))

    #--- load rs_file that contains list of reference_secondaries combinations
    rs_file = os.path.join(data_dir, "reference_secondaries_combinations.json")
    rs_list = json.load(open(rs_file, "r"))

    #--- get earth model file path
    model_file = os.path.join(data_dir, "okl.tvel")
    
    return st, rs_list, model_file
