import streamlit as st

def hello():
    page_id == "hello"
    st.title("ログインに成功したということにしよう")
    st.date_input('日付インプット')

def LoginPage():
    st.title("パスワードベースの SSO で利用くだせえ")
    username = st.text_input("ユーザー名を入力してください")
    password = st.text_input("パスワードを入力してください", type='password')
    st.selectbox('コンボボックス', ('KARAAGE', 'GYOUZA'))
    st.checkbox('チェックボックス')
    st.radio('ラジオボタン', ('A', 'B'))
    
    if st.button(label='ログイン'):
        st.write(username, "さんログインに成功ということで",unsafe_allow_html=True)
        
LoginPage()
