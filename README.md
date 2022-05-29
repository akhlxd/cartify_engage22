# <p align ="center" >CARtify</p>
## <p align ="center" >Test your car's performance before you build it</p>

<p align ="center" ><img src="https://i.imgur.com/6hz7GmZ.png" height="350px" alt="Homepage"/></p>

## Table of Contents 📕

- [About the Challenge](#microsoft-engage-2022)
- [Agile development methodology](#agile-development-methodology)
- [Features](#features-)
- [Future Work](#future-work)
- [Getting Started](#getting-started)
- [Gallery](#gallery)
- [Conclusion](#conclusion)

## Microsoft Engage-2022
* The Challenge
	* Develop an application to demonstrate how the Automotive Industry could harness data to take informed decisions.
	* You could choose to use the data set provided, or use any open-source data set available you might have access to, or create your own.
	* Demonstrate the use of data analytics in identifying: Customer segments, Most popular car specification combination (engine type, fuel, mileage, etc), Right time to launch a new car, etc

## Agile development Methodology
* I divided the one-month program into four sprints. Each sprint consisted of one week period.
* I categorized my sprints into four sections - exploration, basic working model, features creation, adapt phase.
* We were given a problem statement in which we had to make an app for car manufacturers that uses data analysis at its core
* After thinking about the problem statement, I decided to use python for creating a machine learning model that would predict the price of a car with specified features based on its intended audience
* In the second week, I studied and experimented with various algorithms before deciding on XGBoost as it is very efficient and one of the widely used algorithms on kaggle.
* In the third week, I studied about backend development since I had only experience with competetive coding, python and some front-end. I decided to use express as it was easier to learn and widely used
* In the fourth week, I made the website and hooked it all together and fixed some bugs.

## Features
* Since this was a problem statement focusing mainly on data analysis, I decided to invest more time in making the prediction model.
* The Dashboard is fairly simple. The values can be plugged in the form provided.
* The server runs the script and provides the estimated price of the car.
* It also renders interactive graphs in real time.
* It also shows the performance of the car in various aspects(power, engine , mileage, etc.) compared to the cars there in it's price segment.

## Furture Work
* The next version of the application will feature a cleaner UI.
* Adding feature to compare your car with other cars side by side.
* Clean the backend to make it more readable and modulated.
* Add features to generate more graphs based on feature provided by the user.
* Edge case detection and filter out values out of bound(negative values)

## Getting Started
Have latest versions of NodeJS and Python (pip installation) installed on your machine.

### Prerequisistes

- npm
  ```sh
  npm install npm@latest -g
  ```
### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/akhlxd/cartify_engage22.git
   ```
2 Install NPM packages for backend
   ```sh
   npm install
   ```
3. Install python dependencies
   ```sh
   pip install -r requirements.txt
   ```
4. Start the server
   ```sh
   npm run dev
   ```
5. You should get a console log saying 'Server started on port 5000', you can view your website on [http://localhost:5000](http://localhost:5000)

## Gallery
<p align ="center" ><img src="https://i.imgur.com/6hz7GmZ.png" height="350px" alt="Homepage"/></p>
<p align ="center" ><img src="https://i.imgur.com/jZtCGOd.png" height="350px" alt="Homepage"/></p>
<p align ="center" ><img src="https://i.imgur.com/czDbAIf.png" height="350px" alt="Homepage"/></p>
<p align ="center" ><img src="https://i.imgur.com/vKWSvB3.png" height="350px" alt="Homepage"/></p>
<p align ="center" ><img src="https://i.imgur.com/6qmy6yh.png" height="350px" alt="Homepage"/></p>
<p align ="center" ><img src="https://i.imgur.com/Ft7LwBx.png" height="350px" alt="Homepage"/></p>
<p align ="center" ><img src="https://i.imgur.com/ivIYCJZ.png" height="350px" alt="Homepage"/></p>
<p align ="center" ><img src="https://i.imgur.com/6SyUKXe.png" height="350px" alt="Homepage"/></p>


## Conclusion
This one month was a great learning expreience for me. I went into this program knwing next to nothing about web development, but now I have successfully created and implemented my first web based app. I am especially thankful to my mentor Mr. Zeeshan Vohra (https://github.com/zeeshanv55) for his continuous guidance throughout this project. 
