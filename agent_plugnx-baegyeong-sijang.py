# -*- coding: utf-8 -*-
"""PlugNX 보고용 2장 한국어 PPTX — 추진배경 + 시장분석 (맥킨지 톤)."""
import os
import sys

PLUGIN_ROOT = r"C:/Users/admin/.claude/plugins/cache/axlabs/axlabs-mckinsey-pptx/0.1.0"
sys.path.insert(0, PLUGIN_ROOT)

from dataclasses import replace
from mckinsey_pptx import PresentationBuilder, DEFAULT_THEME
from mckinsey_pptx.theme import Typography

KO_THEME = replace(
    DEFAULT_THEME,
    typography=replace(DEFAULT_THEME.typography, family="Apple SD Gothic Neo"),
    copyright_text="ⓒ 2026 PLUGnx",
)

FOOTER = ("참고용·법적 효력 없음. 재무수치는 목표·가정. 비자·금융·환급 판단은 전문가 검증·최신 법령 확인 필요. "
          "출처: 법무부 출입국·외국인정책본부, 고용노동부, 금융위, PROJECT.md〔SSOT〕.")

b = PresentationBuilder(theme=KO_THEME, default_section_marker="PLUGnx 추진배경·시장분석")

# ── 슬라이드 1: 추진배경 ─────────────────────────────────────────
b.add(
    "three_trends_numbered",
    title=("정부 정책이 '들어온 외국인을 오래·합법으로 붙드는 인프라'로 이동 중 "
           "— PlugNX 테제와 정합한 골든윈도"),
    trends=[
        {
            "label": "① 시장 (비가역적 확대)",
            "bullets": [
                "체류외국인 278.3만 명〔법무부 '25.12〕·취업자격 59.4만",
                "인구·노동력 구조상 비가역적 확대 — 되돌릴 수 없는 추세",
                "E-9 도입은 13만→8만으로 축소('26)나 흐름은 유지",
                "정책 무게가 '신규 유입' → '존량(재직·전환·정착) 관리'로 이동",
            ],
        },
        {
            "label": "② 정책 골든윈도 (기조 전환)",
            "bullets": [
                "「양적 확대」 → 「수급 안정 + 관리·신뢰 강화」로 전환",
                "순풍1: E-7-4 숙련전환 점수제 제도화(107개 지역)",
                "순풍2: 외국인 기본인적정보 ICAO 표준 통일",
                "순풍3: 비금융 대안신용·마이데이터 확대 (※「2030 이민정책 미래전략」 5축을 PlugNX 재해석)",
            ],
        },
        {
            "label": "③ 빈 공간 (무주공산)",
            "bullets": [
                "외국인 서비스 업체 28곳+ 전수조사 결과",
                "'채용 이후' 통합 관리(재직 준법)+환급+양면 데이터 결합 보유처 없음",
                "경쟁사는 입국 전·유학생·채용입구·생활정보에 분산",
                "→ '채용 이후 전 영역'은 사실상 무주공산",
            ],
        },
    ],
    subtitle=("시사점: 기업의 외국인 관리 부담↑ + 근로자 권익 공백 + 금융 thin-file이 동시에 커진다 "
              "→ 같은 데이터 하나로 푸는 인프라 기회"),
    source=FOOTER,
)

# ── 슬라이드 2: 시장분석 ─────────────────────────────────────────
b.add(
    "overview_areas",
    title=("B2B 49만·B2C 216만의 이중 시장 + 인터넷은행 외국인 여신 0의 금융 공백"),
    areas=[
        {
            "name": "A. 시장규모 (TAM·목표)",
            "bullets": [
                "TAM B2B 49만 (E계열 취업비자)〔SSOT〕",
                "TAM B2C 216만 (전체 장기체류)〔SSOT〕",
                "목표〔가정〕: PoC 8주 15사·3,300만",
                "ARR 21억(100사·12M) → 60억(300사·24M)",
                "요금제 Starter29 / Growth89 / Compliance169만원·월",
            ],
        },
        {
            "name": "B. 시장 구성 (비자별)",
            "bullets": [
                "E-9 33.7만·H-2 9.3만〔'24말 연보〕",
                "E-7 6.4만·F-4 55.6만〔'24말 연보〕",
                "국적: 중국 35.2%·베트남 12.1%〔법무부〕",
                "재직·전환 존량이 두꺼움 → 관리 수요 큼",
            ],
        },
        {
            "name": "C. 금융 공백 (여신 0)",
            "bullets": [
                "외국인 은행계좌 696만〔'26.4〕",
                "인터넷은행 외국인 신용대출 ≈0 (토스 제외)",
                "병목 = 외국인 thin-file (신용정보 부재)",
                "고용데이터가 그 빈칸을 메움 → 결합 우위",
            ],
        },
        {
            "name": "D. 경쟁 지형",
            "bullets": [
                "정면 경쟁자 부재 ('채용 이후' 양면 결합)",
                "최대 위협 = 은행·카드 외국인 신용평가모형",
                "예: 신한 하이크레딧·코스콤 F-Global",
                "차별 = 검증된 고용·임금 데이터의 양면 결합",
            ],
        },
    ],
    call_out=("수요(278만)와 공백(여신0)이 동시에 열려 있고, 양면 데이터 결합은 무주공산 — 진입 매력"),
    source=FOOTER,
)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "plugnx-추진배경-시장분석.pptx")
b.save(out)
print("SAVED:", out)
