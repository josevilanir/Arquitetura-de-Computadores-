def binario_constante(x):
  dividendo = int(x)
  numero_digitado = dividendo
  quociente = 1
  lista = []

  while quociente >= 1:
    resto = dividendo%2
    lista.insert(0,resto)
    quociente = dividendo // 2
    dividendo = quociente

  antonio = ''.join([str(item) for item in lista])
  antonio_int = int(antonio)
  return "{:016d}".format(antonio_int)