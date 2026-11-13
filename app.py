from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('inicio.html')


@app.route('/compra', methods=['GET', 'POST'])
def compra():

    resultado = None

    if request.method == 'POST':

        cantidad = float(request.form['cantidad'])
        precio = float(request.form['precio'])

        subtotal = cantidad * precio

        if subtotal > 1000:
            descuento = subtotal * 0.10
        else:
            descuento = 0

        total = subtotal - descuento

        resultado = {
            'cantidad': cantidad,
            'precio': precio,
            'subtotal': subtotal,
            'descuento': descuento,
            'total': total
        }

    return render_template('compra.html',
                           resultado=resultado)


@app.route('/salario', methods=['GET', 'POST'])
def salario():

    resultado = None

    if request.method == 'POST':

        horas = float(request.form['horas'])
        pago = float(request.form['pago_hora'])

        if horas <= 40:
            salario_total = horas * pago
        else:
            extras = horas - 40
            salario_total = (40 * pago) + (extras * pago * 2)

        resultado = {
            'horas': horas,
            'pago': pago,
            'salario': salario_total
        }

    return render_template('salario.html',
                           resultado=resultado)


@app.route('/temperatura', methods=['GET', 'POST'])
def temperatura():

    resultado = None

    if request.method == 'POST':

        celsius = float(request.form['celsius'])

        fahrenheit = (celsius * 9/5) + 32
        kelvin = celsius + 273.15

        resultado = {
            'celsius': celsius,
            'fahrenheit': fahrenheit,
            'kelvin': kelvin
        }

    return render_template('temperatura.html',
                           resultado=resultado)


@app.route('/empresa')
def empresa():
    return render_template('empresa.html')


@app.route('/servicios')
def servicios():
    return render_template('servicios.html')


@app.route('/contacto')
def contacto():
    return render_template('contacto.html')


if __name__ == '__main__':
    app.run(debug=True, port=5050)
