import streamlit as st

# 設定頁面配置
st.set_page_config(
    page_title="1分鐘骨骼痛症篩檢",
    page_icon="⏱️", 
    layout="centered"
)

# 自訂 CSS
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
    .report-box {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        border-left: 5px solid #ff4b4b;
    }
    .subtitle {
        font-size: 18px;
        font-weight: 600;
        color: #555;
        margin-top: -15px;
        margin-bottom: 20px;
    }
    /* 讓勾選框的文字大一點，比較好點 */
    .stCheckbox label {
        font-size: 16px;
    }
    /* 區隔線樣式 */
    .section-divider {
        margin-top: 20px;
        margin-bottom: 10px;
        border-top: 1px solid #eee;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 標題區域 ---
st.title("⏱️ 1分鐘骨骼痛症篩檢系統")
st.markdown('<div class="subtitle">Musculoskeletal Screening System</div>', unsafe_allow_html=True)
st.write("請依照您的實際狀況填寫以下資訊，以協助我們進行評估。")
st.markdown("---")

# 免責聲明
st.warning(
    """
    **免責聲明**：
    本報告僅供衛教用途與初步參考，不可取代專業醫療診斷。
    若您感到劇烈不適或有特定徵兆，請務必諮詢專科醫師或物理治療師，進行實體臨床評估。
    """
)

# --- 表單開始 ---
with st.form("intake_form"):
    
    # === Section 1: 基本資料 ===
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

    # === Section 2: 患處定位 ===
    st.markdown("---")
    st.markdown('<div class="main-header">📍 2. 患處定位 (Anatomical Site)</div>', unsafe_allow_html=True)

    pain_location_options = [
        "-- 請下拉選擇詳細部位 --",
        "【頭頸椎】頸椎/後腦勺/落枕",
        "【頭頸椎】顳顎關節 (咀嚼痛)",
        "【上肢】肩膀/肩關節",
        "【上肢】手肘 (內側/外側)",
        "【上肢】手腕/手指",
        "【軀幹】胸椎/上背/膏肓",
        "【軀幹】腰椎/下背痛",
        "【下肢】臀部/髖關節/鼠蹊部",
        "【下肢】膝蓋 (前側/內外側)",
        "【下肢】腳踝/足底",
        "【其他】全身性/上述未列出"
    ]
    pain_location = st.selectbox("請選擇主要疼痛或不適的位置：", pain_location_options)

    c3, c4 = st.columns(2)
    with c3:
        side = st.selectbox("患側位置 (Side)", ["請選擇", "左側", "右側", "雙側", "中央"])
    with c4:
        hand = st.selectbox("慣用手 (Dominant)", ["請選擇", "右撇子", "左撇子"])
    
    st.text_area("補充描述 (選填)：", placeholder="若有特殊狀況可在此描述，若無可跳過...", height=60)

    # === Section 3: 損傷機制 ===
    st.markdown("---")
    st.markdown('<div class="main-header">🩹 3. 損傷機制與分類 (Etiology)</div>', unsafe_allow_html=True)
    
    etiology_options = [
        "運動傷害", "使用過度", "姿勢不良", "意外創傷",
        "骨科術後", "久坐族群", "自然退化", "職業勞損"
    ]
    try:
        etiology = st.pills("請選擇可能的損傷原因 (可複選)", etiology_options, selection_mode="multi")
    except AttributeError:
        etiology = st.multiselect("請選擇可能的損傷原因 (可複選)", etiology_options)

    # === Section 4: 就醫紀錄 ===
    st.markdown("---")
    st.markdown('<div class="main-header">📋 4. 就醫與檢查紀錄 (History)</div>', unsafe_allow_html=True)
    
    history_options = ["尚未就醫", "已看過醫生", "照過 X 光", "照過 MRI/CT", "做過超音波"]
    
    try:
        history = st.pills("是否已經看過醫生或做過檢查？(可複選)", history_options, selection_mode="multi")
    except AttributeError:
        history = st.multiselect("是否已經看過醫生或做過檢查？(可複選)", history_options)

    # === Section 5: 病程與疼痛 ===
    st.markdown("---")
    st.markdown('<div class="main-header">⏱️ 5. 病程與疼痛性質</div>', unsafe_allow_html=True)

    st.selectbox("發生時間", ["剛發生 (1週內)", "亞急性期 (1週-3個月)", "慢性期 (超過3個月)", "反覆發生"])
    
    pain_type_options = ["痠痛/緊繃", "尖銳刺痛", "麻木感", "卡住不順", "灼熱感", "冰冷感"]
    try:
        pain_type = st.pills("疼痛感覺 (可複選)", pain_type_options, selection_mode="multi")
    except:
        pain_type = st.multiselect("疼痛感覺 (可複選)", pain_type_options)

    st.write("") 
    st.markdown("**目前疼痛指數 (VAS: Visual Analog Scale)**")
    vas_score = st.slider("拖動滑桿 (0:不痛, 10:劇痛)", 0, 10, 5)

    if vas_score <= 3:
        st.caption("輕微疼痛")
    elif vas_score <= 6:
        st.caption("中度疼痛")
    else:
        st.caption("重度疼痛")

    # === Section 6: 動作檢測 (大改版 - 分離變痛與緩解) ===
    st.markdown("---")
    st.markdown('<div class="main-header">🚶 6. 動作檢測 (Movement Test)</div>', unsafe_allow_html=True)
    
    # 儲存結果的列表
    agg_factors = [] # 惡化因子
    ease_factors = [] # 緩解因子
    
    # Helper function: 用於顯示分類清楚的選項
    def show_movement_section(part_name, movement_list, passive_list):
        st.info(f"針對 **{part_name}**，請協助我們區分您的疼痛變化模式：")
        
        # --- 1. 惡化因子 (Aggravating) ---
        st.markdown(f"#### 😫 1. 做什麼動作或姿勢會讓疼痛「加劇/變痛」？")
        st.caption("請勾選所有會讓您不舒服的動作")
        
        # 這裡不分欄，讓選項清楚列出，方便區分 Flexion/Extension
        for opt in movement_list:
            if st.checkbox(opt, key=f"agg_{opt}"):
                agg_factors.append(opt)
                
        # --- 2. 緩解因子 (Easing) ---
        st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
        st.markdown(f"#### 😌 2. 做什麼動作或姿勢會感到「緩解/舒服」？")
        st.caption("請勾選會讓您症狀減輕的方式 (包含動作與治療)")

        # 緩解因子包含：原本的動作清單 (因為有些人彎腰痛但走路好) + 被動治療清單
        full_ease_list = movement_list + passive_list
        
        # 使用 2 欄顯示緩解因子，節省空間
        ec1, ec2 = st.columns(2)
        for i, opt in enumerate(full_ease_list):
            # 奇數偶數分欄
            col = ec1 if i % 2 == 0 else ec2
            with col:
                if st.checkbox(opt, key=f"ease_{opt}"):
                    ease_factors.append(opt)

    # --- 邏輯判斷區 ---
    
    # 1. 腰椎/背部 (Flexion vs Extension Bias)
    if "腰" in pain_location or "背" in pain_location:
        # 動作清單：明確區分屈曲、伸直、負重
        movements = [
            "彎腰/前彎 (如洗臉/綁鞋帶)", 
            "坐著/久坐 (如沙發/開車)", 
            "由坐到站的瞬間",
            "向後挺腰/伸懶腰",
            "久站/站立不動", 
            "走路/跑步",
            "床上翻身"
        ]
        # 被動因子
        passives = ["平躺休息", "趴著", "熱敷/冰敷", "按摩"]
        
        show_movement_section("腰背部", movements, passives)

    # 2. 頸椎 (Protraction vs Retraction)
    elif "頸" in pain_location or "落枕" in pain_location:
        movements = [
            "低頭 (滑手機/看書)",
            "抬頭 (看天花板/曬衣)",
            "向後縮下巴 (擠雙下巴)",
            "左右轉頭",
            "長時間靜止 (打電腦/追劇)"
        ]
        passives = ["躺下休息", "手托住頭部", "熱敷/沖熱水澡", "按摩"]
        
        show_movement_section("頸部", movements, passives)

    # 3. 膝蓋 (Load vs Unload)
    elif "膝" in pain_location:
        movements = [
            "上樓梯 (用力時)",
            "下樓梯 (著地時)",
            "蹲下 (全蹲)",
            "久坐後站起來",
            "伸直膝蓋 (完全打直)",
            "彎曲膝蓋 (往後勾)"
        ]
        passives = ["完全不動/休息", "坐著腳伸直", "輕微走動", "熱敷/冰敷"]
        
        show_movement_section("膝蓋", movements, passives)

    # 4. 肩膀 (Elevation vs Rotation)
    elif "肩" in pain_location:
        movements = [
            "手舉高過頭 (大於90度)",
            "手向外平舉 (側平舉)",
            "手背到背後 (扣內衣/抓癢)",
            "手摸對側肩膀",
            "側睡壓到患側"
        ]
        passives = ["手自然垂放", "手有支撐 (扶手/口袋)", "睡覺抱枕頭", "熱敷/冰敷"]
        
        show_movement_section("肩膀", movements, passives)
        
    # 5. 足踝
    elif "踝" in pain_location or "足" in pain_location:
        movements = [
            "下床踩地第一步",
            "踮腳尖 (推蹬)",
            "腳板向上勾",
            "長時間走路/跑步",
            "久站"
        ]
        passives = ["坐著腳抬高", "穿鞋子/鞋墊", "按摩足底", "休息不動"]
        
        show_movement_section("足踝", movements, passives)

    # 6. 其他/通用
    else:
        movements = [
            "彎曲患處",
            "伸直患處",
            "負重/用力時",
            "長時間維持同一姿勢",
            "快速動作時"
        ]
        passives = ["休息不動", "熱敷/冰敷", "輕微活動", "按摩"]
        
        show_movement_section("患處", movements, passives)
        st.text_input("其他補充 (若無可跳過)", placeholder="例如：拿重物時手肘特別痛...")

    # === 按鈕 ===
    st.markdown("---")
    submitted = st.form_submit_button("✨ 產生評估報告", use_container_width=True)


# --- 報告生成區 ---
if submitted:
    st.success("評估報告已生成！")
    
    # 格式化列表輸出
    agg_str = "、".join(agg_factors) if agg_factors else "未勾選"
    ease_str = "、".join(ease_factors) if ease_factors else "未勾選"

    # 1. 顯示使用者輸入摘要
    st.write("---")
    st.subheader("📋 您的輸入摘要")
    
    # 使用 container 來排版
    with st.container():
        st.write(f"**📍 主要患處:** {pain_location}")
        st.write(f"**🔢 疼痛指數:** {vas_score}/10")
        st.markdown("---")
        
        c_res1, c_res2 = st.columns(2)
        with c_res1:
            st.error(f"**😫 惡化因子 (Aggravating):**\n\n {agg_str}")
        with c_res2:
            st.success(f"**😌 緩解因子 (Easing):**\n\n {ease_str}")

    # 2. 區域安全篩檢 (Red Flags Analysis)
    st.markdown("---")
    st.markdown('<div class="main-header">🛡️ 7. 區域安全篩檢 (Red Flags Analysis)</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="report-box">', unsafe_allow_html=True)
    st.write(f"針對您選擇的部位 **「{pain_location}」**，請自我檢測是否有以下狀況：")
    
    if "頭頸" in pain_location:
        st.checkbox("是否伴隨嚴重的頭暈、噁心或複視（看東西有重影）？")
        st.checkbox("是否有雙手同時麻木或無力的現象？")
    elif "腰" in pain_location or "背" in pain_location:
        st.checkbox("是否有大小便失禁或排尿困難的問題？")
        st.checkbox("是否有馬鞍部（鼠蹊部與大腿內側）麻木的感覺？")
        st.checkbox("是否有雙腳同時無力導致容易跌倒？")
    elif "膝" in pain_location:
        st.checkbox("膝蓋是否曾經完全「卡死」動彈不得？")
        st.checkbox("外觀是否有明顯的發紅、發熱或異常腫脹？")
    else:
        st.checkbox("是否在夜間睡覺時也會劇烈疼痛，甚至痛醒？")
        st.checkbox("是否有不明原因的體重減輕或發燒？")
        st.checkbox("疼痛是否與特定的意外撞擊或外傷有關？")
    
    st.markdown("<br><b>⚠️ 注意：若您勾選了上述任何一項，這可能代表較嚴重的病理狀況（Red Flags），強烈建議您儘速前往醫院接受專科醫師的詳細檢查。</b>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)