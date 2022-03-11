from flask import Flask, jsonify, request, render_template, session, make_response
from flask_login import LoginManager, current_user, login_required, login_user, logout_user, fresh_login_required
import os
from flask_cors import CORS
from sqlalchemy import create_engine

# https 에서만 지원하는 기능을 http 에서 테스트하기 위해서 설정하는 플래그
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask( __name__, static_url_path='/static')
CORS(app)
app.secret_key = 'duhee_server' # 세션 생성시 사용할 키

# user login 기능 구현을 위한 lib 사용
login_manager = LoginManager()
login_manager.init_app( app )
login_manager.session_protection = 'strong'


# 세선에 저장된 유저 id 를 이용해서 유저 객체 다시 로드하는 데 필요한 콜백함수 선언
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


# 로그인 되지 않은 유저가 접근했을 때 동작할 행동을 정의하는 함수
@login_manager.unauthorized_handler
def unauthoried():
    return make_response(jsonify(success=False), 401)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080")
    engine = create_engine("mysql+pymysql://root:@localhost:3306/blog_db", echo=True)
