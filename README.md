# Flask-MongoDB-App
This is a Flask application where we are going to connect MongoDB with Flask Application
# | Bek Brace YouTube Channel |
| Bek Brace YouTube Tutorial - Mid November 2023 |

![image](https://github.com/BekBrace/Flask-MongoDB-App/assets/60483846/03b7f7e3-b5dc-4477-bed0-1ac6eb532308)

![image](https://github.com/BekBrace/Flask-MongoDB-App/assets/60483846/a440cb04-e396-461b-9777-d1b5dfebafb5)

# Flask Application with MongoDB Database Connection

This is a simple Flask web application that demonstrates how to connect to a MongoDB database. It allows you to add and delete todo items.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python
- Flask
- MongoDB
- pymongo (Python MongoDB driver)

You can install the required Python packages using pip:

```bash
pip install Flask pymongo
```

Setting up MongoDB
Install MongoDB on your system if you haven't already. You can download it from MongoDB's official website.

Start the MongoDB server in your command prompt:

```bash
mongosh
```

Create a MongoDB database named flask_db and a collection named todos where your data will be stored.

Running the Application
Clone this repository to your local machine:
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

Start the Flask application:
```bash
python app.py
```

The application should now be running on http://127.0.0.1:5000/. You can access it in your web browser.

Usage
To add a new todo item, visit the homepage and use the form to submit a task and its degree of importance.

To delete a todo item, click on the "Delete" button next to the item.

Project Structure
app.py: The main Flask application.
templates/index.html: HTML template for rendering the list of todo items.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
This project was created as an educational resource for connecting Flask with MongoDB.
Feel free to modify this README to include any additional information specific to your project. Enjoy using your Flask application with MongoDB!
