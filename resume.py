# import libraries
from flask import Flask, render_template

#create our app

app = Flask(__name__)

#Create our directory

@app.route('/')
def resume():   
    return render_template("index.html")
  

#start app
if __name__ == "__main__":
    app.run(
        debug=True
    )
