
precio = input("Escribe el precio del producto en 2 decimales:  ")
print(precio[:precio.find(".")], "euros y", precio[precio.find(".")+1:], "céntimos.")
