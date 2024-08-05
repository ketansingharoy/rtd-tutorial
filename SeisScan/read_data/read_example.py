import os
import json
import pickle
from obspy import read_inventory
from obspy.taup import taup_create

def read_example():
    """
    Returns example data. This function returns Obspy.Stream, a list of reference_secondaries and a path to earth model.
    """

    #--- example data directory
    data_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
    data_dir = os.path.realpath(data_dir)
    
    #--- read event information
    event_file = os.path.join(data_dir, "evt_dict.json")
    event_dict = json.load(open(event_file, "r"))

    #--- load data_file that contains obspy stream
    data_file = os.path.join(data_dir, "okl_wavefields-20160711-055516_allsta.p")
    st = pickle.load(open(data_file, "rb"))
    
    #--- read inventory file
    stationxml_file = os.path.join(data_dir, "station-okl.xml")
    inventory = read_inventory(stationxml_file)

    #--- load rs_file that contains list of reference_secondaries combinations
    rs_file = os.path.join(data_dir, "reference_secondaries_combinations.json")
    rs_list = json.load(open(rs_file, "r"))

    #--- get earth model file path
    model_file = os.path.join(data_dir, "okl.tvel")
    model_name = os.path.splitext(os.path.basename(model_file))[0]
    taup_create.build_taup_model(model_file, verbose=False)
    
    return event_dict, st, inventory, rs_list, model_name
