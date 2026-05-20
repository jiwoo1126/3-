import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="음식 추천 앱",
    page_icon="🍜",
    layout="centered"
)

# 음식 데이터
foods = {
    ("기쁨", "맑음", "안 매움"): [
        ("초밥", "https://images.unsplash.com/photo-1579871494447-9811cf80d66c"),
        ("파스타", "https://images.unsplash.com/photo-1521389508051-d7ffb5dc8i")
    ],
    ("우울", "비", "매움"): [
        ("짬뽕", "https://images.unsplash.com/photo-1585032226651-759b368d7246"),
        ("떡볶이", "https://images.unsplash.com/photo-1607301405390-d831c242f59b")
    ],
    ("피곤", "추움", "매움"): [
        ("김치찌개", "https://images.unsplash.com/photo-1590301157890-4810ed352733"),
        ("마라탕", "https://images.unsplash.com/photo-1625944525533-473f1b3d54f6")
    ],
    ("행복", "더움", "안 매움"): [
        ("냉면", "https://images.unsplash.com/photo-1635363638580-c2809d049eee"),
        ("샐러드", "https://images.unsplash.com/photo-1546793665-c74683f339c1")
    ]
}

# 제목
st.title("🍽️ 음식 추천 앱")
st.write("현재 기분과 날씨에 맞는 음식을 추천해드려요!")

# 사용자 입력
mood = st.selectbox(
    "오늘 기분은 어떤가요?",
    ["기쁨", "우울", "피곤", "행복"]
)

weather = st.selectbox(
    "오늘 날씨는 어떤가요?",
    ["맑음", "비", "추움", "더움"]
)

spicy = st.radio(
    "매운 음식 좋아하시나요?",
    ["매움", "안 매움"]
)

# 추천 버튼
if st.button("음식 추천 받기 🍴"):

    key = (mood, weather, spicy)

    if key in foods:
        food = random.choice(foods[key])

        st.success(f"추천 음식: {food[0]}")

        st.image(
            food[1],
            caption=food[0],
            use_column_width=True
        )

    else:
        st.warning("조건에 맞는 음식이 없어요 😢")
