curl -X POST \
    -H "Content-Type: application/json" \
    -d '{
        "prompt": "((die-cut sticker fantasy)) of ((laughing headshot of [(cjw):0.8] [man])) (sticker fantasy), (roaring with laughter, a jolly expression), goofy, graphic sticker art, chibi style, clear skin",
        "negative_prompt": "((out of frame)), ((multiple heads)), sexual, nude, risque, nsfw, full body, multiple stickers, 3d, deformed, weird teeth, breast, penis, extra limbs, hands, feet, out of frame, clipping, duo, clone, double, duplicated",
        "num_outputs": "4",
        "model_name": "niranjansenthilkumar/dreambooth_testing",
        "version": "6919cc1a2bcb421c601347d9052b7e567473a89b54a82dcdef57ba72f00fba55"
        }' \
    http://127.0.0.1:5000/api/predict


curl -X POST -H "Authorization: Token $REPLICATE_API_TOKEN" https://dreambooth-api-experimental.replicate.com/v1/upload/data.zip)


curl -X PUT -H "Content-Type: application/zip" --upload-file data.zip https://storage.googleapis.com/replicate-files/IJyjFJ5QgP3mqQn6E1uOU7S7AGDb428Ez3tRwYkqV7lxLpTt/data.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=replicate-web-production%40replicate-production.iam.gserviceaccount.com%2F20230216%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230216T005714Z&X-Goog-Expires=300&X-Goog-SignedHeaders=content-type%3Bhost&X-Goog-Signature=330d681104b701852d534271963d9bab5b97727dc210df394465c7653af7c4a83e3ae20840720960fde3757f29e54628fede1903d51bdffc1f8e00615c1b90459955cdb617cc9b9dd4d43a476ba594fe0dfb3ebf0d06cc6c8ac666363cb28ab76510124978c5da71cbbce0c81c5e70808b2baaed2938711abb1f1b503e67b2a1ab70f0e048aa1f547d622ce5732dba42ed8f914301175e47c94f18437fd2b239d56d9dca75f7a391e79475734626a601c56f1835ac013e97a89a85939a7b04a6f4606073f5b30290f107c17d69c6f0fbf1a7e65bbc6b1fb69c59f21d0d6d685df24a7a61e60d634ee1f2c7db79a91ea4f9052356f0c443badd6f62d51766f6fe

RESPONSE=$(curl -X POST -H "Authorization: Token $REPLICATE_API_TOKEN" https://dreambooth-api-experimental.replicate.com/v1/upload/data.zip)
curl -X PUT -H "Content-Type: application/zip" --upload-file data.zip "$(jq -r ".upload_url" <<< "$RESPONSE")"
SERVING_URL=$(jq -r ".serving_url" <<< $RESPONSE)


curl -X POST \
    -H "Content-Type: application/json" \
    -d '{
        "model_name": "niranjansenthilkumar/dreambooth_testing2",
        "gender": "man",
        "serving_url": "https://replicate.delivery/pbxt/IJuWH2NVpCLg09TFfyGnNurTQEM5YWHHVwBvZeqhhfweO2wc/data.zip"
        }' \
    http://127.0.0.1:5000/api/dreambooth_create_model



curl -H "Authorization: Token $REPLICATE_API_TOKEN" \
  https://webhook.site/50ac6aa8-bab6-4b0c-831b-3989d9be6811/v1/trainings/eidwinalkfeitlw3isdzinxo74


curl -H "Authorization: Token $REPLICATE_API_TOKEN" \
  https://dreambooth-api-experimental.replicate.com/v1/trainings/eidwinalkfeitlw3isdzinxo74


eidwinalkfeitlw3isdzinxo74


 
 
 
 
 "webhook": "https://example.com/my-webhook",
            "webhook_events_filter": ["start", "completed"]
    }



curl -X POST \
    -H "Authorization: Token $REPLICATE_API_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
            "input": {
                "instance_prompt": "a photo of a cjw man",
                "class_prompt": "a photo of a man",
                "instance_data": "'"$SERVING_URL"'",
                "max_train_steps": 2000,
                "ckpt_base": "https://huggingface.co/prompthero/openjourney/resolve/main/mdjrny-v4.ckpt"
            },
            "model": "niranjansenthilkumar/dreambooth_pj_midjourney",
            "trainer_version": "9c41656f8ae2e3d2af4c1b46913d7467cd891f2c1c5f3d97f1142e876e63ed7a",
            "webhook_completed": "https://example.com/dreambooth-webhook"
        }' \
    https://dreambooth-api-experimental.replicate.com/v1/trainings






# curl -X POST \
#     -H "Authorization: Token $REPLICATE_API_TOKEN" \
#     -H "Content-Type: application/json" \
#     -d '{
#             "input": {
#                 "instance_prompt": "a photo of a cjw man",
#                 "class_prompt": "a photo of a man",
#                 "instance_data": "'"$SERVING_URL"'",
#                 "max_train_steps": 2000,
#                 "ckpt_base": "https://huggingface.co/prompthero/openjourney-v2/resolve/main/openjourney-v2.ckpt"
#             },
#             "model": "niranjansenthilkumar/dreambooth_nj_midjourney",
#             "trainer_version": "9c41656f8ae2e3d2af4c1b46913d7467cd891f2c1c5f3d97f1142e876e63ed7a",
#             "webhook_completed": "https://example.com/dreambooth-webhook"
#         }' \
#     https://dreambooth-api-experimental.replicate.com/v1/trainings


# curl -X POST \
#     -H "Authorization: Token $REPLICATE_API_TOKEN" \
#     -H "Content-Type: application/json" \
#     -d '{
#             "input": {
#                 "instance_prompt": "a photo of a cjw woman",
#                 "class_prompt": "a photo of a woman",
#                 "instance_data": "'"$SERVING_URL"'",
#                 "max_train_steps": 2000,
#                 "ckpt_base": "https://huggingface.co/prompthero/openjourney-v2/resolve/main/openjourney-v2.ckpt"
#             },
#             "model": "niranjansenthilkumar/dreambooth_ananya_openjourneyv2",
#             "trainer_version": "9c41656f8ae2e3d2af4c1b46913d7467cd891f2c1c5f3d97f1142e876e63ed7a",
#             "webhook_completed": "https://example.com/dreambooth-webhook"
#         }' \
#     https://dreambooth-api-experimental.replicate.com/v1/trainings



# curl -X POST \
#     -H "Authorization: Token $REPLICATE_API_TOKEN" \
#     -H "Content-Type: application/json" \
#     -d '{
#             "input": {
#                 "instance_prompt": "a photo of a cjw woman",
#                 "class_prompt": "a photo of a woman",
#                 "instance_data": "'"$SERVING_URL"'",
#                 "max_train_steps": 2000,
#                 "ckpt_base": "https://huggingface.co/prompthero/openjourney/resolve/main/mdjrny-v4.ckpt"
#             },
#             "model": "niranjansenthilkumar/dreambooth_ananya_midjourney",
#             "trainer_version": "9c41656f8ae2e3d2af4c1b46913d7467cd891f2c1c5f3d97f1142e876e63ed7a",
#             "webhook_completed": "https://example.com/dreambooth-webhook"
#         }' \
#     https://dreambooth-api-experimental.replicate.com/v1/trainings




# curl -X POST \
#     -H "Authorization: Token $REPLICATE_API_TOKEN" \
#     -H "Content-Type: application/json" \
#     -d '{
#             "input": {
#                 "instance_prompt": "a photo of a cjw man",
#                 "class_prompt": "a photo of a man",
#                 "instance_data": "'"$SERVING_URL"'",
#                 "max_train_steps": 2000,
#                 "ckpt_base": "https://huggingface.co/prompthero/openjourney/resolve/main/mdjrny-v4.ckpt"
#             },
#             "model": "niranjansenthilkumar/dreambooth_nj_midjourney",
#             "trainer_version": "9c41656f8ae2e3d2af4c1b46913d7467cd891f2c1c5f3d97f1142e876e63ed7a",
#             "webhook_completed": "https://example.com/dreambooth-webhook"
#         }' \
#     https://dreambooth-api-experimental.replicate.com/v1/trainings





# curl -X POST \
#     -H "Authorization: Token $REPLICATE_API_TOKEN" \
#     -H "Content-Type: application/json" \
#     -d '{
#             "input": {
#                 "instance_prompt": "a photo of a cjw",
#                 "class_prompt": "a photo of a person",
#                 "instance_data": "'"$SERVING_URL"'",
#                 "max_train_steps": 2000,
#                 "ckpt_base": "https://huggingface.co/prompthero/openjourney-v2/resolve/main/openjourney-v2.ckpt"
#             },
#             "model": "niranjansenthilkumar/dreambooth_cjw",
#             "trainer_version": "9c41656f8ae2e3d2af4c1b46913d7467cd891f2c1c5f3d97f1142e876e63ed7a",
#             "webhook_completed": "https://example.com/dreambooth-webhook"
#         }' \
#     https://dreambooth-api-experimental.replicate.com/v1/trainings


# curl -X POST \
#     -H "Authorization: Token $REPLICATE_API_TOKEN" \
#     -H "Content-Type: application/json" \
#     -d '{
#             "input": {
#                 "instance_prompt": "a photo of a cyz",
#                 "class_prompt": "a photo of a person",
#                 "instance_data": "'"$SERVING_URL"'",
#                 "max_train_steps": 2000,
#                 "ckpt_base": "https://huggingface.co/prompthero/openjourney-v2/resolve/main/openjourney-v2.ckpt"
#             },
#             "model": "niranjansenthilkumar/dreambooth_cyz",
#             "trainer_version": "9c41656f8ae2e3d2af4c1b46913d7467cd891f2c1c5f3d97f1142e876e63ed7a",
#             "webhook_completed": "https://example.com/dreambooth-webhook"
#         }' \
#     https://dreambooth-api-experimental.replicate.com/v1/trainings



RESPONSE=$(curl -X POST -H "Authorization: Token $REPLICATE_API_TOKEN" https://dreambooth-api-experimental.replicate.com/v1/upload/data.zip)
curl -X PUT -H "Content-Type: application/zip" --upload-file data.zip "$(jq -r ".upload_url" <<< "$RESPONSE")"
SERVINGG_URL=$(jq -r ".serving_url" <<< $RESPONSE)




# curl -X POST \
#     -H "Authorization: Token $REPLICATE_API_TOKEN" \
#     -H "Content-Type: application/json" \
#     -d '{
#             "input": {
#                 "instance_prompt": "a photo of a brb",
#                 "class_prompt": "a photo of a bird",
#                 "instance_data": "'"$SERVING_URL"'",
#                 "max_train_steps": 2000,
#                 "ckpt_base": "https://huggingface.co/prompthero/openjourney/resolve/main/mdjrny-v4.ckpt"
#             },
#             "model": "niranjansenthilkumar/dreambooth_brb",
#             "trainer_version": "9c41656f8ae2e3d2af4c1b46913d7467cd891f2c1c5f3d97f1142e876e63ed7a",
#             "webhook_completed": "https://example.com/dreambooth-webhook"
#         }' \
#     https://dreambooth-api-experimental.replicate.com/v1/trainings


# curl -X POST \
#     -H "Authorization: Token $REPLICATE_API_TOKEN" \
#     -H "Content-Type: application/json" \
#     -d '{
#             "input": {
#                 "instance_prompt": "a photo of a brb",
#                 "class_prompt": "a photo of a bird",
#                 "instance_data": "'"$SERVING_URL"'",
#                 "max_train_steps": 2000,
#                 "ckpt_base": "https://huggingface.co/prompthero/openjourney-v2/resolve/main/openjourney-v2.ckpt"
#             },
#             "model": "niranjansenthilkumar/dreambooth_brb2",
#             "trainer_version": "9c41656f8ae2e3d2af4c1b46913d7467cd891f2c1c5f3d97f1142e876e63ed7a",
#             "webhook_completed": "https://example.com/dreambooth-webhook"
#         }' \
#     https://dreambooth-api-experimental.replicate.com/v1/trainings



curl -H "Authorization: Token $REPLICATE_API_TOKEN" \
  https://dreambooth-api-experimental.replicate.com/v1/trainings/n6uuvbwehfeudfvzgvbry5dm6y
