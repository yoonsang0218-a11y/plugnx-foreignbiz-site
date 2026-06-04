# business-case-9fk2x7.html — 검증 완료 드롭인 (라운드 2·3)

> ⚠️ Codex가 main에서 편집 중 → Claude는 직접 편집하지 않고 인계. 적용 주체가 anchor로 교체/삽입.
> 근거: `r3-strategy-choice.md`·`r3-product.md`·`r3-kpi.md`·`r2-reverify.md`·`99b-synthesis-r2r3.md`.
> 스코어카드: ✅14 · 🟠12 · 🟡7 · ❌2. 수치는 1차 출처·기준시점, 재무는 목표·가정, 비자·정책·금융규제는 참고용.

---

## 🚨 P0 · 라이브 데모 브랜딩 위반 (본문 외부 운영 액션, IR 전 필수)
§07이 "MVP 라이브"의 근거로 링크하는 **plugnx-visaops.netlify.app**가 브랜딩 규칙을 정면 위반:
- `/workers` 헤더·푸터 **"Plug&X VisaOps"**, **"© 2026 Plug&X × Moneeback"** / 랜딩 **"PlugNX Crew"** / `/dashboard` **"Plug&X VisaOps"** / 도메인에 폐기 코드네임 **visaops**.
- PROJECT.md L42 `Plug&X 절대 금지`, L45 `VisaOps·Crew 폐기`. 본문은 `VisaDesk`를 쓰는데 링크 도착지가 불일치 → 투자자가 클릭 시 신뢰 역전.
- **액션**: 라이브 리브랜딩(Plug&X→PlugNX, VisaOps/Crew→VisaDesk, 도메인 교체). 웹 소스 `C:\Users\admin\plugnx-foreign-finance-opportunity\webapp\`. business-case 본문 변경 아님 — **제품/배포 작업**.

---

## §05 Strategic Choice — 8대 신시장 라벨링 (가장 중요)
**(a) Note 박스** — lead 문단 직후 삽입:
```html
<div style="display:inline-flex;align-items:flex-start;gap:8px;margin-top:14px;font-size:12.5px;color:var(--muted);background:var(--soft);border:1px solid var(--border);border-radius:10px;padding:11px 15px">
  Note /// 정부 「2030 이민정책 미래전략」(법무부, 2026.3.3)이 발표한 것은 <b style="color:var(--ink)">5대 핵심 추진과제</b>입니다. 본 사업의 <b style="color:var(--ink)">8대 신시장(코어 3·확장 3·제휴 2)</b>은 이 5대 과제를 민간 사업기회로 재해석한 PlugNX의 시장분류로, 정부 발표 항목과 구분됩니다. [출처: 정책브리핑 newsId 148960240]
</div>
```
**(b) 매핑 표** — 우선순위 매트릭스 위에 삽입:
```html
<table class="dt">
  <thead><tr><th>정부 5대 과제 (2026.3.3 · 사실)</th><th>PlugNX 대응 시장 (해석)</th><th>진입 등급</th></tr></thead>
  <tbody>
    <tr><td>② 비자체계·이민행정 혁신 (E계열 10종 39개→3단계, Hi-Korea 통합·AI 분류심사)</td><td>RegTech (VisaDesk)</td><td><b>코어 — 집중</b></td></tr>
    <tr><td>⑤ 권익보호 + ③ 외국인 임금 자문위원회(임금 적정성)</td><td>FinTech (Moneeback)</td><td><b>코어 — 집중</b></td></tr>
    <tr><td>④ 성실기업 우대 (고용 컴플라이언스)</td><td>HRTech / K-Trust</td><td><b>코어 — 업셀</b></td></tr>
    <tr><td>① 우수·필수인력 유치 (채용 파이프라인)</td><td>채용매칭</td><td>확장 — 옵션</td></tr>
    <tr><td>① 외국인 요양보호사 양성대학 지정</td><td>돌봄</td><td>확장 — 버티컬 PoC</td></tr>
    <tr><td>⑤ 사회통합프로그램 의무화·한국어교육</td><td>사회통합교육</td><td>확장 — 증빙 모듈</td></tr>
    <tr><td>⑤ 정착·생활 지원</td><td>정착생활</td><td>제휴 — 허브</td></tr>
    <tr><td>⑤ 권익보호 강화</td><td>권익보호 리걸테크</td><td>제휴 — referral</td></tr>
  </tbody>
</table>
<p style="font-size:12px;color:var(--muted);margin-top:8px">좌측 과제는 정책브리핑(148960240) 원문 기준 사실, 우측 시장분류·진입등급은 PlugNX 전략 해석(가정).</p>
```
**(c) Decision 01 보강 문장** (RegTech wedge): "정책이 집행 단계로 — ‘지역활력 소상공인 외국인 고용특례’ 2026.5.18~2027.12.31 시범(인구감소지역 89개)으로 준법 수요 실재화. 출입국 신청 ‘대행’은 등록 행정사·변호사 전속(§79의2)이라 VisaDesk는 점검·알림·서류준비까지만, 대행은 전문가 네트워크 라우팅(매칭 수수료)."
**(d) Decision 02 보강** (FinTech): "여신·신용평가 right-to-win은 ‘라이선스 또는 샌드박스 경로’ 명시 시 성립 — 신용스코어 영업화엔 신용정보법 전문개인신용평가/마이데이터 허가 게이트. 혁신금융 샌드박스(통신대안평가 EQUAL 2025.9 ‘외국인 대안신용평가’ 지정 선례) 경로로 단계 진입."
**(e) caveat 각주**: "점수는 전략 평가(가정)·‘8대 신시장’은 PlugNX 사업분류(정부 발표 아님)."

## §07 Product — "검증된 것 vs 남은 위험" (가장 중요)
**(a) 표제 부제 완화**: `MVP는 이미 라이브 — 제품 위험은 검증됨` → 부제 추가 "UI·고객 플로우 위험은 검증, 핵심 AI(OCR)·다국어·환급 정확도는 차기 검증 과제".
**(b) 검증/미검증 표** — lead 아래 삽입:
```html
<table class="dt">
  <thead><tr><th>항목</th><th>상태</th><th>근거 (2026.6 라이브 점검)</th></tr></thead>
  <tbody>
    <tr><td>UI·정보구조·고객 플로우</td><td style="color:var(--ok)"><b>검증됨</b></td><td>랜딩·자가진단·/workers·/dashboard 라이브 렌더링</td></tr>
    <tr><td>모던 스택 안정성</td><td style="color:var(--ok)"><b>검증됨</b></td><td>Next.js 15·React 19·Tailwind 4·Supabase·Vercel/Netlify</td></tr>
    <tr><td>B2B 대시보드 화면</td><td style="color:var(--warn)">약 20여 개</td><td>코어 8 + Moneeback 3 + 확장 9~11 (본문 ‘25’ 보정)</td></tr>
    <tr><td>다국어</td><td style="color:var(--warn)">3개 라이브</td><td>한·영·베 라이브 + 중·태·우즈벡 확대 중(목표)</td></tr>
    <tr><td>GPT-4V OCR (여권·외국인등록증)</td><td style="color:var(--danger)">미검증</td><td>/dashboard/documents는 수동 상태 트래커(282건, 사람 기재) — OCR 증거 없음</td></tr>
    <tr><td>환급 산정 정확도 / ForeignID L1~L3 / 리드 백엔드</td><td style="color:var(--danger)">미검증</td><td>표시 환급액은 추정치 · 인증·신용스코어·/api/lead 실가동 미확인</td></tr>
  </tbody>
</table>
```
**(c) Moneeback 환급 셀 보정**: "표시 금액(평균 1,050만)은 예시 평균이며, 실제 환급액은 체류자격·국적·사회보장협정·납부이력·출국여부에 따라 달라지는 추정치(확정액은 소관기관 조회)."
**(d) 6개 언어 SSOT 보정**: PROJECT.md L16 ‘6개 언어’는 라이브(3개)와 불일치 → ‘3개 라이브 + 3개 확대 중’으로 SSOT 보정 권고.
**(e) 출처 각주**: "라이브 상태·화면 수·기능 성숙도는 2026.6.2 plugnx-visaops.netlify.app 직접 접근 기준(데모는 수시 업데이트)."

## §12 KPI — 선행지표·게이트·벤치마크 라벨
**(a) 전환 단계 분해 각주**: "‘전환 30%’는 세미나→계약(50→15) 기준. 분해 시 세미나→미팅 40%, 미팅→유료 75%. self-serve 무료체험 중앙값(4~6%)과 직접 비교 부적절(범주 오류) — 이건 ‘무료 준법진단=가치 입증 세션’."
**(b) ARR 벤치마크 각주**: "ARR 21억(12M)→60억(24M)=YoY 약 186%. 전통 B2B SaaS($1~5M) 중앙값 40%·AI-네이티브 110% 상회하는 상위 사분위 공격 목표(초기 <$1M 구간은 상위 사분위 최대 300% YoY). NRR>110%·CAC payback<12M 병기 권고."
**(c) 유저 10만 분해 각주**: "24M ‘Moneeback 유저 10만’ = 관리외국인 1만의 10배 = (a)캡티브 전환분(관리외국인×자동유입 60%+) + (b)B2C 단독유입(앱 직접·추천·환급 입소문). ‘전환 60%+’는 B2B 등록자 기준 자동유입률."
**(d) 후행지표 행 추가**: NRR(100→105→110%·가정)·GRR(88→90→90%·가정).
**(e) PoC go/no-go 게이트 박스** (2주/4주/8주 3단계 게이트) — `r3-kpi.md` 참조.
**(f) 섹션 말미 고지**: 모든 KPI는 가정 기반 목표치 · SSOT 인용.

---

## R2 재검증 → 핵심수치 정정 (HTML 인용 시)
| 항목 | 판정 | 조치 |
|---|---|---|
| 이민청 정부조직법 개정안 발의 시점 | 🟠 | **2024.2.2** (정점식 의원 등 10인) — 본문/dossier ‘2026.2.2’는 연도 오류 |
| 지역특화형 5,072명 vs 2026.5.18 고용특례 | ❌ | **별개 제도** — 5,072=F-2-R 다년 배정 쿼터, 고용특례=2026.5.18 시범 완화조치. 동일시 금지 |
| 외국인 비자대행기관 3,725곳 | 🟡 | 1차 출처 미확인 → "확인 필요" 각주 또는 출처 명기 전 사용 자제 |
| K-Trust 쿼터 ±20~30% | 🟡 | 공식 1차 미확인 → "쿼터 우대/제한(가감폭은 운영지침 확인 필요)"로 완화 |
| B2C ARPU 140만 (=1,050만×13%) | 🟠 | 두 입력 모두 가정: 평균환급 1,050만(합산추정)·성공보수 13%(가정) → ‘가정값, 실거래 데이터로 보정’ 라벨 |
| 임금체불 출처 data.go.kr/15068736 | 🟠 | 그 파일은 ‘내국인+외국인 합산’ 전체 통계 → 외국인 한정 수치는 국회 제출자료/보도가 실제 출처로 교정 |
| 자블리 고객사 CJ대한통운 | 🟡 | 핵심 보도엔 쿠팡·롯데글로벌로지스틱스만 → CJ대한통운은 ‘미확인’ 분리 표기 |
| SOM 15만 분모 | 🟡 | B2C 직접 vs B2B 경유 정의 명시 + ARR 300사 환산(약 1.5~1.8만)과 괴리 각주 |
