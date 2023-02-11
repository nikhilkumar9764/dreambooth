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
