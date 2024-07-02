"""
# Legenda das variaveis da função
arg1 = alcohol_price
arg2 = gasoline_price
arg3 = alcohol_city
arg4 = gasoline_city
"""

# Função para calcular qual combustível é mais vantajoso.
def fplus(arg1, arg2, arg3, arg4):
    arg1 = float(arg1)
    arg2 = float(arg2)
    arg3 = float(arg3)
    arg4 = float(arg4)
    
    # Calcular a performance
    alcohol_performance = round(arg3 / arg4 - 0.01, 2)
    
    # Para saber qual combustível é mais econômico
    which_fuel = round(arg1 / arg2, 2)
    
    # Para determinar qual é mais vantajoso
    if which_fuel <= alcohol_performance:
        return 'Alcohol'
    else:
        return 'Gasoline'



"""
# Chamando a função para testes
#teste = fplus(3.63, 5.61, 9.8, 14.2)
#teste = fplus(3.63, 5.61, 8.2, 10.4)
#teste = fplus(3.85, 5.05, 9.8, 14.2)
teste = fplus(3.85, 4.91, 6.2, 8.3)
print(teste)
"""

