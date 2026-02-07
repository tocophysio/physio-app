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
        font-size: 22px;
        font-weight: bold;
        color: #2E86C1;
        margin-top: 25px;
        margin-bottom: 15px;
        padding-bottom: 5px;
        border-bottom: 1px solid #eee;
    }
    .subtitle {
        font-size: 18px;
        font-weight: 600;
        color: #555;
        margin-top: -15px;
        margin-bottom: 20px;
    }
    .warning-box {
        background-color: #fff3cd;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #ffc107;
        margin-bottom: 15px;
    }
    .danger-box {
        background-color: #f8d7da;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #dc3545;
        color: #721c24;
        margin-bottom: 15px;
    }
    .stCheckbox label { font-size: 16px; }
    </style>
    """, unsafe_allow_html=True)

# --- 標題區域 ---
st.title("⏱️ 1分鐘骨骼痛症篩檢系統")
st.markdown('<div class="subtitle">Musculoskeletal Screening System</div>', unsafe_allow_html=True)
st.write("請依照您的實際狀況填寫以下資訊，系統將協助評估風險與動作模式。")
st.markdown("---")

# --- 免責聲明 ---
st.warning(
    """
    **⚠️ 免責聲明 (Disclaimer)**：
    本報告僅供衛教用途與初步參考，**不可取代專業醫療診斷**。
    若您感到劇烈不適或有特定徵兆，請務必諮詢專科醫師或物理治療師，進行實體臨床評估。
    """
)

if "report_generated" not in st.session_state:
    st.session_state.report_generated = False

# --- 表單開始 ---
with st.form("intake_form"):

    # === Section 1: 基本資料 ===
    st.markdown('<div class="main-header">📄 1. 基本資料</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        gender = st.selectbox("生理性別", ["請選擇", "男", "女"], index=0)
    with c2:
        age = st.selectbox("年齡區間", ["18歲以下", "19-30歲", "31-45歲", "46-60歲", "60歲以上"], index=2)

    occupation = st.selectbox("職業類型", [
        "靜態久坐類 (辦公室/司機)",
        "勞力工作類 (搬運/工地)",
        "久站服務類 (專櫃/餐飲)",
        "家務操持",
        "運動員/教練",
        "退休/其他"
    ])

    # === Section 2: 患處定位 ===
    st.markdown('<div class="main-header">📍 2. 患處定位</div>', unsafe_allow_html=True)
    pain_location = st.selectbox("主要疼痛位置", [
        "-- 請選擇 --", "頸椎/頭部", "肩膀/上肢", "腰椎/下背",
        "髖部/骨盆", "膝蓋", "腳踝/足部", "其他"
    ])

    vas_score = st.slider("目前疼痛分數 (0不痛 ~ 10劇痛)", 0, 10, 5)

    # === Section 3: 紅旗警訊 (Red Flags) ===
    st.markdown('<div class="main-header">🛡️ 3. 危險徵兆篩檢 (Red Flags)</div>', unsafe_allow_html=True)
    st.info("此區塊用於篩檢是否需要「立即就醫」。請勾選您目前 **符合** 的狀況：")

    red_flag_options = [
        "有大小便控制問題 (失禁或排尿困難)",
        "近期體重有不明原因的快速減輕",
        "伴隨發燒、畏寒或嚴重夜間痛 (痛到醒來)",
        "曾經有嚴重外傷/跌倒後才出現疼痛",
        "休息不動時也會劇烈疼痛 (Rest Pain)",
        "雙腳/雙手同時出現麻木或無力",
        "胸痛伴隨呼吸困難"
    ]

    selected_red_flags = st.multiselect(
        "請下拉選擇 (若無下列症狀，請選擇「皆沒有」)：",
        options=["皆沒有"] + red_flag_options,
        default=["皆沒有"]
    )

    # === Section 4: 症狀特徵與功能影響 ===
    st.markdown('<div class="main-header">🔍 4. 症狀特徵與影響</div>', unsafe_allow_html=True)

    col_sym1, col_sym2 = st.columns(2)
    with col_sym1:
        st.markdown("**伴隨症狀 (可複選):**")
        symptoms = []
        if st.checkbox("感到無力 (Weakness)"): symptoms.append("無力")
        if st.checkbox("感覺卡住了 (Locking/Clicking)"): symptoms.append("卡住感")
        if st.checkbox("角度上不去/活動受限 (ROM loss)"): symptoms.append("角度受限")
        if st.checkbox("有拉扯感 (Pulling sensation)"): symptoms.append("拉扯感")
        if st.checkbox("麻木或針刺感 (Numbness)"): symptoms.append("麻木")

    with col_sym2:
        st.markdown("**功能影響 (可複選):**")
        impacts = []
        if st.checkbox("影響日常活動 (穿衣/工作)"): impacts.append("影響日常")
        if st.checkbox("影響睡眠 (Sleep disturbance)"): impacts.append("影響睡眠")
        if st.checkbox("需要藥物止痛"): impacts.append("需藥物止痛")
        if st.checkbox("失去平衡/容易跌倒"): impacts.append("失去平衡")

    # === Section 5: 動作模式檢測 ===
    st.markdown('<div class="main-header">🚶 5. 動作模式檢測</div>', unsafe_allow_html=True)

    st.markdown("**😫 什麼時候比較痛 (誘發因子)?**")
    triggers = st.multiselect("請選擇會加劇疼痛的動作 (可複選)", [
        "久坐", "久站", "走路", "上樓梯", "下樓梯",
        "轉身/轉彎", "一動就痛", "不動也痛", "彎腰", "後仰/挺身", "手舉高"
    ])

    st.markdown("**😌 做什麼比較舒服 (緩解因子)?**")
    relievers = st.multiselect("請選擇會減輕疼痛的方式 (可複選)", [
        "休息/不活動", "熱敷", "冰敷", "改變姿勢",
        "晚上較減緩", "走路/活動後", "沒有改善"
    ])

    # === 送出按鈕 ===
    st.markdown("---")
    submit_btn = st.form_submit_button("📋 產生評估報告", use_container_width=True)

# --- 邏輯處理與報告生成 ---
if submit_btn:
    # 驗證必填欄位
    validation_errors = []
    if gender == "請選擇":
        validation_errors.append("請選擇生理性別")
    if pain_location == "-- 請選擇 --":
        validation_errors.append("請選擇疼痛部位")

    if validation_errors:
        for err in validation_errors:
            st.error(f"❌ {err}")
    else:
        st.session_state.report_generated = True

        # 紅旗警訊邏輯判斷
        has_red_flags = False
        valid_red_flags = []

        if "皆沒有" in selected_red_flags and len(selected_red_flags) > 1:
            valid_red_flags = [x for x in selected_red_flags if x != "皆沒有"]
            has_red_flags = True
        elif "皆沒有" in selected_red_flags:
            has_red_flags = False
        elif not selected_red_flags:
            has_red_flags = False
        else:
            valid_red_flags = selected_red_flags
            has_red_flags = True

        # --- 顯示報告 ---
        st.markdown("---")
        st.markdown("## 📊 初步篩檢報告")
        st.markdown('<div class="subtitle">Screening Report</div>', unsafe_allow_html=True)

        # 1. 最優先顯示紅旗警訊結果
        if has_red_flags:
            st.markdown(f"""
            <div class="danger-box">
                <h4>🚨 警告：檢測到紅旗警訊 (Red Flags)</h4>
                <p>您勾選了以下危險徵兆：</p>
                <ul>
                    {''.join([f'<li>{flag}</li>' for flag in valid_red_flags])}
                </ul>
                <p><strong>建議：</strong>這些症狀可能代表較嚴重的病理問題（如神經壓迫、感染、骨折等），
                <b>請勿單純依賴運動改善，建議儘速前往醫院接受專科醫師檢查。</b></p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.success("✅ 紅旗警訊篩檢：未發現明顯危險徵兆 (Safe to proceed with care)")

        # 2. 摘要資訊
        st.markdown("#### 📝 狀況摘要")

        info_c1, info_c2, info_c3 = st.columns(3)
        with info_c1:
            st.metric("性別", gender)
        with info_c2:
            st.metric("年齡", age)
        with info_c3:
            st.metric("疼痛指數", f"{vas_score}/10")

        c_res1, c_res2 = st.columns(2)
        with c_res1:
            st.write(f"**📍 部位:** {pain_location}")
            st.write(f"**💼 職業:** {occupation}")
            st.write(f"**🩺 伴隨症狀:** {'、'.join(symptoms) if symptoms else '無'}")
        with c_res2:
            st.write(f"**⚡ 功能影響:** {'、'.join(impacts) if impacts else '尚可'}")
            st.write(f"**😫 誘發因子:** {'、'.join(triggers) if triggers else '未選擇'}")
            st.write(f"**😌 緩解因子:** {'、'.join(relievers) if relievers else '未選擇'}")

        # 3. 動作模式分析
        st.markdown("---")
        st.markdown("#### 💡 動作模式與建議")

        notes = []

        if "不動也痛" in triggers or "一動就痛" in triggers:
            notes.append(
                "🔸 **急性發炎期特徵**：無論動或不動都不舒服，"
                "建議目前以「休息、消炎、避免疼痛動作」為優先，暫不適合高強度訓練。"
            )

        if "上樓梯" in triggers or "下樓梯" in triggers:
            notes.append(
                "🔸 **承重/膝關節特徵**：上下樓梯疼痛通常與膝關節承受壓力"
                "或核心/臀部肌力不足有關。"
            )

        if "久坐" in triggers and ("彎腰" in triggers or "腰椎/下背" in pain_location):
            notes.append(
                "🔸 **屈曲不耐受 (Flexion Intolerance)**：久坐或彎腰會痛，"
                "建議使用腰靠，每30分鐘起身活動，避免長時間坐沙發。"
            )

        if "後仰/挺身" in triggers:
            notes.append(
                "🔸 **伸直不耐受 (Extension Intolerance)**：後仰或挺身會痛，"
                "建議避免長時間站立，可嘗試輕微前彎或坐下休息。"
            )

        if "手舉高" in triggers and "肩膀" in pain_location:
            notes.append(
                "🔸 **上舉受限 (Overhead Pattern)**：手舉過頭疼痛，"
                "可能涉及肩夾擠或旋轉肌群問題，建議評估肩胛穩定性。"
            )

        if "熱敷" in relievers:
            notes.append("🔹 熱敷能緩解，顯示肌肉緊繃或慢性循環問題可能較明顯。")
        if "冰敷" in relievers:
            notes.append("🔹 冰敷能緩解，顯示目前患處可能仍有急性發炎或腫脹。")
        if "沒有改善" in relievers:
            notes.append("🔹 任何方式都無法改善，建議優先尋求專業評估，釐清疼痛來源。")

        if not notes:
            notes.append("🔹 您的疼痛模式較為複雜，建議由物理治療師進行現場動作評估。")

        for n in notes:
            st.write(n)

        # 4. 結尾建議
        st.markdown("---")
        st.subheader("📌 建議下一步")

        if has_red_flags:
            st.error("🚨 **立即就醫**：您有紅旗警訊，建議儘速就醫進行詳細檢查。")
        elif vas_score >= 7:
            st.warning("⚠️ **建議就醫**：雖無紅旗警訊，但疼痛指數較高，建議盡快就醫或接受物理治療評估。")
        elif vas_score >= 4:
            st.info("💡 **建議追蹤**：中度疼痛，建議安排物理治療師進行完整評估，並注意動作模式調整。")
        else:
            st.success("👍 **持續觀察**：目前疼痛程度較輕，可先透過衛教與自我管理改善，若持續不適再就醫。")

        # 5. 再次提醒免責聲明
        st.caption("⚠️ 本報告僅供衛教參考，不可取代專業醫療診斷。如有疑慮請諮詢醫師或物理治療師。")
        st.caption("📝 本報告可截圖保存，並攜帶至就診時提供給醫療人員參考。")