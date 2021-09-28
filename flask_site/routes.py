from pathlib import Path

from flask import render_template
from lxml import etree
from lxml.etree import Element

from flask_site import app

root_path = Path(__file__).parent
templates_path = root_path / 'templates'


ns = {'x': 'urn:mtconnect.org:MTConnectStreams:1.7'}


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/current")
def current():
    xml_path = templates_path / 'Operator_Current_Example.xml'
    parser = etree.XMLParser(ns_clean=True)
    root = etree.parse(str(xml_path), parser).getroot()
    header = root.find('x:Header', ns)
    components = root.xpath(
        '/x:MTConnectStreams/x:Streams/x:DeviceStream/x:ComponentStream',
        namespaces=ns)
    component = components[0]
    creation_time = header.attrib['creationTime']
    print(components[0].attrib)
    return render_template('current.html', creation_time=creation_time,
                           components=components, ns=ns)


@app.route("/sample")
def sample():
    return render_template('Operator_Current_Example.xml')


@app.route("/probe")
def probe():
    return render_template('probe.html')
