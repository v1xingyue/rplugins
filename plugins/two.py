#coding=utf-8

import state
import logging

def start(*args,**kwargs):
    logging.info(args)
    logging.info(kwargs)
    logging.info(state.get('a'))

