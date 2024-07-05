from flask import Flask, render_template, request, send_file
import boto3
import os
import uuid  # Add this import for generating unique filenames
from dotenv import load_dotenv
from flask_cors import CORS
load_dotenv()

# Get the port from the environment variable or use 4000 as default
port = int(os.environ.get("PORT", 5000))

app = Flask(__name__)
CORS(app)
@app.route('/')
def index():
    return render_template('index3.html')

@app.route('/convert', methods=['POST'])
def convert_text_to_speech():
    text = request.form['text']

    # Save the input text to input.txt
    input_file = 'static/input_text_files/input_{}.txt'.format(uuid.uuid4())
    with open(input_file, 'w') as file:
        file.write(f'interviewer: {text}')
    
    # # Initialize the Polly client
    polly = boto3.client('polly',
                         aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                         aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                         region_name=os.getenv('AWS_REGION'))
    # Initialize the Polly client

    # Call Polly's synthesize_speech API
    response = polly.synthesize_speech(
        Text=text,
        OutputFormat='mp3',
        Engine='neural',
        LanguageCode='en-IN',
        VoiceId='Kajal'  # You can change the voice ID as per your preference
    )
    
    # Generate a unique filename for the audio file
    output_file = 'static/output_audio_files/output_{}.mp3'.format(uuid.uuid4())  # Or specify your desired file path
    with open(output_file, 'wb') as file:
        file.write(response['AudioStream'].read())

    return output_file

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=port)

