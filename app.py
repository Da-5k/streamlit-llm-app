from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from dotenv import load_dotenv
from langchain.schema import SystemMessage, HumanMessage
from langchain.chat_models import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

# import some_module  # Removed as it is not used and causes an error

# 環境変数の読み込み
load_dotenv()

# LLM応答を取得する関数
def get_llm_response(input_text, expert_type):
    # 専門家の種類に応じたシステムメッセージを設定
    if expert_type == "不動産専門家":
        system_message = "あなたは不動産の専門家です。不動産に関する質問に対して正確かつ詳細に回答してください。"
    elif expert_type == "税金専門家":
        system_message = "あなたは税金の専門家です。税金に関する質問に対して正確かつ詳細に回答してください。"
    else:
        system_message = "あなたは一般的なアシスタントです。"

    # LangChainのChatOpenAIを使用して応答を生成
    llm = ChatOpenAI(model_name="gpt-4", temperature=0)
    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=input_text),
    ]
    result = llm(messages)
    return result.content

# StreamlitアプリのUI
st.title("専門家AIアプリ")
st.write("このアプリでは、不動産または税金の専門家としてAIに質問することができます。")
st.write("以下の手順で操作してください：")
st.write("1. 専門家の種類を選択します。")
st.write("2. 質問を入力して「送信」ボタンを押します。")
st.write("3. AIからの回答が画面に表示されます。")

# 専門家の種類を選択
expert_type = st.radio(
    "専門家の種類を選択してください：",
    ["不動産専門家", "税金専門家"]
)

# 入力フォーム
input_text = st.text_input("質問を入力してください：")

# 送信ボタン
if st.button("送信"):
    if input_text.strip():
        # LLM応答を取得
        response = get_llm_response(input_text, expert_type)
        # 結果を表示
        st.write("### AIからの回答:")
        st.write(response)
    else:
        st.error("質問を入力してください。")