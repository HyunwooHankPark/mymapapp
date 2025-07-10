import streamlit as st
import folium
from streamlit_folium import st_folium

st.title("🇨🇭 한국인이 좋아하는 스위스 관광 명소 추천")

# 스위스 주요 명소 정보
locations = [
    {
        "name": "융프라우요흐 (Jungfraujoch)",
        "lat": 46.5475,
        "lon": 7.9806,
        "desc": "알프스의 탑이라 불리는 융프라우요흐. 융프라우 철도를 타고 올라가면 만년설과 빙하를 감상할 수 있습니다. ❄️🏔️"
    },
    {
        "name": "루체른 카펠교 (Chapel Bridge)",
        "lat": 47.0510,
        "lon": 8.3073,
        "desc": "루체른의 상징인 목조 다리, 중세의 아름다움과 강 위의 꽃장식을 즐길 수 있습니다. 🌉🌸"
    },
    {
        "name": "마테호른 (Matterhorn)",
        "lat": 45.9763,
        "lon": 7.6586,
        "desc": "스위스의 아이콘, 초콜릿 토블론 로고로도 유명한 피라미드형 봉우리입니다. 🗻🍫"
    }
]

# 지도 생성
m = folium.Map(location=[46.8182, 8.2275], zoom_start=7)

# 명소 마커 추가
for loc in locations:
    folium.Marker(
        [loc["lat"], loc["lon"]],
        popup=f"<b>{loc['name']}</b><br>{loc['desc']}",
        tooltip=loc["name"],
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(m)

# 스트림릿에 지도 표시
st_folium(m, width=700, height=500)

# 추가 설명
st.markdown("""
---
### ✨ 추천 이유
스위스는 어디를 가도 그림 같은 풍경을 자랑하지만, 이 3곳은 **한국인들에게 특히 인기**가 높고, 스위스의 진수를 느낄 수 있는 곳들입니다.
""")
