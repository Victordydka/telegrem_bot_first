import requests

def generate_text(message_text):
    # Промт - это короткая формулировка, которая предоставляет информацию нейросети о том, что именно требуется от нее (API)
    prompt = {
      "modelUri": "gpt://b1gkkc6ad3buic9g3l2l/yandexgpt/latest",
      "completionOptions": {
        "stream": False,
        "temperature": 0,
        "maxTokens": "2000"
      },
      "messages": [
        {
          "role": "system",
          "text": "Ты — можешь дать ответ на любой вопрос, написать текст на вопрос ок котором тебя просят"
        },
        {
          "role": "user",
          "text": message_text
        }
      ]
    }

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Typ": "application/json",
        "Authorization": "Api-key AQVNzKdZC1UibOtsseDAo3Q4bo162PUYOsEY1lS5"
    }
    response = requests.post(url, headers=headers, json=prompt)
    result = response.json()
    return result['result']['alternatives'][0]['message']['text']


