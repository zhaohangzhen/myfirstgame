import streamlit as st

page = st.sidebar.radio('帝国战争',['注册', '开始游戏'])

def start_html():
  pass

def play_game():
  pass

if page == '注册':
  start_html()
else:
  play_game()
