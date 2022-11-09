import math
from classes import classe, immedieate, separador_rs,separador_rt,separador_rd,separadordiv_rs,separadordiv_rt,immedieate,separador_rdi,separador_rti,separador_rsi,immedieatei,separador_rdiu,separador_rsiu,immedieateiu,separador_rsor,separador_rtor,separador_rdor
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
with open("hex_braulio.txt","w") as file:
  file.write("Instruções")

for n in range(linhas_de_codigo):
  if "add " in (lista[n]):
    op_code = op_code
    rs = separador_rs(lista[n])
    rt = separador_rt(lista[n])
    rd = separador_rd(lista[n])


    bin_rs = binario(rs)
    bin_rt = binario(rt)
    bin_rd = binario(rd)
    functiones = "100000"
    comando = op_code + bin_rs + bin_rt + bin_rd + camarão + functiones
    with open("hex_braulio.txt","a") as file:
      file.write("\n"+sephex(comando))
    n+=1
  elif "sub " in (lista[n]):
    op_code = op_code
    rs = separador_rs(lista[n])
    rt = separador_rt(lista[n])
    rd = separador_rd(lista[n])


    bin_rs = binario(rs)
    bin_rt = binario(rt)
    bin_rd = binario(rd)
    functiones = "100010"
    comando = op_code + bin_rs + bin_rt + bin_rd + camarão + functiones 
    with open("hex_braulio.txt","a") as file:
      file.write("\n"+sephex(comando))
    n+=1  
  elif "div " in (lista[n]):
      op_code  = op_code
      camarão = "0000000000"
      rs = separadordiv_rs(lista[n])
      rt = separadordiv_rt(lista[n])
     


      bin_rs = binario(rs)
      bin_rt = binario(rt)
      
      functiones = "011010"
      comando = op_code + bin_rs + bin_rt + camarão + functiones
      
      with open("hex_braulio.txt","a") as file:
        file.write("\n"+sephex(comando)) 
      n+=1
  elif "syscall" in (lista[n]):
      op_code = op_code
      codigo = "00000000000000000000"
      functiones = "001100"
      comando = op_code + codigo + functiones
      n+=1
      with open("hex_braulio.txt","a") as file:
        file.write("\n"+sephex(comando)) 
  elif "and " in (lista[n]):
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
      with open("hex_braulio.txt","a") as file:
        file.write("\n"+sephex(comando)) 
      n+=1
  elif "mul " in (lista[n]):
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
      with open("hex_braulio.txt","a") as file:
        file.write("\n"+sephex(comando)) 
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
      with open("hex_braulio.txt","a") as file:
        file.write("\n"+sephex(comando)) 
      n+=1
  elif "nop" in (lista[n]):
      comando = "00000000000000000000000000000000"
      
      with open("hex_braulio.txt","a") as file:
        file.write("\n"+sephex(comando))
      n+=1 
  elif "ori" in (lista[n]):
    if (lista[n])[0]=="o":
        op_code = "001101"
        rs = separadordiv_rs(lista[n])
        rt = separadordiv_rt(lista[n])
        bin_rs = binario(rs)
        bin_rt = binario(rt)
        constante = immedieate(lista[n])
        bin_constante = binario_constante(constante)
        comando = op_code + bin_rt + bin_rs + bin_constante
      
        with open("hex_braulio.txt","a") as file:
          file.write("\n"+sephex(comando))
        n+=1   
    else:
      op_code = "001110"
      rs = separador_rdi(lista[n])
      rt = separador_rsi(lista[n])
      bin_rs = binario(rs)
      bin_rt = binario(rt)
      constante = immedieatei(lista[n])
      bin_constante = binario_constante(constante)
      comando = op_code +bin_rt+bin_rs+ bin_constante
      with open("hex_braulio.txt","a") as file:
        file.write("\n"+sephex(comando))   
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
      with open("hex_braulio.txt","a") as file:
        file.write("\n"+sephex(comando)) 
      n+=1 
  elif "slt " in (lista[n]):
    op_code = "000000"
    rs = separador_rs(lista[n])
    rt = separador_rt(lista[n])
    rd = separador_rd(lista[n])


    bin_rs = binario(rs)
    bin_rt = binario(rt)
    bin_rd = binario(rd)
    functiones = "101010"
    camarão = "00000"
    comando = op_code + bin_rs + bin_rt + bin_rd + camarão + functiones
    with open("hex_braulio.txt","a") as file:
      file.write("\n"+sephex(comando)) 
    n+=1
  elif "sra" in (lista[n]):
    op_code = "000000"
    functiones = "000011"
    ra = "00000"
    rs = separador_rs(lista[n])
    rd = separador_rd(lista[n])
    bin_rs = binario(rs)
    bin_rd = binario(rd)
    sa = immedieate(lista[n])
    bin_sa = binario(sa)
    comando = op_code+ra+bin_rs+bin_rd+bin_sa+functiones
    
    with open("hex_braulio.txt","a") as file:
      file.write("\n"+sephex(comando))
    n+=1
  elif "srl" in (lista[n]):
    op_code = "000000"
    functiones = "000010"
    ra = "0000"
    r = "0"
    rs = separador_rs(lista[n])
    rd = separador_rd(lista[n])
    bin_rs = binario(rs)
    bin_rd = binario(rd)
    sa = immedieate(lista[n])
    bin_sa = binario(sa)
    comando = op_code+ra+r+bin_rs+bin_rd+bin_sa+functiones
    with open("hex_braulio.txt","a") as file:
      file.write("\n"+sephex(comando))
    n+=1
  elif "xor " in (lista[n]):
    op_code = "000000"
    rs = separador_rs(lista[n])
    rt = separador_rt(lista[n])
    rd = separador_rd(lista[n])


    bin_rs = binario(rs)
    bin_rt = binario(rt)
    bin_rd = binario(rd)
    functiones = "100110"
    camarão = "00000"
    comando = op_code + bin_rs + bin_rt + bin_rd + camarão + functiones
    
    with open("hex_braulio.txt","a") as file:
      file.write("\n"+sephex(comando))
    n+=1
  elif "addi " in (lista[n]):
    op_code = "001000"
    rs = separador_rdi(lista[n])
    rt = separador_rsi(lista[n])
    bin_rs = binario(rs)
    bin_rt = binario(rt)
    constante = immedieatei(lista[n])
    bin_constante = binario_constante(constante)
    comando = op_code +bin_rt+bin_rs+ bin_constante
    with open("hex_braulio.txt","a") as file:
      file.write("\n"+sephex(comando)) 
    n+=1
  
  elif "addu" in (lista[n]):
    op_code = "000000"
    rs = separador_rsi(lista[n])
    rt = separador_rti(lista[n])
    rd = separador_rdi(lista[n])


    bin_rs = binario(rs)
    bin_rt = binario(rt)
    bin_rd = binario(rd)
    functiones = "100001"
    camarão = "00000"
    comando = op_code + bin_rs + bin_rt + bin_rd + camarão + functiones
    with open("hex_braulio.txt","a") as file:
      file.write("\n"+sephex(comando))
    n+=1
  elif "andi" in (lista[n]):
    op_code = "001100"
    rs = separador_rdi(lista[n])
    rt = separador_rsi(lista[n])
    bin_rs = binario(rs)
    bin_rt = binario(rt)
    constante = immedieatei(lista[n])
    bin_constante = binario_constante(constante)
    comando = op_code +bin_rt+bin_rs+ bin_constante
    with open("hex_braulio.txt","a") as file:
      file.write("\n"+sephex(comando))
    n+=1 
  
  elif "divu" in (lista[n]):
    op_code  = "000000"
    camarão = "0000000000"
    rs = separador_rdi(lista[n])
    rt = separador_rsi(lista[n])
     


    bin_rs = binario(rs)
    bin_rt = binario(rt)
      
    functiones = "011011"
    comando = op_code + bin_rs + bin_rt + camarão + functiones
     
    with open("hex_braulio.txt","a") as file:
      file.write("\n"+sephex(comando))
    n+=1
  elif "mult " in (lista[n]):
    op_code = "000000"  
    rs = separador_rsi(lista[n])
    rd = separador_rdi(lista[n])


    bin_rs = binario(rs)
    
    bin_rd = binario(rd)
    functiones = "011000"
    camarão = '0000000000'
    comando = op_code  + bin_rd+bin_rs + camarão + functiones
    
    with open("hex_braulio.txt","a") as file:
      file.write("\n"+sephex(comando)) 
    n+=1
  elif "slti " in (lista[n]):
    op_code = "001010"
    rs = separador_rdi(lista[n])
    rt = separador_rsi(lista[n])
    bin_rs = binario(rs)
    bin_rt = binario(rt)
    constante = immedieatei(lista[n])
    bin_constante = binario_constante(constante)
    comando = op_code +bin_rt+bin_rs+ bin_constante 
    with open("hex_braulio.txt","a") as file:
      file.write("\n"+sephex(comando))
    n+=1
  
  elif "sltu" in (lista[n]):
    op_code = "000000"
    rs = separador_rsi(lista[n])
    rt = separador_rti(lista[n])
    rd = separador_rdi(lista[n])


    bin_rs = binario(rs)
    bin_rt = binario(rt)
    bin_rd = binario(rd)
    functiones = "101011"
    camarão = "00000"
    comando = op_code + bin_rs + bin_rt + bin_rd + camarão + functiones
    with open("hex_braulio.txt","a") as file:
      file.write("\n"+sephex(comando))
    n+=1
  elif "subu" in (lista[n]):
    op_code = "000000"
    rs = separador_rsi(lista[n])
    rt = separador_rti(lista[n])
    rd = separador_rdi(lista[n])


    bin_rs = binario(rs)
    bin_rt = binario(rt)
    bin_rd = binario(rd)
    functiones = "100011"
    camarão = "00000"
    comando = op_code + bin_rs + bin_rt + bin_rd + camarão + functiones
    
    with open("hex_braulio.txt","a") as file:
      file.write("\n"+sephex(comando))
    n+=1
  
  elif "addiu" in (lista[n]):
    op_code = "001001"
    rs = separador_rdiu(lista[n])
    rt = separador_rsiu(lista[n])
    bin_rs = binario(rs)
    bin_rt = binario(rt)
    constante = immedieateiu(lista[n])
    bin_constante = binario_constante(constante)
    comando = op_code +bin_rt+bin_rs+ bin_constante

    with open("hex_braulio.txt","a") as file:
      file.write("\n"+sephex(comando)) 
    n+=1
  elif "multu" in (lista[n]):
    op_code = "000000"  
    rs = separador_rsiu(lista[n])
    rd = separador_rdiu(lista[n])


    bin_rs = binario(rs)
    
    bin_rd = binario(rd)
    functiones = "011001"
    camarão = '0000000000'
    comando = op_code  + bin_rd+bin_rs + camarão + functiones
    
    with open("hex_braulio.txt","a") as file:
      file.write("\n"+sephex(comando)) 
    n+=1
  elif "sltiu" in (lista[n]):
    op_code = "001011"
    rs = separador_rdiu(lista[n])
    rt = separador_rsiu(lista[n])
    bin_rs = binario(rs)
    bin_rt = binario(rt)
    constante = immedieateiu(lista[n])
    bin_constante = binario_constante(constante)
    comando = op_code +bin_rt+bin_rs+ bin_constante
    with open("hex_braulio.txt","a") as file:
      file.write("\n"+sephex(comando)) 
    n+=1
  elif "or " in (lista[n]):
    op_code = "000000"
    rs = separador_rsor(lista[n])
    rt = separador_rtor(lista[n])
    rd = separador_rdor(lista[n])
    bin_rs = binario(rs)
    bin_rt = binario(rt)
    bin_rd = binario(rd)
    functiones = "100101"
    camarão = "00000"
    comando = op_code + bin_rs + bin_rt + bin_rd + camarão + functiones
    with open("hex_braulio.txt","a") as file:
      file.write("\n"+sephex(comando))
    n+=1



