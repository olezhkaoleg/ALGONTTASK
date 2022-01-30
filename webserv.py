#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      olezhkaoleg
#
# Created:     29.01.2022
# Copyright:   (c) olezhkaoleg 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from flask import Flask, request, jsonify
from plotly.offline import plot
from plotly.graph_objs import Scatter
import generator
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots

app = Flask(__name__)

@app.route('/python/', methods = ['POST'])
def writefunc_in_db():
    json_data = request.get_json()
    time_data = json_data['time']
    CPU_data = json_data['CPU']
    output = CPU_data + " " + time_data
    return jsonify(str = output)

@app.route('/')
def hello():
    newdata = generator.load_data()
    CPU = []
    avgCPU = []
    avgtime = []
    time = []
    avgsum = 0
    for count,i in enumerate(newdata):
        CPU.append(float(i[0]))
        time.append(i[1])
        avgsum += float(i[0])
        if count % 12 == 1:
            avgtime.append(i[1])
            avgCPU.append(avgsum / 12)
            avgsum = 0



    fig = go.Figure()
    fig.add_trace(go.Scatter(x = time, y = CPU))
    fig.add_trace(go.Scatter(x = avgtime, y = avgCPU))

    my_plot_div = plot(fig, output_type='div')
    return my_plot_div




if __name__ == '__main__':
    app.run(debug=True)
