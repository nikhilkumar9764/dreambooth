import json
import replicate
from flask import (
    Flask,
    jsonify,
    request,
)
import os
import requests

REPLICATE_TOKEN = os.getenv('REPLICATE_API_TOKEN')

app = Flask(__name__)

# Create a Dreambooth Version
@app.route("/api/dreambooth_create_model", methods=["POST"])
def predict():
    body = request.get_json()

    #parameters from call 
    model_name = body["model_name"]
    serving_url = body["serving_url"]
    gender = body["gender"]

    return jsonify({"model_id": 0})

    headers = {'Content-Type': 'application/json', 'Authorization': 'Token ' + REPLICATE_TOKEN}
    url = "https://dreambooth-api-experimental.replicate.com/v1/trainings"

    input = ""
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
            "webhook": "https://example.com/my-webhook",
            "webhook_events_filter": ["start", "completed"]
    }

    print(123)

    r = requests.post(url, headers=headers, json=data)

    print(256)
    print(r.status_code, r.json())

    print(512)

    return jsonify({"model_id": 0})




    # curl -X POST \
    # -H "Authorization: Token $REPLICATE_API_TOKEN" \
    # -H "Content-Type: application/json" \
    # -d '{
    #         "input": {
    #             "instance_prompt": "a photo of a cjw person",
    #             "class_prompt": "a photo of a person",
    #             "instance_data": "'"$SERVING_URL"'",
    #             "max_train_steps": 2000
    #         },
    #         "model": "yourusername/yourmodel",
    #         "trainer_version": "cd3f925f7ab21afaef7d45224790eedbb837eeac40d22e8fefe015489ab644aa",
    #         "webhook_completed": "https://example.com/dreambooth-webhook"
    #     }' \
    # https://dreambooth-api-experimental.replicate.com/v1/trainings


# # Predict
# @app.route("/api/predict", methods=["POST"])
# def predict():
#     body = request.get_json()
#     prompt = body["prompt"]

#     # Get model
#     model = replicate.models.get("prompthero/openjourney")
#     version = model.versions.get(
#         "9936c2001faa2194a261c01381f90e65261879985476014a0a37a334593a05eb"
#     )

#     inputs = {
#     # Input prompt
#     'prompt': "a photo of a cjw man",

#     # Specify things to not see in the output
#     # 'negative_prompt': ...,

#     # A starting image from which to generate variations (aka 'img2img').
#     # If this input is set, the `width` and `height` inputs are ignored
#     # and the output will have the same dimensions as the input image.
#     # 'image': open("path/to/file", "rb"),

#     # Width of output image. Maximum size is 1024x768 or 768x1024 because
#     # of memory limits
#     'width': 512,

#     # Height of output image. Maximum size is 1024x768 or 768x1024 because
#     # of memory limits
#     'height': 704,

#     # Prompt strength when using init image. 1.0 corresponds to full
#     # destruction of information in init image
#     'prompt_strength': 0.8,

#     # Number of images to output.
#     # Range: 1 to 4
#     'num_outputs': 1,

#     # Number of denoising steps
#     # Range: 1 to 500
#     'num_inference_steps': 50,

#     # Scale for classifier-free guidance
#     # Range: 1 to 20
#     'guidance_scale': 7.5,

#     # Choose a scheduler
#     'scheduler': "DDIM",

#     # Random seed. Leave blank to randomize the seed
#     # 'seed': ...,

#     # Disable safety check. Use at your own risk!
#     'disable_safety_check': False,
#     }


#     output = version.predict(prompt=prompt)

#     return jsonify({"prediction_url": output[0]})



if __name__ == "__main__":
    app.run(debug=True)