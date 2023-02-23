import replicate
from flask import (
    Flask,
    jsonify,
    request,
)
import os
import requests
import subprocess
import json
import requests
import shutil
import zipfile
from PIL import Image
import cv2


REPLICATE_TOKEN = os.getenv('REPLICATE_API_TOKEN')

app = Flask(__name__)
# Create a Dreambooth Version
@app.route("/api/dreambooth_create_model", methods=["POST"])
def dreambooth_create_model():
    body = request.get_json()

    #parameters from call 
    model_name = body["model_name"]
    serving_url = body["serving_url"]
    gender = body["gender"]
    notes = body["notes"]
    webhook = body["webhook_url"]

    headers = {'Content-Type': 'application/json', 'Authorization': 'Token ' + REPLICATE_TOKEN}
    url = "https://dreambooth-api-experimental.replicate.com/v1/trainings"

    data = {
            "input": {
                "instance_prompt": "a photo of a cjw " + gender,
                "class_prompt": "a photo of a " + gender,
                "instance_data": serving_url,
                "max_train_steps": 2000,
                "ckpt_base": "https://huggingface.co/prompthero/openjourney/resolve/main/mdjrny-v4.ckpt"
            },
            "model": model_name,
            "trainer_version": "9c41656f8ae2e3d2af4c1b46913d7467cd891f2c1c5f3d97f1142e876e63ed7a",
            "notes": notes,
            "webhook": webhook
    }

    r = requests.post(url, headers=headers, json=data)
    return r.json()

# Webhook
@app.route('/api/webhook', methods=['POST'])
def webhook():
    # Process the webhook data here, e.g. update a database or send a notification
    data = request.get_json()
    print(data)
    return 'Webhook received'

# Predict
@app.route("/api/predict", methods=["POST"])
def predict():
    
    body = request.get_json()
    prompt = body["prompt"]
    negative_prompt = body["negative_prompt"]
    num_outputs = body["num_outputs"]
    model_name = body["model_name"]
    version = body["version"]

    # Get model
    model = replicate.models.get(model_name)
    version = model.versions.get(version)

    inputs = {
        # Input prompt
        'prompt': prompt,

        # Specify things to not see in the output
        'negative_prompt': negative_prompt,

        # Width of output image. Maximum size is 1024x768 or 768x1024 because
        # of memory limits
        'width': 512,

        # Height of output image. Maximum size is 1024x768 or 768x1024 because
        # of memory limits
        'height': 704,

        # Prompt strength when using init image. 1.0 corresponds to full
        # destruction of information in init image
        'prompt_strength': 0.8,

        # Number of images to output.
        # Range: 1 to 4
        'num_outputs': num_outputs,

        # Number of denoising steps
        # Range: 1 to 500
        'num_inference_steps': 50,

        # Scale for classifier-free guidance
        # Range: 1 to 20
        'guidance_scale': 7.5,

        # Choose a scheduler
        'scheduler': "DDIM",

        # Disable safety check. Use at your own risk!
        'disable_safety_check': False,
    }

    output = version.predict(**inputs)
    return jsonify({"prediction_url": output})

# Upload Images
@app.route('/api/upload', methods=['POST'])
def upload():
    # Send a POST request to the Replicate API to get the upload URL
    headers = {'Authorization': 'Token ' + REPLICATE_TOKEN}
    response = requests.post('https://dreambooth-api-experimental.replicate.com/v1/upload/data.zip', headers=headers)

    # Extract the upload URL and serving URL from the response
    upload_url = response.json()['upload_url']
    serving_url = response.json()['serving_url']

    # Get the zip file from the request
    zip_file = request.files['file']

    # Upload the zip file to the upload URL using a PUT request
    response = requests.put(upload_url, data=zip_file, headers={'Content-Type': 'application/zip'})

    # Return the serving URL as the response
    return jsonify({'serving_url': serving_url})

if __name__ == "__main__":
    app.run(debug=True)





# @app.route('/api/process_images', methods=['POST'])
# def process_images():
#     # Get the zip file from the request
#     zip_file = request.files['file']

#     # Create a temporary directory to extract the zip file into
#     temp_dir = 'temp'
#     os.makedirs(temp_dir, exist_ok=True)
#     with zipfile.ZipFile(zip_file, 'r') as zip_ref:
#         zip_ref.extractall(temp_dir)

#     # Convert all images to JPEG and save them in a new directory
#     output_dir = 'output'
#     os.makedirs(output_dir, exist_ok=True)

#     temp_dir = "temp/data"

#     for filename in os.listdir(temp_dir):
#         print(filename)
#         if not filename.endswith('.jpg') or not filename.endswith('.JPG') or not filename.endswith('.jpeg') or not filename.endswith('.JPEG'):
#             image = Image.open(os.path.join(temp_dir, filename))
#             image = image.convert('RGB')
#             new_filename = os.path.splitext(filename)[0] + '.jpg'
#             image.save(os.path.join(output_dir, new_filename))