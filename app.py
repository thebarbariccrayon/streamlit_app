from flask import Flask, request, jsonify
from datetime import datetime
import os
import json
import logging
import subprocess
import csv
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    data = []
    with open('/home/dlewellyn/hpc_testing_tools/results/test_log.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return jsonify(data)
if __name__ == '__main__':
	#start_log()
	#logger.info('GRID Field Agent ' + version + ' Service Started')
	#config.read('field_agent.conf')
	#hostname = config['agent_config']['HOST']
    #hostname = '192.168.4.222'
    app.run()
