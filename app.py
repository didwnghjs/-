import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# Streamlit 페이지 기본 설정 (고등학생 사용자가 모바일/웹 어디서나 편하게 볼 수 있도록 설정)
st.set_page_config(
    page_title="과일 & 7 슬롯머신 시뮬레이터",
    page_icon="🎰",
    layout="centered",
    initial_sidebar_state="collapsed"
)

def load_html_app():
    """
    htmls/index.html 파일을 안전하게 읽어오는 함수입니다.
    예외 처리를 통해 파일이 없거나 읽기 오류가 발생했을 때 한국어로 친절한 안내를 제공합니다.
    """
    try:
        # 요구사항에 명시된 정확한 상대 경로 지정
        html_path = Path(__file__).resolve().parent / "html" / "index.html"
        
        with open(html_path, "r", encoding="utf-8") as f:
            return f.read()
            
    except FileNotFoundError:
        st.error("⚠️ 슬롯머신 파일(html/index.html)을 찾을 수 없습니다. 경로를 다시 한번
