from pprint import pprint
import requests

class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)}

    def upload_url(self, filename):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": "disk:/test/" + filename, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, filename):
        href = self.upload_url(filename=filename).get("href")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            return print('Файл успешно загружен на Я.Диск')
        return print('Ошибка загрузки')

if __name__ == '__main__':
    token = "AQAAAAAnHkVjAADLW-zHXz4qMET8o8dC7qH-gLU"
    # path_to_file = "text2.txt"
    path_to_file = r'C:\Users\Екатерина\Desktop\учеба\аблон.txt'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
