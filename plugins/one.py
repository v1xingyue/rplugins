#coding=utf-8

import logging
import state

def start(*args,**kwargs):
    state.set("a","b from plugin one")
    logging.info(args)
    logging.info(kwargs)
