import math
from binariotodecimal import carlos

def sephex(x):
  x = int(x)
  um = x%10000
  x = (x - um)//10000 
  dois = x%10000
  x = (x - dois)//10000 
  tres = x%10000
  x = (x - tres)//10000 
  quatro = x%10000
  x = (x - quatro)//10000 
  cinco = x%10000
  x = (x - cinco)//10000 
  seis = x%10000
  x = (x - seis)//10000 
  sete = x%10000
  x = (x - sete)//10000 
  oito = x%10000
  x = (x - oito)//10000 
  
  um_decimal = carlos(um)
  dois_decimal = carlos(dois)
  tres_decimal = carlos(tres)
  quatro_decimal = carlos(quatro)
  cinco_decimal = carlos(cinco)
  seis_decimal = carlos(seis)
  sete_decimal = carlos(sete)
  oito_decimal = carlos(oito)
  
  
  
  
  
  um_hex = hex(um_decimal)[2:]
  dois_hex = hex(dois_decimal)[2:]
  tres_hex = hex(tres_decimal)[2:]
  quatro_hex = hex(quatro_decimal)[2:]
  cinco_hex = hex(cinco_decimal)[2:]
  seis_hex = hex(seis_decimal)[2:]
  sete_hex = hex(sete_decimal)[2:]
  oito_hex = hex(oito_decimal)
  
  codigo = oito_hex+sete_hex+seis_hex+cinco_hex+quatro_hex+tres_hex+dois_hex+um_hex
  return codigo