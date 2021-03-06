#!/usr/bin/python

from operator import truediv
import numpy as np
import matplotlib.pyplot as plt
import subprocess
from operator import add
import os


def identify_router_of_app(nwid_list, wkld_router_info):
    #get each the group id and router id that belongs to each application
    groupsize = 32
    routersize = 4
    app_nwid = [int(x) for x in nwid_list]
    app_groupid = [int (x) / groupsize for x in app_nwid] 
    app_ingrouprouterid = [int ((x%groupsize)/ routersize) for x in app_nwid]

    #  print app1_nwid
    #  print app1_groupid
    #  print app1_ingrouprouterid
    #  print len(app1_groupid)
    #  print len(app1_ingrouprouterid)

    app_group_router_id = []
    for groupid,routerid in zip(app_groupid, app_ingrouprouterid):
        item = [groupid, routerid]
        if item not in app_group_router_id:#remove dumplicated
            app_group_router_id.append(item)
    #select rows in workload that belongs to each Application
    app_matrix = []
    for row in wkld_router_info:
        for item in app_group_router_id:
            if(row[1] == item[0] and row[2] == item[1]):
                app_matrix.append(row)

    return app_matrix





def sep_app_router_from_wkld(app_name, path, output_info='stats'):
    for subdir in next(os.walk(path))[1]:
        lp_output_folder = os.path.join(path, subdir)
        wkld_router_file = os.path.join(lp_output_folder, 'dragonfly-router-'+output_info)
        #  print wkld_router_file
        header = open(wkld_router_file, 'r').readline()
        all_router_data = np.genfromtxt(wkld_router_file, delimiter=None, skip_header=1, names=['lpid', 'groupid', 'routerid', 'lc1', 'lc2', 'lc3','lc4', 'lc5', 'lc6', 'lc7','lc8', 'gc1', 'gc2', 'gc3','gc4'])

        app_mpi_replay_stats_file = os.path.join(lp_output_folder, app_name+'.csv')
        #  print app_mpi_replay_stats_file
        app_mpi_replay_stats = np.genfromtxt(app_mpi_replay_stats_file, delimiter=None, names=['app', 'appid','rank', 'rankid', 'lpid', 'nwid', 'nsends', 'nrecvs', 'nbsent', 'nbrecv','sendtime','communtime','computetime'])

        allrouter = all_router_data.view(np.float64).reshape(len(all_router_data), -1)
        app = app_mpi_replay_stats.view(np.float64).reshape(len(app_mpi_replay_stats), -1)
        app_nwid = app[:,5]
        app_router_info = identify_router_of_app(app_nwid, allrouter)

        app_router_info_file = os.path.join(lp_output_folder, app_name+"_router_"+output_info+".csv")
        with open(app_router_info_file, 'w') as outputfile:
            outputfile.write(header)
            np.savetxt(outputfile, app_router_info, delimiter=" ")


if __name__ == "__main__":
    subprocess.call("./getappfromwkld.sh")
    sep_app_router_from_wkld('AMG', '.', 'traffic')
    sep_app_router_from_wkld('AMG', '.', 'stats')
    sep_app_router_from_wkld('MG', '.', 'traffic')
    sep_app_router_from_wkld('MG', '.', 'stats')
    sep_app_router_from_wkld('CR', '.', 'traffic')
    sep_app_router_from_wkld('CR', '.', 'stats')

