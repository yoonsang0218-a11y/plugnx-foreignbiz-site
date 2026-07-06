# -*- coding: utf-8 -*-
"""
PlugNX 외국인 신사업 — 추진배경 + 시장규모 (슬라이드 4·5만 발췌)
원본 빌드 스크립트 agent_background_market_summary.py의 슬라이드 4(추진배경,
three_trends_numbered)와 슬라이드 5(시장규모, funnel)를 그대로 가져온 2슬라이드 덱.
모든 수치·출처는 원본(background-market-summary.html)에서 그대로 가져옴(신규 수치 생성 없음).
"""
import sys
from dataclasses import replace

PLUGIN_ROOT = r"C:/Users/admin/.claude/plugins/cache/axlabs/axlabs-mckinsey-pptx/0.1.0"
sys.path.insert(0, PLUGIN_ROOT)

from mckinsey_pptx import PresentationBuilder, DEFAULT_THEME  # noqa: E402
from mckinsey_pptx.theme import Typography  # noqa: E402
from pptx.dml.color import RGBColor  # noqa: E402

# 폰트 상수 — Windows 환경(맑은 고딕)
KO_FONT = "맑은 고딕"   # Malgun Gothic — 한글·라틴·숫자 모두 포함, Windows 기본 탑재

# 한국어 테마 — 맑은 고딕(Hangul 렌더링) + 단일 블루 #0066cc
KO_PALETTE = replace(
    DEFAULT_THEME.palette,
    bright_blue=RGBColor(0, 102, 204),     # #0066cc — 단일 강조 블루
    mid_blue=RGBColor(0, 102, 204),
    light_blue=RGBColor(64, 145, 220),
    deep_navy=RGBColor(15, 30, 50),
    dark_navy=RGBColor(20, 38, 60),
    status_red=RGBColor(215, 0, 21),       # #d70015 — 손해·위험 수치 전용
)
KO_THEME = replace(
    DEFAULT_THEME,
    palette=KO_PALETTE,
    typography=replace(DEFAULT_THEME.typography, family=KO_FONT),
    copyright_text="ⓒ 2026 PlugNX",
)

SECTION = "외국인 신사업 · 추진배경/시장분석"

# 공통 출처 푸터
SRC_POLICY = ("출처: 법무부 「’25.12 출입국·외국인정책 통계월보」 · "
              "법무부 「2030 이민정책 미래전략」(’26.3) · "
              "중소기업중앙회 「2025 외국인력 고용 종합애로 실태조사」(1,223사) · "
              "고용노동부 E-9 도입쿼터. 비자·정책 수치는 자주 개정되는 참고 정보.")
SRC_MARKET = ("출처: 법무부 「’25.12 출입국·외국인정책 통계월보」 · "
              "장기체류 216.06만 분해(등록 160.66만+거소 55.39만, ’25.11) · "
              "E-9 약 30.2만(시사저널). SAM/SOM 전환 가정은 사업기획서 가정값.")

b = PresentationBuilder(theme=KO_THEME, default_section_marker=SECTION,
                        auto_page_numbers=True)

# ───────────────────────────────────────────────────────────────────
# 슬라이드 1 (원본 4번) — 추진배경 : three_trends_numbered (구조적 트리플 추진력 01·02·03)
# ───────────────────────────────────────────────────────────────────
b.add(
    "three_trends_numbered",
    title="왜 지금 — 경기가 아니라 ‘구조’가 만든 수요, 3개의 추진력",
    subtitle="정책 기조도 「양적 확대」→「수급 안정+관리·신뢰 강화」로 전환 (정책 골든타임)",
    trends=[
        {"label": "01 인구 절벽 · 일할 사람이 사라진다",
         "bullets": [
             "2030년까지 생산연령인구 약 −313만 명",
             "산업계 최소 112만 부족(법무부 2030 이민정책 미래전략)",
             "외국인력은 ‘선택’이 아니라 ‘필수 인프라’",
         ]},
        {"label": "02 구조적 인력난 · “사람이 없어서” 쓴다",
         "bullets": [
             "내국인 미고용 사유 92.9% = ‘내국인 취업 기피’",
             "고용 사유 82.6% = ‘내국인 구인난’ (중기중앙회 2025)",
             "인건비 절감(13.4%) 아닌, 경기와 무관한 구조 수요",
         ]},
        {"label": "03 정주화·고숙련화 · 노동력 → 소비·금융 고객",
         "bullets": [
             "유학 30.9만(+17.1%, 증가폭 1위)·영주 22.1만(+8.9%)",
             "결혼이민 18.8만(+3.7%) — 단기 순환 → 정주·반복 수요",
             "정책: E-9 13만→8만(−38.5%), 존량(재직·전환·정착) 관리로 무게 이동",
         ]},
    ],
    section_marker=SECTION,
    source=SRC_POLICY,
)

# ───────────────────────────────────────────────────────────────────
# 슬라이드 2 (원본 5번) — 시장규모 : funnel (TAM 278만 → SAM 216만 → B2B 49만)
# ───────────────────────────────────────────────────────────────────
b.add(
    "funnel",
    title="시장 규모 — 278만이 B2C 216만(사람)·B2B 49만(사업장) 두 시장으로 분기",
    subtitle="B2B의 49만은 ‘기업 수’가 아니라 E계열 취업 외국인 ‘근로자 풀’ — 사업장(社) vs 사람(名)으로 분리",
    stages=[
        {"name": "TAM · 전체 체류외국인 (’25.12)", "value": "278만 명",
         "description": "전년比 +5.0% · 깔때기 진입 최상단 · ’27~’28 300만 돌파 추정"},
        {"name": "SAM · 장기체류 잠재고객 (’25.11)", "value": "216만 명",
         "description": "B2C TAM(환급·금융·관리) = 등록 160.66만 + 거소신고 외국국적동포 55.39만"},
        {"name": "B2B wedge · E계열 취업 풀", "value": "49만 명",
         "description": "B2B TAM(기업 고용·비자 관리) = E-1~E-10 / 그중 E-9 약 30.2만(광·제조 80%+)"},
    ],
    section_marker=SECTION,
    source=SRC_MARKET,
    footnote=("주: 취업자격 59.4만(광의, H-2·C-4 포함)과 B2B TAM 49만(E계열)은 정의가 다른 별개 수치. "
              "유학 30.9만(+17.1%)·영주 22.1만(+8.9%)은 정주·금융 신규 고객층."),
)

out_path = r"C:/Users/admin/plugnx-foreignbiz/output/background-market-summary-slides-4-5.pptx"
b.save(out_path)
print("SAVED:", out_path)
print("SLIDES:", len(b.prs.slides._sldIdLst))
