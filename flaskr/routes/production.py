from flask import Blueprint, request 
from controllers.productionController import *
from flask import render_template, redirect
from flask import flash
from flask import g
from flask import session


productionsbp = Blueprint('production', __name__, template_folder='templates', url_prefix='/productions')

@productionsbp.route('/', methods=['GET'])
def index():
    print("ruta '/' -> Index de productoras")
    return render_template('productions/index.html', productions=read_productions())

@productionsbp.route('/productions_filtered', methods=['GET'])
def movies_filtered():
    print("ruta '/productions_filtered' -> Index de productoras")
    min_foundation_year = request.args.get('min')
    max_foundation_year = request.args.get('max')
   
    return render_template('productions/index.html', productions = read_productions_by_filter(min_foundation_year=min_foundation_year,max_foundation_year=max_foundation_year))


@productionsbp.route('/<alias>', methods=['GET'])
def show(alias):
    number_notable_movies=get_number_of_notable_movies(alias)
    print("ruta '/<production_alias>' -> Mostrar una película")
    print(number_notable_movies)
    return render_template('productions/show.html', production=read_production(alias),number_notable_movies=number_notable_movies)


# @productionsbp.route('/<slug>/comments', methods=['POST'])
# def create_comment_route(slug):
#     print("ruta POST a '/<movie_slug>/comments' -> Crear un comentario")
#     user_id = g.user._id
#     username = g.user.username
#     comment = request.form['comment']
#     rating = request.form['rating']
    
#     try:       
#         #creates user in the database
#         create_review(slug, user_id, username, comment, rating)
#     except Exception as e:
#         print("Error al crear el comentario:", e)
#         flash("Error al crear el comentario: " + str(e), "error")
#         return redirect("/movies/"+slug)
    
 #   return redirect("/movies/"+slug)