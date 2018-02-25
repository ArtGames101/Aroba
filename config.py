try:
    from user import logindata as l
except:
    pass
try:
    NAMETAG = l.USERNAME
except:
    NAMETAG = None
currentgame = 'snake'
