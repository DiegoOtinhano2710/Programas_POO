from flask import Flask, render_template, request, flash, redirect, url_for
from sqlalchemy import func
from models import db, Sucursal, Repartidor, Transporte, Paquete
from datetime import datetime
import os

def create_app():
    app=Flask(__name__)
    app.secret_key = os.urandom(24)
    base_dir = os.path.abspath(os.path.dirname(__file__))
    database_path = os.path.join(base_dir, 'datos.sqlite3')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{database_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route('/')
    def inicio():
        lista_sucursales=Sucursal.query.all()
        return render_template('inicio.html', sucursales=lista_sucursales)
    
    @app.route('/paquete/<int:sucursal_id>', methods=['GET','POST'])
    def paquete(sucursal_id):
        try:
            sucursal=Sucursal.query.get(sucursal_id)
            if request.method == 'POST': 
                peso = request.form.get('peso')
                peso = float(peso)
                if peso.is_integer():
                    peso = int(peso)
                nomdestinatario = request.form.get('nomdestino')
                dirdestinatario = request.form.get('dirdestino')
                entregado = False  # El campo entregado se pone en False por defecto
                ultimo_numeroenvio = db.session.query(func.max(Paquete.numeroenvio)).scalar() or 0
                # Crea una instancia de la clase Paquete con los datos recibidos
                nuevo_paquete = Paquete(numeroenvio=ultimo_numeroenvio + 1, peso=peso, nomdestinatario=nomdestinatario,
                                        dirdestinatario=dirdestinatario, entregado=entregado,observaciones=None , idsucursal=sucursal.id, 
                                        idtransporte=None, idrepartidor=None) 
                # Guarda el paquete en la base de datos
                db.session.add(nuevo_paquete)
                db.session.commit()
                flash("¡Paquete registrado correctamente!")
        except Exception as e:
            db.session.rollback()
            flash(f"Error al registrar el paquete: {str(e)}")
            return redirect(url_for('paquete', sucursal_id=sucursal_id))
        return render_template('registro_paquete.html', sucursal_id=sucursal_id)

    
    @app.route('/salida_transporte/<int:sucursal_id>', methods=['GET','POST'])
    def salida_transporte(sucursal_id):
        lista_paquetes=Paquete.query.all()
        return render_template('salida_transporte.html', sucursal_id=sucursal_id, lista_paquetes=lista_paquetes)

    @app.route('/registrar_transporte/<int:sucursal_id>', methods=['GET', 'POST'])
    def registrar_transporte(sucursal_id):
        if request.method != 'POST':
            return redirect(url_for('salida_transporte', sucursal_id=sucursal_id))
        paquetes_elegidos = request.form.getlist('paquetes')
        if not paquetes_elegidos:
            flash('Error: No se seleccionaron paquetes para el transporte.', 'error')
            return redirect(url_for('salida_transporte', sucursal_id=sucursal_id))
        try:
            # Crea el transporte con destino a esa sucursal
            ultimo_numerotransporte = db.session.query(func.max(Transporte.numerotransporte)).scalar() or 0
            nuevo_transporte = Transporte(numerotransporte=ultimo_numerotransporte + 1, fechahorasalida=datetime.now(),
                                          fechahorallegada=None,idsucursal=sucursal_id)
            db.session.add(nuevo_transporte)
            db.session.flush()  # Para obtener el ID del nuevo transporte
            # Asigna el transporte a cada paquete elegido
            paquetes_asignados = 0
            for paquete_id in paquetes_elegidos:
                try:
                    paquete = Paquete.query.get(int(paquete_id))
                    if paquete:
                        paquete.idtransporte = nuevo_transporte.id
                        paquetes_asignados += 1
                    else:
                        flash(f'Advertencia: No se encontró el paquete con ID {paquete_id}', 'warning')
                except ValueError:
                    flash(f'Error: ID de paquete inválido: {paquete_id}', 'error')
            db.session.commit()
            flash(f'¡Transporte asignado correctamente a {paquetes_asignados} paquete(s)!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error inesperado al asignar el transporte: {str(e)}', 'error')
        return redirect(url_for('salida_transporte', sucursal_id=sucursal_id))

    @app.route('/llegada_transporte/<int:sucursal_id>', methods=['GET','POST'])
    def llegada_transporte(sucursal_id):
        lista_transporte=Transporte.query.all()
        return render_template('llegada_transporte.html', sucursal_id=sucursal_id, lista_transporte=lista_transporte)

    @app.route('/registrar_llegada/<int:sucursal_id>', methods=['GET','POST'])
    def registrar_llegada(sucursal_id):
        try: 
            transporte_id = request.form.get('transporte')
            if transporte_id is None:
                raise ValueError("No se seleccionó ningún transporte")
            
            transporte = Transporte.query.get(int(transporte_id))
            if transporte is None:
                raise ValueError(f"No se encontró el transporte con ID {transporte_id}")
            
            transporte.fechahorallegada = datetime.now()
            db.session.commit()
            flash('¡El transporte llegó con éxito!')
        except Exception as e:
            db.session.rollback()
            flash(f'Error al asignar la llegada del transporte: {str(e)}')
        return redirect(url_for('llegada_transporte', sucursal_id=sucursal_id))


    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)




