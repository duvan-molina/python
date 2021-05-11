menu = """
Bienvenido al conversor de moneda 💰
1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos
Elige una opción: """

option = int(input(menu))

def converter(pesos, value_dollar):
  dollar = pesos / value_dollar
  dollar = round(dollar, 2)
  dollar = str(dollar)
  return dollar
  
def showMessage(message, coin):
  pesos = float(input("¿Cuantos pesos " + message + " tienes?: "))
  print("Tienes en total: $" + converter(pesos, coin) + " dólares")

if option == 1:
  showMessage("colombianos", 3875)
elif option == 2:
  showMessage("argentinos", 65)
elif option == 3:
  showMessage("mexicanos", 24)
else:
  print("Ingresa una opción correcta")  