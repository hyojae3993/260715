import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. 페이지 기본 설정 및 디자인
st.set_page_config(
    page_title="가축 질병 & 약품 정보 분석 대시보드",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 청소년 대상 전문가 한마디 스타일링
st.title("🔬 청소년을 위한 가축 질병 & 동물약품 분석실")
st.caption("주니어 방역관 여러분! 최신 2025-2026년 데이터를 통해 가축 전염병 반등의 원인과 약품의 역할을 알아봅시다.")

# 2. 데이터 가상 생성 (2025-2026 최신 방역 통계 반영 트렌드)
# 3대 질병 동시 유행 및 ASF 폭발적 증가 추세 반영
disease_data = pd.DataFrame({
    '연도': ['2023', '2024', '2025', '2026(현재)'],
    '아프리카돼지열병(ASF)': [10, 8, 14, 25],
    '고병원성 조류인플루엔자(HPAI)': [32, 49, 53, 56],
    '구제역(FMD)': [0, 0, 1, 3]
})

medicine_data = pd.DataFrame({
    '축종': ['소(한우/낙농)', '돼지(양돈)', '가금류(닭/오리)', '반려동물/기타'],
    '백신(억원)': [450, 620, 380, 500],
    '항생/항균제(억원)': [210, 340, 190, 150],
    '소독제/기타(억원)': [120, 210, 150, 90]
})

# 3. 사이드바 - 전문가의 상호작용 교육 세션
st.sidebar.header("🧭 방역 통제실")
student_name = st.sidebar.text_input("너의 이름은 무엇이니?", "예비 방역관")
st.sidebar.markdown(f"**{student_name}**님, 환영합니다! 분석하고 싶은 축종이나 질병을 선택하여 데이터를 탐색해보세요.")

selected_disease = st.sidebar.selectbox(
    "자세히 살펴볼 가축 질병을 선택하세요",
    ['아프리카돼지열병(ASF)', '고병원성 조류인플루엔자(HPAI)', '구제역(FMD)']
)

# 4. 메인 화면 - 1구역: 최근 발병률 반등 인사이트 (핵심 교육)
st.markdown("---")
st.header("🚨 2025-2026 가축 질병 발병률 반등 경보")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="2026년 ASF 발생 건수", value="25건", delta="역대 최고치 기록 📈")
with col2:
    st.metric(label="동절기 조류인플루엔자 가금농장 감염", value="56건", delta="전년 대비 상승")
with col3:
    st.metric(label="3대 가축전염병 동시 발생", value="소·돼지·닭 전체", delta="2년 연속 동시 유행 ⚠️")

# 인터랙티브 Plotly 선그래프 시각화
fig_disease = px.line(
    disease_data, 
    x='연도', 
    y=['아프리카돼지열병(ASF)', '고병원성 조류인플루엔자(HPAI)', '구제역(FMD)'],
    labels={'value': '발생 건수', 'variable': '질병 종류'},
    title="📊 [연도별 추이] 주요 가축 전염병 발생 건수 변화 그래프",
    markers=True,
    color_discrete_sequence=["#FF4B4B", "#FFAA00", "#1C83E1"]
)
fig_disease.update_layout(hovermode="x unified", template="seaborn")
st.plotly_chart(fig_disease, use_container_width=True)

# 전문가의 깊이 있는 인사이트 설명 박스
st.info(f"""
### 💡 방역 전문가 {student_name}에게 전하는 실시간 발병 인사이트
현재 그래프에서 **{selected_disease}**의 추이를 유심히 보세요! 
2025~2026년에 들어와 모든 곡선이 급격하게 위로 꺾이는 **'반등 현상'**이 관찰됩니다. 그 이유는 무엇일까요?

1. **지구온난화와 기후변화**: 겨울철 철새들이 예년보다 일찍 오거나 늦게 북상하면서 오염원이 저수지와 하천에 오래 잔류하게 되었습니다.
2. **사료 원료 다변화에 따른 리스크**: 최근 아프리카돼지열병(ASF) 역학조사 결과, 일부 오염된 사료 원료에 의해 농장에 바이러스가 유입된 새로운 경로가 발견되었습니다.
3. **방역 사각지대**: 산 속 야생 멧돼지 개체수의 재확산과 통제망을 벗어난 소규모 가축 시설이 질병 확산의 주된 고리가 되고 있습니다.
""")

# 5. 메인 화면 - 2구역: 동물 약품 정보 분석
st.markdown("---")
st.header("💊 가축을 지키는 무기: 동물용 의약품 시장 분석")
st.markdown("질병이 번지는 것을 막기 위해 농가와 수의사들은 어떤 약품을 가장 많이 사용할까요? 금액 기준으로 알아봅시다.")

# 누적 바 차트 구현 (Plotly)
fig_med = px.bar(
    medicine_data,
    x='축종',
    y=['백신(억원)', '항생/항균제(억원)', '소독제/기타(억원)'],
    title="🛒 축종별 동물용 의약품 소비 규모 (백신 vs 항생제 vs 소독제)",
    barmode='stack',
    color_discrete_sequence=["#228B22", "#FF6347", "#87CEEB"]
)
fig_med.update_layout(yaxis_title="시장 규모 (단위: 억원)", template="ggplot2")
st.plotly_chart(fig_med, use_container_width=True)

# 교육적 마무리 퀴즈 및 미션 제공
st.success("""
### 🛡️ 주니어 방역관의 미션: 원헬스(One Health)를 실천하라!
동물의 건강은 곧 우리 인간의 건강, 그리고 지구의 환경과 하나로 연결되어 있다는 개념을 **원헬스(One Health)**라고 불러요. 
가축 질병을 예방하기 위해 무조건 항생제를 많이 쓰는 것은 오히려 '슈퍼 박테리아' 같은 약물 내성 문제를 일으킬 수 있어요! 

따라서 미래의 전문가들은 **[백신을 통한 선제적 면역 형성]**과 **[철저한 환경 소독 및 출입 통제]**를 가장 중요하게 생각한답니다. 
여러분이 만든 이 대시보드가 가축들을 질병으로부터 구하는 첫걸음이 될 거예요! 🌟
""")
