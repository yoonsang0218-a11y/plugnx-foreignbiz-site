# -*- coding: utf-8 -*-
"""PlugNX 2026 하반기 경영전략회의 — 논의자료2(외국인 사업) Appendix 2장.
   ① 추진배경 · ② 시장규모 (Q1). 한국어 / Apple SD Gothic Neo 테마.
   템플릿 제약상(b.add 전용, 수동 도형 금지) 두 장 모두
   executive_summary_takeaways 로 구성 — Appendix 톤(헤드라인+요약+구조화 본문+▶)을 보존."""
import os, sys
from dataclasses import replace

PLUGIN_ROOT = r"C:/Users/admin/.claude/plugins/cache/axlabs/axlabs-mckinsey-pptx/0.1.0"
sys.path.insert(0, PLUGIN_ROOT)

from mckinsey_pptx import PresentationBuilder, DEFAULT_THEME
from mckinsey_pptx.theme import Typography

KO_THEME = replace(
    DEFAULT_THEME,
    typography=replace(DEFAULT_THEME.typography, family="Apple SD Gothic Neo"),
    copyright_text="ⓒ 2026 PLUGnx",
)

FOOTER = ("참고용·법적효력 없음. 재무수치는 목표·가정이며 PoC·LOI 실측 대상. "
          "PROJECT.md(SSOT)")
SRC = "법무부 출입국·외국인정책본부, 고용노동부, 금융위, PROJECT.md(SSOT)"

b = PresentationBuilder(theme=KO_THEME, default_section_marker="논의자료2 · 외국인")

# ===== 슬라이드 1 — ① 추진배경 =====
b.add(
    "executive_summary_takeaways",
    title="정부 정책이 '들어온 외국인을 오래·합법으로 붙드는 인프라'로 이동 — '채용 이후'는 무주공산",
    section_marker="Appendix ①  1/2",
    sections=[
        {
            "takeaway": "Appendix: 외국인 재직관리·환급 사업 — ① 추진배경",
            "bullets": [
                "A0 요약 — 체류외국인 278.3만〔법무부 '25.12〕 시대, 기업은 엑셀로 관리하고 "
                "근로자는 받을 돈을 놓치며 금융사는 외국인을 평가 못 한다",
                "세 통증을 같은 데이터로 푸는 빈 공간 — 당사 인증(ForeignID)·금융권(케이뱅크 등) "
                "관계가 그대로 진입 자산",
            ],
        },
        {
            "takeaway": "① 세 통증이 동시에 발생한다",
            "bullets": [
                "기업: 비자만료·자격외취업 시 사업주 제재 부담",
                "근로자: 미수령 환급(연금·보험·퇴직금)·금융 접근 부재",
                "금융사: 외국인 thin-file(신용정보 부재)로 평가 불가",
            ],
        },
        {
            "takeaway": "② 정책 골든윈도 — 기조가 「양적 확대」→「수급 안정+관리·신뢰」로 이동",
            "bullets": [
                "순풍: E-7-4 숙련전환 점수제(107개 지역)〔법무부〕",
                "순풍: 외국인 기본인적정보 ICAO 표준 통일 → ForeignID 정합〔법무부〕",
                "순풍: 비금융 대안신용 확대 → BackWon+ForeignID 신호 길목〔금융위〕",
            ],
        },
        {
            "takeaway": "③ 빈 공간 — '채용 이후 통합관리+환급+양면데이터' 보유사 없음",
            "bullets": [
                "외국인 서비스 업체 전수조사 결과 해당 결합 보유사 부재〔'26.6 검증〕",
                "경쟁사는 입국 전·유학생·채용입구·생활정보에 분산",
            ],
        },
    ],
    final_conclusion="▶ 기업 관리부담↑ + 근로자 권익공백 + 금융 thin-file이 동시에 커진다 "
                     "→ 같은 데이터 하나로 푸는 인프라 기회",
    source=SRC,
    footnote=FOOTER,
)

# ===== 슬라이드 2 — ② 시장규모 (Q1) =====
b.add(
    "executive_summary_takeaways",
    title="Q1. 시장 규모는 괜찮은가? (체류외국인 278.3만·취업자격 59.4만)",
    section_marker="Appendix ②  2/2",
    sections=[
        {
            "takeaway": "Appendix: 외국인 재직관리·환급 사업 — ② 시장규모",
            "bullets": [
                "A1 요약 — B2B TAM 49만(E계열 취업비자)·B2C TAM 216만(장기체류)〔SSOT〕",
                "외국인 은행계좌 696만인데 인터넷은행 신용대출 ≈0 — 데이터 공백이 곧 기회〔'26.4〕",
            ],
        },
        {
            "takeaway": "시장 모수 (구분 · 모수 · 라벨)",
            "bullets": [
                "체류외국인 총계 — 2,783,247명〔법무부 '25.12〕",
                "취업자격 — 594,047명〔법무부 '25.12〕",
                "B2B TAM(VisaDesk) — 49만(E계열)〔SSOT〕",
                "B2C TAM(BackWon) — 216만(장기체류)〔SSOT〕",
            ],
        },
        {
            "takeaway": "구성 · 공백",
            "bullets": [
                "비자별 — E-9 33.7만·H-2 9.3만·E-7 6.4만·F-4 55.6만〔'24말 연보〕",
                "국적 — 중국 35.2%·베트남 12.1%〔법무부〕",
                "금융공백 — 계좌 696만 vs 인터넷은행 여신 ≈0〔'26.4〕",
                "목표 — PoC 8주 15사·3,300만 → ARR 21억(100사) → 60억(300사)〔가정·SSOT〕",
            ],
        },
    ],
    final_conclusion="▶ E-9 13만→8만으로 신규유입은 줄지만, 정책 무게가 '존량(재직·전환·정착) 관리'로 "
                     "이동 → 우리 타깃은 오히려 두터워짐",
    source=SRC,
    footnote=FOOTER,
)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "plugnx-외국인-추진배경-시장규모.pptx")
b.save(out)
print("SAVED:", out)
