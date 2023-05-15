from flask import Flask, render_template,redirect, request
import random
app=Flask(__name__,static_folder='assets')

@app.route("/")
def home():
	return redirect("/templates/index")
@app.route("/templates/index")
def home_templates():
	return render_template("index.html")
@app.route("/templates/member_id", methods=['POST','GET'])

def member_id_templates():
	
	return render_template("member_id.html")
@app.route("/templates/member",methods=['POST','GET'])
def form_member():
	a="Add grocery"
	if request.method=="POST":
	    a= request.form['text']
	return render_template("member.html",displaytext=a)

@app.route("/templates/manager",methods=['POST','GET'])
def manager_templates():
    return render_template("manager.html")
@app.route("/templates/manager2", methods=['POST','GET'])
def manager_page_templates():
	t="inventory list"
	if request.method=="POST":
	    t=request.form['text']	
	return render_template("manager2.html",displaytext=t)

if __name__=="__main__":
	app.run(host='0.0.0', port=80,debug=True,threaded=True)

