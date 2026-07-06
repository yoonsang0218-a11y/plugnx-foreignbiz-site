# -*- coding: utf-8 -*-
"""
PlugNX 외국인 신사업 — 추진배경 및 시장분석 (요약)
McKinsey-style 한국어 PPTX 빌드 스크립트.
원본: output/background-market-summary.html (3섹션) → 7장으로 확장.
모든 수치·출처는 원본 HTML에서 그대로 가져옴(신규 수치 생성 없음).
"""
import os
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
# 1. 표지 — cover_slide
# ───────────────────────────────────────────────────────────────────
b.add(
    "cover_slide",
    title="외국인 신사업 · 추진배경 및 시장분석",
    subtitle="체류외국인 278만 시대, ‘채용 이후’를 붙드는 인프라 — PlugNX VisaDesk · BackWon · ForeignID",
    client="PlugNX",
    date="2026",
    confidentiality="CONFIDENTIAL",
    section_marker=SECTION,
)

# ───────────────────────────────────────────────────────────────────
# 2-A. Executive Summary KPI — kpi_dashboard (278 / -313 / 112+ / 92.9%)
# ───────────────────────────────────────────────────────────────────
b.add(
    "kpi_dashboard",
    title="한눈에 — 정주화·구조적 인력난·정책 골든타임의 트리플 추진력",
    subtitle="시장은 이미 도래했고, 정책 무게는 ‘채용 이후’ 관리·신뢰로 이동 중",
    kpis=[
        {"label": "체류외국인 (’25.12)", "value": "278만",
         "delta": "전년比 +5.0%", "delta_dir": "up",
         "context": "2,783,247명 · ’27~’28 300만 돌파 추정"},
        {"label": "생산연령인구 감소 (~2030)", "value": "−313만",
         "delta": "구조적 감소", "delta_dir": "down",
         "context": "법무부 2030 이민정책 미래전략(통계청 추계)"},
        {"label": "’30 산업계 부족인력", "value": "112만+",
         "delta": "최소 부족", "delta_dir": "down",
         "context": "법무부 2030 이민정책 미래전략(’26.3)"},
        {"label": "내국인 취업 기피", "value": "92.9%",
         "delta": "경기 무관 구조 수요", "delta_dir": "flat",
         "context": "중기중앙회 2025 실태조사(1,223사)"},
    ],
    columns=4,
    section_marker=SECTION,
    source=SRC_POLICY,
    footnote=None,
)

# ───────────────────────────────────────────────────────────────────
# 2-B. Executive Summary 논리 — executive_summary_takeaways (핵심 3줄)
# ───────────────────────────────────────────────────────────────────
b.add(
    "executive_summary_takeaways",
    title="요약 — 트리플 추진력 × 두 시장 × 경쟁 공백을 PlugNX가 선점",
    sections=[
        {"takeaway": "① 시장은 정주화·구조적 인력난·정책 골든타임의 트리플 추진력이 동시에 작동",
         "bullets": [
             "2030년까지 생산연령인구 −313만, 산업계 최소 112만 부족 → 외국인력은 ‘필수 인프라’",
             "내국인 취업 기피 92.9%·구인난 82.6% — 인건비(13.4%)가 아닌 경기 무관 구조 수요",
             "유학 +17.1%·영주 +8.9% → 노동력에서 소비·금융 고객으로 시장의 ‘질’이 이동",
         ]},
        {"takeaway": "② 278만은 B2C 216만(사람)과 B2B 49만(사업장) 두 시장으로 갈라짐",
         "bullets": [
             "B2C TAM = 장기체류 216만(환급·금융·관리 대상)",
             "B2B TAM = E계열(E-1~E-10) 취업 풀 약 49만(기업 고용·비자 관리 대상)",
             "E-9 신규는 둔화하나 숙련전환·계절·정주는 확대 → 매년 반복되는 구독·금융 시장",
         ]},
        {"takeaway": "③ B2B 준법 + B2C 환급 + 인증을 동시에 쥔 플레이어는 공백 — PlugNX가 선점",
         "bullets": [
             "VisaDesk(고용 준법) × BackWon(환급·금융)을 ForeignID 인증·데이터 위에 결합",
             "클링커즈는 B2C 금융 슈퍼앱·대출중개 지향 — 환급 미진출·자체 인증/B2B 데이터 미보유",
             "고용+금융 데이터 = 외국인 대체 신용스코어의 길목 → 양면 네트워크로 진입",
         ]},
    ],
    final_conclusion="‘채용 이후의 모든 것’을 양면 데이터로 묶어 비어 있는 자리를 선점 — 지금이 정책 골든타임.",
    section_marker=SECTION,
    source=SRC_POLICY,
)

# ───────────────────────────────────────────────────────────────────
# 3. 추진배경 — three_trends_numbered (구조적 트리플 추진력 01·02·03)
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
# 4. 시장규모 — funnel (TAM 278만 → SAM 216만 → B2B 49만)
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

# ───────────────────────────────────────────────────────────────────
# 5. 기회·경쟁공백 — two_column_compare (Right-to-win vs 경쟁 공백)
# ───────────────────────────────────────────────────────────────────
b.add(
    "two_column_compare",
    title="우리가 들어갈 자리 — ‘채용 이후’를 양면(B2B+B2C)으로 독점하는 공백",
    subtitle="기업 고용 준법(VisaDesk)과 근로자 환급·금융(BackWon)을 하나의 인증 인프라(ForeignID)·데이터 위에 결합",
    left_label="왜 PlugNX가 이기는가 (Right-to-win)",
    right_label="경쟁 공백 (’26.6 검증)",
    left_items=[
        "양면 네트워크 — 기업 등록→근로자 자동 유입(전환 60%+·CAC 0)〔가정〕",
        "고용+금융 데이터 결합 = 외국인 대체 신용스코어의 길목",
        "정책 정합 — K-Trust·임금자문위·비자 단순화에 직접 연결",
        "전환비용·전문가 네트워크(행정사·변호사)로 단순 중개와 차별화",
    ],
    right_items=[
        "클링커즈(glow)는 B2C 금융 슈퍼앱·대출중개 지향 — 환급 미진출",
        "자체 본인인증·B2B 고용데이터 미보유 → 양면 결합 불가",
        "vivisa×클링커즈 동맹(비자→대체신용)은 신용스코어 길목 경쟁 신호 → 분기 워치",
        "→ B2B 준법 + B2C 환급 + 인증을 동시에 쥔 플레이어는 아직 공백",
    ],
    left_color="blue",
    right_color="navy",
    show_arrow=True,
    section_marker=SECTION,
    source="출처: PlugNX 경쟁 검증(’26.6) · 사업기획서 v1.0. 전환율 등 〔가정〕 표기는 확정 실적 아님.",
    footnote=None,
)

# ───────────────────────────────────────────────────────────────────
# 6. B2B2C 플라이휠 — process_flow_horizontal (5단계 순환)
# ───────────────────────────────────────────────────────────────────
b.add(
    "process_flow_horizontal",
    title="B2B2C 플라이휠 — 한 번 들어가면 양쪽이 서로를 키운다",
    subtitle="B2B 진입이 B2C 유입을 만들고, B2C 만족이 다시 B2B 근속·유지를 키우는 순환 구조",
    steps=[
        {"name": "기업이 근로자 등록", "description": "VisaDesk로 고용·체류·비자 준법 관리 진입"},
        {"name": "근로자 BackWon 자동 유입", "description": "전환 60%+ · CAC 0〔가정〕"},
        {"name": "B2C 환급·금융 만족", "description": "미수령 연금·보험·퇴직금 환급 + 급여 적정성"},
        {"name": "기업 근속률 ↑", "description": "근로자 만족이 이직·이탈을 낮춤"},
        {"name": "B2B 유지·확장", "description": "유지율·계정 확장으로 ARR 누적"},
    ],
    section_marker=SECTION,
    source="출처: 사업기획서 v1.0 플라이휠 가정. 전환율·CAC는 〔가정〕 목표치(확정 실적 아님).",
    footnote=None,
)

# ───────────────────────────────────────────────────────────────────
# 7-A. 목표 — kpi_dashboard (가정 기반)
# ───────────────────────────────────────────────────────────────────
b.add(
    "kpi_dashboard",
    title="목표 — 가정 기반 목표치(확정 실적 아님)",
    subtitle="PoC → 12개월 → 24개월 ARR 경로 · 요금 Starter/Growth/Compliance",
    kpis=[
        {"label": "PoC (8주)", "value": "15사",
         "delta": "3,300만원", "delta_dir": "flat",
         "context": "8주 파일럿 · 〔가정〕 목표"},
        {"label": "12개월 ARR", "value": "21억",
         "delta": "100사", "delta_dir": "up",
         "context": "구독 누적 〔가정〕 목표"},
        {"label": "24개월 ARR", "value": "60억",
         "delta": "300사", "delta_dir": "up",
         "context": "구독 누적 〔가정〕 목표"},
        {"label": "월 요금(만원)", "value": "29·89·169",
         "delta": "Starter/Growth/Compliance", "delta_dir": "flat",
         "context": "Enterprise 별도"},
    ],
    columns=4,
    section_marker=SECTION,
    source=("출처: 사업기획서 v1.0. 전환율·ARR·요금 등은 〔가정〕 기반 목표치이며 확정 실적이 아님. "
            "본 요약의 시장 해석은 법무부 「2030 이민정책 미래전략」(5대 과제)을 PlugNX가 민간 사업기회로 재해석한 것."),
    footnote=None,
)

# ───────────────────────────────────────────────────────────────────
# 7-B. 결론 — dark_navy_summary (한 문장 + 면책)
# ───────────────────────────────────────────────────────────────────
b.add(
    "dark_navy_summary",
    body=("[결론]: 시장은 정주화·구조적 인력난·정책 골든타임의 트리플 추진력이 작동하고, "
          "경쟁은 B2B 준법과 B2C 환급을 동시에 쥔 플레이어가 비어 있다. "
          "PlugNX는 ‘채용 이후의 모든 것’을 양면 데이터로 묶어 이 공백을 선점한다."),
    eyebrow="외국인 신사업 · 추진배경 및 시장분석",
    corner_text="PlugNX",
    section_marker=SECTION,
    footnote=("면책: 비자·환급·세무 판단은 법적 효력 없는 참고 정보로, 행정사·변호사·세무사 검증과 "
              "최신 법령 확인이 필요. 정책·통계 수치는 자주 개정되므로 인용 시 최신 1차 통계 재확인."),
)

out_path = r"C:/Users/admin/plugnx-foreignbiz/output/background-market-summary.pptx"
b.save(out_path)
print("SAVED:", out_path)
print("SLIDES:", len(b.prs.slides._sldIdLst))
