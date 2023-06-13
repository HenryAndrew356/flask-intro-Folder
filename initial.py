from flask import Flask, render_template
from datetime import datetime


'''
Creando la instancia de la clase Flask
__name__
    variable propia de Python
    indica que este es el archivo principal del proyecto
'''       
app=Flask(__name__)




'''
Endpoint
decorator
    patron de software
        Usado para modificar el comportamiento del metodo de una clase sin
        necesidad de aplicar otros metodos como herencia
        Tampoco es necesario modificar el comportamiento del metodo de dicha clase
'''
@app.route('/')
def initialRoute():
    print('Ingreso al endpoint Inicial')
    return 'Bienvenido al endpoint inicial'


@app.route('/route_02')
def def_rout3_02():
    return {
        'hour':datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    }

@app.route('/ruta_test')
def def_route_test():
    return render_template('/frontend/index.html')

'''
Levantameinto del servidor
    Se encuentra en espera de posibles peticiones en tiempo indeterminado

debug
    -   true : ante la deteccion de cambios en el codigo automaticamente se reinicia y 
        agrega los nuevos cambios
    -   default value : False
'''
app.run(
    debug=True
)

