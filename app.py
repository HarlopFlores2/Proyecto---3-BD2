from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
import RtreeQuery
import SequentialQuery
import KDTree
import os

app = Flask(__name__, static_folder='static')

CORS(app)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/query', methods=['POST'])
def query():
    file = request.files['file']
    k = int(request.form['k'])
    filename = secure_filename(file.filename)
    filepath = os.path.join('images', filename)
    file.save(filepath)
    
    rtree_query = RtreeQuery.RtreeQuery('./dict_encoding.pickle')
    distances_rtree, result_rtree, time_rtree = rtree_query.knn_query(filepath, k)
    result_rtree = [path.replace('/mnt/c/proyecto3-bd2/', '/') for path in result_rtree]
    
    sequential_query = SequentialQuery.SequentialQuery('./dict_encoding.pickle')
    distances_sequential, result_sequential, time_sequential = sequential_query.knn_query(filepath, k)
    result_sequential = [path.replace('/mnt/c/proyecto3-bd2/', '/') for path in result_sequential]

    kdtree_query = KDTree.KDTree('./dict_encoding.pickle')
    distances_kdtree, result_kdtree, time_kdtree = kdtree_query.knn_query(filepath, k)
    result_kdtree = [path.replace('/mnt/c/proyecto3-bd2/', '/') for path in result_kdtree]

    return jsonify({
        "result_rtree": result_rtree, 
        "result_sequential": result_sequential, 
        "result_kdtree": result_kdtree,
        "time_rtree": time_rtree,
        "time_sequential": time_sequential,
        "time_kdtree": time_kdtree,
        "distances_rtree": distances_rtree,
        "distances_sequential": distances_sequential,
        "distances_kdtree": distances_kdtree
    })

@app.route('/lfw/<path:filename>')
def custom_static(filename):
    return send_from_directory('lfw', filename)

if __name__ == '__main__':
    app.run(debug=True)
