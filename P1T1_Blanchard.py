from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return """
    
    <H4> My name is cornholio!</H4>
    
    <p> I need TP for my bunghole!!</p>
    
    <p> Bunghole Bunghole Bunghole<p/>
   
    """


app.run(host='0.0.0.0', port=81)
