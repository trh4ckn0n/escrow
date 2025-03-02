from flask import Flask, render_template, request, redirect, url_for
from database import db, Signalement
from scraper import get_suspected_scammers

app = Flask(__name__)

# Configuration de la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'supersecret'

# Initialisation de la base de données
db.init_app(app)

@app.route('/')
def index():
    # Récupérer les signalements de la base de données
    signalements = Signalement.query.all()
    # Récupérer les arnaqueurs du web
    escrocs_web = get_suspected_scammers()
    return render_template('index.html', signalements=signalements, escrocs_web=escrocs_web)

@app.route('/signaler', methods=['GET', 'POST'])
def signaler():
    if request.method == 'POST':
        nom = request.form['nom']
        email = request.form['email']
        telephone = request.form['telephone']
        description = request.form['description']

        # Ajouter le nouveau signalement à la base de données
        nouveau_signalement = Signalement(nom=nom, email=email, telephone=telephone, description=description)
        db.session.add(nouveau_signalement)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('signaler.html')

if __name__ == '__main__':
    # Créer les tables de la base de données
    with app.app_context():
        db.create_all()

    # Lancer l'application Flask
    app.run(debug=False, host="0.0.0.0")
