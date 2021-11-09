Blood Alcohol Content Calculator
This program is intended to calculate the Blood Alcohol Content(BAC), how long it will take for the BAC to get back to zero, and display a graph of the BAC over time. 

Getting Started
First open the scraping.py file and run the code to import the alcohol percentage data into the scrapedcsv.csv. Next open the app.py and run the code. This will provide an html link that is inputted into your browser and display the inputs. The first 10 inputs are regarding the quantity of alcohol the user has consumed in standard sizes: shots are 1.25 oz, glasses of wine are 5 oz, and glasses of beer are 12 oz. If no alcohol was consumed for any of the inputs please enter ‘0’. The following inputs ask for the user’s weight in pounds, how many hours ago was their first drink, and their gender. The output will generate a graph representing the BAC % over time as well as a text line stating the current BAC% and the quantity of hours until the percentage is back to 0. 

Limitations
The biggest limitation we incurred in this program is in regards to the user inputs. If each input is not entered or is not the correct type of variable then the output will not be generated accordingly. Another limitation we incurred is the range of the x axis on the graph. Altough BAC % cannot be negative the line extends under the x axis. Lastly, the graph display has a visibility limitation in that it cannot display over 50 hours. We chose this range because anything over this would be pretty unrealistic and  makes it difficult to accurately see when the BAC % reaches zero.

Technologies
Install “chromedriver” application for scraping data. Microsoft excel is required to write the csv file.

Things Learned
Abhijot Mann: The new component I learned was integrating the Flask App. This had three components essentially. First, the app.py file had to be set up for the input data to be transferred to the calculator. Next the input_data.html file creates the inputs for the user. Lastly, the calculator.py had to be configured with functions that can be used by the app.py. Initially, this process seemed to be extremely confusing in that I had to set up 3 different variables across each file for the same value to be used. After linking the alcohol inputs into the function for calculating alcohol content and BAC% this became much easier to understand.

Austin Lee :
One concept that I learned was saving a plot or chart into an API so that it may easily be integrated into the flask application. This allows for any changes that happen on the back to easily render data to the front end without the need of changing anything on the front end application. This makes it easy for us to display our chart with accordance to our user input. The difficulty here was when I did not return the variable for my io.Bytes()-- this lead to an error on the flask end where it could not and return that API.

Rishika Parakh: My new component was Scraping.
After finding an appropriate website that listed different types of alcohols along with their alcohol %, we used Beautiful Soup to parse through the information and grab the relevant data. Since the website we used had listed the % in ranges, we decided to calculate the average for each and use those numbers for our project. Finally, these numbers were saved as a csv which we then linked in our Calculator.py file to use in the formulas. 

# intro_to_programming_final
