Description:

This Flask application utilizes Amazon Polly for real-time text-to-speech conversion. It allows users to input text, which is then converted into speech that can be heard instantly.
The APIs used in the provided setup instructions follow a RESTful architecture.
Below are the setup steps and instructions on how to use the application:

STEPS for setup :

1. Clone repository
2. pip install -r requirements.txt
3. Create a ".env" file specifying values of AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, and, AWS_REGION
4. python app3.py
5. navigating to http://localhost:5000

Steps for how to use :

1. Enter text in Text Box you want to convert into speech
2. Click on "Convert to Speech" Button - text will be converted and audible - also the "audio" and "text" files will be saved inside there respective folder inside "static" folder
3. if want to continue follow up from step 1
else
4. Ctrl + c to close the app

Credits :

This app uses Amazon Polly for Realtime Speech to Text Conversion.

Try it Live On : tts-api-final.onrender.com/
