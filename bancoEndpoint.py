from banco import *
from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/EntidadData/', methods=['GET'])
def Entidad():
    Entidad = request.args.get('EntidadNombre')
    return jsonify(getBancoInfo(Entidad))


@app.route('/EntidadLista/', methods=['GET'])
def EntidadLista():
    return jsonify(getEntidadLista())


@app.route('/dashboard/', methods=['GET', 'POST'])
def dashboard():
    if request.method=='POST':
        entidadList=getEntidadLista()
        entidad = request.values.get('entidad')
        entidadSingleList = getEntidadInfo(entidad)
        print(entidad)
        return render_template("dashboard.html",entidadList=entidadList, entidadSingleList=entidadSingleList)


    else:
        entidadList=getEntidadLista()
        return render_template("dashboard.html",entidadList=entidadList)




if __name__ == '__main__':
    app.run(host='139.144.35.12', port=5000, debug=True)  # run our Flask app
