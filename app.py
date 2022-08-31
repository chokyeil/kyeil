from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.tndyy3u.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def postingList():
    return render_template('PostingList.html')

@app.route('/test')
def posting():
    return render_template('posting.html')

@app.route("/postinglist", methods=["POST"])
def postinglist_post():
    picture_receive = request.form['picture_give']
    name_receive = request.form['name_give']
    title_receive = request.form['title_give']
    star_receive = request.form['star_give']
    comment_receive = request.form['comment_give']

    print(name_receive)

    doc = {
        'picture' : picture_receive,
        'name': name_receive,
        'title': title_receive,
        'star': star_receive,
        'comment': comment_receive
    }

    db.posting.insert_one(doc)

    return jsonify({'msg': 'POST(속초 포스팅) 연결 완료!'})

@app.route("/posting", methods=["POST"])
def posting_post():
    picture_receive = request.form['picture_give']
    name_receive = request.form['name_give']
    title_receive = request.form['title_give']
    star_receive = request.form['star_give']
    comment_receive = request.form['comment_give']

    print(name_receive)

    doc = {
        'picture' : picture_receive,
        'name': name_receive,
        'title': title_receive,
        'star': star_receive,
        'comment': comment_receive
    }

    db.posting.insert_one(doc)

    return jsonify({'msg': 'POST(속초 포스팅) 연결 완료!'})

@app.route("/posting/done", methods=["POST"])
def posting_done():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg': 'POST(완료) 연결 완료!'})

@app.route("/posting", methods=["GET"])
def posting_get():
    return jsonify({'msg': 'GET 연결 완료!'})

@app.route("/postinglist", methods=["GET"])
def postinglist_get():
    posting_list = list(db.posting.find({}, {'_id': False}))

    return jsonify({'postings': posting_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
