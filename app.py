# -*- coding: utf-8 -*-
"""
Created on Wed May 18 19:33:15 2022

@author: souja
"""

import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome"
    
@app.route("/how_are_you")
def hello():
    return "I am Good. What about u"
    
if __name__ == "__main__":
    app.run(port=8080)
    
