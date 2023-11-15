from expression_tree import ExpressionTree

expression_tree = ExpressionTree('')

while True:

    print('MENU\n1. Ingresar expresión aritmética\n2. Evaluar expresión aritmética\n3. Ver notaciones\n4. Salir')
    opcion = int(input('Ingrese una opcion: '))

    if opcion == 1:

        print('\n')

        print('Expresiones aritmeticas')
        print('Por ejemplo: ((j+2)*8)')
        expression = str(input('Ingrese su expresión aritmética: '))
        expression_tree = ExpressionTree(expression)

        print('Notacion prefija ->', expression_tree.prefijo())
        input('Presione cualquier tecla...')

        print('\n')

    elif opcion == 2:
        print('\n')

        variable = input('Ingrese la variable que se encuentra dentro de la expresion: ')
        number = int(input('Ingrese el numero a evaluar: '))
        print('Resultado de la evaluación: ', expression_tree.evaluate(number, variable))

        print('\n')

    elif opcion == 3:

        print('\n')
        print('---NOTACIONES---')
        print('Notacion prefija ->', expression_tree.prefijo())
        print('Notacion infija ->', expression_tree.infijo())
        print('Notacion postfija ->', expression_tree.postfijo())
        input('Presione cualquier tecla...')
        print('\n')

    elif opcion == 4:
        break

    else:
        raise Exception('No ingresaste alguna de las opciones :(')
