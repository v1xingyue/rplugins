#coding=utf-8

kvdb = {}

def set(k,v):
    kvdb[k] = v

def get(k):
    return kvdb[k]

#### LILO 后进后出
def nlist(k,v):
    kvdb[k] = [v]

def nadd(k,v):
    kvdb[k].append(v)

def nshift(k):
    return kvdb[v].popleft()

### LIFO Last In First Out
def nstack(k,v):
    kvdb[k] = [v]

def npush(k,v):
    kvdb[k].append(v)

def npop(k):
    kvdb[k].append(v)

#### hash 结构
def nhash(n,k,v):
    kvdb[n] = {}
    kvdb[n][k] = v

def nhashget(n,k):
    return kvdb[n][k]


