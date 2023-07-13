# getting the cpu and memory metrics #

import psutil
# creating the application using flask server ,render template hold htm that display graphical view of usage #
from flask import Flask, render_template
# creating an app from flask and giving parameter as name#
app = Flask(__name__)

# setting where the app should run on /which mean home path #
@app.route('/')
# create a function and declare three variables inside ,cpu tp get its usage and memory to get its usage#
def index():
    cpu_metric = psutil.cpu_percent()
    mem_metric = psutil.virtual_memory().percent
    Message = None
# check cpu n memory if its  given metrics is above then to scale up or #
    if cpu_metric > 80 or mem_metric > 80:
        Message = "High cpu or Memory max utilization detected,Please scale up "
 # commenting out the code below is to call the template declaration for graphical view which is in index.html and giving its parameters to the code below #
   # return f"CPU Utilization: {cpu_percent} and Memory Utilization: {mem_percent}"#
    return render_template("index.html", cpu_metric=cpu_metric, mem_metric=mem_metric, message=Message)
# function call#
if __name__ == '__main__':
# run on a localocal host #
    app.run(debug=True, host='0.0.0.0')



