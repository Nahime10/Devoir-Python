from flask import Blueprint, render_template,request,redirect
from flask_login import login_required
from .models import User

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def login():
    message = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if email == "" or password == "":
            message = "Tous les champs sont obligatoires"
            return render_template("login.html", message=message)
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            if password == existing_user.password:
                return redirect("/acceuil")
            else:
                message = "Mot de passe incorrect"
                return render_template("login.html", message=message)
        else:
            message = "Compte avec cette adresse e-mail n'existe pas"
            return render_template("login.html", message=message)
    return render_template("login.html")
