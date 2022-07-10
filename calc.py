import hashlib

def hash_senha(senha):
  return hashlib.sha256(senha.encode()).hexdigest()

add_senha = '1234'
hash_senha1 = hash_senha(add_senha)

print('Return Function hash_senha: ' + hash_senha1)

def soma (num,num1):
    result = num + num1
    return result

print('Return Function soma: ', soma(5,5))