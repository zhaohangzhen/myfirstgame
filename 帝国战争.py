import streamlit as st

page = st.sidebar.radio('帝国战争',['注册', '开始游戏'])

def start_html():
  st.image('微信图片_20240606215133.jpg')
  st.title('编程猫社区')

def play_game():
  pass

if page == '注册':
  start_html()
else:
  play_game()
