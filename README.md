Fake News Detection

This is a web application built with Django that allows users to check if a piece of news is real or fake. The application uses a machine learning model to make predictions based on the input text provided by the user.

Features
 #User authentication (login required to use the prediction service)
 #Input news text and predict whether it is real or fake
 #Display the entered news text and prediction result
 #Styled UI for better user experience
 



Installation
Clone the repository:

git clone https : https://github.com/yourusername/fake_news_detection.git
cd fake_news_detection


Make migrations and migrate the database:

python manage.py makemigrations
python manage.py migrate

Create a superuser to access the Django admin : python manage.py createsuperuser

Run the development server : python manage.py runserver

Access the application:
Open your web browser and go to http://127.0.0.1:8000/
Log in using the superuser credentials you created
Usage
Login:

Navigate to the login page and enter your credentials.
If you do not have an account, create a superuser account via the command line.
Predict:

After logging in, you will be redirected to the prediction page.
Enter the news text you want to check in the text box.
Click the "Predict" button to see the result.
The result will show whether the news is "Real" or "Fake" along with the entered text.
Note
Ensure that you have the fake_news_model.pkl and vectorizer.pkl files in the project directory. These files contain the trained machine learning model and the vectorizer used for making predictions.

Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes.

License
This project is licensed under the MIT License. See the LICENSE file for details.
