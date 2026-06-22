# -*- coding: utf-8 -*-

import streamlit as st

def apply_custom_style():
    """
    Streamlit 앱 전체에 커스텀 CSS 스타일을 적용합니다.
    """
    css_content = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&family=Outfit:wght@300;400;500;600;700;800&display=swap');

    /* 전체 앱 서체 적용 */
    html, body, [class*="css"], .stApp {
        font-family: 'Noto Sans KR', 'Outfit', sans-serif !important;
    }

    /* 메인 컨테이너 패딩 조절 */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
    }

    /* 메인 헤더 그라디언트 배너 */
    .shinkai-header {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 40%, #c2410c 80%, #ea580c 100%);
        color: white;
        padding: 3rem 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
        text-align: center;
        position: relative;
        overflow: hidden;
    }

    .shinkai-header::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: radial-gradient(circle at 70% 20%, rgba(255, 255, 255, 0.1) 0%, transparent 60%);
        pointer-events: none;
    }

    .shinkai-header h1 {
        font-size: 2.6rem !important;
        font-weight: 900 !important;
        color: white !important;
        margin-bottom: 0.8rem !important;
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.6);
        letter-spacing: -0.05em;
    }

    .shinkai-header p {
        font-size: 1.15rem !important;
        font-weight: 400 !important;
        color: #f1f5f9 !important;
        text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.5);
        margin: 0 auto !important;
        max-width: 800px;
        opacity: 0.95;
        line-height: 1.6;
    }

    /* 사이드바 스타일 개선 */
    section[data-testid="stSidebar"],
    [data-testid="stSidebar"] > div,
    [data-testid="stSidebarContent"],
    [data-testid="stSidebar"] [data-testid="stSidebarUserContent"],
    .stSidebar,
    .stSidebar > div {
        background-color: #f8fafc !important;
        background: #f8fafc !important;
    }
    
    section[data-testid="stSidebar"],
    .stSidebar {
        border-right: 1px solid #e2e8f0 !important;
    }
    
    [data-testid="stSidebar"] .stMarkdown p,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] label {
        color: #334155 !important;
    }
    
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] strong {
        color: #0f172a !important;
    }

    [data-testid="stSidebar"] [data-testid="stWidgetLabel"] p {
        color: #0f172a !important;
        font-weight: 600 !important;
    }

    [data-testid="stSidebar"] label p {
        color: #334155 !important;
    }

    /* 탭 메뉴 스타일링 */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #f1f5f9;
        padding: 8px;
        border-radius: 12px;
    }

    .stTabs [data-baseweb="tab"] {
        height: 45px;
        white-space: pre-wrap;
        background-color: transparent;
        border-radius: 8px;
        color: #475569;
        font-weight: 600;
        border: none;
        transition: all 0.2s ease;
        padding: 0 16px;
    }

    .stTabs [data-baseweb="tab"]:hover {
        background-color: rgba(255, 255, 255, 0.6);
        color: #0f172a;
    }

    .stTabs [aria-selected="true"] {
        background-color: white !important;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
        color: #1e3a8a !important;
    }

    /* 배경지 리스트 카드 */
    .spot-card {
        background-color: white;
        padding: 24px;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04);
        border: 1px solid #e2e8f0;
        margin-bottom: 24px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
    }

    .spot-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 30px rgba(30, 58, 138, 0.08);
        border-color: #bfdbfe;
    }

    .spot-card-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid #f1f5f9;
        padding-bottom: 12px;
        margin-bottom: 16px;
    }

    .spot-title {
        font-size: 1.35rem;
        font-weight: 700;
        color: #0f172a;
    }

    .spot-movie-badge {
        padding: 4px 10px;
        border-radius: 9999px;
        font-size: 0.78rem;
        font-weight: 700;
        color: white;
    }

    .spot-loc {
        font-size: 0.88rem;
        color: #64748b;
        margin-bottom: 14px;
        font-weight: 500;
        display: flex;
        align-items: center;
        gap: 6px;
    }

    .spot-section-title {
        font-size: 0.95rem;
        font-weight: 700;
        color: #1e3a8a;
        margin-top: 12px;
        margin-bottom: 6px;
    }

    .spot-desc {
        font-size: 0.96rem;
        color: #334155;
        line-height: 1.6;
        margin-bottom: 14px;
    }

    .spot-tips-box {
        background-color: #f8fafc;
        border-left: 4px solid #cbd5e1;
        padding: 12px 16px;
        border-radius: 0 8px 8px 0;
        font-size: 0.9rem;
        color: #475569;
        line-height: 1.5;
    }

    /* 테스트 결과 매칭 카드 */
    .result-wrapper {
        background: #f8fafc;
        border-radius: 20px;
        padding: 30px;
        border: 1px solid #e2e8f0;
        margin-top: 25px;
    }

    .matching-card {
        background: white;
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.03);
        border: 1px solid #f1f5f9;
        text-align: center;
        transition: all 0.3s ease;
    }

    .matching-card:hover {
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08);
    }

    .matching-score {
        font-size: 2.2rem;
        font-weight: 800;
        margin-top: 8px;
        font-family: 'Outfit', sans-serif;
    }

    /* 타임라인 여정 디자인 */
    .timeline-container {
        position: relative;
        padding-left: 24px;
        border-left: 2px dashed #cbd5e1;
        margin-left: 12px;
    }

    .timeline-node {
        position: absolute;
        left: -9px;
        top: 4px;
        width: 16px;
        height: 16px;
        border-radius: 50%;
        background-color: #1e3a8a;
        border: 3px solid white;
        box-shadow: 0 0 0 2px #cbd5e1;
    }

    .timeline-card {
        background-color: white;
        border-radius: 12px;
        padding: 16px 20px;
        box-shadow: 0 3px 10px rgba(0, 0, 0, 0.03);
        border: 1px solid #f1f5f9;
        margin-bottom: 24px;
    }

    .timeline-day-badge {
        background-color: #1e3a8a;
        color: white;
        padding: 3px 8px;
        border-radius: 6px;
        font-size: 0.8rem;
        font-weight: 700;
        display: inline-block;
        margin-bottom: 8px;
    }

    /* 아카이브 그리드 포스터 */
    .archive-poster {
        border-radius: 16px;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
        overflow: hidden;
        transition: transform 0.3s ease;
        margin-bottom: 20px;
    }

    .archive-poster:hover {
        transform: scale(1.02);
    }
    
    /* 구분선 데코레이션 */
    .beauty-divider {
        height: 3px;
        background: linear-gradient(to right, #1e3a8a, #ea580c, transparent);
        margin: 2rem 0;
        border-radius: 2px;
    }
    </style>
    """
    st.markdown(css_content, unsafe_allow_html=True)
