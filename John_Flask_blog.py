#import the libraries need 
from flask import Flask, render_template, url_for #importing Flask class and the template function for html, url_for is a function that helps to find exact location of routes for us

app = Flask(__name__) #creating an app variable and setting it to be an instance of the flask class

posts = [ #represent and creating dummy blogs
    {
        'author' : 'John',
        'title' : 'Blog Post 1', 
        'content': 'First post content', 
        'date_posted': 'Jan 13, 2022'
    }, 
    {
        'author' : 'Lim',
        'title' : 'Blog Post 2', 
        'content': 'Second post content', 
        'date_posted': 'Jan 14, 2022'
    }

]

# the app.route decorator is basically to add functionality to the app, the foward / is the root(home) page of the website 
@app.route("/") #routes are basically what we type into our browser to go to different pages
@app.route("/home")
def home():                             #the posts data is stored in this argument
    return render_template('home.html', posts = posts) #pulling the html structure from the template

@app.route("/about") #routes are basically what we type into our browser to go to different pages
def about():
    return render_template('about.html', title = 'About')

if __name__ == '__main__':
    app.run(debug=True) 
    #if I do not use this, then have to change directory on Command prompt to this folder, set FLASK_APP = John_Flask_blog then flask run

#Note 
# 404 response means the page doesnt exist