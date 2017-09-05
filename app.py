from flask import Flask,render_template,jsonify,request, json, redirect, url_for
app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to Python Flask!"

@app.route('/signUp')
def signUp():
    return render_template('signUp.html')

@app.route('/hypervisor')
def hypervisor():
    return render_template('hypervisor.html')

@app.route('/hyp')
def hyp():
    return render_template('hyp.html')

@app.route('/signUpUser', methods=['POST'])
def signUpUser():
    z = "disabling the HV "+request.json[0]['hyp']+" through IPMI"
    # print type(request)
    # l = request.json[0]['hyp']
    # j = l['hyp']
    # print "l is ", l
    # cloudname = request.form['clouds[0]name']
    # return json.dumps({'status':'OK','user':user,'pass':password,'cloudname':cloudname,'vmname':vmname,'service':service,'action':action,'cpumem':cpumem,'controller':controller,'comp':comp});
    # return json.dumps({'status':'OK','cloudname':cloudname});
    # return jsonify(z)
    # return "true"
    return render_template('hyp.html')

if __name__ == "__main__":
    app.run(debug="True",port=8080)
