from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "Hello flask"
 def about("/about"):
    return "About page"

def contact("/contact"):
    return "Contact page"

if __name__=="__main__":
    app.run(debug=True)