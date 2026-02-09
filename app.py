import streamlit as st

st.set_page_config(page_title="1分鐘骨骼痛症篩檢", page_icon="🦴", layout="centered")

st.markdown("""
    <style>
    .main-header {
        font-size: 22px; font-weight: bold; color: #1a1a2e;
        margin-top: 25px; margin-bottom: 15px; padding-bottom: 8px;
        border-bottom: 2px solid #2E86C1;
    }
    .subtitle {
        font-size: 17px; font-weight: 500; color: #666;
        margin-top: -15px; margin-bottom: 20px; letter-spacing: 0.5px;
    }
    .danger-box {
        background-color: #f8d7da; padding: 15px; border-radius: 8px;
        border-left: 5px solid #dc3545; color: #721c24; margin-bottom: 15px;
    }
    .pattern-box {
        background-color: #e8f4f8; padding: 14px 16px; border-radius: 6px;
        border-left: 4px solid #2E86C1; margin-bottom: 10px;
        font-weight: 600; color: #1a1a2e;
    }
    .nerve-box {
        background-color: #fff3e0; padding: 14px 16px; border-radius: 6px;
        border-left: 4px solid #e65100; margin-bottom: 10px;
        font-weight: 600; color: #1a1a2e;
    }
    .joint-box {
        background-color: #e8f5e9; padding: 14px 16px; border-radius: 6px;
        border-left: 4px solid #2e7d32; margin-bottom: 10px;
        font-weight: 600; color: #1a1a2e;
    }
    .inflam-box {
        background-color: #fce4ec; padding: 14px 16px; border-radius: 6px;
        border-left: 4px solid #c62828; margin-bottom: 10px;
        font-weight: 600; color: #1a1a2e;
    }
    .muscle-box {
        background-color: #e3f2fd; padding: 14px 16px; border-radius: 6px;
        border-left: 4px solid #1565c0; margin-bottom: 10px;
        font-weight: 600; color: #1a1a2e;
    }
    .bone-box {
        background-color: #efebe9; padding: 14px 16px; border-radius: 6px;
        border-left: 4px solid #5d4037; margin-bottom: 10px;
        font-weight: 600; color: #1a1a2e;
    }
    .vascular-box {
        background-color: #f3e5f5; padding: 14px 16px; border-radius: 6px;
        border-left: 4px solid #7b1fa2; margin-bottom: 10px;
        font-weight: 600; color: #1a1a2e;
    }
    .sympathetic-box {
        background-color: #fff8e1; padding: 14px 16px; border-radius: 6px;
        border-left: 4px solid #f9a825; margin-bottom: 10px;
        font-weight: 600; color: #1a1a2e;
    }
    .acuity-box {
        background-color: #f5f5f5; padding: 14px 16px; border-radius: 6px;
        border-left: 4px solid #616161; margin-bottom: 10px;
        font-weight: 600; color: #1a1a2e;
    }
    .pain-chip {
        display: inline-block; padding: 4px 12px; margin: 3px;
        border-radius: 16px; font-size: 13px; font-weight: 500;
    }
    .chip-muscle { background-color: #e3f2fd; border: 1px solid #1565c0; color: #0d47a1; }
    .chip-ligament { background-color: #e8f5e9; border: 1px solid #2e7d32; color: #1b5e20; }
    .chip-nerve { background-color: #fff3e0; border: 1px solid #e65100; color: #bf360c; }
    .chip-sympathetic { background-color: #fff8e1; border: 1px solid #f9a825; color: #e65100; }
    .chip-bone { background-color: #efebe9; border: 1px solid #5d4037; color: #3e2723; }
    .chip-fracture { background-color: #f8d7da; border: 1px solid #dc3545; color: #721c24; }
    .chip-vascular { background-color: #f3e5f5; border: 1px solid #7b1fa2; color: #4a148c; }
    .section-label {
        font-size: 16px; font-weight: 600; color: #333;
        margin-top: 10px; margin-bottom: 5px;
    }
    .stCheckbox label { font-size: 15px; }
    </style>
""", unsafe_allow_html=True)

st.title("骨骼肌肉痛症 — 1 分鐘快速篩檢")
st.markdown('<div class="subtitle">Musculoskeletal Quick Screening System</div>', unsafe_allow_html=True)
st.write("請依照您的實際狀況填寫以下資訊，系統將依據臨床邏輯協助初步評估。")
st.markdown("---")

st.warning(
    "**免責聲明｜Disclaimer**　"
    "本報告僅供衛教用途與初步參考，不可取代專業醫療診斷。"
    "若您感到劇烈不適或出現特定徵兆，請務必諮詢專科醫師或物理治療師進行實體臨床評估。"
)

if "report_generated" not in st.session_state:
    st.session_state.report_generated = False


def get_region_key(loc):
    if "頸" in loc or "頭" in loc: return "cervical"
    if "肩" in loc: return "shoulder"
    if "手肘" in loc or "手腕" in loc or "手指" in loc: return "wrist_hand"
    if "腰" in loc or "下背" in loc: return "lumbar"
    if "髖" in loc or "骨盆" in loc: return "hip"
    if "膝" in loc: return "knee"
    if "踝" in loc or "足" in loc: return "ankle"
    return "general"

def is_spine(r): return r in ("cervical", "lumbar")
def is_upper_limb(r): return r in ("shoulder", "wrist_hand")
def is_lower_limb(r): return r in ("hip", "knee", "ankle")


PAIN_QUALITY_OPTIONS = [
    "抽筋感 (Cramping) — 肌肉緊縮、抽住的感覺",
    "鈍痛 (Dull) — 悶悶的、不尖銳的不舒服",
    "酸痛 (Aching) — 像運動後的痠、持續性的不適",
    "尖銳痛 (Sharp) — 像刀割、非常明確的痛感",
    "陣陣刺痛 (Shooting) — 一陣一陣竄過去的痛",
    "閃電般痛 (Lightning) — 像觸電、瞬間劇痛",
    "灼熱感 (Burning) — 像燒燙、熱辣辣的",
    "有壓力感 (Pressure) — 悶脹、壓迫的感覺",
    "針蟄感 (Stinging) — 像被蟲蟄、表淺的刺痛",
    "深部痛 (Deep) — 來自很深層、說不出確切位置",
    "煩人的隱痛 (Nagging) — 持續存在、揮之不去",
    "尖銳且無法忍受 (Sharp & Intolerable) — 劇烈到無法承受",
    "抽痛 (Throbbing) — 隨心跳一跳一跳地痛",
    "擴散的 (Diffuse) — 範圍廣、界線不清楚",
    "按壓痛 (Tender) — 壓下去才痛、有明確痛點",
]

PAIN_TISSUE_MAP = {
    "抽筋感": ["muscle"],
    "鈍痛": ["muscle", "ligament", "bone"],
    "酸痛": ["muscle", "ligament", "sympathetic"],
    "尖銳痛": ["nerve_root", "nerve", "fracture"],
    "陣陣刺痛": ["nerve_root"],
    "閃電般痛": ["nerve"],
    "灼熱感": ["sympathetic"],
    "有壓力感": ["sympathetic"],
    "針蟄感": ["sympathetic"],
    "深部痛": ["bone"],
    "煩人的隱痛": ["bone"],
    "尖銳且無法忍受": ["fracture"],
    "抽痛": ["vascular"],
    "擴散的": ["vascular"],
    "按壓痛": ["muscle"],
}

TISSUE_LABELS = {
    "muscle": "肌肉 (Muscle)",
    "ligament": "韌帶 / 關節囊 (Ligament / Capsule)",
    "nerve_root": "神經根 (Nerve Root)",
    "nerve": "周邊神經 (Peripheral Nerve)",
    "sympathetic": "交感神經 / 神經病變 (Sympathetic / Neuropathic)",
    "bone": "骨骼 (Bone)",
    "fracture": "骨折 (Fracture)",
    "vascular": "血管 (Vascular)",
}

TISSUE_CHIP = {
    "muscle": "chip-muscle", "ligament": "chip-ligament",
    "nerve_root": "chip-nerve", "nerve": "chip-nerve",
    "sympathetic": "chip-sympathetic", "bone": "chip-bone",
    "fracture": "chip-fracture", "vascular": "chip-vascular",
}

TISSUE_BOX = {
    "muscle": "muscle-box", "ligament": "joint-box",
    "nerve_root": "nerve-box", "nerve": "nerve-box",
    "sympathetic": "sympathetic-box", "bone": "bone-box",
    "fracture": "inflam-box", "vascular": "vascular-box",
}


def parse_pain_quality(pq_list):
    result = {}
    for pq in pq_list:
        short = pq.split("(")[0].strip()
        for key in PAIN_TISSUE_MAP:
            if key in short:
                for tissue in PAIN_TISSUE_MAP[key]:
                    result.setdefault(tissue, [])
                    if key not in result[tissue]:
                        result[tissue].append(key)
                break
    return result


def get_tissue_priority(hits):
    order = ["fracture", "vascular", "nerve_root", "nerve", "sympathetic", "bone", "ligament", "muscle"]
    return [t for t in order if t in hits]


MYOFASCIAL = {
    "cervical": {"muscles": "上斜方肌、提肩胛肌、胸鎖乳突肌、深層屈肌群", "common": "長時間低頭、螢幕位置不當、枕頭不合適", "self_care": "頸部伸展、調整螢幕高度、注意枕頭"},
    "shoulder": {"muscles": "斜方肌、菱形肌、棘下肌、三角肌", "common": "聳肩打字、側睡壓迫、重複手臂動作", "self_care": "肩膀放鬆、肩胛穩定訓練"},
    "wrist_hand": {"muscles": "前臂屈肌群、伸肌群、大魚際肌", "common": "打字/滑手機、握力過度、重複動作", "self_care": "前臂伸展、人體工學調整"},
    "lumbar": {"muscles": "腰方肌、豎脊肌群、多裂肌、腰大肌", "common": "久坐駝背、搬重物不當、核心不足", "self_care": "腰部伸展、核心訓練、使用腰靠"},
    "hip": {"muscles": "臀大肌、臀中肌、梨狀肌、髂腰肌", "common": "久坐臀肌失能、骨盆不對稱", "self_care": "臀肌啟動、髖屈肌伸展"},
    "knee": {"muscles": "股四頭肌、髂脛束、膕旁肌群", "common": "肌力不平衡、過度跑步/深蹲", "self_care": "股四頭肌與膕旁肌伸展、漸進式訓練"},
    "ankle": {"muscles": "腓腸肌、比目魚肌、脛後肌、足底筋膜", "common": "久站、鞋子不合、扁平足/高弓足", "self_care": "小腿伸展、足底按摩、鞋墊支撐"},
    "general": {"muscles": "局部肌群", "common": "長時間固定姿勢", "self_care": "伸展放鬆、調整姿勢"},
}

LOCKING = {
    "cervical": {"causes": "小面關節卡鎖、急性落枕、頸椎退化", "example": "轉頭某角度突然卡住", "note": "伴上肢放射痛需排除椎間盤"},
    "shoulder": {"causes": "關節唇撕裂、鈣化性肌腱炎、肩關節沾黏", "example": "手舉到某角度突然卡住或彈響", "note": "伴疼痛或脫位感建議影像"},
    "wrist_hand": {"causes": "板機指、TFCC 損傷、腕關節游離體", "example": "手指彎曲卡住彈不回來", "note": "板機指好發拇指與中指"},
    "lumbar": {"causes": "小面關節卡鎖、急性肌肉痙攣、腰椎不穩定", "example": "彎腰後直不起來（閃到腰）", "note": "反覆卡鎖需評估脊椎穩定性"},
    "hip": {"causes": "髖關節唇撕裂、彈響髖、游離體", "example": "走路或抬腿時髖關節彈響", "note": "伴鼠蹊部痛需評估關節唇"},
    "knee": {"causes": "半月板損傷、游離體、髕骨軌跡異常", "example": "蹲下站起時卡住或彈響", "note": "完全鎖住高度懷疑半月板"},
    "ankle": {"causes": "前方撞擊、距骨軟骨損傷、腓骨肌腱滑脫", "example": "背屈時前方卡住", "note": "反覆扭傷後卡感可能慢性不穩定"},
    "general": {"causes": "游離體、肌腱滑動異常", "example": "特定動作卡住或彈響", "note": "伴疼痛或腫脹建議就醫"},
}

JOINT_PAIN = {
    "cervical": {
        "young": "頸椎小面關節功能障礙、韌帶過度拉伸、姿勢性關節壓力",
        "older": "頸椎小面關節退化、椎間盤退化性變化、鉤椎關節增生",
        "note_young": "年輕族群較少退化性問題，通常與姿勢、使用習慣或外傷有關",
        "note_older": "40 歲以上較常見退化性變化，但影像退化不一定等於症狀來源",
    },
    "shoulder": {
        "young": "肩鎖關節損傷、盂肱關節韌帶鬆弛、肩關節不穩定",
        "older": "肩鎖關節退化、盂肱關節退化、旋轉肌群慢性損傷",
        "note_young": "年輕族群肩膀鈍痛較常與過度使用或運動傷害有關",
        "note_older": "深層鈍痛且夜間加劇需注意旋轉肌群病變",
    },
    "wrist_hand": {
        "young": "腕關節韌帶扭傷、TFCC 損傷、關節囊發炎",
        "older": "CMC 關節退化、Heberden's nodes、舟月骨韌帶損傷",
        "note_young": "年輕族群手部關節問題多與重複動作或運動外傷有關",
        "note_older": "好發拇指基部與指末端關節",
    },
    "lumbar": {
        "young": "腰椎小面關節功能障礙、韌帶過度負荷、薦髂關節功能異常、椎間盤早期損傷",
        "older": "腰椎小面關節退化、椎間盤退化、薦髂關節功能障礙",
        "note_young": "年輕族群的腰椎關節問題通常與姿勢不良、負重方式或核心不足有關，不一定代表退化",
        "note_older": "退化性變化常見但不一定是疼痛主因，需結合理學檢查",
    },
    "hip": {
        "young": "髖關節唇損傷、股骨髖臼夾擠（FAI）、髖關節韌帶扭傷",
        "older": "髖關節退化性關節炎、股骨頭缺血性壞死、髖關節唇損傷",
        "note_young": "年輕族群髖部鈍痛需注意 FAI 或關節唇問題，尤其好發於運動族群",
        "note_older": "典型為鼠蹊部深層鈍痛，活動後改善",
    },
    "knee": {
        "young": "髕骨軟化症、韌帶扭傷（ACL/MCL）、滑膜皺壁症候群、半月板損傷",
        "older": "退化性關節炎、軟骨磨損、髕骨軟化症",
        "note_young": "年輕族群膝蓋鈍痛較常與運動負荷、肌力不平衡或韌帶問題有關",
        "note_older": "晨僵：起床後僵硬，活動後改善",
    },
    "ankle": {
        "young": "踝關節韌帶扭傷後遺、距骨軟骨損傷、踝關節不穩定",
        "older": "踝關節退化性關節炎、距骨軟骨損傷、足弓結構異常",
        "note_young": "年輕族群踝關節鈍痛常見於反覆扭傷後的慢性不穩定",
        "note_older": "反覆扭傷可能提早退化",
    },
    "general": {
        "young": "關節囊損傷、韌帶過度負荷",
        "older": "退化性關節變化、軟骨磨損",
        "note_young": "年輕族群較少退化問題，多與使用方式有關",
        "note_older": "持續加重建議影像檢查",
    },
}

ROM_LOSS = {
    "cervical": {"causes": "小面關節僵硬、急性落枕、頸椎退化", "note": "伴上肢症狀需排除神經壓迫"},
    "shoulder": {"causes": "冰凍肩、旋轉肌群損傷、關節囊沾黏", "note": "五十肩典型各方向漸進喪失"},
    "wrist_hand": {"causes": "屈肌腱沾黏、骨折後僵硬", "note": "手部精細動作需完整活動度"},
    "lumbar": {"causes": "急性痙攣、椎間盤突出急性期、退化性僵硬", "note": "急性期受限通常是保護性的"},
    "hip": {"causes": "髖關節退化、關節囊緊縮、髖屈肌攣縮", "note": "內轉與屈曲受限是退化早期徵兆"},
    "knee": {"causes": "關節積液、半月板嵌頓、術後沾黏", "note": "無法完全伸直或彎曲影響步態"},
    "ankle": {"causes": "扭傷後僵硬、跟腱緊縮、前方撞擊", "note": "背屈不足影響深蹲與上下樓梯"},
    "general": {"causes": "關節囊緊縮、肌肉痙攣", "note": "區分『不敢動』與『動不了』很重要"},
}


with st.form("intake_form"):
    st.markdown('<div class="main-header">1. 基本資料</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        gender = st.selectbox("生理性別", ["請選擇", "男", "女"], index=0)
    with c2:
        age = st.selectbox("年齡區間", ["18歲以下", "19-30歲", "31-45歲", "46-60歲", "60歲以上"], index=2)
    occupation = st.selectbox("職業類型", [
        "靜態久坐類 (辦公室/司機)", "勞力工作類 (搬運/工地)",
        "久站服務類 (專櫃/餐飲)", "家務操持", "運動員/教練", "退休/其他"
    ])

    st.markdown('<div class="main-header">2. 患處定位與病程</div>', unsafe_allow_html=True)
    pain_location = st.selectbox("主要疼痛位置", [
        "-- 請選擇 --", "頸椎 / 頭部", "肩膀 / 上肢", "手肘 / 手腕 / 手指",
        "腰椎 / 下背", "髖部 / 骨盆", "膝蓋", "腳踝 / 足部", "其他"
    ])
    vas_score = st.slider("目前疼痛分數（VAS: 0 = 不痛，10 = 劇痛）", 0, 10, 5)

    st.markdown('<div class="section-label">這個問題持續多久了？</div>', unsafe_allow_html=True)
    duration = st.radio("請選擇最接近的時間範圍：", [
        "剛發生（一週內）— 急性期 Acute",
        "一陣子了（2 週 ~ 3 個月）— 亞急性期 Subacute",
        "很久了（超過 3 個月）— 慢性期 Chronic",
    ], index=0, horizontal=True)

    st.markdown('<div class="section-label">疼痛的刺激程度（Irritability）</div>', unsafe_allow_html=True)
    st.caption("幫助判斷目前組織的敏感程度")
    irritability = st.radio("請選擇最符合您的狀況：", [
        "很容易被激發 — 輕微動作或還沒動就開始痛，且痛很久才消退",
        "需要一定活動量才會痛 — 動一陣子才痛，休息後會改善",
        "要比較大的動作才會痛 — 只有特定動作或大力時才不舒服",
    ], index=1)

    st.markdown('<div class="section-label">疼痛範圍有無變化？</div>', unsafe_allow_html=True)
    spreading = st.radio("與剛開始相比，疼痛的位置或範圍：", [
        "維持在原來的位置，沒有改變",
        "範圍有擴大，或會延伸到其他部位",
        "有時候痛的位置會跑來跑去",
    ], index=0)

    st.markdown('<div class="main-header">3. 疼痛性質（依 Magee 分類）</div>', unsafe_allow_html=True)
    st.caption("不同的疼痛感覺對應不同的組織來源")
    pain_quality = st.multiselect("您的疼痛感覺最接近哪些？（可複選）", PAIN_QUALITY_OPTIONS)

    st.markdown('<div class="main-header">4. 危險徵兆篩檢（Red Flags）</div>', unsafe_allow_html=True)
    st.info("以下項目用於排除需要立即就醫的狀況。")
    selected_red_flags = st.multiselect("若無下列症狀請選擇「皆沒有」：", [
        "皆沒有",
        "大小便控制問題（失禁或排尿困難）",
        "近期不明原因體重快速減輕",
        "伴隨發燒、畏寒或嚴重夜間痛（痛到醒來）",
        "嚴重外傷 / 跌倒後才出現的疼痛",
        "靜止不動時仍劇烈疼痛（Rest Pain）",
        "雙側肢體同時出現麻木或無力",
        "胸痛伴隨呼吸困難"
    ], default=["皆沒有"])

    st.markdown('<div class="main-header">5. 伴隨症狀與功能影響</div>', unsafe_allow_html=True)
    cs1, cs2 = st.columns(2)
    with cs1:
        st.markdown('<div class="section-label">伴隨症狀（可複選）</div>', unsafe_allow_html=True)
        symptoms = []
        if st.checkbox("感到無力（Weakness）"): symptoms.append("無力")
        if st.checkbox("感覺卡住（Locking / Clicking）"): symptoms.append("卡住感")
        if st.checkbox("活動角度受限（ROM Loss）"): symptoms.append("角度受限")
    with cs2:
        st.markdown('<div class="section-label">功能影響（可複選）</div>', unsafe_allow_html=True)
        impacts = []
        if st.checkbox("影響日常活動（穿衣/工作）"): impacts.append("影響日常")
        if st.checkbox("影響睡眠（Sleep Disturbance）"): impacts.append("影響睡眠")
        if st.checkbox("需要藥物止痛"): impacts.append("需藥物止痛")
        if st.checkbox("容易失去平衡 / 跌倒"): impacts.append("失去平衡")

    st.markdown('<div class="main-header">6. 動作模式檢測</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-label">什麼情況會讓疼痛加劇？（誘發因子）</div>', unsafe_allow_html=True)
    triggers = st.multiselect("可複選", [
        "久坐", "久站", "走路", "上樓梯", "下樓梯",
        "轉身 / 轉彎", "一動就痛", "不動也痛",
        "彎腰", "後仰 / 挺身", "手舉高", "打噴嚏 / 咳嗽"
    ], key="triggers")
    st.markdown('<div class="section-label">什麼方式能讓疼痛緩解？（緩解因子）</div>', unsafe_allow_html=True)
    relievers = st.multiselect("可複選", [
        "休息 / 不活動", "熱敷", "冰敷", "改變姿勢",
        "晚上較減緩", "走路 / 活動後改善", "沒有任何改善"
    ], key="relievers")

    st.markdown("---")
    submit_btn = st.form_submit_button("產生評估報告", use_container_width=True)


if submit_btn:
    errors = []
    if gender == "請選擇": errors.append("請選擇生理性別")
    if pain_location == "-- 請選擇 --": errors.append("請選擇疼痛部位")
    if errors:
        for e in errors: st.error(e)
    else:
        st.session_state.report_generated = True
        region = get_region_key(pain_location)
        spine = is_spine(region)
        upper = is_upper_limb(region)
        lower = is_lower_limb(region)

        is_acute = "剛發生" in duration
        is_subacute = "一陣子" in duration
        is_chronic = "很久了" in duration

        high_irritability = "很容易被激發" in irritability
        mod_irritability = "需要一定活動量" in irritability
        low_irritability = "要比較大的動作" in irritability

        spreading_stable = "維持在原來" in spreading
        spreading_expanding = "範圍有擴大" in spreading
        spreading_migrating = "跑來跑去" in spreading

        is_young = age in ["18歲以下", "19-30歲", "31-45歲"]
        is_older = age in ["46-60歲", "60歲以上"]

        has_red_flags = False
        valid_red_flags = []
        if "皆沒有" in selected_red_flags and len(selected_red_flags) > 1:
            valid_red_flags = [x for x in selected_red_flags if x != "皆沒有"]; has_red_flags = True
        elif "皆沒有" not in selected_red_flags and selected_red_flags:
            valid_red_flags = selected_red_flags; has_red_flags = True

        tissue_hits = parse_pain_quality(pain_quality)
        tissue_priority = get_tissue_priority(tissue_hits)
        has_muscle = "muscle" in tissue_hits
        has_ligament = "ligament" in tissue_hits
        has_nerve_root = "nerve_root" in tissue_hits
        has_nerve = "nerve" in tissue_hits
        has_sympathetic = "sympathetic" in tissue_hits
        has_bone = "bone" in tissue_hits
        has_fracture = "fracture" in tissue_hits
        has_vascular = "vascular" in tissue_hits
        has_any_nerve = has_nerve_root or has_nerve or has_sympathetic

        has_weakness = "無力" in symptoms
        has_locking = "卡住感" in symptoms
        has_rom_loss = "角度受限" in symptoms

        flexion_agg = any(t in triggers for t in ["久坐", "彎腰"])
        sneeze_agg = "打噴嚏 / 咳嗽" in triggers
        extension_agg = any(t in triggers for t in ["後仰 / 挺身", "久站"])
        rest_pain = "不動也痛" in triggers
        move_pain = "一動就痛" in triggers
        disc_pattern = flexion_agg or sneeze_agg
        stenosis_pattern = extension_agg
        mixed_spine = disc_pattern and stenosis_pattern

        myo = MYOFASCIAL.get(region, MYOFASCIAL["general"])
        lock = LOCKING.get(region, LOCKING["general"])
        rom = ROM_LOSS.get(region, ROM_LOSS["general"])

        jt_raw = JOINT_PAIN.get(region, JOINT_PAIN["general"])
        if is_young:
            jt = {"causes": jt_raw["young"], "note": jt_raw["note_young"]}
        else:
            jt = {"causes": jt_raw["older"], "note": jt_raw["note_older"]}

        # =================== 報告 ===================
        st.markdown("---")
        st.markdown("## 篩檢評估報告")
        st.markdown('<div class="subtitle">Screening Assessment Report</div>', unsafe_allow_html=True)

        if has_red_flags:
            st.markdown(f"""
            <div class="danger-box">
                <b>紅旗警訊（Red Flags）— 檢測到危險徵兆</b><br><br>
                您勾選了以下項目：
                <ul>{''.join([f'<li>{f}</li>' for f in valid_red_flags])}</ul>
                <b>臨床建議：</b>上述症狀可能代表較嚴重的病理問題，建議儘速就醫。
            </div>""", unsafe_allow_html=True)
        else:
            st.success("紅旗警訊篩檢：未發現需立即就醫的危險徵兆")

        st.markdown("#### 基本資訊")
        m1, m2, m3 = st.columns(3)
        with m1: st.metric("性別", gender)
        with m2: st.metric("年齡", age)
        with m3: st.metric("VAS 疼痛指數", f"{vas_score} / 10")
        rc1, rc2 = st.columns(2)
        with rc1:
            st.write(f"**部位：** {pain_location}")
            st.write(f"**職業：** {occupation}")
            st.write(f"**伴隨症狀：** {'、'.join(symptoms) if symptoms else '無'}")
        with rc2:
            st.write(f"**功能影響：** {'、'.join(impacts) if impacts else '尚可'}")
            st.write(f"**誘發因子：** {'、'.join(triggers) if triggers else '未選擇'}")
            st.write(f"**緩解因子：** {'、'.join(relievers) if relievers else '未選擇'}")

        # === 病程與疼痛行為 ===
        st.markdown("---")
        st.markdown("#### 病程與疼痛行為分析")

        if is_acute:
            phase_label = "急性期（Acute）— 一週內"
            phase_detail = (
                "您的症狀屬於 **急性期**，組織可能正處於發炎與修復的初始階段。\n\n"
                "**急性疼痛的臨床特徵（Magee）：**\n"
                "- 疼痛通常較為嚴重、連續、甚至可能造成失能\n"
                "- 疼痛程度和持續時間嚴重到需要尋求協助\n"
                "- 動作發生前或僅少許活動就會產生症狀\n"
                "- 疼痛通常在動作停止後仍會持續一段時間\n"
                "- 常伴隨焦慮感\n\n"
                "**處理原則：**\n"
                "- 此階段以 **保護、減少發炎、控制疼痛** 為優先\n"
                "- 避免反覆測試或刺激疼痛動作\n"
                "- 相對休息（不是完全不動），避免加劇因子\n"
                "- 可考慮冰敷（急性發炎期）"
            )
        elif is_subacute:
            phase_label = "亞急性期（Subacute）— 2 週至 3 個月"
            phase_detail = (
                "您的症狀屬於 **亞急性期**，組織正處於修復與重塑的過渡階段。\n\n"
                "**亞急性期的臨床特徵：**\n"
                "- 疼痛程度通常已比急性期減輕\n"
                "- 開始能區分哪些動作會加劇、哪些不會\n"
                "- 組織正在癒合，但尚未完全恢復強度\n\n"
                "**處理原則：**\n"
                "- 此階段適合 **漸進式恢復活動**\n"
                "- 開始進行不會加劇疼痛的動作訓練\n"
                "- 注意不要過度保護（避免廢用性萎縮）\n"
                "- 如果症狀沒有逐漸改善，應重新評估診斷"
            )
        else:
            phase_label = "慢性期（Chronic）— 超過 3 個月"
            phase_detail = (
                "您的症狀屬於 **慢性期**，已超過一般組織修復的預期時間。\n\n"
                "**慢性疼痛的臨床特徵（Magee）：**\n"
                "- 疼痛是加劇性的（aggravating），但程度通常較急性期不強烈\n"
                "- 患者通常已經歷過這種疼痛，可能發展出自己的應對方式\n"
                "- 慢性疼痛常與 **憂鬱** 情緒有關（相對於急性期的焦慮）\n"
                "- 需要考慮疼痛是否已超越組織損傷本身，涉及 **中樞敏感化**\n\n"
                "**處理原則：**\n"
                "- 此階段需要 **全面性的評估與處理**\n"
                "- 除了物理層面，也需關注心理、睡眠、活動量等因素\n"
                "- 漸進式增加負荷與活動，建立信心\n"
                "- 過度依賴影像或反覆檢查可能增加焦慮，不一定有幫助"
            )

        st.markdown(f'<div class="acuity-box">{phase_label}</div>', unsafe_allow_html=True)
        st.markdown(phase_detail)
        st.write("")

        if high_irritability:
            irr_label = "高刺激性（High Irritability）"
            irr_detail = (
                "您的疼痛 **非常容易被激發**，輕微動作甚至還沒動就開始痛，且消退很慢。\n\n"
                "**臨床意義：**\n"
                "- 組織處於高度敏感狀態，可能仍有明顯的發炎反應\n"
                "- 或者神經系統對刺激的反應已經放大（周邊或中樞敏感化）\n\n"
                "**處理原則：**\n"
                "- 評估和治療時需要非常 **謹慎**，避免過度刺激\n"
                "- 活動量應從非常低的起點開始，緩慢漸進\n"
                "- 每次只改變一個變因，觀察反應"
            )
            if is_chronic:
                irr_detail += (
                    "\n\n**注意：** 您同時處於慢性期且高刺激性。這種組合較不尋常——"
                    "慢性期疼痛通常已不那麼容易被激發。若仍然高度敏感，需考慮：\n"
                    "- 是否有未被發現的結構問題\n"
                    "- 是否已發展為中樞敏感化\n"
                    "- 建議尋求專科醫師或疼痛科評估"
                )
        elif mod_irritability:
            irr_label = "中度刺激性（Moderate Irritability）"
            irr_detail = (
                "您的疼痛需要 **一定程度的活動量** 才會被誘發，休息後能改善。\n\n"
                "**臨床意義：**\n"
                "- 組織有一定的承受能力，但超過負荷閾值就會產生症狀\n"
                "- 這是最常見的臨床表現\n\n"
                "**處理原則：**\n"
                "- 找出「剛好不會引發疼痛」的活動量作為基準線\n"
                "- 在基準線上漸進式增加負荷\n"
                "- 可以進行適度的檢查與治療"
            )
        else:
            irr_label = "低刺激性（Low Irritability）"
            irr_detail = (
                "您的疼痛只有在 **較大的動作或特定動作** 時才會出現。\n\n"
                "**臨床意義：**\n"
                "- 組織的承受能力相對良好\n"
                "- 可以進行較完整的動作測試和評估\n\n"
                "**處理原則：**\n"
                "- 可以較積極地進行活動和訓練\n"
                "- 針對誘發疼痛的特定動作進行分析和改善\n"
                "- 適合進行較完整的理學檢查"
            )

        st.markdown(f'<div class="acuity-box">{irr_label}</div>', unsafe_allow_html=True)
        st.markdown(irr_detail)
        st.write("")

        if spreading_expanding:
            st.markdown('<div class="nerve-box">症狀範圍擴大（Expanding / Radiating）</div>', unsafe_allow_html=True)
            d = "您的疼痛範圍有 **擴大或延伸** 的趨勢。\n\n**臨床意義：**\n- 疼痛範圍擴大可能代表問題在惡化\n"
            if has_any_nerve:
                d += "- 合併神經性疼痛特徵，擴散若沿固定路徑，高度提示 **神經根壓迫加重**\n"
            if spine:
                d += "- 在脊椎問題中，疼痛向遠端延伸通常被視為不理想的進展方向\n"
            d += "\n**建議：** 疼痛範圍持續擴大應優先就醫。"
            st.markdown(d)
            st.write("")
        elif spreading_migrating:
            st.markdown('<div class="sympathetic-box">症狀位置游移（Migrating）</div>', unsafe_allow_html=True)
            d = "您的疼痛位置 **會跑來跑去**，沒有固定。\n\n**臨床意義：**\n- 多個部位同時有問題\n- 牽連痛（referred pain）\n- 中樞敏感化\n"
            if is_chronic: d += "- 慢性期合併游移性疼痛，中樞敏感化可能性較高\n"
            if has_sympathetic: d += "- 合併交感神經性疼痛特徵，需注意複雜性疼痛機制\n"
            d += "\n**建議：** 建議完整評估。"
            st.markdown(d)
            st.write("")

        if is_acute and high_irritability and (rest_pain or move_pain):
            st.markdown(
                "**病程整合提示：** 急性期 + 高刺激性 + 動靜皆痛 → "
                "組織正處於高度發炎或損傷狀態，目前 **不適合積極的動作測試或運動介入**。"
            )
            st.write("")
        if is_chronic and low_irritability:
            st.markdown(
                "**病程整合提示：** 慢性期 + 低刺激性 → "
                "適合 **較積極的功能性訓練與回歸日常活動**，重點在漸進式增加負荷。"
            )
            st.write("")
        if is_chronic and "沒有任何改善" in relievers:
            st.markdown(
                "**病程整合提示：** 慢性期 + 任何方式皆無法改善 → "
                "需考慮 **中樞敏感化、心理社會因素**，建議多面向評估。"
            )
            st.write("")

        # === 疼痛性質 → 組織來源 ===
        st.markdown("---")
        st.markdown("#### ⭐ 疼痛性質 → 組織來源分析")
        st.caption("依據 Magee's Orthopedic Physical Assessment 疼痛性質與組織來源對照")

        if pain_quality and tissue_priority:
            chips_html = ""
            for pq in pain_quality:
                short = pq.split("—")[0].strip()
                pk = None
                for key in PAIN_TISSUE_MAP:
                    if key in short: pk = key; break
                css = TISSUE_CHIP.get(PAIN_TISSUE_MAP[pk][0], "chip-neutral") if pk else "chip-neutral"
                chips_html += f'<span class="pain-chip {css}">{short}</span>'
            st.markdown(f"**所選疼痛性質：** {chips_html}", unsafe_allow_html=True)
            st.write("")

            st.markdown("⭐ **可能涉及的組織來源（依臨床優先順序）：**")
            for tissue in tissue_priority:
                descriptors = tissue_hits[tissue]
                label = TISSUE_LABELS[tissue]
                box_cls = TISSUE_BOX[tissue]
                desc_str = "、".join(descriptors)

                st.markdown(f'<div class="{box_cls}">{label}</div>', unsafe_allow_html=True)

                if tissue == "fracture":
                    d = (
                        f"疼痛描述「{desc_str}」提示可能涉及 **骨折**。\n\n"
                        "- 尖銳且無法忍受的劇痛，尤其在外傷後出現，需高度警覺\n"
                    )
                    if is_acute: d += "- 處於急性期，若有明確外傷史，骨折可能性更高\n"
                    d += "\n**建議：** 立即安排 X 光。"

                elif tissue == "vascular":
                    d = (
                        f"疼痛描述「{desc_str}」提示可能涉及 **血管性** 問題。\n\n"
                        "- 抽痛（搏動性）或擴散不清，可能與血管充血或循環障礙有關\n"
                        "- 需排除：深層靜脈血栓（DVT）、動脈供血不足\n\n"
                        "**建議：** 合併患肢腫脹或膚色改變，儘速就醫。"
                    )

                elif tissue == "nerve_root":
                    d = f"疼痛描述「{desc_str}」提示可能涉及 **神經根** 問題。\n\n"
                    if spine:
                        if disc_pattern and not stenosis_pattern:
                            d += "結合動作模式（彎腰/久坐/咳嗽加劇），**高度指向椎間盤突出壓迫神經根**。\n"
                            if region == "lumbar": d += "- 典型放射：腰→臀→大腿後→小腿→足部\n"
                            else: d += "- 典型放射：頸→肩→上臂→前臂→手指\n"
                        elif stenosis_pattern and not disc_pattern:
                            d += "結合動作模式（後仰/久站加劇），**指向椎間孔狹窄壓迫神經根**。\n"
                        elif mixed_spine:
                            d += "彎曲與伸直都加劇，可能同時有椎間盤與椎孔問題。\n"
                        else:
                            d += "目前尚無明確動作模式區分方向。彎腰加劇→椎間盤；後仰加劇→椎孔狹窄。\n"
                    elif upper:
                        d += "發生在上肢，需鑑別頸椎神經根壓迫 vs 周邊神經卡壓。\n"
                        if region == "wrist_hand": d += "- 腕隧道、肘隧道、頸椎 C6-C8 皆需考慮\n"
                    elif lower:
                        d += "發生在下肢，需排除腰椎神經根壓迫。\n"
                        if disc_pattern: d += "合併彎腰/久坐加劇，腰椎椎間盤來源可能性上升。\n"
                    if has_weakness: d += "\n合併無力，壓迫程度可能較嚴重。\n"
                    if spreading_expanding: d += "\n合併症狀範圍擴大，神經壓迫可能正在惡化。\n"
                    d += "\n**建議：** 安排 MRI 與神經學評估。"

                elif tissue == "nerve":
                    d = (
                        f"疼痛描述「{desc_str}」提示可能涉及 **周邊神經** 問題。\n\n"
                        "- 閃電般瞬間劇痛是神經幹受刺激的典型表現\n"
                    )
                    if region == "wrist_hand": d += "- 常見：腕隧道（正中神經）、肘隧道（尺神經）\n"
                    elif lower: d += "- 常見：坐骨神經、腓神經、跗管症候群\n"
                    d += "\n**建議：** 紀錄觸電感的位置與延伸方向。"

                elif tissue == "sympathetic":
                    d = (
                        f"疼痛描述「{desc_str}」提示可能涉及 **交感神經 / 神經病變性** 疼痛。\n\n"
                        "- 灼熱、壓力感、針蟄感的組合暗示自主神經系統異常參與\n"
                        "- 考慮：CRPS、周邊神經病變、帶狀疱疹後神經痛\n"
                    )
                    if is_chronic: d += "\n慢性期出現交感神經性特徵，需注意中樞敏感化。\n"
                    d += "\n**建議：** 此類疼痛需疼痛科或神經科評估。"

                elif tissue == "bone":
                    d = f"疼痛描述「{desc_str}」提示可能涉及 **骨骼** 層面的問題。\n\n"
                    if is_young:
                        d += (
                            "- 年輕族群需考慮：壓力性骨折（疲勞性骨折，好發於運動量突然增加時）、"
                            "骨骼生長相關問題\n"
                            "- 退化性問題在此年齡層較不常見\n"
                        )
                    else:
                        d += "- 需考慮：壓力性骨折、骨內壓力變化、骨質疏鬆相關問題\n"
                    if "影響睡眠" in impacts: d += "- 夜間深部骨骼痛需排除較嚴重的病理\n"
                    d += "\n**建議：** 持續且負重加劇的深部痛，建議安排 X 光。"

                elif tissue == "ligament":
                    d = f"疼痛描述「{desc_str}」提示可能涉及 **韌帶或關節囊** 層面的問題。\n\n"
                    d += f"- **{pain_location} 可能相關：** {jt['causes']}\n"
                    d += f"- **臨床提示：** {jt['note']}\n"
                    if has_locking: d += "\n合併卡住感，更需注意關節內部結構的問題。"
                    if is_young:
                        d += (
                            "\n\n您的年齡層較少出現退化性問題。韌帶 / 關節囊的不適"
                            "通常與使用方式、姿勢習慣或過去的受傷有關，"
                            "透過適當的訓練和調整通常能有效改善。"
                        )
                    elif is_older:
                        if is_chronic and "走路 / 活動後改善" in relievers:
                            d += "\n\n慢性期 + 活動後改善 → 退化性關節問題的「晨僵」模式值得注意。"
                    d += "\n\n**建議：** 避免反覆刺激不適部位，適度活動有助於關節健康。"

                elif tissue == "muscle":
                    d = (
                        f"疼痛描述「{desc_str}」提示可能涉及 **肌肉** 來源。\n\n"
                        f"- **{pain_location} 常見肌群：** {myo['muscles']}\n"
                        f"- **好發情境：** {myo['common']}\n"
                    )
                    if "按壓痛" in descriptors:
                        d += (
                            "\n**關於引痛點（Trigger Point）：**\n"
                            "您有明確的按壓痛，這可能代表存在肌筋膜引痛點。"
                            "引痛點是指局部組織有過度刺激（hyperirritability），"
                            "在該處施壓會感到酸痛。引痛點處常伴有組織緊繃，"
                            "可觸摸到帶狀的肌肉收縮硬塊。"
                            "當敏感度增加到足夠大時，可產生穩定的、深層的、"
                            "酸酸的牽連痛（referred pain）。\n\n"
                            "- 正常肌肉不會有引痛點\n"
                            "- 找出引痛點有助於診斷\n"
                            "- 施壓引痛點時可能重現（reproduce）您的症狀\n"
                        )
                    if is_acute: d += "\n急性期肌肉損傷以保護、消炎為主，避免過度伸展或按壓。"
                    elif is_chronic: d += "\n慢性肌肉疼痛通常對物理治療反應良好。"
                    d += f"\n\n**自我照護：** {myo['self_care']}"
                else:
                    d = ""

                if d:
                    st.markdown(d); st.write("")

            if len(tissue_priority) >= 3:
                st.markdown("**提示：** 涉及多種組織來源，建議由專業人員鑑別。")
        elif pain_quality:
            st.info("所選疼痛性質無法明確對應，建議專業評估。")
        else:
            st.info("未選擇疼痛性質。")

        # === 動作模式與症狀交叉分析 ===
        st.markdown("---")
        st.markdown("#### 動作模式與症狀交叉分析")

        st.markdown("##### A. 伴隨症狀分析")
        sym_notes = []

        if has_weakness and has_any_nerve:
            d = "伴隨無力且疼痛具神經特徵，神經壓迫可能已影響運動神經。\n\n"
            if spine and disc_pattern: d += "結合屈曲誘發 → 椎間盤壓迫神經根可能性高。\n"
            elif spine and stenosis_pattern: d += "結合伸直誘發 → 椎孔狹窄壓迫可能性高。\n"
            if is_acute: d += "\n急性期合併無力更需積極處理。"
            d += "\n\n**建議：** 優先安排影像與神經學檢查。"
            sym_notes.append(("nerve-box", "神經壓迫合併肌力下降", d))
        elif has_weakness:
            d = "有無力感但疼痛性質未偏向神經。可能：疼痛抑制、廢用萎縮、肌腱損傷。"
            if is_chronic: d += "\n慢性期無力可能與長時間不活動導致的肌力流失有關。"
            sym_notes.append(("nerve-box", "肌力下降徵兆", d))

        if has_locking and has_rom_loss:
            extra = ""
            if has_ligament: extra = "\n合併韌帶/關節囊疼痛，更支持關節結構問題。"
            sym_notes.append(("joint-box", "關節內部障礙模式",
                f"同時有卡住感與角度受限。\n\n"
                f"- {pain_location} 常見：{lock['causes']}\n"
                f"- 典型表現：{lock['example']}\n"
                f"- 注意事項：{lock['note']}{extra}"
            ))
        elif has_locking:
            sym_notes.append(("joint-box", "關節卡鎖徵兆",
                f"有卡住或彈響感。\n\n- {pain_location} 常見：{lock['causes']}\n- {lock['example']}\n- {lock['note']}"
            ))
        elif has_rom_loss:
            extra = ""
            if has_muscle: extra = "\n合併肌肉性疼痛，保護性痙攣可能性較高。"
            if is_acute: extra += "\n急性期的活動受限通常是保護性的。"
            sym_notes.append(("joint-box", "活動度受限",
                f"角度上不去或受限。\n\n- {pain_location} 常見：{rom['causes']}\n- {rom['note']}{extra}"
            ))

        if sym_notes:
            for b, t, d in sym_notes:
                st.markdown(f'<div class="{b}">{t}</div>', unsafe_allow_html=True); st.markdown(d); st.write("")
        else:
            st.info("未勾選明顯伴隨症狀。")

        st.markdown("##### B. 動作模式分析")
        mv_notes = []

        if rest_pain or move_pain:
            d = "動靜皆痛，典型急性發炎期。以保護、消炎為優先。"
            if "冰敷" in relievers: d += "\n\n冰敷有效，支持急性發炎。"
            if is_acute: d += "\n\n處於急性期，此反應屬預期中。"
            elif is_chronic: d += "\n\n但已處於慢性期，動靜皆痛持續超過 3 個月較不尋常，需考慮是否有未發現的問題或中樞敏感化。"
            if high_irritability: d += "\n合併高刺激性，目前不適合積極介入。"
            mv_notes.append(("inflam-box", "急性發炎期", d))

        if spine:
            if disc_pattern and not stenosis_pattern:
                agg = [t for t in ["久坐", "彎腰", "打噴嚏 / 咳嗽"] if t in triggers]
                d = (
                    f"誘發因子：{'、'.join(agg)}\n\n"
                    "**屈曲負荷加劇 — 椎間盤方向（Discogenic Pattern）**\n\n"
                    "前彎、久坐、咳嗽加劇 → 椎間盤源性問題：\n"
                    "- 前彎/坐姿增加椎間盤後方壓力\n"
                    "- 咳嗽/打噴嚏瞬間增加腹內壓\n\n"
                    "**建議：** 使用腰靠、每 30 分鐘起身、避免彎腰搬重物。"
                )
                if "走路 / 活動後改善" in relievers: d += "\n\n走路緩解更支持椎間盤方向。"
                if has_nerve_root: d += "\n合併神經根痛，壓迫可能性上升。"
                if is_acute: d += "\n\n急性期椎間盤問題，前 2 週以保護為主。"
                elif is_chronic: d += "\n\n慢性期椎間盤問題，需評估核心穩定性與動作控制。"
                mv_notes.append(("pattern-box", "屈曲負荷型 — 椎間盤方向", d))

            elif stenosis_pattern and not disc_pattern:
                agg = [t for t in ["後仰 / 挺身", "久站"] if t in triggers]
                d = (
                    f"誘發因子：{'、'.join(agg)}\n\n"
                    "**伸直負荷加劇 — 椎孔狹窄方向（Stenosis / Facet Pattern）**\n\n"
                    "後仰/久站加劇 → 椎間孔狹窄或小面關節問題：\n"
                    "- 後仰時椎間孔縮小\n"
                )
                if region == "lumbar": d += "- 走路漸漸麻痛需坐下前彎休息 → 神經性間歇性跛行\n"
                d += "\n**建議：** 避免久站或後仰，前彎/坐下通常能緩解。"
                if is_older: d += "\n中老年退化性問題常見，建議影像檢查。"
                if has_nerve_root: d += "\n合併神經根痛，椎孔狹窄可能性上升。"
                mv_notes.append(("pattern-box", "伸直負荷型 — 椎孔狹窄方向", d))

            elif mixed_spine:
                d = "彎曲與伸直都加劇。可能多重問題或急性發炎期。"
                if is_acute: d += "\n急性期任何方向都可能刺激組織。"
                d += "\n\n**建議：** 脊椎中立，儘速影像檢查。"
                mv_notes.append(("inflam-box", "混合型脊椎負荷模式", d))
        else:
            if "彎腰" in triggers and region == "hip":
                mv_notes.append(("pattern-box", "髖關節屈曲受限模式",
                    "彎腰時髖部痛：FAI、關節唇損傷、需排除腰椎轉移。"))
            if "久坐" in triggers and not spine:
                d = f"久坐加劇 {pain_location} 的不適。\n- {myo['common']}\n\n**建議：** 每 30 分鐘起身。{myo['self_care']}"
                if is_chronic: d += "\n慢性久坐相關疼痛通常反映姿勢與肌力問題。"
                mv_notes.append(("muscle-box", "久坐相關不適", d))

        stairs = [t for t in triggers if t in ["上樓梯", "下樓梯"]]
        if stairs:
            d = f"誘發因子：{'、'.join(stairs)}\n\n"
            if "下樓梯" in stairs and "上樓梯" not in stairs:
                d += "下樓梯（離心）較痛：PFPS、髕骨肌腱炎。"
            elif "上樓梯" in stairs and "下樓梯" not in stairs:
                d += "上樓梯（向心）較痛：股四頭肌不足、髕骨軌跡異常。"
            else:
                d += "上下樓梯皆痛，承重能力明顯下降。"
            if has_locking: d += f"\n合併卡住感：{lock['note']}"
            if has_bone: d += "\n合併骨骼性疼痛，注意壓力性骨折。"
            d += "\n\n**建議：** 減少樓梯，從低負荷訓練開始。"
            mv_notes.append(("pattern-box", "承重模式異常", d))

        if "手舉高" in triggers:
            d = "手舉過頭痛。"
            if region == "shoulder":
                d += "\n肩膀：肩夾擠、旋轉肌群損傷、肩峰下滑囊炎。"
                if has_weakness: d += "\n合併無力，注意旋轉肌群撕裂。"
            d += "\n\n**建議：** 暫避過肩動作，先肩胛穩定訓練。"
            mv_notes.append(("pattern-box", "上舉受限", d))

        if "轉身 / 轉彎" in triggers:
            d = "轉身時痛。"
            if spine: d += "\n脊椎旋轉：小面關節壓力、椎間盤剪力、核心控制不佳。\n\n**建議：** 整個身體一起轉，核心抗旋轉訓練。"
            mv_notes.append(("pattern-box", "旋轉不耐受", d))

        if "走路" in triggers:
            d = "走路引發疼痛。\n\n"
            wk = {"ankle": "足底筋膜炎、跟腱炎、踝不穩定", "knee": "軟骨磨損、承重異常",
                   "lumbar": "區分椎間盤（走路改善）vs 椎管狹窄（走路加劇）", "hip": "髖退化、臀中肌無力"}
            d += f"- {wk.get(region, '進一步評估')}\n"
            if spine and has_nerve_root and stenosis_pattern:
                d += "\n走路加劇 + 神經根痛 + 後仰加劇 → **神經性間歇性跛行**。"
            if has_vascular: d += "\n合併血管性疼痛，需鑑別血管性 vs 神經性跛行。"
            mv_notes.append(("pattern-box", "步行疼痛", d))

        if mv_notes:
            for b, t, d in mv_notes:
                st.markdown(f'<div class="{b}">{t}</div>', unsafe_allow_html=True); st.markdown(d); st.write("")
        else:
            st.info("未選擇明顯誘發因子。")

        st.markdown("##### C. 緩解因子分析")
        rel = []
        if "熱敷" in relievers and "冰敷" in relievers:
            rel.append("**熱敷與冰敷皆有效：** 同時有緊繃與發炎。急性冰敷，慢性熱敷。")
        elif "熱敷" in relievers:
            n = "**熱敷有效：** 肌肉緊繃或循環不良為主。"
            if has_muscle: n += f" {myo['self_care']}"
            if is_acute: n += " 注意：急性期若仍有明顯發炎，冰敷可能更合適。"
            rel.append(n)
        elif "冰敷" in relievers:
            rel.append("**冰敷有效：** 可能仍有急性發炎。每次 15–20 分。")
        if "走路 / 活動後改善" in relievers:
            n = "**活動後緩解：**"
            if spine and disc_pattern: n += " 椎間盤模式中走路緩解是典型特徵。"
            elif "久坐" in triggers: n += " 越不動越痛模式。"
            if is_chronic and has_ligament: n += f" 慢性期 + 韌帶痛 + 活動改善 → {jt['note']}"
            rel.append(n)
        if "改變姿勢" in relievers:
            rel.append("**改變姿勢有效：** 疼痛與特定姿勢高度相關。")
        if "休息 / 不活動" in relievers and "走路 / 活動後改善" not in relievers:
            n = "**休息有效但活動未改善：** 可能仍處發炎階段。"
            if spine and stenosis_pattern: n += " 椎孔狹窄中坐下前彎緩解也是典型。"
            rel.append(n)
        if "沒有任何改善" in relievers:
            n = "**任何方式皆無法改善：** 疼痛較複雜。"
            if has_sympathetic: n += " 合併交感神經性疼痛，可能涉及中樞敏感化。"
            if is_chronic: n += " 慢性期合併無法改善，強烈建議多面向評估。"
            n += " **強烈建議專業評估。**"
            rel.append(n)

        if rel:
            for r in rel: st.markdown(f"- {r}")
            st.write("")
        else:
            st.info("未選擇緩解因子。")

        if impacts:
            st.markdown("##### D. 功能影響評估")
            if "影響睡眠" in impacts:
                n = "- **睡眠受影響：** 問題可能較嚴重。"
                if has_bone: n += " 合併骨骼痛，夜間痛需排除嚴重病理。"
                if is_chronic: n += " 慢性疼痛與睡眠障礙常互相影響。"
                st.markdown(n)
            if "失去平衡" in impacts:
                n = "- **平衡/跌倒風險：** 安全警訊。"
                if has_any_nerve and spine: n += " 合併脊椎神經症狀，需注意脊髓壓迫。"
                st.markdown(n)
            if "需藥物止痛" in impacts:
                n = "- **需藥物控制：** 建議搭配物理治療。"
                if is_chronic: n += " 長期用藥需評估是否產生依賴或掩蓋問題。"
                st.markdown(n)
            if "影響日常" in impacts:
                st.markdown("- **日常功能受限：** 建議積極治療。")

        st.markdown("---")
        st.markdown("#### 綜合建議")

        if has_red_flags:
            st.error("**立即就醫** — 您有紅旗警訊。")
        elif has_fracture:
            st.error("**建議儘速就醫** — 疼痛性質提示骨折可能。")
        elif has_vascular:
            st.warning("**建議就醫** — 疼痛性質提示血管問題。")
        elif vas_score >= 7:
            st.warning("**建議就醫** — 疼痛指數偏高。")
        elif is_acute and high_irritability:
            st.warning("**建議就醫或密切觀察** — 急性期且高刺激性，建議由專業人員評估。")
        elif is_chronic and "沒有任何改善" in relievers:
            st.warning("**建議多面向評估** — 慢性期且無法改善，需考慮疼痛科、心理、睡眠等因素。")
        elif vas_score >= 4:
            if is_chronic:
                st.info("**建議追蹤** — 中度慢性疼痛。重點在漸進式恢復功能，而非過度保護。")
            else:
                st.info("**建議追蹤** — 中度疼痛，建議安排完整評估。")
        else:
            if is_chronic:
                st.success("**持續觀察** — 疼痛程度較輕但已持續一段時間，可透過適度活動改善。")
            else:
                st.success("**持續觀察** — 疼痛程度較輕，先透過衛教與自我管理改善。")

        st.markdown("---")
        st.caption(
            "本報告僅供衛教參考，不可取代專業醫療診斷。如有疑慮請諮詢醫師或物理治療師。"
            "　｜　疼痛性質分類依據：Magee DJ. Orthopedic Physical Assessment."
            "　｜　本報告可截圖保存，攜帶至就診時提供醫療人員參考。"
        )