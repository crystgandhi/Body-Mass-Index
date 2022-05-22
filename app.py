from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/' , methods=['POST','GET'])
def bmi():
    if request.method=="POST":
        name=request.form.get('username')
        weight=int(request.form.get('userweight'))
        height=int(request.form.get('userheight'))
        email=request.form.get('useremail')
        bmi=calc_bmi(weight,height)
         
        return render_template("bmi.html", name=name, weight=weight, height=height, email=email, bmi=bmi)
    
def calc_bmi(weight,height):
    return round((weight/(height/100)**2),2)

if __name__==("__main__"):
    app.run(debug=True)

    #return render_template("bmi.html", name="name", weight="weight", height="height", email="email", bmi="bmi")
    #return render_template("bmi.html", name=name, weight=weight, height=height, email=email, bmi=bmi)