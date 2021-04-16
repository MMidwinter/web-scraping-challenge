from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import MarsScraping

#setting up Flask instance
app = Flask(__name__)

#Establish mongo connection
#mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_scraping")
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_scraping"
mongo = PyMongo(app)

@app.route("/")
def home():

    #Find a record
    mars_data = mongo.db.collection.find_one()

    #Return data and template
    return render_template("index.html", mars=mars_data)


#Creating the scraping route
@app.route("/scrape")
def scrape():

    #Run the scrape function
    mars_scraping_data = MarsScraping.scrape_mars()
    #Update Mongo
    mongo.db.collection.update({}, mars_scraping_data, upsert=True)

    #Go back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)