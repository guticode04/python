from flask import Flask
from config import Config

app = Flask(__name__)

# configuration variables
# need double quotes inside brackets '[]'
# app.config['greeting'] = 'This worked'

# app.config["greeting"] = 'This worked'

app.config.from_object(Config)



# @app.route('/')
# def hello():
#   return '<h1> Hello World! </h1>'
#   # def(goodbye) within scope
# # def(goodbye) not in scope of "hello" function

# @app.route('/works')

# def hi():
#   return f'<h1>{app.config["BYE"]} </h1>'

# Dev time Python Part 2

# def test(n):
#   # return n + 2
#   return "lets g" + ("o" * n) + "!"


# "ff66ff" => valid?
# has '#' hash
# 6 characters?
# alphanumeric?
# case sensitive
# string? => ALWAYS STRING
# abcdef + 1234556789

def valid_hex(code):
  if len(code) != 7 or code[0] != "#":
    return "False"

  valid_list = list('abcdef0123456789')
  # for char in code[1:].lower():
  #   if char not in valid_list:
  #     return "False"
      #can be a one line if statement
      #  if char not in valid_list: return "False"
  
  # using while loop
  i = 1
  while i < len(code):
    if code[i].lower() not in valid_list: return "False"
    i += 1

  return "True"

@app.route('/')
def basics():
  return f'<h1>{valid_hex("#ff66ff")}</h1>'


# Dev Time July 14th
@app.route('/item<int:id>')
def item(id):
  return f'<h1>Item {id}</h1>'

@app.route('/sample')
def sample_page():
  return ```
    <!doctype html>
    <html>
      <head>
        <title> Home - Sample App</title>
      </head>
      <body>
        <h1>Sample App</h1>
        <h2>Home Page</h2>
        <p> coming to a browser near you... </p>
      </body>
    </html>
  ```