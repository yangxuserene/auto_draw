#!/usr/bin/python
from operator import truediv
import numpy as np
import matplotlib.pyplot as plt
import subprocess
import os

def sep_app_msg_stats(app_name, path):

    for subdir in next(os.walk(path))[1]:
        lp_output_folder = os.path.join(path, subdir)
        wkld_msg_stats_file = os.path.join(lp_output_folder, 'dragonfly-msg-stats')
        app_mpi_replay_stats_file = os.path.join(lp_output_folder, app_name+'.csv')
        header = open(wkld_msg_stats_file, 'r').readline()
        wkld_msg_stats = np.genfromtxt(wkld_msg_stats_file, delimiter=None, skip_header=1, names=['lpid', 'tid', 'datasize', 'time', 'packets', 'avghop','busytime'])

        #the APP.csv file is got by "grep "APP 0/1/2" mpi-replay-stats > APP.csv "
        app_mpi_replay_stats = np.genfromtxt(app_mpi_replay_stats_file, delimiter=None, names=['app', 'appid','rank', 'rankid', 'lpid', 'nwid', 'nsends', 'nrecvs', 'nbsent', 'nbrecv','sendtime','communtime','computetime'])

        #'tid' in wkld_msg_stats is correspondint to 'nwid' in app_mpi_replay_stats
        #transfrom ndarray to 2D array
        wkld = wkld_msg_stats.view(np.float64).reshape(len(wkld_msg_stats), -1)
        app  = app_mpi_replay_stats.view(np.float64).reshape(len(app_mpi_replay_stats), -1)

        app_nwid = app[:, 5]#get the 'nwid' of each app
        #according to nwid in application,  get corresponding rows of each app from workload data
        app_msg_stats = wkld[np.in1d(wkld[:,1], app_nwid)]
        #  print np.array_equal(app_msg_stats[:, 1],app_nwid)
        app_msg_stats_file = os.path.join(lp_output_folder, app_name+"-msg-stats.csv")
        with open(app_msg_stats_file, 'w') as outputfile:
            outputfile.write(header)
            np.savetxt(outputfile, app_msg_stats, delimiter=" ")

if __name__ == "__main__":
    subprocess.call("./getappfromwkld.sh")
    sep_app_msg_stats('AMG', '.')
    sep_app_msg_stats('CR', '.')
    sep_app_msg_stats('MG', '.')

