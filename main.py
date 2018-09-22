from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

form = '''
<!doctype html>
    <body>
        <form>
            <label for="first-name">First Name</label>
            <input id="first-name" type="text" name="first_name" />
            <input type="submit" />
        </form>
    </body>
</html>


'''


@app.route("/")
def index():
    return "Hello World"

app.run()    
