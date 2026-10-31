import streamlit as st
from dataclasses import dataclass
from pathlib import Path

st.set_page_config(
    page_title="HỆ CHUYÊN GIA TƯ VẤN TAI NGHE",
    page_icon="🎧",
    layout="wide",
)

IMAGE_DIR = Path(__file__).parent / "images"

# ============================================================
# CƠ SỞ TRI THỨC: 12 sản phẩm theo tài liệu 
# Các trường "None" nghĩa là thông tin chưa được xác nhận.
# ============================================================
PRODUCTS = [
    {
        "code": "SP1", "name": "Lenovo LP40 Pro",
        "brand": "Lenovo", "type": "Bluetooth", "form": "Nhét tai",
        "purposes": {"Nghe nhạc", "Giải trí", "Đàm thoại", "Chơi game"},
        "price_min": 150_000, "price_max": 250_000,
        "battery": 5, "battery_total": 25, "water": "IPX5",
        "water_level": 2, "noise": "Micro đàm thoại; chưa xác nhận ANC",
        "mic_noise": False, "anc": False, "device": {"Bluetooth"},
        "uncertain": {"water", "noise"},
    },
    {
        "code": "SP2", "name": "OPPO MH135",
        "brand": "OPPO", "type": "Có dây", "form": "Nhét tai",
        "purposes": {"Nghe nhạc", "Giải trí", "Học tập / học online", "Văn phòng"},
        "price_min": 220_000, "price_max": 220_000,
        "battery": None, "battery_total": None, "water": "Không có thông tin chống nước",
        "water_level": 0, "noise": "Không có chức năng chống ồn được xác nhận",
        "mic_noise": False, "anc": False, "device": {"3,5 mm"},
        "uncertain": set(),
    },
    {
        "code": "SP3", "name": "Soundcore R50i",
        "brand": "Soundcore by Anker", "type": "Bluetooth", "form": "Nhét tai",
        "purposes": {"Nghe nhạc", "Giải trí", "Đàm thoại", "Học tập / học online"},
        "price_min": 300_000, "price_max": 350_000,
        "battery": 10, "battery_total": 30, "water": "IPX5",
        "water_level": 2, "noise": "Micro kép + AI giảm ồn khi gọi; không có ANC",
        "mic_noise": True, "anc": False, "device": {"Bluetooth"},
        "uncertain": set(),
    },
    {
        "code": "SP4", "name": "Xiaomi Redmi Buds 6 Play",
        "brand": "Xiaomi", "type": "Bluetooth", "form": "Nhét tai",
        "purposes": {"Nghe nhạc", "Giải trí", "Đàm thoại", "Học tập / học online", "Chơi game"},
        "price_min": 299_000, "price_max": 360_000,
        "battery": 7.5, "battery_total": 36, "water": "IPX4",
        "water_level": 1, "noise": "AI giảm tiếng ồn khi gọi; không có ANC được xác nhận",
        "mic_noise": True, "anc": False, "device": {"Bluetooth"},
        "uncertain": set(),
    },
    {
        "code": "SP5", "name": "Baseus Bowie WM02",
        "brand": "Baseus", "type": "Bluetooth", "form": "Nhét tai",
        "purposes": {"Nghe nhạc", "Giải trí", "Đàm thoại", "Học tập / học online", "Chơi game"},
        "price_min": 300_000, "price_max": 500_000,
        "battery": 5, "battery_total": 25, "water": "Chưa xác định chuẩn chính thức",
        "water_level": None, "noise": "Micro đàm thoại; chưa xác nhận ANC",
        "mic_noise": False, "anc": False, "device": {"Bluetooth"},
        "uncertain": {"water", "noise"},
    },
    {
        "code": "SP6", "name": "Realme Buds Air 2",
        "brand": "Realme", "type": "Bluetooth", "form": "Nhét tai",
        "purposes": {"Nghe nhạc", "Giải trí", "Đàm thoại", "Học tập / học online", "Chơi game"},
        "price_min": 450_000, "price_max": 500_000,
        "battery": 5, "battery_total": 25, "water": "IPX5",
        "water_level": 2, "noise": "ANC + micro kép giảm ồn khi gọi",
        "mic_noise": True, "anc": True, "device": {"Bluetooth"},
        "uncertain": set(),
    },
    {
        "code": "SP7", "name": "Logitech H340",
        "brand": "Logitech", "type": "Có dây", "form": "Chụp tai",
        "purposes": {"Văn phòng", "Học tập / học online", "Đàm thoại"},
        "price_min": 490_000, "price_max": 690_000,
        "battery": None, "battery_total": None, "water": "Không có thông tin chống nước",
        "water_level": 0, "noise": "Đệm tai hạn chế một phần tiếng ồn; không phải ANC",
        "mic_noise": False, "anc": False, "device": {"USB-A"},
        "uncertain": set(),
    },
    {
        "code": "SP8", "name": "HyperX Cloud Earbuds II",
        "brand": "HyperX", "type": "Có dây", "form": "Nhét tai",
        "purposes": {"Chơi game", "Nghe nhạc", "Giải trí"},
        "price_min": 750_000, "price_max": 750_000,
        "battery": None, "battery_total": None, "water": "Không có thông tin chống nước",
        "water_level": 0, "noise": "Nút tai silicon cách âm thụ động",
        "mic_noise": False, "anc": False, "device": {"3,5 mm"},
        "uncertain": set(),
    },
    {
        "code": "SP9", "name": "Huawei FreeBuds SE 4",
        "brand": "Huawei", "type": "Bluetooth", "form": "Nhét tai",
        "purposes": {"Văn phòng", "Học tập / học online", "Nghe nhạc", "Đàm thoại"},
        "price_min": 790_000, "price_max": 790_000,
        "battery": 8.5, "battery_total": 42.5, "water": "IP54",
        "water_level": 3, "noise": "ANC; micro giảm ồn khi gọi chưa được xác nhận trong dữ liệu",
        "mic_noise": False, "anc": True, "device": {"Bluetooth", "USB-C"},
        "uncertain": set(),
    },
    {
        "code": "SP10", "name": "Sony WF-C510",
        "brand": "Sony", "type": "Bluetooth", "form": "Nhét tai",
        "purposes": {"Nghe nhạc", "Giải trí", "Đàm thoại", "Học tập / học online"},
        "price_min": 790_000, "price_max": 1_290_000,
        "battery": 11, "battery_total": 22, "water": "IPX4",
        "water_level": 1, "noise": "Micro đàm thoại; không có ANC",
        "mic_noise": False, "anc": False, "device": {"Bluetooth"},
        "uncertain": set(),
    },
    {
        "code": "SP11", "name": "Samsung Galaxy Buds Core",
        "brand": "Samsung", "type": "Bluetooth", "form": "Nhét tai",
        "purposes": {"Văn phòng", "Học tập / học online", "Nghe nhạc", "Đàm thoại", "Giải trí"},
        "price_min": 990_000, "price_max": 1_190_000,
        "battery": 8.5, "battery_total": 35, "water": "IP54",
        "water_level": 3, "noise": "ANC; micro giảm ồn khi gọi chưa được xác nhận trong dữ liệu",
        "mic_noise": False, "anc": True, "device": {"Bluetooth", "USB-C"},
        "uncertain": set(),
    },
    {
        "code": "SP12", "name": "HyperX Cloud III",
        "brand": "HyperX", "type": "Có dây", "form": "Chụp tai",
        "purposes": {"Chơi game", "Nghe nhạc", "Giải trí", "Đàm thoại"},
        "price_min": 1_790_000, "price_max": 1_790_000,
        "battery": None, "battery_total": None, "water": "Không có thông tin chống nước",
        "water_level": 0, "noise": "Thiết kế chụp tai kín hạn chế một phần tiếng ồn; không phải ANC",
        "mic_noise": False, "anc": False, "device": {"3,5 mm", "USB-A", "USB-C"},
        "uncertain": set(),
    },
    {
        "code": "SP13", "name": "Sony MDR-ZX110AP On-Ear Headphones",
        "brand": "Sony", "type": "Có dây", "form": "Chụp tai",
        "purposes": {"Học tập / học online", "Nghe nhạc", "Giải trí", "Đàm thoại"},
        "price_min": 350_000, "price_max": 650_000,
        "battery": None, "battery_total": None, "water": "Không có thông tin chống nước",
        "water_level": 0, "noise": "Thiết kế chụp tai kín hạn chế một phần tiếng ồn; Micro đàm thoại; không có ANC",
        "mic_noise": False, "anc": False, "device": {"3,5 mm"},
        "uncertain": set(),
    },
    {
        "code": "SP14", "name": "Apple EarPods MMTN2",
        "brand": "Apple", "type": "Có dây", "form": "Nhét tai",
        "purposes": {"Học tập / học online", "Nghe nhạc", "Giải trí", "Đàm thoại"},
        "price_min": 490_000, "price_max": 540_000,
        "battery": None, "battery_total": None, "water": "Apple công bố khả năng chống mồ hôi và nước, nhưng không công bố chuẩn IP cụ thể cho mẫu này.",
        "water_level": 0, "noise": "Micro đàm thoại; không có ANC",
        "mic_noise": False, "anc": False, "device": {"Lightning"},
        "uncertain": set(),
    },
    {
        "code": "SP15", "name": "Samsung IA500",
        "brand": "Samsung", "type": "Có dây", "form": "Nhét tai",
        "purposes": {"Học tập / học online", "Nghe nhạc", "Giải trí", "Đàm thoại"},
        "price_min": 100_000, "price_max": 300_000,
        "battery": None, "battery_total": None, "water": "Không có thông tin chống nước",
        "water_level": 0, "noise": "Thiết kế nhét tai với đệm silicone hỗ trợ cách âm thụ động; Micro đàm thoại; không có ANC",
        "mic_noise": False, "anc": False, "device": {"3,5 mm"},
        "uncertain": set(),
    },
    {
        "code": "SP16", "name": "Xiaomi Type-C",
        "brand": "Xiaomi", "type": "Có dây", "form": "Nhét tai",
        "purposes": {"Học tập / học online", "Nghe nhạc", "Giải trí", "Đàm thoại"},
        "price_min": 160_000, "price_max": 200_000,
        "battery": None, "battery_total": None, "water": "IP54.",
        "water_level": 3, "noise": "Thiết kế nhét tai với đệm silicone hỗ trợ cách âm thụ động; Micro đàm thoại; không có ANC",
        "mic_noise": False, "anc": False, "device": {"USB-C"},
        "uncertain": set(),
    },
    {
        "code": "SP17", "name": "Edifier W800BT SE",
        "brand": "Edifier", "type": "Bluetooth", "form": "Chụp tai",
        "purposes": {"Học tập / học online", "Nghe nhạc", "Giải trí", "Chơi game"},
        "price_min": 500_000, "price_max": 900_000,
        "battery": 45, "battery_total": 45, "water": "Không có thông tin chống nước",
        "water_level": 0, "noise": "Thiết kế chụp tai giúp hạn chế tiếng ồn bên ngoài; không có ANC",
        "mic_noise": False, "anc": False, "device": {"Bluetooth"},
        "uncertain": set(),
    },
    {
        "code": "SP18", "name": "JBL C200 SIU",
        "brand": "JBL", "type": "Có dây", "form": "Nhét tai",
        "purposes": {"Học tập / học online", "Nghe nhạc", "Giải trí", "Đàm thoại"},
        "price_min": 200_000, "price_max": 400_000,
        "battery": None, "battery_total": None, "water": "Không có thông tin chống nước",
        "water_level": 0, "noise": "Thiết kế nhét tai với đệm silicone hỗ trợ cách âm thụ động; không có ANC",
        "mic_noise": False, "anc": False, "device": {"3,5 mm"},
        "uncertain": set(),
    },
    {
        "code": "SP19", "name": "Havit E336C",
        "brand": "Havit", "type": "Có dây", "form": "Nhét tai",
        "purposes": {"Học tập / học online", "Nghe nhạc", "Giải trí", "Đàm thoại"},
        "price_min": 99_000, "price_max": 160_000,
        "battery": None, "battery_total": None, "water": "Không có thông tin chống nước",
        "water_level": 0, "noise": "Thiết kế nhét tai với đệm silicone hỗ trợ cách âm thụ động; không có ANC",
        "mic_noise": False, "anc": False, "device": {"USB-C"},
        "uncertain": set(),
    },
    {
        "code": "SP20", "name": "Asus Tuf H3",
        "brand": "Asus", "type": "Có dây", "form": "Chụp tai",
        "purposes": {"Chơi game", "Văn phòng", "Học tập / học online", "Nghe nhạc", "Giải trí", "Đàm thoại"},
        "price_min": 990_000, "price_max": 990_000,
        "battery": None, "battery_total": None, "water": "Không có thông tin chống nước",
        "water_level": 0, "noise": "Thiết kế chụp tai giúp hạn chế tiếng ồn bên ngoài; Micro đàm thoại; không có ANC",
        "mic_noise": False, "anc": False, "device": {"3,5 mm"},
        "uncertain": set(),
    },
    {
        "code": "SP21", "name": "Audio Technica ATH-J100",
        "brand": "Audio Technica", "type": "Có dây", "form": "Nhét tai",
        "purposes": {"Học tập / học online", "Nghe nhạc", "Giải trí"},
        "price_min": 100_000, "price_max": 390_000,
        "battery": None, "battery_total": None, "water": "Không có thông tin chống nước",
        "water_level": 0, "noise": "Thiết kế nhét tai với đệm silicone hỗ trợ cách âm thụ động; không có ANC",
        "mic_noise": False, "anc": False, "device": {"3,5 mm"},
        "uncertain": set(),
    },
    {
        "code": "SP22", "name": "Razer Kraken V3 X",
        "brand": "Razer", "type": "Có dây", "form": "Chụp tai",
        "purposes": {"Chơi game", "Học tập / học online", "Nghe nhạc", "Giải trí", "Đàm thoại", "Văn phòng"},
        "price_min": 1_100_000, "price_max": 1_500_000,
        "battery": None, "battery_total": None, "water": "Không có thông tin chống nước",
        "water_level": 0, "noise": "Thiết kế chụp tai giúp hạn chế tiếng ồn bên ngoài; Micro đàm thoại; không có ANC",
        "mic_noise": False, "anc": False, "device": {"USB-C"},
        "uncertain": set(),
    },
]

PURPOSES = [
    "Chơi game", "Nghe nhạc", "Học tập / học online",
    "Văn phòng", "Giải trí", "Đàm thoại"
]
BRAND_OPTIONS = ["Không yêu cầu"] + sorted({p["brand"] for p in PRODUCTS})
DEVICE_OPTIONS = ["Không yêu cầu", "Bluetooth", "3,5 mm", "USB-A", "USB-C", "Lightning"]
BUDGETS = {
    "Không giới hạn": (0, 99_999_999),
    "Dưới 300.000đ": (0, 300_000),
    "300.000–700.000đ": (300_000, 700_000),
    "700.000–1.200.000đ": (700_000, 1_200_000),
    "Trên 1.200.000đ": (1_200_000, 99_999_999),
}
WATER_OPTIONS = {
    "Không yêu cầu chống nước": "none",
    "Tối thiểu IPX4": "ipx4",
    "Tối thiểu IPX5": "ipx5",
    "Yêu cầu IP54": "ip54",
}
NOISE_OPTIONS = {
    "Không yêu cầu chống ồn": "none",
    "Micro giảm ồn khi đàm thoại": "mic",
    "Chống ồn chủ động ANC": "anc",
    "ANC và micro giảm ồn khi đàm thoại": "both",
}
QUESTION_KEYS = [
    "primary", "purposes", "budget", "brand", "device",
    "battery", "noise", "water",
]

def reset_following_questions(question_index):
    st.session_state["show_results"] = False
    for key in QUESTION_KEYS[question_index + 1:]:
        st.session_state.pop(key, None)

def battery_matches(p, choice):
    if choice == "Có pin từ 5 giờ trở lên":
        return p["battery"] is not None and p["battery"] >= 5
    if choice == "Có pin từ 8 giờ trở lên":
        return p["battery"] is not None and p["battery"] >= 8
    if choice == "Có pin từ 11 giờ trở lên":
        return p["battery"] is not None and p["battery"] >= 11
    if choice == "Không dùng pin / có dây":
        return p["battery"] is None
    return True

def fmt_price(n):
    return f"{int(n):,}".replace(",", ".") + "đ"

def knowledge_base_table():
    import pandas as pd

    return pd.DataFrame([
        {
            "Mã": p["code"], "Sản phẩm": p["name"], "Loại": p["type"],
            "Kiểu dáng": p["form"],
            "Giá": f"{fmt_price(p['price_min'])}–{fmt_price(p['price_max'])}",
            "Pin": f"{p['battery']} giờ" if p["battery"] is not None else "Không dùng pin",
            "Chống nước": p["water"], "Chống ồn": p["noise"],
        }
        for p in PRODUCTS
    ])

def price_matches(p, bounds):
    lo, hi = bounds
    # Giá sản phẩm giao với khoảng ngân sách được chọn.
    return p["price_max"] >= lo and p["price_min"] <= hi

def hard_requirements_match(p, water_choice, noise_choice, device_choice, battery_choice):
    if device_choice != "Không yêu cầu" and device_choice not in p["device"]:
        return False
    if battery_choice == "Có pin từ 5 giờ trở lên" and (p["battery"] is None or p["battery"] < 5):
        return False
    if battery_choice == "Có pin từ 8 giờ trở lên" and (p["battery"] is None or p["battery"] < 8):
        return False
    if battery_choice == "Có pin từ 11 giờ trở lên" and (p["battery"] is None or p["battery"] < 11):
        return False
    if battery_choice == "Không dùng pin / có dây" and p["battery"] is not None:
        return False
    if water_choice == "ipx4" and (p["water_level"] is None or p["water_level"] < 1):
        return False
    if water_choice == "ipx5" and (p["water_level"] is None or p["water_level"] < 2):
        return False
    if water_choice == "ip54" and p["water_level"] != 3:
        return False
    if noise_choice == "mic" and not p["mic_noise"]:
        return False
    if noise_choice == "anc" and not p["anc"]:
        return False
    if noise_choice == "both" and not (p["anc"] and p["mic_noise"]):
        return False
    return True

def score_product(p, purposes, budget_bounds, battery_choice):
    score = 0
    reasons = []

    matched_purposes = purposes.intersection(p["purposes"])
    if purposes:
        purpose_ratio = len(matched_purposes) / len(purposes)
        score += round(4 * purpose_ratio, 2)
        if matched_purposes:
            reasons.append("phù hợp mục đích: " + ", ".join(sorted(matched_purposes)))

    if price_matches(p, budget_bounds):
        score += 3
        reasons.append("giá nằm trong hoặc giao với ngân sách")
    else:
        score -= 1

    if battery_choice == "Không yêu cầu":
        pass
    elif battery_choice == "Có pin từ 5 giờ trở lên" and p["battery"] is not None and p["battery"] >= 5:
        score += 1
        reasons.append("đạt thời lượng pin tối thiểu")
    elif battery_choice == "Có pin từ 8 giờ trở lên" and p["battery"] is not None and p["battery"] >= 8:
        score += 1
        reasons.append("đạt thời lượng pin tối thiểu")
    elif battery_choice == "Có pin từ 11 giờ trở lên" and p["battery"] is not None and p["battery"] >= 11:
        score += 1
        reasons.append("đạt thời lượng pin tối thiểu")
    elif battery_choice == "Không dùng pin / có dây" and p["battery"] is None:
        score += 1
        reasons.append("không cần sạc pin")

    return score, reasons

def water_requirement_text(value):
    return {
        "none": "Không yêu cầu chống nước",
        "ipx4": "Tối thiểu IPX4",
        "ipx5": "Tối thiểu IPX5",
        "ip54": "IP54",
    }[value]

if st.query_params.get("view") == "knowledge-base":
    st.title("Danh sách các sản phẩm")
    st.caption(f"Danh sách đầy đủ {len(PRODUCTS)} sản phẩm.")
    st.link_button("← Quay lại tư vấn", "?")
    st.dataframe(knowledge_base_table(), use_container_width=True, hide_index=True)
    st.stop()

st.markdown("""
<style>
.block-container {padding-top: 1.8rem; padding-bottom: 2.5rem; max-width: 1200px;}
.hero {padding: 2rem 1.5rem; border-radius: 18px; background: linear-gradient(120deg,#635bff,#49c7df); color: white; margin-bottom: 1rem; text-align: center;}
.hero h1 {font-size: clamp(2.2rem, 4vw, 3.2rem); margin: 0; line-height: 1.2;}
.hero p {margin: 0; opacity: .96;}
.small {font-size: .88rem; opacity: .8;}
.pill {display:inline-block; padding: .2rem .55rem; border-radius: 999px; background:linear-gradient(120deg,#635bff,#49c7df); color:white; font-size:.8rem; margin-right:.25rem;}
.st-key-search_button button {background:linear-gradient(120deg,#635bff,#49c7df); color:#fff; border:1px solid #635bff;}
.st-key-search_button button:hover {background:linear-gradient(120deg,#554de0,#3aaac2); border-color:#554de0; color:#fff;}
.st-key-search_button button:focus:not(:active) {color:#fff; border-color:#635bff;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <h1>🎧 HỆ CHUYÊN GIA TƯ VẤN TAI NGHE</h1>
</div>
""", unsafe_allow_html=True)

st.subheader("🧭 Bắt đầu tư vấn")
st.info("Chọn lần lượt theo thứ tự đã đánh số để tìm được sản phẩm phù hợp.")

left, right = st.columns(2)
with left:
    primary = st.selectbox(
        "1. Loại tai nghe ưu tiên",
        ["Có dây", "Chụp tai", "Bluetooth", "Không ưu tiên"],
        index=3,
        key="primary",
        on_change=reset_following_questions,
        args=(0,),
        help="Chọn loại để giới hạn danh sách tư vấn; chọn Không ưu tiên để giữ mọi loại."
    )
candidates = [
    p for p in PRODUCTS
    if primary == "Không ưu tiên"
    or (primary == "Có dây" and p["type"] == "Có dây")
    or (primary == "Bluetooth" and p["type"] == "Bluetooth")
    or (primary == "Chụp tai" and p["form"] == "Chụp tai")
]

with right:
    purpose_options = [purpose for purpose in PURPOSES if any(purpose in p["purposes"] for p in candidates)]
    purposes_selected = st.multiselect(
        "2. Mục đích sử dụng",
        purpose_options,
        key="purposes",
        on_change=reset_following_questions,
        args=(1,),
    )

if purposes_selected:
    candidates = [
        p for p in candidates
        if set(purposes_selected).intersection(p["purposes"])
    ]

left, right = st.columns(2)
with left:
    budget_options = [
        label for label, bounds in BUDGETS.items()
        if label == "Không giới hạn" or any(price_matches(p, bounds) for p in candidates)
    ]
    budget_label = st.selectbox(
        "3. Ngân sách",
        budget_options,
        key="budget",
        on_change=reset_following_questions,
        args=(2,),
    )
budget_bounds = BUDGETS[budget_label]
candidates = [p for p in candidates if price_matches(p, budget_bounds)]

with right:
    brand_options = ["Không yêu cầu"] + sorted({p["brand"] for p in candidates})
    brand_choice = st.selectbox(
        "4. Thương hiệu",
        brand_options,
        key="brand",
        on_change=reset_following_questions,
        args=(3,),
    )
if brand_choice != "Không yêu cầu":
    candidates = [p for p in candidates if p["brand"] == brand_choice]

left, right = st.columns(2)
with left:
    device_options = ["Không yêu cầu"] + [
        device for device in DEVICE_OPTIONS[1:]
        if any(device in p["device"] for p in candidates)
    ]
    device_choice = st.selectbox(
        "5. Thiết bị kết nối",
        device_options,
        key="device",
        on_change=reset_following_questions,
        args=(4,),
    )
if device_choice != "Không yêu cầu":
    candidates = [p for p in candidates if device_choice in p["device"]]

with right:
    battery_choices = [
        "Không yêu cầu",
        "Có pin từ 5 giờ trở lên",
        "Có pin từ 8 giờ trở lên",
        "Có pin từ 11 giờ trở lên",
        "Không dùng pin / có dây",
    ]
    battery_options = [
        choice for choice in battery_choices
        if choice == "Không yêu cầu" or any(battery_matches(p, choice) for p in candidates)
    ]
    battery_choice = st.selectbox(
        "6. Thời lượng pin",
        battery_options,
        key="battery",
        on_change=reset_following_questions,
        args=(5,),
        help="Chỉ lọc theo pin khi chọn một yêu cầu cụ thể.",
    )
candidates = [p for p in candidates if battery_matches(p, battery_choice)]

left, right = st.columns(2)
with left:
    noise_options = [
        label for label, choice in NOISE_OPTIONS.items()
        if choice == "none" or any(
            hard_requirements_match(p, "none", choice, device_choice, battery_choice)
            for p in candidates
        )
    ]
    noise_label = st.selectbox(
        "7. Khả năng chống ồn",
        noise_options,
        key="noise",
        on_change=reset_following_questions,
        args=(6,),
    )
    noise_choice = NOISE_OPTIONS[noise_label]
candidates = [
    p for p in candidates
    if hard_requirements_match(p, "none", noise_choice, device_choice, battery_choice)
]

with right:
    water_options = [
        label for label, choice in WATER_OPTIONS.items()
        if choice == "none" or any(
            hard_requirements_match(p, choice, noise_choice, device_choice, battery_choice)
            for p in candidates
        )
    ]
    water_label = st.selectbox(
        "8. Khả năng chống nước",
        water_options,
        key="water",
        on_change=reset_following_questions,
        args=(7,),
    )
    water_choice = WATER_OPTIONS[water_label]
candidates = [
    p for p in candidates
    if hard_requirements_match(p, water_choice, noise_choice, device_choice, battery_choice)
]
st.caption(f"Còn {len(candidates)} sản phẩm phù hợp với các lựa chọn hiện tại.")

if st.button("TÌM TAI NGHE PHÙ HỢP", use_container_width=True, key="search_button"):
    st.session_state["show_results"] = True

if st.session_state.get("show_results", False):
    ranked = []
    for p in candidates:
        score, reasons = score_product(
            p, set(purposes_selected), budget_bounds, battery_choice
        )
        ranked.append((score, p, reasons))
    ranked.sort(key=lambda x: (x[0], -x[1]["price_min"]), reverse=True)

    st.markdown("---")
    st.subheader("Kết quả tư vấn")
    st.caption(f"Ưu tiên chính: {primary} · Ngân sách: {budget_label} · Hãng: {brand_choice} · Kết quả: {len(ranked)} sản phẩm")

    if not ranked:
        st.warning("Chưa tìm thấy sản phẩm phù hợp với mục đích, ngân sách và các yêu cầu đã chọn. Hãy thử chọn lại ngân sách, chọn thêm mục đích hoặc giảm bớt yêu cầu về kết nối/pin/chống ồn/chống nước.")
    else:
        st.markdown("#### Danh sách đề xuất")
        for rank, (score, p, reasons) in enumerate(ranked, start=1):
            with st.expander(f"{rank}. {p['name']}"):
                image_col, details_col = st.columns([1, 4])
                with image_col:
                    st.image(str(IMAGE_DIR / f"{p['code']}.png"), use_container_width=True)
                with details_col:
                    c1, c2 = st.columns(2)
                    with c1:
                        st.write(f"**Thương hiệu sản phẩm:** {p['brand']}")
                        st.write(f"**Loại:** {p['type']} · **Kiểu dáng:** {p['form']}")
                        st.write(f"**Mục đích:** {', '.join(sorted(p['purposes']))}")
                        st.write(f"**Pin mỗi lần sạc:** {str(p['battery']) + ' giờ' if p['battery'] is not None else 'Không dùng pin'}")
                        st.write(f"**Pin cùng hộp sạc:** {str(p['battery_total']) + ' giờ' if p['battery_total'] is not None else 'Không áp dụng'}")
                    with c2:
                        st.write(f"**Chống nước:** {p['water']}")
                        st.write(f"**Chống ồn:** {p['noise']}")
                        st.write(f"**Kết nối:** {', '.join(sorted(p['device']))}")
                        st.write(f"**Giá tiền:** Khoảng {fmt_price(p['price_min'])} - {fmt_price(p['price_max'])}")  
        st.link_button("Xem cơ sở tri thức (22 sản phẩm)", "?view=knowledge-base")
else:
    st.info("Chọn các tiêu chí bên trên rồi nhấn **Tìm tai nghe phù hợp** để xem kết quả.")
    st.markdown("### Danh sách các sản phẩm")
    c1, c2, c3 = st.columns(3)
    c1.metric("Tổng sản phẩm", "22")
    c2.metric("Có dây", "13")
    c3.metric("Bluetooth", "9")
    st.link_button("Xem danh sách sản phẩm", "?view=knowledge-base")
