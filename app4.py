from flask import Flask, render_template, request, send_file
import boto3
import os
import uuid  # Add this import for generating unique filenames

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index3.html')

@app.route('/convert', methods=['POST'])
def convert_text_to_speech():
    text = request.form['text']
    
    # Initialize the Polly client
    polly = boto3.client('polly',
                         aws_access_key_id='***', # Replace *** with your respective key
                         aws_secret_access_key='****', # Replace **** with your respective key
                         region_name='**') # Replace ** with your respective key
    
    # Call Polly's synthesize_speech API
    response = polly.synthesize_speech(
        Text=text,
        OutputFormat='mp3',
        Engine='neural',
        LanguageCode='en-IN',
        VoiceId='Kajal'  # You can change the voice ID as per your preference
    )
    
    # Generate a unique filename for the audio file
    output_file = 'static/output_{}.mp3'.format(uuid.uuid4())  # Or specify your desired file path
    with open(output_file, 'wb') as file:
        file.write(response['AudioStream'].read())

    return output_file

if __name__ == "__main__":
    app.run(debug=True)