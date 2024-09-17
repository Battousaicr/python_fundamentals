PASSWORD = "ASDFASDFAS"

def pre_checkout():
    return checkout(3,5,"Jorge")

def checkout(cantidad, precio, cliente):
    '''
    Aqui va todo el codigo
    '''
    # Variables locales
    variable_checkout1 = 1
    total = checkout_total(cantidad, precio) 
    resultado = "{} compro cantidad: {} \n con el precio: {} \n para total: {}".format(cliente,cantidad, precio, total)
    return resultado

def checkout_total(cantidad, precio):
    return cantidad * precio
