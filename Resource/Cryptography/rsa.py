from factordb.factordb import FactorDB
from Crypto.Util.number import inverse, long_to_bytes

c = 964354128913912393938480857590969826308054462950561875638492039363373779803642185
n = 1584586296183412107468474423529992275940096154074798537916936609523894209759157543
e = 65537

f=FactorDB(n)
f.connect()
p,q=f.get_factor_list()

phi=(p-1)*(q-1)
d=inverse(e,phi)

t=pow(c,d,n)
print(long_to_bytes(t))

