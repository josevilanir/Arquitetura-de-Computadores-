import math
from classes import classe, separador_rs,separador_rt,separador_rd
from conversorbinario import binario
from conversorhex import sephex




with open ("braulio.txt","r") as file:
  lista = file.readlines()
  linhas_de_codigo = len(lista) 
  n = 0
  functiones = "00000"
  op_code = "000000"
  camarão = "00000"


for n in range(linhas_de_codigo):
  if "add" in (lista[n]):
    op_code = op_code
    rs = separador_rs(lista[n])
    rt = separador_rt(lista[n])
    rd = separador_rd(lista[n])


    bin_rs = binario(rs)
    bin_rt = binario(rt)
    bin_rd = binario(rd)
    functiones = "100000"
    comando = op_code + bin_rs + bin_rt + bin_rd + camarão + functiones
    print(lista[n])
    print(sephex(comando))
    n+=1
  elif "sub" in (lista[n]):
    op_code = op_code
    rs = separador_rs(lista[n])
    rt = separador_rt(lista[n])
    rd = separador_rd(lista[n])


    bin_rs = binario(rs)
    bin_rt = binario(rt)
    bin_rd = binario(rd)
    functiones = "100010"
    comando = op_code + bin_rs + bin_rt + bin_rd + camarão + functiones
    print(lista[n])
    print(sephex(comando))
    n+=1 
  
  


