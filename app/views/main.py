# -*- coding: utf-8 -*-

# Import flask dependencies
from flask import render_template, redirect, url_for
from flask_classy import FlaskView
from flask.ext.login import login_required, current_user
from flask_security.forms import LoginForm, RegisterForm
from app.views.recommend_food import recommend_food

from app.models import Food, security
import random


# 로그인 렌더링 할때 dict으로 넘기면 추가적으로 매개변수를 줄수 있음
@security.login_context_processor
def security_login_context_processor():
    return dict(register_user_form=RegisterForm())


# 회원가입 렌더링 할때 dict으로 넘기면 추가적으로 매개변수를 줄수 있음
# 렌더링 할 때 모달을 어떻게 띄우지??
@security.register_context_processor
def security_register_context_processor():
    return dict(login_user_form=LoginForm())


class MainView(FlaskView):
    route_base = '/'

    # 현재 로그인 한 유저에게 role 추가하는 코드
    def index(self):
        loginform = LoginForm()
        registerform = RegisterForm()

        if not current_user.is_authenticated():
            # 로그인을 아예 안 함.
            return render_template("main/index.html", login_user_form=loginform, register_user_form=registerform)
        elif current_user.is_authenticated() and not current_user.is_evaluate:
            # 로그인은 했는데 평가를 안 함.
            return redirect(url_for('StartView:index'))
        elif current_user.is_authenticated() and current_user.is_evaluate:
            # 로그인도 하고 평가도 함.
            return redirect(url_for('MainView:recommend'))
        elif not current_user.confirmed_at:
            return render_template('main/confirm.html')
        else:
            # 아무것도 해당 안 됨.
            return render_template("main/index.html")

    @login_required
    def recommend(self):
        foods = Food.query.all()

        try:
            food_name = recommend_food(current_user)
        except:
            food_name = random.choice(foods).foodName

        return render_template('main/recommend.html', foodName=food_name)
