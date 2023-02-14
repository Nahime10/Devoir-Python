from website import db
from flask import Blueprint, render_template, request, redirect, url_for
from .models import User
import re

auth = Blueprint('auth', __name__)

@auth.route('/signup')
def home():
    return render_template('sign-up.html')


@auth.route('/logout')
def logout():
    return redirect(url_for('views.login'))



@auth.route('/acceuil')
def acceuil():
    return render_template('index.html')

@auth.route('/submit', methods=['GET', 'POST'])
def submit():
    message = ""
    if request.method == 'POST':
        firstname = request.form["nom"]
        fname = request.form["prenom"]
        mail = request.form["email"]
        password1 = request.form["password1"]
        password2 = request.form["confirm_password"]
        new_user = User(nom=firstname, prenom=fname, email=mail, password=password1)
        existing_user = User.query.filter_by(email=mail).first()

        if not all([firstname, fname, mail, password1, password2]):
            message = "Tous les champs sont obligatoires"
            return render_template("sign-up.html", message=message)
        elif password1 != password2:
            message2 = "Les mots de passe ne correspondent pas"
            return render_template("sign-up.html", message=message2)
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", mail):
            message3 = "Adresse e-mail non valide"
            return render_template("sign-up.html", message=message3)
        elif existing_user:
            message4 = "Un compte avec cette adresse e-mail existe déjà"
            return render_template("sign-up.html", message=message4)    
        else:
            try:
                db.session.add(new_user)
                db.session.commit()
                return redirect('/')
            except Exception:
                message5 = "Erreur lors de l'enregistrement, veuillez réessayer plus tard"
                return render_template("sign-up.html", message=message5)
    return render_template("sign-up.html")
