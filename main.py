import streamlit as dt

# 1. 페이지 기본 설정 및 디자인 (별도 라이브러리 없이 CSS 주입)
st.set_page_config(
    page_title="MBTI 포켓몬 & 직업 매칭",
    page_icon="🔮",
    layout="centered"
)

# 시각적 흥미를 위한 커스텀 CSS 스타일링
st.markdown("""
    <style>
    .main-title {
        font-size: 3rem !important;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(45deg, #FF5353, #FFCC00, #4682B4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    .sub-title {
        text-align: center;
        color: #666;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    .mbti-box {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #FFCC00;
        margin-bottom: 20px;
    }
    .job-tag {
        display: inline-block;
        background: #4682B4;
        color: white;
        padding: 6px 12px;
        border-radius: 20px;
        margin: 5px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# 2. MBTI별 포켓몬 & 직업 데이터 구조화 (공식 이미지 URL 활용)
# 이미지 출처: 포켓몬 공식 이미지 데이터베이스
mbti_pokemon_db = {
    "ISTJ": {"name": "꼬부기", "img": "https://pokemon.com", "jobs": ["⚖️ 회계사 및 세무사", "🕵️ 준법감시인", "💻 시스템 엔지니어"]},
    "ISFJ": {"name": "이상해씨", "img": "https://pokemon.com", "jobs": ["🏥 간호사 및 의료인", "🏫 초등교사", "복지사 및 상담가"]},
    "INFJ": {"name": "뮤", "img": "https://pokemon.com", "jobs": ["지치지 않는 심리상담사", "✍️ 소설가 및 작가", "🧭 환경/인권 운동가"]},
    "INTJ": {"name": "뮤츠", "img": "https://pokemon.com", "jobs": ["🚀 전략 기획자", "🔬 연구원 및 과학자", "♟️ 투자 분석가"]},
    "ISTP": {"name": "파이리", "img": "https://pokemon.com", "jobs": ["🏎️ 카레이서/엔지니어", "🛠️ 정밀 기계 전문가", "🕵️ 포렌식 전문가"]},
    "ISFP": {"name": "메타몽", "img": "https://pokemon.com", "jobs": ["🎨 그래픽 디자이너", "🎵 작곡가 및 뮤지션", "💐 플로리스트"]},
    "INFP": {"name": "이브이", "img": "https://pokemon.com", "jobs": ["🎨 예술가/크리에이터", "📚 사서 및 아키비스트", "🌱 카운셀러"]},
    "INTP": {"name": "후딘", "img": "https://pokemon.com", "jobs": ["💻 소프트웨어 아키텍트", "📊 빅데이터 분석가", "🧠 철학자 및 교수"]},
    "ESTP": {"name": "피카츄", "img": "https://pokemon.com", "jobs": ["🔥 소방관 및 경찰관", "📈 주식 트레이더", " 스포츠 에이전트"]},
    "ESFP": {"name": "푸린", "img": "https://pokemon.com", "jobs": ["🎬 연예인 및 배우", " 이벤트 기획자", "✈️ 항공 승무원"]},
    "ENFP": {"name": "토게피", "img": "https://pokemon.com", "jobs": ["📱 마케팅 크리에이터", " 기획자 및 스타트업 창업", "🎤 이벤트 MC"]},
    "ENTP": {"name": "팬텀", "img": "https://pokemon.com", "jobs": ["💡 발명가 및 벤처캐피탈리스트", "정치 평론가", " Management Consultant"]},
    "ESTJ": {"name": "괴력몬", "img": "https://pokemon.com", "jobs": ["🏢 대기업 프로젝트 매니저", "👨‍✈️ 군 장교 및 경찰 간부", " 행정 공무원"]},
    "ESFJ": {"name": "해피너스", "img": "https://pokemon.com", "jobs": ["🤝 인사(HR) 전문가", "🏨 호텔 지어인", "🏫 학원 강사"]},
    "ENFJ": {"name": "망나뇽", "img": "https://pokemon.com", "jobs": [" 시민단체 리더", "🗣️ 외교관", "🤝 비영리 기구 운영자"]},
    "ENTJ": {"name": "리자몽", "img": "https://pokemon.com", "jobs": ["👑 기업 최고경영자(CEO)", "💼 경영 컨설턴트", " 변호사"]}
}

# 3. 메인 화면 구성
st.markdown('<h1 class="main-title">🔮 MBTI 포켓몬 연구소</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">당신의 성향과 꼭 닮은 포켓몬과 최고의 직업을 찾아보세요!</p>', unsafe_allow_html=True)

st.write("---")

# 4. 사용자 입력 및 상호작용
mbti_list = list(mbti_pokemon_db.keys())
selected_mbti = st.selectbox(
    "👉 당신의 MBTI를 선택하고 마법을 부려보세요!", 
    mbti_list,
    index=None,
    placeholder="여기를 눌러 MBTI 선택하기..."
)

# 5. 매칭 결과 출력 및 시각 효과 triggers
if selected_mbti:
    # 성향에 따른 시각적 팡팡 효과 구현 (E성향은 풍선, I성향은 차분한 눈 효과)
    if "E" in selected_mbti:
        st.balloons()
    else:
        st.snow()
       
    pokemon_info = mbti_pokemon_db[selected_mbti]
    
    st.success(f"🎉 {selected_mbti} 분석 완료! 당신과 동기화된 포켓몬을 공개합니다!")
    
    # 레이아웃 분할 (좌측: 이미지, 우측: 설명 및 직업)
    col1, col2 = st.columns([1, 1.2])
    
    with col1:
        st.image(pokemon_info["img"], use_container_width=True)
        st.markdown(f"<h3 style='text-align: center; color: #FF5353;'>✨ {pokemon_info['name']} ✨</h3>", unsafe_allow_html=True)
        
    with col2:
        st.markdown(f"""
        <div class="mbti-box">
            <h4>🧬 {selected_mbti} 유형의 특징</h4>
            <p>당신은 {pokemon_info['name']}(와)과 영혼의 주파수가 일치합니다! 
            가지고 있는 잠재력과 성향이 매우 닮아있네요.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 💼 추천하는 환상의 직업 TOP 3")
        for job in pokemon_info["jobs"]:
            st.markdown(f"- **{job}**")
            
        st.info("💡 위 직업들은 당신의 내면적 강점과 업무 스타일을 기반으로 매칭되었습니다.")
