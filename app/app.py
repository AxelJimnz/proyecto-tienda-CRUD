
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@db/recauderia_db'
db = SQLAlchemy(app)

# Definir el modelo primero
class Reporte(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    contenido = db.Column(db.Text)

# Crear las tablas dentro del contexto de la aplicación
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    reportes = Reporte.query.all()
    return render_template('index.html', reportes=reportes)

@app.route('/catalogo')
def catalogo():
    return render_template('catalogo.html')

@app.route('/ofertas')
def ofertas():
    return render_template('ofertas.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/add', methods=['POST'])
def add():
    titulo = request.form.get('titulo')
    contenido = request.form.get('contenido')
    nuevo_reporte = Reporte(titulo=titulo, contenido=contenido)
    db.session.add(nuevo_reporte)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    reporte = Reporte.query.get(id)
    reporte.titulo = request.form.get('titulo')
    reporte.contenido = request.form.get('contenido')
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    reporte = Reporte.query.get(id)
    db.session.delete(reporte)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        print(f"Error: {e}")