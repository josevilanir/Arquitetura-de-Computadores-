from turtle import rt
import math
registradores = {'$0 ':"0",'$at':'1','$v0':'2','$v1':'3','$a0':'4','$a1':'5','$a2':'6','$a3':'7','$t0':'8','$t1':'9','$t2':'10','$t3':'11','$t4':'12','$t5':'13','$t6':'14','$t7':'15','$s0':'16','$s1':'17','$s2':'18','$s3':'19','$s4':'20','$s5':'21','$s6':'22','$s7':'23','$t8':'24','$t9':'25','$k0':'26','$k1':'27','$gp':'28','$sp':'29','$fp':'30','$ra':'31'}

def separador_rs(linha_codigo):
  rs = linha_codigo[8]+linha_codigo[9]+linha_codigo[10]
  rs_regis = registradores[rs]
  return rs_regis

def separador_rt(linha_codigo):
  rt = linha_codigo[12]+linha_codigo[13]+linha_codigo[14]
  rt_regis = registradores[rt]
  return rt_regis

def separador_rd(linha_codigo):
  rd = linha_codigo[4]+linha_codigo[5]+linha_codigo[6]
  rd_regis = registradores[rd]
  
  return rd_regis

def separadordiv_rs(linha_codigo):
  rs = linha_codigo[4]+linha_codigo[5]+linha_codigo[6]
  rs_regis = registradores[rs]
  return rs_regis

def separadordiv_rt(linha_codigo):
  rt = linha_codigo[8]+linha_codigo[9]+linha_codigo[10]
  rt_regis = registradores[rt]
  return rt_regis

def immedieate(linha_codigo):
    constante = linha_codigo[12]+linha_codigo[13]
    constante=  str(constante)
    return constante
def immedieatei(linha_codigo):
    if len(linha_codigo)==14:
      constante = linha_codigo[13]
      constante=  str(constante)
      return constante
    elif len(linha_codigo)==15:
      constante = linha_codigo[13]+linha_codigo[14]
      constante=  str(constante)
      return constante
    elif len(linha_codigo)==16:
      constante = linha_codigo[13]+linha_codigo[14]+linha_codigo[15]
      constante=  str(constante)
      return constante
    elif len(linha_codigo)==17:
      constante = linha_codigo[13]+linha_codigo[14]+linha_codigo[15]+linha_codigo[16]
      constante=  str(constante)
      return constante
    elif len(linha_codigo)==18:
      constante = linha_codigo[13]+linha_codigo[14]+linha_codigo[15]+linha_codigo[16]+linha_codigo[17]
      constante=  str(constante)
      return constante
def immedieateiu(linha_codigo):
    if len(linha_codigo)==15:
      constante = linha_codigo[14]
      constante=  str(constante)
      return constante
    elif len(linha_codigo)==16:
      constante = linha_codigo[14]+linha_codigo[15]
      constante=  str(constante)
      return constante
    elif len(linha_codigo)==17:
      constante = linha_codigo[14]+linha_codigo[15]+linha_codigo[16]
      constante=  str(constante)
      return constante
    elif len(linha_codigo)==18:
      constante = linha_codigo[14]+linha_codigo[15]+linha_codigo[16]+linha_codigo[17]
      constante=  str(constante)
      return constante
    elif len(linha_codigo)==19:
      constante = linha_codigo[14]+linha_codigo[15]+linha_codigo[16]+linha_codigo[17]+linha_codigo[18]
      constante=  str(constante)
      return constante
def separador_rti(linha_codigo):
  rt = linha_codigo[13]+linha_codigo[14]+linha_codigo[15]
  rt_regis = registradores[rt]
  return rt_regis

def separador_rdi(linha_codigo):
  rd = linha_codigo[5]+linha_codigo[6]+linha_codigo[7]
  rd_regis = registradores[rd]
  
  return rd_regis
def separador_rsi(linha_codigo):
  rs = linha_codigo[9]+linha_codigo[10]+linha_codigo[11]
  rs_regis = registradores[rs]
  return rs_regis
def separador_rdiu(linha_codigo):
  rd = linha_codigo[6]+linha_codigo[7]+linha_codigo[8]
  rd_regis = registradores[rd]
  return rd_regis
def separador_rsiu(linha_codigo):
  rs = linha_codigo[10]+linha_codigo[11]+linha_codigo[12]
  rs_regis = registradores[rs]
  return rs_regis
def classe(linha_codigo):
    if "add" or "Add" in linha_codigo:
      opcode = "000000"
      rs = bin(rs)
      rt = bin(rt)
      rd = bin(rd)
      shamt = "00000"
      func = "100000"
      if "SUB" in func:
        func = "100010"
    codigo = opcode + rs + rt + rd +shamt + func
    return codigo

def separador_rsor(linha_codigo):
  rs = linha_codigo[7]+linha_codigo[8]+linha_codigo[9]
  rs_regis = registradores[rs]
  return rs_regis

def separador_rtor(linha_codigo):
  rt = linha_codigo[11]+linha_codigo[12]+linha_codigo[13]
  rt_regis = registradores[rt]
  return rt_regis

def separador_rdor(linha_codigo):
  rd = linha_codigo[3]+linha_codigo[4]+linha_codigo[5]
  rd_regis = registradores[rd]
  
  return rd_regis













