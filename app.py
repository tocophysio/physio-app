import streamlit as st

# 設定頁面配置
st.set_page_config(
    page_title="初診評估表單",
    page_icon="🏥",
    layout="centered"
)

# 自訂 CSS 來美化標題和間距
st.markdown("""
    <style>
    .main-header {
        font-size: 24px;
        font-weight: bold;
        color: #2E86C1;
        margin-top: 20px;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
    }
    .icon { margin-right: 10px; }
    .stSelectbox, .stTextArea, .stSlider { margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏥 物理治療/復健 初診評估表")
st.info("請依照您的實際狀況填寫以下資訊，以協助我們進行評估。")

with st.form("intake_form"):
    # --- Section 1: 基本資料 ---
    st.markdown('<div class="main-header">📄 1. 基本資料 (Profile)</div>', unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        gender = st.selectbox("生理性別", ["請選擇", "男", "女", "其他"], index=0)
    with c2:
        age_group = st.selectbox("年齡區間", ["請選擇", "18歲以下", "19-30歲", "31-45歲", "46-60歲", "60歲以上"], index=0)

    occupation_options = [
        "請選擇",
        "--- 靜態/久坐類 ---",
        "辦公室內勤 (行政/會計)",
        "電腦工程師/設計師",
        "職業駕駛 (長途/外送)",
        "學生 (K書/手機族)",
        "--- 勞力/重複動作類 ---",
        "重勞力工作 (工地/搬運)",
        "重複性上肢 (產線/包裝)",
        "家庭主婦/主夫 (家務)",
        "--- 久站/精細動作類 ---",
        "醫護人員 (久站/彎腰)",
        "服務業 (久站/走動)",
        "精細手部 (美髮/音樂家)",
        "老師/講師",
        "--- 運動與其他 ---",
        "運動員/健身教練",
        "退休樂齡族"
    ]
    occupation = st.selectbox("職業與生活型態", occupation_options)

    # --- Section 2: 患處定位 ---
    st.markdown("---")
    st.markdown('<div class="main-header">📍 2. 患處定位 (Anatomical Site)</div>', unsafe_allow_html=True)

    pain_location_options = [
        "-- 請下拉選擇詳細部位 --",
        "【頭頸椎與神經】頸椎/後腦勺/落枕",
        "【頭頸椎與神經】顳顎關節 (咀嚼痛)",
        "【上肢與肩膀】肩膀/肩關節/旋轉肌",
        "【上肢與肩膀】手肘/網球肘/高爾夫球肘",
        "【上肢與肩膀】手腕/手指/腕隧道",
        "【腰椎與骨盆】胸椎/上背/膏肓",
        "【腰椎與骨盆】腰椎/下背痛/閃到腰",
        "【腰椎與骨盆】薦髂關節/臀部/梨狀肌",
        "【下肢與膝踝】髖關節/鼠蹊部",
        "【下肢與膝踝】膝蓋 (前側/內外側)",
        "【下肢與膝踝】腳踝/阿基里斯腱/足底",
        "【其他】其他/全身性/上述未列出"
    ]
    pain_location = st.selectbox("請選擇主要疼痛或不適的位置：", pain_location_options)

    c3, c4 = st.columns(2)
    with c3:
        side = st.selectbox("患側位置 (Side)", ["請選擇", "左側 (Left)", "右側 (Right)", "雙側 (Bilateral)", "中央/不分左右"])
    with c4:
        hand = st.selectbox("慣用手 (Dominant)", ["請選擇", "右撇子", "左撇子"])
    
    st.text_area("補充描述 (主訴/發生經過)：", placeholder="請盡量詳細描述發生原因或感覺。例如：昨天搬重物時突然聽到腰部『啪』一聲，之後就彎不下去了...", height=100)

    # --- Section 3: 損傷機制 ---
    st.markdown("---")
    st.markdown('<div class="main-header">🩹 3. 損傷機制與分類 (Etiology)</div>', unsafe_allow_html=True)
    
    # 使用 multiselect 或 pills (Streamlit 新版功能)
    etiology_options = [
        "🏃 運動傷害", "🔄 使用過度", "🧘 姿勢不良", "💥 意外創傷",
        "🏥 骨科術後", "🪑 久坐族群", "⏳ 自然退化", "💼 職業勞損"
    ]
    # 如果你的 Streamlit 版本 < 1.40，請改用 st.multiselect
    try:
        etiology = st.pills("請選擇可能的損傷原因 (可複選)", etiology_options, selection_mode="multi")
    except AttributeError:
        etiology = st.multiselect("請選擇可能的損傷原因 (可複選)", etiology_options)

    # --- Section 4: 就醫紀錄 ---
    st.markdown("---")
    st.markdown('<div class="main-header">📋 4. 就醫與檢查紀錄 (History)</div>', unsafe_allow_html=True)
    
    history_options = ["❌ 尚未就醫", "👨‍⚕️ 已看過醫生", "🦴 照過 X 光", "🧲 照過 MRI/CT", "📡 做過超音波"]
    
    try:
        history = st.pills("是否已經看過醫生或做過檢查？(可複選)", history_options, selection_mode="multi")
    except AttributeError:
        history = st.multiselect("是否已經看過醫生或做過檢查？(可複選)", history_options)
        
    st.text_area("檢查結果描述 (或醫生的診斷)：", placeholder="例如：醫生說是骨刺、X光骨頭沒事、或是MRI顯示半月板撕裂...", height=80)

    # --- Section 5: 病程與疼痛 ---
    st.markdown("---")
    st.markdown('<div class="main-header">⏱️ 5. 病程與疼痛性質</div>', unsafe_allow_html=True)

    st.selectbox("發生時間", ["剛發生 (1週內)", "亞急性期 (1週-3個月)", "慢性期 (超過3個月)", "反覆發生"])
    
    pain_type_options = ["😫 痠痛/緊繃", "⚡ 尖銳刺痛", "🔌 麻麻的", "🔒 卡住不順", "🔥 灼熱感", "🧊 冰冷感"]
    try:
        pain_type = st.pills("疼痛感覺 (可複選)", pain_type_options, selection_mode="multi")
    except:
        pain_type = st.multiselect("疼痛感覺 (可複選)", pain_type_options)

    st.write("") # Spacer
    st.markdown("**目前疼痛指數 (VAS: Visual Analog Scale)**")
    vas_score = st.slider("拖動滑桿 (0:不痛, 10:劇痛)", 0, 10, 5)
    
    if vas_score <= 3:
        st.caption("😊 輕微疼痛")
    elif vas_score <= 6:
        st.caption("😐 中度疼痛")
    else:
        st.caption("😫 重度疼痛")

    # --- Submit Button ---
    st.markdown("---")
    submitted = st.form_submit_button("送出評估表單", use_container_width=True)

if submitted:
    st.success("表單已成功送出！(此為演示，資料未儲存)")
    st.json({
        "性別": gender,
        "年齡": age_group,
        "職業": occupation,
        "主要患處": pain_location,
        "患側": side,
        "損傷機制": etiology,
        "VAS分數": vas_score
    })
