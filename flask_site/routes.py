from flask_site import app
from flask import Flask, render_template, url_for, flash, redirect, send_file



@app.route("/")
def home():
    #return render_template ('Operator_Current_Example.xml')
    return render_template ('home.html')

@app.route("/current")
def current():
    #return render_template ('Operator_Current_Example.xml')
    return render_template ('current.html')

@app.route("/sample")
def sample():
    #return render_template ('Operator_Current_Example.xml')
    return render_template ('sample.html')

@app.route("/probe")
def probe():
    #return render_template ('Operator_Current_Example.xml')
    return render_template ('probe.html')
