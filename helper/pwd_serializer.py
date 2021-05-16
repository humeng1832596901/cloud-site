from itsdangerous import TimedJSONWebSignatureSerializer as SafeSerializer
from config import SECRET_KEY
def dumps_data(data):
    #生成校验令牌，令牌有效期为十分钟
    s = SafeSerializer(SECRET_KEY,expires_in = 600)
    return s.dumps(data)

def loads_data(data):
    #检验令牌
    s = SafeSerializer(SECRET_KEY)
    try:
        return s.loads(data)
    except:
        return -1

#测试
'''
token = dumps_data(47)
print(token)
token_s = ""
tmp = str(token)
for i in range(2,len(tmp)-1):
    token_s += tmp[i]
print(bytes(token_s,encoding='utf-8'))
user = loads_data(bytes(token_s,encoding='utf-8'))
print(user)
print(type(user))
'''
#print(loads_data(b'eyJhbGciOiJIUzUxMiIsImlhdCI6MTYyMTE0NDk3MSwiZXhwIjoxNjIxMTQ4NTcxfQ.NDc.Ntw4zptEnzlmytkGg8zNP9jXZQdhnxvnTyGbNKxONUPcbReP1GEfr6BRc5ukewPojmtjCORe0slzQ_pJUTtvZg'))
#print(loads_data(b'eyJhbGciOiJIUzUxMiIsImlhdCI6MTYyMTE0NTEyOSwiZXhwIjoxNjIxMTQ4NzI5fQ.NDU.Ixon1h9514R8Ck8GfN7TlBih11KacrhYOFX2WzCkYiKxc5wZCZOdOyHO7tvgo2m_0yLZPAs1dReq2s5J9EydFg'))
