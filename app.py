# -*- coding: utf-8 -*-
# Reload trigger: sidebar color updated to light mode

import streamlit as st
import pandas as pd
import numpy as np
import data
import style

# 1. 페이지 설정 (PC 사용 우선 - 와이드 레이아웃 적용)
st.set_page_config(
    page_title="신카이 마코토 성지순례 여행 추천 시스템",
    page_icon="📍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. 커스텀 CSS 스타일 적용
style.apply_custom_style()

# 3. 세션 상태 초기화 (사용자 취향 테스트 캐싱 및 유지용)
if "test_completed" not in st.session_state:
    st.session_state.test_completed = False
if "recommended_movie" not in st.session_state:
    st.session_state.recommended_movie = None
if "test_results" not in st.session_state:
    st.session_state.test_results = {}
if "selected_spots_generator" not in st.session_state:
    st.session_state.selected_spots_generator = []

# 4. 사이드바 내비게이션 구성
st.sidebar.markdown(
    """
    <div style='text-align: center; margin-bottom: 20px;'>
        <h2 style='margin-bottom: 5px; font-weight: 800; background: linear-gradient(135deg, #ff7e5f, #feb47b); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>SHINKAI TRIP</h2>
        <span style='font-size: 0.85rem; color: #475569; font-weight:500;'>성지순례 일본 여행 추천 시스템</span>
    </div>
    """, 
    unsafe_allow_html=True
)

st.sidebar.markdown("<div style='height: 1px; background-color: #e2e8f0; margin-bottom: 20px;'></div>", unsafe_allow_html=True)

menu = st.sidebar.radio(
    "🧭 서비스 메뉴 바로가기",
    ["🏠 홈 (Home)", "✨ 여행 취향 테스트", "📍 실제 배경지 탐색", "🗺 성지순례 코스 생성기", "🎬 작품 아카이브"],
    index=0
)

st.sidebar.markdown("<div style='height: 2px; background-color: #e2e8f0; margin-top: 30px; margin-bottom: 20px;'></div>", unsafe_allow_html=True)

# 사이드바 하단 정보창
st.sidebar.markdown(
    """
    <div style='padding: 15px; background-color: #f1f5f9; border-radius: 10px; font-size: 0.85rem; line-height: 1.6; border: 1px solid #e2e8f0;'>
        <div style='font-weight: 700; color: #0f172a; margin-bottom: 5px;'>💡 수록 작품 안내</div>
        <ul style='margin-bottom: 0; padding-left: 18px; color: #334155;'>
            <li>너의 이름은 (2016)</li>
            <li>날씨의 아이 (2019)</li>
            <li>스즈메의 문단속 (2022)</li>
        </ul>
        <div style='margin-top: 10px; font-size: 0.75rem; color: #64748b; text-align: center;'>
            © Shinkai Trip Project. All rights reserved.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# 5. 각 메뉴별 페이지 화면 렌더링
if menu == "🏠 홈 (Home)":
    # ----------------------------------------------------
    # HOME PAGE
    # ----------------------------------------------------
    st.markdown(
        """
        <div class="shinkai-header">
            <h1>황혼의 시간 여행
            : 신카이 마코토 작품 속 풍경을 따라 떠나는 일본 여행</h1>
            <p>그 시절 우리가 사랑했던 황혼의 하늘, 쏟아져 내리던 비의 궤적, 문 너머 마주한 상실과 회복의 풍경들...<br>
            영화 속 찬란한 영상미를 자아냈던 실제 배경지들을 탐방하고 나만의 맞춤형 여행 코스를 완성해 보세요.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("<h2 class='sub-title'>🌟 주요 서비스 안내</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(
            """
            <div class="spot-card" style="min-height: 350px;">
                <div class="spot-card-header">
                    <span class="spot-title">✨ 여행 취향 테스트</span>
                    <span class="spot-movie-badge" style="background-color: #ff7e5f;">TEST</span>
                </div>
                <div class="spot-desc" style="margin-top: 10px;">
                    나의 <b>여행 성향(여행지 타입, 강도, 동행자, 선호 스타일)</b>을 입력하면,
                    수천 개의 시나리오 가중치 분석을 거쳐 나에게 딱 맞는 <b>신카이 마코토 추천 작품</b>과 
                    어울리는 여행 컨셉을 정밀 매칭해 드립니다.
                </div>
                <div class="spot-tips-box" style="margin-top: 15px;">
                    💡 2분 남짓한 간단한 설문을 완료하고 나만의 운명적인 작품을 진단해 보세요!
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("👉 취향 테스트 시작하기", key="btn_go_test", use_container_width=True):
            st.info("왼쪽 사이드바에서 '✨ 여행 취향 테스트' 메뉴를 선택해 주세요!")
            
    with col2:
        st.markdown(
            """
            <div class="spot-card" style="min-height: 350px;">
                <div class="spot-card-header">
                    <span class="spot-title">📍 실제 배경지 탐색</span>
                    <span class="spot-movie-badge" style="background-color: #3b5998;">EXPLORER</span>
                </div>
                <div class="spot-desc" style="margin-top: 10px;">
                    도쿄 도심의 화려한 스카이라인부터 시골의 고즈넉한 대자연까지, 영화 속 찬란한 한 장면을 장식한 
                    <b>14곳의 실제 배경지 좌표</b>와 현장 정보를 매핑합니다.
                    현실의 구도와 영화 속 씬의 차이점, 필수 꿀팁을 확인해 보세요.
                </div>
                <div class="spot-tips-box" style="margin-top: 15px;">
                    📍 인터랙티브 일본 성지 지도를 통해 직관적으로 장소 위치를 살펴볼 수 있습니다.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("👉 실제 배경지 탐색하기", key="btn_go_explorer", use_container_width=True):
            st.info("왼쪽 사이드바에서 '📍 실제 배경지 탐색' 메뉴를 선택해 주세요!")
            
    with col3:
        st.markdown(
            """
            <div class="spot-card" style="min-height: 350px;">
                <div class="spot-card-header">
                    <span class="spot-title">🗺 성지순례 코스 생성기</span>
                    <span class="spot-movie-badge" style="background-color: #9467BD;">ROUTE</span>
                </div>
                <div class="spot-desc" style="margin-top: 10px;">
                    내가 가고 싶은 스폿들을 골라 담기만 하세요! 
                    <b>여행 일정(1박 2일 ~ 3박 4일) 및 동행인 조합</b>에 맞춰, 교통 수단 안내, 일자별 최적 동선 시나리오, 
                    도심/소도시 연계 이용 노선까지 맞춤 가이드를 생성합니다.
                </div>
                <div class="spot-tips-box" style="margin-top: 15px;">
                    🗺 실제 일본 대중교통 시스템(JR 패스, 페리 등)을 고려한 현실적인 이동 솔루션을 제공합니다.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("👉 코스 생성하러 가기", key="btn_go_generator", use_container_width=True):
            st.info("왼쪽 사이드바에서 '🗺 성지순례 코스 생성기' 메뉴를 선택해 주세요!")

    st.markdown("<div class='beauty-divider'></div>", unsafe_allow_html=True)
    st.markdown("<h2 class='sub-title'>🎬 수록 명작 소개</h2>", unsafe_allow_html=True)
    
    # 세 영화 미리보기 카드
    mv_col1, mv_col2, mv_col3 = st.columns(3)
    
    with mv_col1:
        st.markdown(
            """
            <div class="matching-card" style="border-top: 6px solid #FF4B4B;">
                <h3 style="color:#0f172a; margin-bottom: 5px;">너의 이름은</h3>
                <span style="font-size:0.85rem; color:#888; display:block; margin-bottom:12px;">Your Name (2016)</span>
                <p style="font-size:0.92rem; color:#555; text-align:left; line-height:1.5; min-height:110px;">
                    "아직 만나지 못한 너를, 찾고 있어." 시골 소녀 미츠하와 도쿄 소년 타키의 기적 같은 몸 바뀜과 시공간을 초월한 운명적 사랑. 도쿄 신주쿠 요츠야와 나가노 스와 호수, 기후 산골마을의 대비되는 미학을 극대화한 신카이 마코토 최고의 흥행작.
                </p>
                <div style="font-size:0.82rem; font-weight:700; color:#FF4B4B; margin-top:10px;">🚩 주요 성지: 스가 신사, 스와 호, 히다 후루카와</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
    with mv_col2:
        st.markdown(
            """
            <div class="matching-card" style="border-top: 6px solid #1F77B4;">
                <h3 style="color:#0f172a; margin-bottom: 5px;">날씨의 아이</h3>
                <span style="font-size:0.85rem; color:#888; display:block; margin-bottom:12px;">Weathering With You (2019)</span>
                <p style="font-size:0.92rem; color:#555; text-align:left; line-height:1.5; min-height:110px;">
                    "기적은 하늘 위뿐만이 아니었다." 이상 기후로 내내 비가 내리는 도쿄, 하늘을 맑게 만드는 능력을 지닌 가출 소녀 히나와 방황하는 남고생 호다카의 청춘 판타지. 비가 갠 후 도쿄 빌딩 숲 위로 쏟아지는 경이로운 햇살의 감동.
                </p>
                <div style="font-size:0.82rem; font-weight:700; color:#1F77B4; margin-top:10px;">🚩 주요 성지: 롯폰기 힐즈 스카이덱, 타바타 역 언덕길</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
    with mv_col3:
        st.markdown(
            """
            <div class="matching-card" style="border-top: 6px solid #9467BD;">
                <h3 style="color:#0f172a; margin-bottom: 5px;">스즈메의 문단속</h3>
                <span style="font-size:0.85rem; color:#888; display:block; margin-bottom:12px;">Suzume (2022)</span>
                <p style="font-size:0.92rem; color:#555; text-align:left; line-height:1.5; min-height:110px;">
                    "다녀오겠습니다." 일본 각지의 폐허 속에 존재하는 재난의 문을 단속해 나가는 용감한 소녀 스즈메와 요석에 걸려 의자가 된 청년 소타의 전국 대모험. 동일본 대지진의 아픈 과거를 위로하고 다정하게 안아주는 대서사 로드무비.
                </p>
                <div style="font-size:0.82rem; font-weight:700; color:#9467BD; margin-top:10px;">🚩 주요 성지: 분고모리 기관고, 신 오차노미즈 역</div>
            </div>
            """,
            unsafe_allow_html=True
        )

elif menu == "✨ 여행 취향 테스트":
    # ----------------------------------------------------
    # PREFERENCE TEST PAGE
    # ----------------------------------------------------
    st.markdown(
        """
        <div class="shinkai-header" style="background: linear-gradient(135deg, #1e1b4b, #311042, #7c2d12);">
            <h1>✨ 신카이 트립 여행 취향 테스트</h1>
            <p>당신의 여행 취향과 스타일을 바탕으로 어울리는 신카이 마코토 작품과 성지 순례 방향을 설계해 드립니다.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("<h3 style='margin-bottom: 20px;'>📝 질문에 답해 나만의 여행지 추천 받기</h3>", unsafe_allow_html=True)
    
    # 2컬럼 레이아웃으로 폼 구성해 가독성 업그레이드
    col_q1, col_q2 = st.columns(2)
    
    with col_q1:
        st.markdown(f"**{data.TEST_QUESTIONS['destination']['title']}**")
        dest_choice = st.radio(
            "선택해 주세요",
            list(data.TEST_QUESTIONS['destination']['options'].keys()),
            format_func=lambda x: f"{x} - {data.TEST_QUESTIONS['destination']['options'][x]}",
            label_visibility="collapsed"
        )
        
        st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
        
        st.markdown(f"**{data.TEST_QUESTIONS['companion']['title']}**")
        comp_choice = st.radio(
            "선택해 주세요",
            list(data.TEST_QUESTIONS['companion']['options'].keys()),
            format_func=lambda x: f"{x} - {data.TEST_QUESTIONS['companion']['options'][x]}",
            label_visibility="collapsed"
        )
        
    with col_q2:
        st.markdown(f"**{data.TEST_QUESTIONS['intensity']['title']}**")
        intens_choice = st.radio(
            "선택해 주세요",
            list(data.TEST_QUESTIONS['intensity']['options'].keys()),
            format_func=lambda x: f"{x} - {data.TEST_QUESTIONS['intensity']['options'][x]}",
            label_visibility="collapsed"
        )
        
        st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
        
        st.markdown(f"**{data.TEST_QUESTIONS['styles']['title']}**")
        style_choices = st.multiselect(
            "나의 취향 스타일 (최대 3개)",
            data.TEST_QUESTIONS['styles']['options'],
            default=data.TEST_QUESTIONS['styles']['options'][:2],
            help="가장 마음에 드는 키워드를 선택해 주세요. 가중치 매칭에 활용됩니다."
        )
        
    # 스타일 선택 개수 가이드라인
    if len(style_choices) > 3:
        st.warning("⚠ 취향 스타일은 최대 3개까지 선택하는 것을 권장합니다. 초과 선택 시 정확도가 분산될 수 있습니다.")
    elif len(style_choices) == 0:
        st.error("⚠ 취향 스타일을 최소 1개 이상 선택해 주세요.")

    # 제출 버튼
    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    submit_btn = st.button("🔍 내 여행 성향 분석 및 결과 도출하기", use_container_width=True, type="primary")
    
    if submit_btn and len(style_choices) > 0:
        # 가중치 알고리즘 실행
        recommended_movie, results = data.calculate_recommendation(
            dest_choice, intens_choice, comp_choice, style_choices
        )
        
        # 세션 스테이트 저장
        st.session_state.test_completed = True
        st.session_state.recommended_movie = recommended_movie
        st.session_state.test_results = results
        
        # 성지순례 코스 생성기 연동용 선택 자동 설정
        filtered_spots = [spot["name"] for spot in data.SPOTS if spot["movie"] == recommended_movie]
        st.session_state.selected_spots_generator = filtered_spots[:3] # 매칭 명소 기본 프리셋 제공
        
    # 결과 화면 출력
    if st.session_state.test_completed:
        rec_m = st.session_state.recommended_movie
        res = st.session_state.test_results
        movie_info = data.MOVIES[rec_m]
        
        st.markdown("<div class='beauty-divider'></div>", unsafe_allow_html=True)
        st.markdown(f"<h2 class='sub-title' style='text-align: center; font-size: 2.2rem;'>🏆 당신과 매칭되는 운명적 작품은... <b>' {rec_m} '</b> 입니다!</h2>", unsafe_allow_html=True)
        
        # 결과 대시보드
        res_col1, res_col2 = st.columns([3, 2])
        
        with res_col1:
            st.markdown(
                f"""
                <div class="spot-card" style="border-left: 6px solid {movie_info['accent_color']};">
                    <div style="font-size: 1.5rem; font-weight: 800; color: {movie_info['accent_color']}; margin-bottom: 5px;">
                        {rec_m} <span style="font-size: 1rem; color: #888;">{movie_info['title_en']}</span>
                    </div>
                    <div style="font-size: 0.9rem; color: #64748b; font-weight: 600; margin-bottom: 15px;">개봉연도: {movie_info['year']}</div>
                    <div style="font-size: 1rem; font-weight: 700; color: #1e293b; margin-bottom: 8px;">📖 추천 매칭 요약</div>
                    <div class="spot-desc" style="background-color: #f8fafc; padding: 15px; border-radius: 8px; border: 1px dashed #e2e8f0; font-size: 0.95rem;">
                        {"<b>도심과 감성</b>의 완벽한 결합! 붉은 실의 인연을 따라 떠나는 도쿄 도심 속 아련한 주택가 산책과 잔잔한 나가노 호수, 기후의 철도 간이역 성지순례를 즐겨보세요." if rec_m == "너의 이름은" else ""}
                        {"<b>비 갠 뒤 맑은 도쿄의 찬란함</b>! 트렌디한 도쿄 신주쿠, 시바코엔 야경, 롯폰기 힐즈 최고층 하늘 옥상 전망대 등 생동감 넘치고 트렌디한 인스타그램 핫플 여행에 제격입니다." if rec_m == "날씨의 아이" else ""}
                        {"<b>대자연을 달리는 장엄한 로드트립</b>! 온천 마을, 아름다운 항구 소도시, 세토대교 고베 야경, 도호쿠 유적까지 조용한 소도시 힐링과 문화 체험을 위주로 힐링하기에 최적입니다." if rec_m == "스즈메의 문단속" else ""}
                    </div>
                    <div style="margin-top: 15px; font-size: 0.95rem; font-weight: 700; color: #1e293b; margin-bottom: 8px;">🎬 이런 매력 포인트를 즐길 수 있어요:</div>
                    <ul style="padding-left: 20px; font-size: 0.93rem; color: #475569; line-height: 1.6;">
                        <li>{" &nbsp;".join([f"✨ {f}<br>" for f in movie_info['features']])}</li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True
            )
            
        with res_col2:
            st.markdown(
                """
                <div class="result-wrapper">
                    <h4 style="margin-top:0; color:#1e293b; text-align:center; font-weight:700;">📊 작품별 매칭 분석 결과</h4>
                """,
                unsafe_allow_html=True
            )
            
            # 각 영화 매칭률 프로그레스바로 시각화
            for m_name, pct in res.items():
                m_color = data.MOVIES[m_name]['accent_color']
                st.markdown(f"<div style='font-size:0.92rem; font-weight:700; color:#1e293b; display:flex; justify-content:space-between; margin-bottom:4px;'><span>{m_name}</span> <span>{pct}%</span></div>", unsafe_allow_html=True)
                st.progress(pct / 100.0)
                
            st.markdown(
                f"""
                    <div style="margin-top: 20px; padding: 15px; background: white; border-radius: 12px; border: 1px solid #e2e8f0; text-align: center;">
                        <span style="font-size: 0.82rem; color: #64748b; font-weight: 600; display: block; margin-bottom: 2px;">나에게 맞는 베스트 추천 명소</span>
                        <span style="font-size: 1.15rem; font-weight: 800; color: {movie_info['accent_color']};">
                            {"📍 스가 신사 계단 & 스와 호수" if rec_m == "너의 이름은" else ""}
                            {"📍 롯폰기 힐즈 스카이덱 & 타바타 언덕" if rec_m == "날씨의 아이" else ""}
                            {"📍 분고모리 기관고 & 오차노미즈 성교" if rec_m == "스즈메의 문단속" else ""}
                        </span>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
        st.success("🎉 결과가 분석되었습니다! '📍 실제 배경지 탐색' 메뉴 또는 '🗺 성지순례 코스 생성기' 메뉴로 이동해 일정과 지도를 연동해 보세요.")

elif menu == "📍 실제 배경지 탐색":
    # ----------------------------------------------------
    # SPOT EXPLORER PAGE
    # ----------------------------------------------------
    st.markdown(
        """
        <div class="shinkai-header" style="background: linear-gradient(135deg, #0284c7, #0369a1, #075985);">
            <h1>📍 작품별 실제 배경지 탐색</h1>
            <p>현실 속 신카이 마코토 작품 속의 배경지 지도를 직접 확인하고 방문 꿀팁과 세부 장소 정보를 확인하세요.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # 필터 옵션
    st.markdown("<h3 style='margin-bottom:10px;'>🔍 원하는 작품 필터링</h3>", unsafe_allow_html=True)
    
    # 세션 스테이트에 추천 영화가 있으면 기본적으로 해당 영화 필터를 지정해주는 스마트 편의성 제공
    default_filter_idx = 0
    if st.session_state.recommended_movie:
        m_list = ["전체", "너의 이름은", "날씨의 아이", "스즈메의 문단속"]
        if st.session_state.recommended_movie in m_list:
            default_filter_idx = m_list.index(st.session_state.recommended_movie)
            
    selected_movie_filter = st.selectbox(
        "작품별로 배경지를 분류하여 볼 수 있습니다:",
        ["전체", "너의 이름은", "날씨의 아이", "스즈메의 문단속"],
        index=default_filter_idx
    )
    
    # 데이터 필터링
    if selected_movie_filter == "전체":
        filtered_spots = data.SPOTS
    else:
        filtered_spots = [spot for spot in data.SPOTS if spot["movie"] == selected_movie_filter]
        
    st.markdown(f"<h4 style='color:#1e3a8a; font-weight:700; margin-bottom:12px;'>📍 성지 정보 카드 리스트 ({len(filtered_spots)}개 장소)</h4>", unsafe_allow_html=True)
    
    # 스폿 리스트 출력
    for spot in filtered_spots:
        m_color = data.MOVIES[spot["movie"]]["accent_color"]
        
        st.markdown(
            f"""
            <div class="spot-card" style="border-left: 6px solid {m_color};">
                <div class="spot-card-header">
                    <span class="spot-title">{spot['name']}</span>
                    <span class="spot-movie-badge" style="background-color: {m_color};">{spot['movie']}</span>
                </div>
                <div class="spot-loc">
                    🌏 지역: <b>{spot['location']}</b> ({spot['region_group']})
                </div>
                <div class="spot-section-title">🎬 영화 속 명장면 묘사</div>
                <div class="spot-desc">{spot['scene']}</div>
                <div class="spot-section-title">🏢 실제 현실 장소 특징</div>
                <div class="spot-desc">{spot['description']}</div>
                <div class="spot-tips-box">
                    <b>📝 방문 꿀팁 가이드</b><br>
                    {spot['tips']}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

elif menu == "🗺 성지순례 코스 생성기":
    # ----------------------------------------------------
    # COURSE GENERATOR PAGE
    # ----------------------------------------------------
    st.markdown(
        """
        <div class="shinkai-header" style="background: linear-gradient(135deg, #4d7c0f, #3f6212, #14532d);">
            <h1>🗺 커스텀 성지순례 코스 생성기</h1>
            <p>방문하고 싶은 영화 속 장소를 선택하여 일정(1박 2일 ~ 3박 4일)과 동행자에 맞는 일본 철도망 및 노선 기반 현실 여행 루트를 생성하세요.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("<h3 style='margin-bottom:15px;'>📍 가고 싶은 장소 담기</h3>", unsafe_allow_html=True)
    
    # 다중 선택을 편하게 하기 위한 분류
    spots_by_movie = {}
    for spot in data.SPOTS:
        spots_by_movie.setdefault(spot["movie"], []).append(spot["name"])
        
    st.info("💡 여행 코스에 포함할 배경지들을 체크해 주세요. 다수 선택할 경우 지역 연계 동선 시나리오가 활성화됩니다.")
    
    # 3개 열로 나뉘어 체크박스/다중선택 구성
    col_sel1, col_sel2, col_sel3 = st.columns(3)
    
    selected_spots = []
    
    with col_sel1:
        st.markdown("**🎬 너의 이름은 명소**")
        for spot_name in spots_by_movie["너의 이름은"]:
            # 세션 스테이트 설정 연동
            default_val = spot_name in st.session_state.selected_spots_generator
            if st.checkbox(spot_name, value=default_val, key=f"chk_{spot_name}"):
                selected_spots.append(spot_name)
                
    with col_sel2:
        st.markdown("**🎬 날씨의 아이 명소**")
        for spot_name in spots_by_movie["날씨의 아이"]:
            default_val = spot_name in st.session_state.selected_spots_generator
            if st.checkbox(spot_name, value=default_val, key=f"chk_{spot_name}"):
                selected_spots.append(spot_name)
                
    with col_sel3:
        st.markdown("**🎬 스즈메의 문단속 명소**")
        for spot_name in spots_by_movie["스즈메의 문단속"]:
            default_val = spot_name in st.session_state.selected_spots_generator
            if st.checkbox(spot_name, value=default_val, key=f"chk_{spot_name}"):
                selected_spots.append(spot_name)
                
    st.markdown("<div class='beauty-divider'></div>", unsafe_allow_html=True)
    
    # 상세 옵션 설정
    st.markdown("### ⚙ 여행 조건 상세 설정")
    col_opt1, col_opt2, col_opt3 = st.columns(3)
    
    with col_opt1:
        duration = st.selectbox(
            "📅 여행 기간을 선택해 주세요",
            ["1박 2일 (도심지 퀵 투어)", "2박 3일 (표준 핵심 코스)", "3박 4일 (여유로운 완전 정복)"]
        )
    with col_opt2:
        transportation = st.selectbox(
            "🚃 선호 이동 수단",
            ["JR 열차 및 대중교통", "렌터카 드라이브"]
        )
    with col_opt3:
        theme = st.selectbox(
            "🎒 여행 테마 스타일",
            ["사진 촬영 중심 (인생샷 투어)", "풍경 및 역사 힐링 중심", "가벼운 랜드마크 스키핑"]
        )
        
    st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)
    generate_btn = st.button("🗺 성지순례 여행 코스 시나리오 생성하기", type="primary", use_container_width=True)
    
    if generate_btn:
        if not selected_spots:
            st.error("⚠ 최소 1개 이상의 장소를 체크해 주세요!")
        else:
            # 선택한 명소 정보 모음
            selected_spot_objects = [spot for spot in data.SPOTS if spot["name"] in selected_spots]
            
            # 동적으로 코스 렌더링
            st.markdown("<div class='beauty-divider'></div>", unsafe_allow_html=True)
            st.markdown(f"### 📋 생성된 맞춤형 성지순례 여정 루트 ({duration})")
            
            # 동선 요약 분석
            movies_represented = set([s["movie"] for s in selected_spot_objects])
            regions_represented = set([s["location"].split(" ")[0] for s in selected_spot_objects])
            
            # 대중교통/렌트 분석 팁
            st.subheader("💡 코스 루트 분석 및 핵심 어드바이스")
            
            summary_tips = []
            if len(regions_represented) > 1:
                summary_tips.append("🚨 **장거리 광역 동선 포함**: 여러 도시에 걸친 광역 코스입니다. 일본 신칸센이나 특급 열차 탑승 예약이 필요합니다. 대중교통 이용 시 'JR 전국 패스'나 지역 연계 패스권 구매가 경제적입니다.")
            else:
                summary_tips.append("✅ **도심/지역 집중 동선**: 도쿄 대도시권 내부나 특정 소도시 위주의 코스입니다. 현지 지하철 1일권이나 스이카(Suica) 교통 카드로도 부담 없이 알차게 둘러볼 수 있습니다.")
                
            if "요요기 회관 터 (철거)" in selected_spots:
                summary_tips.append("⚠ **철거 명소 주의**: 선택하신 날씨의 아이 '요요기 회관'은 현재 완전 철거된 상태입니다. 건물의 직접 관람은 불가능하므로 터 부근에서 철로변 도심의 아련한 분위기를 느끼는 콘셉트로 스케줄을 계획하세요.")
                
            if "오쓰치정 고향 집터 (이와테현)" in selected_spots:
                summary_tips.append("💡 **도호쿠 원정 팁**: 이와테현 오쓰치정은 도쿄에서도 신칸센을 타고 수 시간 이동하는 도호쿠 끝자락의 한적한 마을입니다. 정숙한 마을 분위기를 존중해야 합니다.")
                
            if "분고모리 기관고 (오이타현)" in selected_spots and transportation == "JR 열차 및 대중교통":
                summary_tips.append("🚂 **규슈 로컬 철도 연계**: 분고모리 기관고가 있는 구스정은 열차 배차 간격이 매우 깁니다. JR 유후인노모리 관광 열차 탑승권이나 규슈 횡단열차 예약을 권장합니다.")

            # 박스 안에 안내문 출력
            st.markdown(
                f"""
                <div style='background-color:#eff6ff; padding:20px; border-radius:12px; border-left: 5px solid #1d4ed8; font-size:0.95rem; color:#1e3a8a; line-height:1.7; margin-bottom:20px;'>
                    {'<br>'.join(summary_tips)}
                </div>
                """,
                unsafe_allow_html=True
            )
            
            # 일자별 코스 동적 분할 분배 알고리즘
            # 14개 장소를 지역별로 정렬하여 일자별로 최적 분배
            # Kanto(도쿄), Chubu/Kansai/Kyushu 등 원격지 분배
            tokyo_spots = [s for s in selected_spot_objects if "도쿄" in s["location"]]
            other_spots = [s for s in selected_spot_objects if "도쿄" not in s["location"]]
            
            # 일자 수 정의
            days_count = 2
            if "2박" in duration:
                days_count = 3
            elif "3박" in duration:
                days_count = 4
                
            # 일자별 장소 분할
            day_plans = {i: [] for i in range(1, days_count + 1)}
            
            if days_count == 2:
                # 1박 2일: 도쿄 위주 배치, 타 지역은 마지막에
                day_plans[1] = tokyo_spots[:3]
                day_plans[2] = tokyo_spots[3:] + other_spots
            elif days_count == 3:
                # 2박 3일: 도쿄 1, 도쿄 2, 외곽 3
                day_plans[1] = tokyo_spots[:2]
                day_plans[2] = tokyo_spots[2:5]
                day_plans[3] = tokyo_spots[5:] + other_spots
            else:
                # 3박 4일: 여유롭게 분산
                day_plans[1] = tokyo_spots[:2]
                day_plans[2] = tokyo_spots[2:4]
                day_plans[3] = tokyo_spots[4:6] + [s for s in other_spots if s["region_group"].startswith("Chubu") or s["region_group"].startswith("Kansai")]
                day_plans[4] = [s for s in other_spots if s["region_group"].startswith("Kyushu") or s["region_group"].startswith("Shikoku") or s["region_group"].startswith("Tohoku")]
            
            # 비어있는 일정이 생기지 않도록 분배 조절
            all_assigned_spots = []
            for d in range(1, days_count + 1):
                if not day_plans[d]:
                    # 남은 것 중 이전 일자에서 넘김
                    for prev_d in range(1, d):
                        if len(day_plans[prev_d]) > 1:
                            move_spot = day_plans[prev_d].pop()
                            day_plans[d].append(move_spot)
                            break
            
            # 타임라인 UI 출력
            for d in range(1, days_count + 1):
                spots_for_day = day_plans[d]
                if not spots_for_day:
                    continue
                    
                st.markdown(
                    f"""
                    <div style='margin-top: 15px;'>
                        <span class="timeline-day-badge">Day {d} 여정</span>
                        <span style='font-size:0.95rem; color:#64748b; font-weight:600; margin-left: 10px;'>
                            {"도쿄 중심가 감성 필사 투어" if d==1 else ""}
                            {"도쿄 근외곽 랜드마크 정밀 탐방" if d==2 else ""}
                            {"광역 연계 시골 및 소도시 철도 이동 여행" if d==3 else ""}
                            {"도호쿠 및 규슈 등 일본 정취 깊은 곳으로의 여정" if d==4 else ""}
                        </span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                
                # 해당 일자의 장소 노드 출력
                for i, spot in enumerate(spots_for_day):
                    m_color = data.MOVIES[spot["movie"]]["accent_color"]
                    
                    # 상세 동선 가이드 멘트 동적 생성
                    if "스가 신사" in spot["name"]:
                        move_tip = "🚇 도쿄 지하철 마루노우치선 '요츠야 3초메역' 3번 출구에서 주택가 방면 도보 10분 소요. 계단 경사가 있으니 편한 스니커즈 착용 권장."
                    elif "보도교" in spot["name"]:
                        move_tip = "🚇 JR 소부선 '시나노마치역' 개찰구 우측 보도교 방향 바로 연결. 역 근처 개방 편의점이 있으니 가볍게 음료를 사서 거닐기 좋습니다."
                    elif "미술관" in spot["name"]:
                        move_tip = "🚇 도쿄 지하철 지요다선 '노기자카역' 6번 출구 연결. 2층 미술관 카페는 인기가 높으니 오전이나 평일 오후 애프터눈 티타임에 맞춰 입장해 보세요."
                    elif "스와 호" in spot["name"]:
                        move_tip = "🚆 JR 중앙선 '카미스와역' 하차 후 다테이시 공원까지 도보 약 35분(가파른 언덕길) 또는 택시 탑승 권장(약 10분, 1500엔 선). 황혼 타임 40분 전 대기 필수."
                    elif "히다 후루카와" in spot["name"]:
                        move_tip = "🚆 나고야역에서 특급 히다 열차 환승 후 히다후루카와역 하차. 기차가 정차하는 순간 촬영을 위해 하루 2~3회 열차 시간표 사전 파악 필수."
                    elif "요요기 회관" in spot["name"]:
                        move_tip = "🚇 JR 요요기역 북쪽 출구 도보 2분. 현재 건물은 철거 완료되어 빈 공터이므로 요요기역 철로와 언덕 골목을 천천히 산책하는 형태로 분위기를 느껴보세요."
                    elif "시바 코엔" in spot["name"]:
                        move_tip = "🚇 도쿄 지하철 미타선 '시바코엔역' A4 출구 도보 2분. 밤 11시 전에 가야 불 켜진 화려한 도쿄 타워의 따스한 붉은 조명을 촬영할 수 있습니다."
                    elif "전망대" in spot["name"]:
                        move_tip = "🚇 도쿄 지하철 히비야선 '롯폰기역' 1C 출구 연결. 52층 전망대 매표소에서 옥상 스카이덱 티켓 추가 발권 필요. 바람막이 외투 지참 권장."
                    elif "타바타" in spot["name"]:
                        move_tip = "🚇 JR 야마노테선 '타바타역' 남구(무인 개찰구) 나와 철조망을 끼고 계단을 내려오면 바로 언덕길 도달. 기차가 통과할 때의 사운드와 함께 촬영하는 것이 팁."
                    elif "기관고" in spot["name"]:
                        move_tip = "🚆 JR 규슈 '분고모리역' 도보 5분. 유후인이나 오이타에서 로컬 완행열차로 연계 가능. 인근 소도시 온천 료칸 투어와 결합한 숙박 일정 수립 추천."
                    elif "야와타하마" in spot["name"]:
                        move_tip = "🚢 벳푸 항구에서 '우와지마 운수 페리'를 탑승해 야와타하마항에 도착하면 규슈-시코쿠 간 배 위에서 펼쳐지는 세토내해의 경치를 고스란히 느낄 수 있습니다."
                    elif "아카시" in spot["name"]:
                        move_tip = "🚇 JR 고베선 '마이코역' 하차 후 바로 공원 연결. 유리 바닥 위에서 바라보는 사장교 구조와 바다의 모습이 아찔하여 고베 관광 전후 코스로 탁월합니다."
                    elif "히지리바시" in spot["name"]:
                        move_tip = "🚇 JR 오차노미즈역 성교 출구 도보 1분. 다리 난간 아래로 교차하는 마루노우치선 주황색 지하철과 주오선 열차 3개가 교차하는 삼각 철로 크로스가 핵심 셔터 찬스."
                    else:
                        move_tip = "🚙 렌터카 혹은 인근 시골 지역 로컬 버스를 사전 확인해야 원활히 닿을 수 있습니다."

                    st.markdown(
                        f"""
                        <div class="timeline-container">
                            <div class="timeline-node" style="background-color: {m_color};"></div>
                            <div class="timeline-card">
                                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                                    <span style="font-weight:700; font-size:1.15rem; color:#0f172a;">Spot {i+1}. {spot['name']}</span>
                                    <span class="spot-movie-badge" style="background-color: {m_color};">{spot['movie']}</span>
                                </div>
                                <div style="font-size:0.85rem; color:#64748b; margin-bottom:10px; font-weight:500;">
                                    📍 위치: {spot['location']}
                                </div>
                                <div style="font-size:0.92rem; color:#334155; margin-bottom:10px; line-height:1.5;">
                                    💬 <b>방문 테마:</b> {spot['scene']}
                                </div>
                                <div style="background-color:#f8fafc; padding:10px 14px; border-radius:6px; border-left:3px solid {m_color}; font-size:0.88rem; color:#475569;">
                                    🚗 <b>교통 및 상세 경로 가이드</b><br>
                                    {move_tip}
                                </div>
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
            
            st.success("🎉 일본 성지순례 추천 최적 여행 코스가 설계되었습니다! 장소들의 상세 팁을 바탕으로 알찬 성지순례 여행 계획을 구성해 보세요.")

elif menu == "🎬 작품 아카이브":
    # ----------------------------------------------------
    # MOVIE ARCHIVE PAGE
    # ----------------------------------------------------
    st.markdown(
        """
        <div class="shinkai-header" style="background: linear-gradient(135deg, #581c87, #4c1d95, #3b0764);">
            <h1>🎬 신카이 마코토 작품 아카이브</h1>
            <p>신카이 마코토 감독의 세부 작품 줄거리, 테마 특징 및 대표 OST 정보를 체계적으로 한 눈에 탐색해 보세요.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    selected_arch_movie = st.selectbox(
        "📚 정보를 확인하고 싶은 작품을 선택해 주세요:",
        ["너의 이름은", "날씨의 아이", "스즈메의 문단속"]
    )
    
    movie_data = data.MOVIES[selected_arch_movie]
    m_color = movie_data["accent_color"]
    
    st.markdown(f"<h2 class='sub-title' style='color:{m_color}; border-bottom: 2px solid {m_color}; padding-bottom:10px; margin-bottom:20px;'>🎞 {selected_arch_movie} (Your Name)</h2>" if selected_arch_movie == "너의 이름은" else f"<h2 class='sub-title' style='color:{m_color}; border-bottom: 2px solid {m_color}; padding-bottom:10px; margin-bottom:20px;'>🎞 {selected_arch_movie}</h2>", unsafe_allow_html=True)
    
    col_arc1, col_arc2 = st.columns([1, 1])
    
    with col_arc1:
        st.markdown("<h4 style='font-weight:700;'>🎬 메인 줄거리 (Synopsis)</h4>", unsafe_allow_html=True)
        st.markdown(
            f"""
            <div style="background-color: #f8fafc; border-left: 5px solid {m_color}; padding: 20px; border-radius: 0 12px 12px 0; font-size: 0.98rem; line-height: 1.7; color: #334155; white-space: pre-line; margin-bottom:25px;">
                {movie_data['synopsis']}
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.markdown("<h4 style='font-weight:700;'>🎸 작품 시그니처 특징</h4>", unsafe_allow_html=True)
        features_list = ""
        for feat in movie_data['features']:
            features_list += f"<li style='margin-bottom:8px; line-height:1.5;'>✨ {feat}</li>"
            
        st.markdown(
            f"""
            <ul style="padding-left: 20px; font-size: 0.95rem; color: #475569;">
                {features_list}
            </ul>
            """,
            unsafe_allow_html=True
        )
        
    with col_arc2:
        st.markdown("<h4 style='font-weight:700;'>🎵 대표 사운드트랙 (OST)</h4>", unsafe_allow_html=True)
        st.write("신카이 마코토 작품에서 절대 빼놓을 수 없는 핵심 음악 목록입니다:")
        
        for ost_item in movie_data['ost']:
            st.markdown(
                f"""
                <div style="background-color: white; border: 1px solid #e2e8f0; border-radius: 8px; padding: 12px 16px; margin-bottom: 12px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
                    <div style="font-weight: 700; color: {m_color}; font-size: 0.95rem;">💿 {ost_item['title']}</div>
                    <div style="font-size: 0.85rem; color: #64748b; margin-top: 4px;">{ost_item['desc']}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
        # 유튜브 공식 트레일러 연동 (임베드 렌더링)
        st.markdown("<h4 style='font-weight:700; margin-top:20px;'>🎥 공식 트레일러 영상</h4>", unsafe_allow_html=True)
        st.video(movie_data['youtube_url'])
        st.markdown(
            f"""
            <div style="font-size:0.8rem; color:#64748b; text-align:center; margin-top:4px;">
                🍿 공식 예고편 재생 시 {selected_arch_movie} 특유의 몽환적인 감성을 더 잘 체감할 수 있습니다.
            </div>
            """,
            unsafe_allow_html=True
        )

# 레이아웃 푸터 장식
st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)
st.markdown("<div class='beauty-divider'></div>", unsafe_allow_html=True)
st.markdown(
    """
    <div style='text-align: center; color: #94a3b8; font-size: 0.85rem; padding-bottom: 20px;'>
        <b>신카이 마코토 성지순례 여행 추천 시스템 (Shinkai Trip)</b> | 제작: Antigravity AI 코딩 어시스턴트<br>
        <i>"아직 가보지 못한 장소에서, 당신을 찾고 있습니다."</i>
    </div>
    """,
    unsafe_allow_html=True
)
