from flask_site import app, api
from flask import Flask, render_template, make_response
from flask_restful import Resource, Api

import lxml.html
from lxml import etree

def convert_xml_to_html(xsl, xml):
    #this doesnt work -_-
    xslt_doc = etree.parse(xsl)
    xslt_transformer = etree.XSLT(xslt_doc)
    source_doc = etree.parse(xml)
    output_doc = xslt_transformer(source_doc)
    output_doc.write("flask_site\\XML\\output-toc.html", pretty_print=True)

@app.route("/")
def home():
    return render_template ('home.html')

@app.route("/current")
def current():
    convert_xml_to_html('flask_site\\templates\\styles\\Streams.xsl', 'flask_site\\templates\\Operator_Current_Example.xml')
    return render_template('current.html')

@app.route("/sample")
def sample():
    return render_template ('Operator_Current_Example.xml')

@app.route("/probe")
def probe():
    return render_template ('probe.html')
