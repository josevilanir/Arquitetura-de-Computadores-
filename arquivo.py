import math
from classes import classe, immedieate, separador_rs,separador_rt,separador_rd,separadordiv_rs,separadordiv_rt,immedieate
from conversorbinario import binario
from conversorhex import sephex
from binario_constante import binario_constante




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
    
  elif "div" in (lista[n]):
      op_code  = op_code
      camarão = "0000000000"
      rs = separadordiv_rs(lista[n])
      rt = separadordiv_rt(lista[n])
     


      bin_rs = binario(rs)
      bin_rt = binario(rt)
      
      functiones = "011010"
      comando = op_code + bin_rs + bin_rt + camarão + functiones
      print(lista[n])
      print(sephex(comando))
      n+=1 
  elif "syscall" in (lista[n]):
      op_code = op_code
      codigo = "00000000000000000000"
      functiones = "001100"
      comando = op_code + codigo + functiones
      print(lista[n])
      print(sephex(comando))
      n+=1 
  elif "and" in (lista[n]):
      op_code = op_code
      rs = separador_rs(lista[n])
      rt = separador_rt(lista[n])
      rd = separador_rd(lista[n])


      bin_rs = binario(rs)
      bin_rt = binario(rt)
      bin_rd = binario(rd)
      functiones = "100100"
      camarão = '00000'
      comando = op_code + bin_rs + bin_rt + bin_rd + camarão + functiones
      print(lista[n])
      print(sephex(comando))
      n+=1 
  elif "mul" in (lista[n]):
      op_code = "011100"  
      rs = separador_rs(lista[n])
      rt = separador_rt(lista[n])
      rd = separador_rd(lista[n])


      bin_rs = binario(rs)
      bin_rt = binario(rt)
      bin_rd = binario(rd)
      functiones = "000010"
      camarão = '00000'
      comando = op_code + bin_rs + bin_rt + bin_rd + camarão + functiones
      print(lista[n])
      print(sephex(comando))
      n+=1 
  elif "nor" in (lista[n]):
      op_code = "000000"  
      rs = separador_rs(lista[n])
      rt = separador_rt(lista[n])
      rd = separador_rd(lista[n])


      bin_rs = binario(rs)
      bin_rt = binario(rt)
      bin_rd = binario(rd)
      functiones = "100111"
      camarão = '00000'
      comando = op_code + bin_rs + bin_rt + bin_rd + camarão + functiones
      print(lista[n])
      print(sephex(comando))
      n+=1 
  elif "nop" in (lista[n]):
      comando = "00000000000000000000000000000000"
      print(lista[n])
      print(sephex(comando))
      n+=1 
  elif "ori" in (lista[n]):
      op_code = "001101"
      rs = separadordiv_rs(lista[n])
      rt = separadordiv_rt(lista[n])
      bin_rs = binario(rs)
      bin_rt = binario(rt)
      constante = immedieate(lista[n])
      bin_constante = binario_constante(constante)
      comando = op_code + bin_rt + bin_rs + bin_constante
      print(lista[n])
      print(sephex(comando))
      n+=1 
  elif "sll" in (lista[n]):
      op_code = "000000"
      functiones = "000000"
      ra = "00000"
      rs = separador_rs(lista[n])
      rd = separador_rd(lista[n])
      bin_rs = binario(rs)
      bin_rd = binario(rd)
      sa = immedieate(lista[n])
      bin_sa = binario(sa)
      comando = op_code+ra+bin_rs+bin_rd+bin_sa+functiones
      print(lista[n])
      print(sephex(comando))
      n+=1 
