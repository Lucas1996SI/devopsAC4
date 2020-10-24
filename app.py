import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(_name_)

@app.route('/')
def nao_entre_em_panico():
    a = 0
    b = 1
    c = 0
    retorno = ""
    for cont in range(50):
        c = a
        a = b + a
        b = c
        retorno += str(a) + ","

    return retorno

if _name_ == "_main_":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
