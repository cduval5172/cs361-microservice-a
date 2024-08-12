from icrawler.builtin import GoogleImageCrawler
import requests
import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/search_image', methods=['POST'])
def search_image():
    data = request.get_json()
    keyword = data.get('keyword')

    crawler = GoogleImageCrawler(storage={'root_dir': 'downloaded_images'})
    crawler.crawl(keyword=keyword, max_num=5)

    response = {
        'status': 'success',
        'message': f'Images for the keyword "{keyword}" have been downloaded to directory.'
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(port=5001)