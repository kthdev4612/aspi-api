from flask import request, render_template



def form():
    print('formulaire')

    return render_template('index.html')