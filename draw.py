#!/usr/bin/python
from load_app_data import APP
import plot_method as pmd


if __name__ == "__main__":
    #  amg = APP('AMG', ['cyan', 'teal'])

    #  amg.load_commtime_data('.')
    #  pmd.comm_time_plot(amg, 10)

    #  amg.load_msg_data()
    #  pmd.msg_busytime_plot(amg,11)
    #  pmd.msg_avghop_plot(amg, 12)
    #  pmd.msg_latency_plot(amg,13)

    #  amg.load_router_stats_data()
    #  pmd.router_lch_stats_plot(amg, 14)
    #  pmd.router_gch_stats_plot(amg, 15)

    #  amg.load_router_traffic_data()
    #  pmd.router_gch_traffic_plot(amg, 16)
    #  pmd.router_lch_traffic_plot(amg, 17)

#===========================================
    #  mg = APP('MG', ['pink', 'purple'])

    #  mg.load_commtime_data('.')
    #  pmd.comm_time_plot(mg, 20)

    #  mg.load_msg_data()
    #  pmd.msg_busytime_plot(mg,21)
    #  pmd.msg_avghop_plot(mg, 22)
    #  pmd.msg_latency_plot(mg,23)

    #  mg.load_router_stats_data()
    #  pmd.router_lch_stats_plot(mg, 24)
    #  pmd.router_gch_stats_plot(mg, 25)

    #  mg.load_router_traffic_data()
    #  pmd.router_gch_traffic_plot(mg, 26)
    #  pmd.router_lch_traffic_plot(mg, 27)

#===========================================
    cr = APP('CR', ['blue', 'black'])

    cr.load_commtime_data('.')
    pmd.comm_time_plot(cr, 30)

    cr.load_msg_data()
    pmd.msg_busytime_plot(cr, 31)
    pmd.msg_avghop_plot(cr, 32)
    pmd.msg_latency_plot(cr, 33)

    cr.load_router_stats_data()
    pmd.router_lch_stats_plot(cr, 34)
    pmd.router_gch_stats_plot(cr, 35)

    cr.load_router_traffic_data()
    pmd.router_gch_traffic_plot(cr, 36)
    pmd.router_lch_traffic_plot(cr, 37)


#  ===========================================

    #  pmd.plt.show()
