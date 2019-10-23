from flask import Flask, render_template, request
import random, requests

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'




# 사용자로부터 이름을 입력받을 From 페이지
@app.route('/vonvon')
def vonvon():
  return render_template('vonvon.html')

# 전달받은 이름을 기준으로 넘어올 각종 정보를 가공헤서 돌려주는 (응답)로직!
@app.route('/godmademe')
def godmademe():
  # 1. 사용자가 입력한 데이터를 가져온다. (Flask의 request 기능 사용)
  name = request.args.get('user_name')
  # 2. 사용자에게 보여줄 여러가지 재밌는 특성들 리스트를 만든다.
  first_list = ['잘생김', '못생김', '많이 못생김', '존잘...', '조각상']
  second_list = ['자신감', '귀찮음', '쑥스러움', '열정적임', '귀찮음']
  third_list = ['허세', '물욕', '식욕', '똘기']
  # 3. 리스트에서 랜덤으로 하나씩을 선택한다.
  first = random.choice(first_list)
  second = random.choice(second_list)
  third = random.choice(third_list)

  # 4. 가공한 정보를 템플릿에 담아서 사용자에게 보여준다. 
  return render_template('godmademe.html',name_html=name, first_html=first, second_html=second, third_html=third)


# 1. 사용자로부터 임의의 텍스트를 입력받아, 아스키 아트로 변환해서 돌려준다.
# 이떄, 아스키 아트 폰트는 랜덤으로 하나를 지정해서 변환한다.
@app.route('/char')
def char():
  return render_template('char.html')

@app.route('/result')
def result():
  # 1. 사용자가 입력한 Form 데이터를 가져온다.
  word = request.args.get('word')

  # 2. APTII API로 요청을 보내서, 응답 결과를 변수에 담는다. (폰트 정보들)
  fonts = requests.get('http://artii.herokuapp.com/fonts_list').text

  # 3. 가져온 폰트들을 리스트 형태로 바꾼다.
  fonts = fonts.split('\n')

  # 4. 폰트 하나를 랜덤으로 선택한다.
  font = random.choice(fonts)

  # 5. 사용자가 입력한 단어와 랜덤으로 선택한 폰트 정보를 담아서 API에게 요청한다.
  result = requests.get(f'http://artii.herokuapp.com/make?text={ word }&font={ font }').text

  # 6. 최종 결과물을 사용자에게 돌려준다.
  return render_template('result.html', result=result)


# debug 모드를 활성화해서 서버 새로고침을 생략 / 파일 최하단에 위치
if __name__ == '__main__':
    app.run(debug=True)