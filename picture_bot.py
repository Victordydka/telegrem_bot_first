import requests
import base64
import time
from random import randint


def generate_image(prompt_text):
    # Промт - это короткая формулировка, которая предоставляет информацию нейросети о том, что именно требуется от нее (API)
    prompt = {
        "modelUri": "art://b1gkkc6ad3buic9g3l2l/yandex-art/latest",
        "generationOptions": {
          "seed": randint(10000, 2000000000)
        },
        "messages": [
          {
            "weight": 1,
            "text": prompt_text
          }
        ]
        }
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/imageGenerationAsync"  # по чему будем делать запрос

    #заголовок сообщения (что будем передовать)
    headers = {
            "Content-Type": "application/json",
            "Authorization": "Api-Key AQVN3NQG8yDrJq6yJAxxpKJyPdmG2pPAKxgrOHKm"
        }

    response = requests.post(url=url, headers=headers, json=prompt)
    result = response.json()
    print(result)

    operation_id = result['id']

    operation_url = f"https://llm.api.cloud.yandex.net:443/operations/{operation_id}"

    while True:
        operation_response = requests.get(url=operation_url, headers=headers)
        operation_result = operation_response.json()
        print(operation_result)
        if 'response' in operation_result:
            image_base64 = operation_result['response']['image']
            image_data = base64.b64decode(image_base64)
            return image_data
        else:
            print('Пожалуйста ожидайте, ваше изображение не готово')
            time.sleep(5)


