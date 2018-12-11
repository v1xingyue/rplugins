#coding=utf-8

kvdb = {}

def set(k,v):
    kvdb[k] = v

def get(k):
    return kvdb[k]

