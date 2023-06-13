from flask import Flask, render_template, request
'''
    request
        show the information solicitada by the client
        Only its functional into of the ENDPOINT
'''
from datetime import datetime

#   As it is microframework it is neccesary to install each library
from flask_cors import CORS

'''
Creando la instancia de la clase Flask
__name__
    variable propia de Python
    indica que este es el archivo principal del proyecto
'''       
app=Flask(__name__)


#   The class CORS, en caso se le asigne solamente las instancia de la clase Flask, entonces modificara los CORS para que pueden ser accedidos por todo el mundo, (cualquier origen, metodo, cabecera (header) )
CORS(app)
#   CORS(app=app)  <-  funciona igual


#   make list for data of tuples
products=[]


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


@app.route('/route_dictionaire')
def def_route_dictionaire():
    #  strftime : string for time
    return {
        'hour':datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    }

@app.route('/route_test')
def def_route_test():
    return render_template('/frontend/index.html')


@app.route('/products',methods=['POST'])
def products_management():
    #   .get_json()     <-      convert the Json que el cliente envia a un diccionario para que python lo pueda entender
    print(request.get_json())
    product=request.get_json()
    products.append(product)
    return {
        'message':'Succesfully created product',
        'content':product
    }

@app.route('/return_products',methods=['GET'])
def list_of_producs():
    return{
        'message':'Los productos son:',
        'content':products
    }

'''
    Se encuentra en espera de posibles peticiones en tiempo indeterminado
debug
    -   true : ante la deteccion de cambios en el codigo automaticamente se reinicia y 
        agrega los nuevos cambios
    -   default value : False
'''
app.run(
    debug=True
)

