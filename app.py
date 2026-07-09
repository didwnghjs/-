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
    html/index.html 파일을 안전하게 읽어오는 함수입니다.
    예외 처리를 통해 파일이 없거나 읽기 오류가 발생했을 때 한국어로 친절한 안내를 제공합니다.
    """
    try:
        # 요구사항에 명시된 정확한 상대 경로 지정
        html_path = Path(__file__).resolve().parent / "html" / "index.html"
        
        with open(html_path, "r", encoding="utf-8") as f:
            return f.read()
            
    except FileNotFoundError:
        st.error("⚠️ 슬롯머신 파일(html/index.html)을 찾을 수 없습니다. 경로를 다시 한번 확인해주세요.")
        return None
    except Exception as e:
        st.error(f"⚠️ 웹앱을 불러오는 중 예기치 못한 오류가 발생했습니다: {str(e)}")
        return None

def main():
    # HTML 콘텐츠 불러오기
    html_content = load_html_app()
    
    if html_content:
        # Streamlit 스크롤 영역 설정 및 컴포넌트 래핑 출력
        # 모바일 및 카드형 레이아웃이 깨지지 않도록 충분한 높이(height=850)를 지정하고 스크롤을 허용합니다.
        components.html(
            html_content,
            height=850,
            scrolling=True
        )

if __name__ == "__main__":
    main()
