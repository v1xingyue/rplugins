#coding=utf-8

import sys
import logging
import importlib

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', datefmt='%a, %d %b %Y %H:%M:%S')

run_code = """
plugins.one
plugins.two
"""

for run_plugin_name in run_code.split("\n"):
    if run_plugin_name.strip() != "":
        r_plugin = importlib.import_module(run_plugin_name)
        r_plugin.start(sys.argv,a=15,b=30)

