from flask import Flask, request, jsonify, render_template, url_for #Blueprint
import data_model

#pp = Blueprint('api', __name__)
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('page_initial.html')

# Rota para selecionar as missões dentro de um intervalo de datas
@app.route('/missao/<data_inicial>/<aula_final>', methods=['GET']) 
def get_missao(data_inicial, aula_final):
  return jsonify(data_model.get_search(data_inicial, aula_final))

# Rota para listar todas as missões
@app.route('/missao', methods=['GET']) 
def get_all():
  return jsonify(data_model.get_all())

# Rota para adicionar uma missão 
@app.route('/missao/add')
def add_missao():
  try:
    data_lancamento = request.get_json() 
    response = data_model.insert(data_lancamento)
    print("Success")
    return jsonify(response)
  except Exception as e:
    return jsonify({'error': str(e)}) 
  finally:
    return render_template('criar_missao.html')

# Rota para atualizar uma missão
@app.route('/missao/update', methods=['PUT'])
def update_missao():
  item = request.get_json()
  return jsonify(data_model.update(item))

# Rota para deletar uma missão
@app.route('/missao/delete/<int:id>', methods=['DELETE'])
def delete_missao(id):
  try:
    response = data_model.delete(id)
    return jsonify(response)
  except Exception as e:
    return jsonify({'error': str(e)})
  
if __name__ == '__main__':
  app.run(debug=True)
