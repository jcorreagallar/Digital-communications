import numpy as np
from random import randint

def redundancyBits(l): 
    for k in range(l): 
        if 2**k >= l + k + 1: 
            return k

def generateMatrix(l,c):
  gen_matrix = np.identity(l,dtype=int)
  for i in range(c):
    new_row = np.ones((1,l),dtype= int)
    new_row[0][i] = 0
    gen_matrix = np.append(gen_matrix,new_row, axis=0)
  return gen_matrix

def operationMatrix(word,gen_matrix):
    N = len(gen_matrix)
    l = len(word)
    result = word * gen_matrix
    aux_code = np.zeros((1,l),dtype = int)
    aux_bits = np.zeros((1,N-l),dtype = int)

    for i in range(len(gen_matrix)):
        if i >= l:
          vec_aux = result[i]
          vec_aux = np.delete(vec_aux,i-l)
          P = None
          for j in range(len(vec_aux)):
              if j > 1:
                P = P ^ vec_aux[j]
              elif j == 1:
                P = vec_aux[j] ^ vec_aux[j-1]
          aux_bits[0][i-l] = P
        else:
          aux_code[0][i] = result[i][i]
    return aux_code, aux_bits

def orderedCode(code,bits_parity):
    l = len(code[0])
    s = len(bits_parity[0])
    N = l + s 
    hamming = np.zeros((1,N),dtype = int)
    for pos in range(1,len(hamming[0]) + 1):
      if len(bits_parity[0]) > 0 and (pos == 1 or pos % 2 == 0):
        hamming[0][pos-1] = bits_parity[0][0]
        bits_parity = np.delete(bits_parity,0)
        bits_parity = np.reshape(bits_parity,(1,len(bits_parity)))
      else:
        hamming[0][pos-1] = code[0][0]
        code = np.delete(code,0)
        code = np.reshape(code,(1,len(code)))
    return hamming

def tx(message):
    pos = randint(0,len(message[0])-1)
    message[0][pos] = randint(0,1)
    return message 

def rx(receive,c):
  l = len(receive[0]) - c
  redundant_row = []
  data_row = []

  for pos in range(1,len(receive[0]) + 1):
    if len(redundant_row) < c and (pos == 1 or pos % 2 == 0):
      redundant_row = np.append(redundant_row, receive[0][pos - 1])
    else:
      data_row = np.append(data_row, receive[0][pos - 1])
  
  matrix = generateMatrix(l,c)
  matrix = matrix[l:]
  result = np.array(data_row, dtype=int) * matrix
  aux_bits = np.zeros((1,c),dtype = int)
  for i in range(len(matrix)):
      vec_aux = result[i]
      vec_aux = np.delete(vec_aux,i)
      P = None
      for j in range(len(vec_aux)):
        if j > 1:
          P = P ^ vec_aux[j]
        elif j == 1:
          P = vec_aux[j] ^ vec_aux[j-1]
      aux_bits[0][i] = P ^ np.array(redundant_row[i],dtype=int)
  return aux_bits.dot(2**np.arange(aux_bits.size)[::-1])

word = [0,1,1,0]
l = len(work)
c = redundancyBits(l)
gen_matrix = generateMatrix(l,c)
code, bits_parity= operationMatrix(work,gen_matrix)
hamming = orderedCode(code,bits_parity)
print("Código enviado:", hamming)
send = tx(hamming)
print("Código recibido:", send)
result = rx(send,c)
print("Error en el bit:" , result)


