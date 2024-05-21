from obtener_rango_ip import obtener_direcciones_de_red


red = input("Ingrese red: ")
mask = input("Ingrese Mascara /")
rango_de_red = red+"/"+mask

rango1 = obtener_direcciones_de_red(rango_de_red)
largo = (len(rango1))
rango = (largo/2)
rango = int(rango)