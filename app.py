from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gossip.db'
db = SQLAlchemy(app)

class Gossip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/add_gossip', methods=['POST'])
def add_gossip():
    data = request.json
    if 'content' not in data:
        return jsonify({'error': 'Gossip content is required'}), 400
    
    new_gossip = Gossip(content=data['content'])
    db.session.add(new_gossip)
    db.session.commit()
    return jsonify({'message': 'Gossip added successfully'})

@app.route('/get_gossips', methods=['GET'])
def get_gossips():
    gossips = Gossip.query.order_by(Gossip.timestamp.desc()).all()
    return jsonify([{'content': g.content, 'timestamp': g.timestamp.strftime('%Y-%m-%d %H:%M:%S')} for g in gossips])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
