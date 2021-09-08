import re 
from datetime import datetime, timedelta 
from itertools import groupby 
from typing import List, Tuple 

from flask import Flask, jsonify, request 
from flask_cors import CORS 
from flask_socketio import SocketIO, emit
from sqlalchemy import func 
from sqlalchemy.orm import Session 

from .config import Config 


app = Flask(__name__) 
cors = CORS(app, resources={r"/api/*":{"origins": "*"}}) 
socketio = SocketIO(app, cors_allowed_origins="*")


if __name__ == '__main__': 
    socketio.run(app, debug=True, port=5123)