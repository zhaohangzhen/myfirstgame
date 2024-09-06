import streamlit as st

page = st.sidebar.radio('帝国战争',['注册', '开始游戏'])

def start_html():
  st.image('微信图片_20240606215133.jpg')
  go = st.selectbox('编程猫社区', ['进入编程猫社区实现幻想工作室'])
  if go == '进入编程猫社区':
    st.link_button('', 'https://shequ.codemao.cn/work_shop/24992')

def play_game():
  pass

if page == '注册':
  start_html()
else:
  play_game()
