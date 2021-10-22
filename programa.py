from flask import Flask
from flask.helpers import url_for
from flask import render_template
from flask.templating import render_template_string

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     a = 12
#     data = {}
#     data["pavadinimas"] = "Titulinis"
#     data["duomenys"] = "<p>Hello, World!</p><p>" + str(a) + "</p>"
    
#     return render_template("bendras.html", data=data)

@app.route("/")
def titulinis():
    return render_template('bendras_sablonas.html')

@app.route("/paieska/")
def paieska():
    return render_template('paieska.html')

@app.route("/register/")
def registracija():
    return render_template('bendras_sablonas.html')

@app.route("/subscribe/")
def prenumerata():
    return render_template('prenumerata.html')


@app.route("/daugybos_lentele/")
def lentele():
    lentele = '<table class="table table-striped table-bordered ">'
    lentele += '<tr>'
    for a in range(1, 10):

        lentele += '<td>'
        for b in range(1, 11):
            # lentele += str(a) + ' &times; ' + str(b) + ' = ' + str(a * b) + '<br>'
            lentele += '{} &times; {} = {}<br>'.format(a, b, a*b)
        lentele += '</td>'
        
        if a % 3 == 0:
            lentele += '</tr>'
            if a != 9:
                lentele += '<tr>'

    # lentele += '</tr>'

    lentele += '</table>'


    lentele = render_template('lenteles_sablonas.html')


    return render_template('daugyba.html', lentele=lentele)

@app.route("/sachmatu_lenta/")
def sachmatai():
    return render_template('bendras_sablonas.html')

@app.route("/kalendorius/")
def kalendorius():
    return render_template('bendras_sablonas.html')






# senas kodas

@app.route("/pirmas/")
def pirmas_funkcija():
    data = {}
    data["pavadinimas"] = "Pirmas puslapis"
    data["duomenys"] = "<p>Pirmas vidinis puslapis</p>"
    
    return render_template("bendras.html", data=data)

counter = 0

@app.route("/skaitliukas/")
def skaitliukas():
    global counter
    counter += 1
    return "<p>" + str(counter) + "</p>" + url_for("pirmas_funkcija")

@app.route("/skaitliukas/<reset>")
def skaitliukas_reset(reset):
    global counter
    counter = int(reset)
    return "<p>" + str(counter) + "</p>"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")