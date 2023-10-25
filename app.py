# importing from flask module the Flask class, the render_template function, the request function, url_for 
# and redirect function to redirect to index home page after updating the app database
from flask import Flask, render_template, request, url_for, redirect 
# Mongoclient is used to create a mongodb client, so we can connect on the localhost 
# with the default port
from pymongo import MongoClient
# ObjectId function is used to convert the id string to an objectid that MongoDB can understand
from bson.objectid import ObjectId
# Instantiate the Flask class by creating a flask application
app = Flask(__name__)
# Create the mongodb client
client = MongoClient('localhost', 27017)
# Get and Post Route
@app.route("/", methods=('GET', 'POST'))
def index():
    if request.method == "POST":   # if the request method is post, then insert the todo document in todos collection
        content = request.form['content']
        degree = request.form['degree']
        todos.insert_one({'content': content, 'degree': degree})
        return redirect(url_for('index')) # redirect the user to home page
    all_todos = todos.find()    # display all todo documents
    return render_template('index.html', todos = all_todos) # render home page template with all todos
#Delete Route
@app.post("/<id>/delete/")
def delete(id): #delete function by targeting a todo document by its own id
    todos.delete_one({"_id":ObjectId(id)}) #deleting the selected todo document by its converted id
    return redirect(url_for('index')) # again, redirecting you to the home page 
db = client.flask_database # creating your flask database using your mongo client 
todos = db.todos # creating a collection called "todos"
# The dunder if __name__ code block
if __name__ == "__main__":
    app.run(debug=True) #running your server on development mode, setting debug to True
