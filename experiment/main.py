#!/usr/bin/python
# Filename: main.py
import os
import sys

# Import MobileInsight modules
from mobile_insight.monitor import OnlineMonitor
from mobile_insight.analyzer import Analyzer
from pprint import pprint


class CustomAnalyser(Analyzer):
    def __init__(self):
        super(CustomAnalyser, self).__init__()
        self.add_source_callback(self.callback)

    def set_source(self, source):
        super(CustomAnalyser, self).set_source(source)
        source.enable_log("LTE_MAC_UL_Transport_Block")
        source.enable_log("LTE_MAC_DL_Transport_Block")
        source.enable_log("LTE_PHY_PUSCH_CSF")
        source.enable_log("LTE_PHY_PUCCH_CSF")
        source.enable_log("LTE_PHY_PDCCH_PHICH_Indication_Report")
        source.enable_log("LTE_PHY_PDCCH_Decoding_Result")

    def callback(self, msg):
        if msg.type_id == 'LTE_PHY_PDCCH_Decoding_Result':
            data = msg.data.decode()
            pprint(data)


if __name__ == "__main__":
    src = OnlineMonitor()
    src.set_serial_port('/dev/ttyUSB0')  # the serial port to collect the traces
    src.set_baudrate(9600)  # the baudrate of the port

    analyser = CustomAnalyser()
    analyser.set_source(src)

    src.run()
