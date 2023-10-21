from flask import Flask, request, jsonify
import re
app = Flask(__name__)


def contains_invalid_characters(keyword):
    # 정규 표현식을 사용하여 한글, 영어, 숫자 이외의 문자를 검색
    pattern = "[^가-힣a-zA-Z0-9]"
    return bool(re.search(pattern, keyword))


@app.route('/api/check_keyword', methods=['POST'])
def check_keyword():
    data = request.get_json()
    if 'keyword' not in data:
        return jsonify({'message': '키워드를 제공해야 합니다.'}), 400

    keyword = data['keyword']

    if contains_invalid_characters(keyword):
        return jsonify({'message': '유효하지 않은 문자가 포함되어 있습니다.'}), 400
    else:
        return jsonify({'message': '키워드는 유효합니다.'}), 200


@app.route('/api/get_test', methods=['GET'])
def get_test():
    return jsonify({'message': '요청은 유효합니다.'}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
