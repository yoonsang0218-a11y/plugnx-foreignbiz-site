# R3 · 07 Product Feasibility (MVP 라이브)

**헤드라인**: MVP는 진짜 라이브다 — 랜딩·자가진단·/workers 환급계산기·/dashboard(약 20여 페이지) 모두 가동 확인. 단, ① 라이브 사이트가 금지 표기 'Plug&X VisaOps/Crew'를 쓰고 ② GPT-4V OCR은 화면상 미구현(서류함은 수동 트래커) ③ '25페이지·6개 언어'는 실제(약 20여 페이지·3개 언어 라이브, 나머지 확대 중)와 괴리 → '제품 위험 검증됨'은 'UI·플로우 위험은 검증, 핵심 AI(OCR)·다국어·정확도 위험은 미검증'으로 한정해야 한다.

**검증 총평**: §07 핵심 주장 9건을 1차 출처(plugnx-visaops.netlify.app 및 하위 라우트, PROJECT.md, Next.js 공식)로 반증 시도한 결과: 'MVP 라이브'와 '모던 스택 안정성'은 supported, 그러나 정량·정성 디테일에서 다수 보정이 필요하다. (1) '25페이지'는 라이브상 미명시·실측 약 20~23개로 needs-update. (2) '6개 언어'는 §07 본문 자체는 '다국어(한·영·베)' 3개로 정확히 적었으나 PROJECT.md SSOT가 '6개 언어'로 단정 — 라이브 3개 + 로드맵 3개로 보정 필요(needs-update). (3) GPT-4V OCR은 스택 나열일 뿐 라이브 기능 미관측 → uncertain(약함). (4) 'Plug&X VisaOps/Crew' 및 plugnx-visaops 도메인은 PROJECT.md 금지 표기 정면 위반 → refuted, IR 전 정정 필수. (5) '제품 위험 검증됨'은 UI·정보구조·고객플로우 한정으로 부분 supported. 결론: '라이브 MVP'라는 큰 주장은 진실이나, 정량 수치·핵심 AI·브랜딩에서 과대표기가 있어 'needs-update/일부 refuted'로 한정 표기해야 투자자 신뢰 훼손을 막는다.

## 심화 분석 (근거·출처)
- **랜딩·자가진단·/workers·/dashboard가 실제로 접근·렌더링되어 MVP 라이브 주장은 사실로 확인된다** _(신뢰 high, 기준 2026-06-02)_
  - 근거: plugnx-visaops.netlify.app 랜딩에 헤드라인 '외국인 고용, 이렇게 단순해집니다', 9문항 자가진단(0/9 카운터·클릭형·플랜 추천), 요금제 Starter 29만/Growth 89만/Compliance 169만/Enterprise 별도가 모두 렌더링. /workers는 'AI 자동 환급 계산'(국민연금 평균 520만·고용보험 180만·퇴직금 350만=1,050만) 3단계 플로우와 CTA '내 환급금 확인하기'가 라이브. /dashboard는 로그인게이트 없이 샘플사 데이터(외국인 47명·90일내 만료 8·임금위반 3·서류미비 12)와 종합 리스크 '72/100·C등급', 만료알림 테이블, 전문가 티켓 3건, K-Trust 모듈이 렌더링됨.
  - 출처: https://plugnx-visaops.netlify.app/dashboard
- **라이브 사이트가 PROJECT.md가 금지한 'Plug&X' 및 폐기 코드네임 'VisaOps/Crew'를 전면에 노출 — 본문은 'VisaDesk'를 쓰지만 링크 도착지와 불일치한다(투자자 클릭 시 신뢰 훼손 리스크)** _(신뢰 high, 기준 2026-06-02)_
  - 근거: /workers·/dashboard 페이지가 'Plug&X VisaOps × Moneeback', 랜딩이 'PlugNX Crew'로 렌더링. 도메인도 plugnx-visaops.netlify.app(폐기 코드네임 VisaOps 포함). PROJECT.md 브랜딩 규칙: 'Plug&X 표기는 절대 쓰지 않는다', 제품명은 VisaDesk이며 코드네임 VisaOps·Crew는 폐기. 본문 §07 카드·lead는 올바르게 'VisaDesk'를 쓰므로 본문↔라이브 사이트 표기 불일치가 존재.
  - 출처: https://plugnx-visaops.netlify.app/workers
- **본문의 'B2B 25페이지 대시보드'는 실제 라이브 네비게이션상 약 20~22개 라우트로, 수치가 다소 과장 — 정확 카운트+기준일 표기 필요** _(신뢰 high, 기준 2026-06-02)_
  - 근거: 라이브 /dashboard 네비게이션 실측: 코어 8(대시보드/근로자/비자체크/서류함/리스크/티켓/리포트/K-Trust) + Moneeback 3(금융복지/급여적정성/환급출국) + 사업확장 9~11(전문가마켓/교육온보딩/비자쿼터/채용파이프라인/금융연계/다사업장/알림자동화/벤치마크/구독결제 등) = 합계 약 20~22개. 페이지 어디에도 '25페이지'를 명시하는 텍스트는 없음. → '25페이지'는 서브뷰·미노출 라우트 포함 추정치이거나 과대 표기.
  - 출처: https://plugnx-visaops.netlify.app/dashboard
- **'6개 언어' 다국어는 로드맵이지 라이브가 아니다 — 실제 가동 언어는 한·영·베 3개, 나머지(중·태·우즈벡)는 '확대 중'** _(신뢰 high, 기준 2026-06-02)_
  - 근거: 랜딩 '한국어·영어·베트남어를 기본 지원하며, 중국·태국·우즈베크 등 확대 중입니다'. /workers 언어 스위처도 한국어·영어·베트남어 3개만 노출. PROJECT.md는 Moneeback을 '6개 언어'로 기술하나 라이브 구현은 3개 → 본문이 '6개 언어 라이브'로 단정하면 검증 실패. '3개 언어 라이브 + 3개 확대 중(목표)'로 표기해야 정확.
  - 출처: https://plugnx-visaops.netlify.app/workers
- **핵심 AI 기능 'GPT-4V OCR'은 라이브 화면상 미구현 — /dashboard/documents는 OCR·여권/외국인등록증 자동인식이 없는 수동 상태 트래커다. 이것이 '제품 위험 검증됨' 주장의 최대 약점** _(신뢰 high, 기준 2026-06-02)_
  - 근거: /dashboard/documents는 서류 제출현황(총 282건: 제출 198·대기 54·수정필요 30)을 비자유형별 체크리스트와 상태아이콘(✅완료/❌미제출/⚠️만료임박/🔄검토중)으로 보여주는 '순수 문서 트래커'. 모든 상태가 수동 설정으로 보이며 여권 스캔·외국인등록증 인식·OCR·컴퓨터비전 자동분석 증거 없음. 본문 기술스택 카드의 'OpenAI(GPT-4V)'는 스택 나열일 뿐 라이브 기능으로 관측되지 않음. ForeignID L1~L3 인증·OCR 성숙도는 미검증 영역.
  - 출처: https://plugnx-visaops.netlify.app/dashboard/documents
- **환급 계산기 표시값(연금 520만·보험 180만·퇴직금 350만=1,050만)은 예시 평균치이며, 실제 환급액은 협정국·국적·납부이력·출국여부에 좌우되는 추정치임을 제품·본문 모두 고지해야 한다** _(신뢰 medium, 기준 2026-06-02)_
  - 근거: foreign-visa-kb/refund-system.md: '모든 금액은 추정치이며 확정액은 소관 기관 조회로만 확정', 국민연금 반환일시금은 '사회보장협정 체결국·상호주의 적용국' 국민만 청구 가능(국가별 상이). 라이브 /workers는 visa type·근무기간 입력 후 'AI 자동 계산'을 표방하나, 표시 평균(1,050만)을 개인 확정액처럼 오인시키면 안 됨. 99-synthesis도 '1,050만'은 산정범위·기준시점 명시 필요(국민연금 단일 시 1인 평균 약 870만)로 지적.
  - 출처: https://plugnx-visaops.netlify.app/workers
- **기술스택(Next.js 15·React 19·Tailwind 4·Supabase·OpenAI·Netlify)은 모두 2025~2026 기준 양산 안정 단계라는 본문 주장은 사실에 부합한다** _(신뢰 high, 기준 2026-06-02)_
  - 근거: Next.js 15는 안정 릴리스(React 19 지원·Turbopack dev 안정), React 19는 정식(2024.4.25 GA 후 생태계 안정화), Tailwind CSS v4는 2025 초 출시(빌드 약 5배·무설정). 셋 모두 2025 시점 production-ready로 확인 → '검증된 모던 스택' 표현 유효. 다만 '스택이 안정적'인 것과 '제품 핵심 기능(OCR·신용스코어)이 구현·검증됐다'는 별개임을 구분 표기 권고.
  - 출처: https://nextjs.org/blog/next-15
- **자가진단(9문항)→플랜 추천→리드 수집 깔때기는 라이브이나, 리드 캡처(이메일/전화) 단계가 화면상 명시적으로 확인되지 않아 'lead_submit_success 이벤트·/api/lead 가동'은 코드 레벨 추가 확인 필요** _(신뢰 medium, 기준 2026-06-02)_
  - 근거: 랜딩 자가진단은 9문항 클릭형·'0/9 문항 답변 완료' 카운터·'모든 문항에 답하시면 추천 결과가 표시됩니다'까지 라이브 확인. 그러나 결과 후 이메일/전화 제출(리드 캡처) 화면은 fetch에서 명시 확인되지 않음. 본문 '리드 수집 API /api/lead → Slack·Resend·콘솔 fallback'·이벤트(cta_click/diagnose_complete/lead_submit_success)는 코드/네트워크 호출 검증 전까지 'UI 라이브, 백엔드 연동은 확인 필요'로 한정 표기 권고.
  - 출처: https://plugnx-visaops.netlify.app/#diagnose

## 검증 결과

| 주장 | 판정 | 교정값 | 출처 | 비고 |
|---|---|---|---|---|
| 라이브 사이트 브랜딩이 PlugNX/VisaDesk 규칙을 준수한다 | ❌ refuted | 정면 위반 확인. /workers 헤더·푸터 'Plug&X VisaOps'·'© 2026 Plug&X × Moneeback', 랜딩 'PlugNX Crew', /dashboard 'Plug&X VisaOps', 도메인 plugnx-visaops.netlify.app(폐기 코드네임 VisaOps 포함). PROJECT.md L42 'Plug&X 절대 금지', L45 'VisaOps·Crew 폐기'. §07 본문은 'VisaDesk' 사용 → 본문↔링크도착지 불일치. IR 전 라이브 리브랜딩(Plug&X→PlugNX, VisaOps/Crew→VisaDesk, 도메인 교체) 필수. | https://plugnx-visaops.netlify.app/workers | 1차 확인된 가장 명확한 refuted. 투자자가 §07 'VisaDesk 라이브' 버튼 클릭 시 'Plug&X VisaOps'로 도착 → 신뢰 훼손. 최우선 정정 항목. |
| B2B 대시보드는 25페이지다 | 🟠 needs-update | 라이브 네비 실측 약 20~23개 라우트(코어8: 대시보드/근로자/비자체크/서류함/리스크/티켓/리포트/K-Trust + Moneeback3: 금융복지/급여적정성/환급출국 + 확장9~11: 전문가마켓/교육온보딩/비자쿼터/채용/금융연계/다사업장/알림자동화/벤치마크/구독결제 등). '25페이지'는 서브뷰 포함 추정치이거나 과대표기 → '핵심 라우트 약 20여 개(2026.6.2 기준)'로 보정. | https://plugnx-visaops.netlify.app/dashboard | 심화 베이스라인 확정. 라이브 어디에도 '25페이지' 명시 텍스트 없음(실측 네비 약 23개 항목·로그아웃/설정 제외 시 약 20). PROJECT.md는 '대시보드 25개 페이지'로 표기하나 라이브 카운트와 불일치 → 정확 카운트+기준일 병기 필요. |
| Moneeback은 6개 언어를 지원한다 (§07 '다국어 근로자 페이지') | 🟠 needs-update | 라이브 언어 스위처 3개(한국어·영어·Tiếng Việt). 랜딩 명문: '한국어·영어·베트남어를 기본 지원하며, 중국·태국·우즈베크 등 확대 중'. → '3개 언어 라이브 + 3개 확대 중(목표)'로 표기. ※ §07 본문 기능셀은 이미 '다국어(한·영·베)'로 정확히 기술 — '6개 언어'는 PROJECT.md SSOT(L16) 측 표현이므로 SSOT를 라이브 정합으로 보정 필요. | https://plugnx-visaops.netlify.app/workers | 주의: §07 HTML 본문은 '다국어(한·영·베)'로 정확. needs-update 대상은 PROJECT.md '6개 언어' 단정과 그를 인용하는 IR 진술. 라이브=3개. 1차 확인됨(스위처·랜딩 카피). |
| '제품 위험은 검증됨' (§07 타이틀 'MVP는 이미 라이브 — 제품 위험은 검증됨') | 🟠 needs-update | '제품 위험 일부 검증'으로 한정. 검증됨: UI·정보구조·고객 플로우(랜딩→자가진단→플랜, /workers 환급플로우, /dashboard 운영뷰)·모던 스택 안정성. 미검증: GPT-4V OCR·다국어 풀구현(라이브 3개)·환급 산정 정확도·ForeignID L1~L3 인증·리드 백엔드(/api/lead) 실가동·멀티테넌시. → 타이틀을 '제품·시장적합 위험 일부 검증'으로 완화 권고. | https://plugnx-visaops.netlify.app | '검증됨' 단정은 미검증 핵심기능을 포함하므로 과대. needs-update로 보정. 단 '라이브 MVP 존재' 자체는 경쟁사 대비 강한 차별점으로 유효. |
| 환급 평균 1,050만원(연금520·보험180·퇴직금350) | 🟠 needs-update | 라이브 /workers 표시값=평균 추정(국민연금520+고용보험180+퇴직금350=1,050만). 라이브에 면책 명문 존재: '본 서비스는 법무부와 무관하며, 환급 가능 여부를 보장하지 않습니다. 실제 환급액은 개인 상황에 따라 달라질 수 있습니다.' → IR/본문에도 '협정국·국적·납부이력·출국여부 의존 추정치, 산정범위·기준시점' 각주 필요. 국민연금 단일 시 1인 평균 약 870만(내부 99-synthesis) 병기 권고. | https://plugnx-visaops.netlify.app/workers | 라이브 면책 고지 존재는 가점(개인 확정액 오인 방지). 다만 평균을 개인 확정액처럼 보이게 하면 위험. PROJECT.md 공통원칙1·2(참고용·수치 변동) 정합. |
| GPT-4V OCR(여권·외국인등록증 자동인식)이 구현되어 있다 | 🟡 uncertain | /dashboard/documents는 순수 수동 상태 트래커(총 282건: 제출198·미제출54·수정필요30, 아이콘 완료/미제출/만료임박/검토중 모두 수동, 업로더 '김인사' 등 사람 기재). OCR·여권스캔·외국인등록증 인식·컴퓨터비전 증거 없음. §07 스택카드 'OpenAI(GPT-4V)'는 라이브 기능이 아닌 스택 나열로 한정 표기 → '핵심 AI(OCR·신용스코어) 구현 성숙도 미검증'. | https://plugnx-visaops.netlify.app/dashboard/documents | 1차 확인 안 됨 → supported 금지, uncertain(약함) 유지. 라이브 화면상 OCR 일절 미관측. ForeignID L1~L3 인증·환급 정확도와 함께 미검증 영역. §07 '구현 완료' 뉘앙스가 OCR까지 포함하면 과대표기. |
| 리드 수집 퍼널(자가진단 9문항→플랜추천→리드 캡처)이 백엔드까지 가동된다 (/api/lead, lead_submit_success 이벤트) | 🟡 uncertain | UI 라이브 확인(9문항·'0/9 문항 답변 완료'·'모든 문항에 답하시면 추천 결과가 표시됩니다'·플랜추천). 그러나 진단 완료 후 이메일/전화 리드캡처 폼이 화면상 명시 미관측, 다음 단계는 '자가진단으로 시작'·'8주 PoC' CTA로 연결. §07의 '리드 수집 API /api/lead → Slack·Resend·콘솔 fallback' 및 이벤트(cta_click/diagnose_complete/lead_submit_success)는 코드/네트워크 검증 전까지 'UI 라이브, 백엔드 연동 확인 필요'로 한정. | https://plugnx-visaops.netlify.app/#diagnose | 심화 confidence medium 반영. 1차(화면)로 백엔드 호출 미확인 → supported 금지, uncertain. 코드/네트워크 레벨 추가 검증 권고. |
| MVP가 라이브이며 핵심 기능이 가동 중이다 (랜딩·자가진단·/workers·/dashboard 접근성) | ✅ supported | 유지(supported). 단 '/dashboard는 로그인 게이트 없이 직접 접근, 단 샘플사(한성기공·김현수 팀장) 더미데이터로 렌더링'임을 명시 — 실제 인증/멀티테넌시 작동은 별개. | https://plugnx-visaops.netlify.app/dashboard | 1차 확인됨. 랜딩 '외국인 고용, 이렇게 단순해집니다'+9문항(0/9 카운터)+요금제 29/89/169/Enterprise, /workers 3단계 환급플로우+CTA '내 환급금 확인하기', /dashboard 외국인47·만료8·임금위반3·서류미비12·종합리스크 72/100 C등급·전문가티켓·K-Trust 모두 무로그인 렌더링. 라이브 주장 자체는 진실. |
| 기술 스택(Next.js15·React19·Tailwind4·Supabase·OpenAI·Netlify)은 양산 안정 단계다 | ✅ supported | 유지(supported). Next.js 15 안정 릴리스(React19 지원·Turbopack dev 안정), React 19 정식 GA 후 안정화, Tailwind v4 2025 출시 production-ready. → '검증된 모던 스택' 유효. 단 '스택 안정' ≠ '핵심 기능(OCR·신용스코어) 구현·검증'임을 구분 표기. | https://nextjs.org/blog/next-15 | 스택 성숙도는 공식 출처 일치로 supported. 다만 §07이 스택 안정성을 제품기능 검증으로 확장 인용하지 않도록 경계. |

## 본문 보완안
- **[문장] @ §07 Product / lead 문단 — '핵심 기능이 가동 중. B2B 25페이지 대시보드…구현 완료' 문장 교체**
  - plugnx-visaops.netlify.app에 핵심 기능이 실제로 가동 중입니다(2026.6 확인). 랜딩·9문항 자가진단·근로자 환급 페이지(/workers)·B2B 대시보드(/dashboard, 약 20여 개 관리 화면)가 로그인 없이 접근·동작하며, 샘플사 데이터로 리스크 점수(72/100·C등급)·만료 알림·전문가 티켓·K-Trust 모듈까지 렌더링됩니다. 즉 'UI·정보구조·고객 플로우' 차원의 제품 위험은 데모 가능한 수준으로 낮췄습니다. 다만 OCR 자동 서류인식·다국어 풀구현·환급 정확도 등 핵심 AI 기능은 아직 검증 대상으로 남아 있습니다.
- **[표] @ §07 Product / lead 또는 features 블록 하단 — '검증된 것 vs 남은 위험' 박스 신설(가장 중요한 보완)**
  - 제품 위험 — 검증된 것과 남은 것 (2026.6 라이브 점검) | 항목 | 상태 | 근거 | UI·정보구조·고객 플로우 | 검증됨 | 랜딩·자가진단·/workers·/dashboard 라이브 렌더링 | B2B 대시보드 화면 수 | 약 20여 개 라이브(본문 '25'는 보정) | 코어 8+Moneeback 3+확장 9~11 라우트 실측 | 다국어 | 부분 검증(3/6 라이브) | 한·영·베 라이브, 중·태·우즈벡 '확대 중' | 환급 계산기 | 라이브(예시 평균치) | 연금 520·보험 180·퇴직금 350=1,050만(추정·국적/협정국 의존) | GPT-4V OCR(여권·외국인등록증 자동인식) | 미검증 | /dashboard/documents는 수동 상태 트래커, OCR 미관측 | ForeignID L1~L3 인증·신용스코어 | 미검증 | 라이브 화면상 인증 플로우 비노출 | ※ 스택(Next.js15·React19·Tailwind4·Supabase·OpenAI·Netlify)은 양산 안정 단계이나, '스택 안정'과 '핵심 기능 검증'은 구분한다.
- **[문장] @ §07 Product / 표제 'MVP는 이미 라이브 — 제품 위험은 검증됨' 보정**
  - 부제 권고: 'MVP는 이미 라이브 — UI·고객 플로우 위험은 검증, 핵심 AI(OCR)·다국어·환급 정확도는 차기 검증 과제'. '제품 위험은 검증됨'을 무한정 단정하면 OCR 미구현·다국어 미완성이 드러날 때 신뢰가 역전됩니다.
- **[문장] @ §07 Product / features 블록 'Moneeback 환급' 셀 보정**
  - Moneeback 환급 — 연금·보험·퇴직금 30초 추정 체크(라이브, 한·영·베). 표시 금액(평균 1,050만원)은 예시 평균이며, 실제 환급액은 체류자격·국적·사회보장협정 체결 여부·납부이력·출국 여부에 따라 달라지는 추정치입니다. 확정액은 국민연금공단·근로복지공단 등 소관기관 조회로만 확인됩니다(참고용).
- **[문장] @ §07 Product / 기술 스택 카드 또는 lead 직전 — 브랜딩 불일치 시정 액션(내부 노트용, 본문 노출 여부는 총괄 판단)**
  - [운영 액션 — 본문 외부 또는 각주] 라이브 데모 사이트가 현재 'Plug&X VisaOps / PlugNX Crew' 및 도메인 visaops로 렌더링되어 PROJECT.md 브랜딩 규칙(Plug&X 금지·VisaDesk/PlugNX 통일·코드네임 VisaOps·Crew 폐기)과 불일치합니다. 투자자가 본문 링크를 클릭하면 본문(VisaDesk)과 도착지(Plug&X VisaOps)의 표기 괴리가 노출됩니다 → IR 전 사이트 카피·도메인 별칭을 PlugNX VisaDesk로 정정 권고.
- **[각주] @ §07 Product / 분석·운영 인프라 카드 보강**
  - ※ 리드 수집 API(/api/lead → Slack·Resend·콘솔 fallback)와 분석 이벤트(cta_click·diagnose_complete·lead_submit_success)는 설계상 가동 항목입니다. 자가진단·CTA UI는 라이브 확인됐으나, 실제 리드 캡처(이메일/전화 제출)와 백엔드 알림 연동은 네트워크·코드 레벨 추가 점검으로 최종 확인이 필요합니다(2026.6 기준 UI 라이브·백엔드 연동 확인 필요).
- **[각주] @ §07 Product / 섹션 말미 — 라이브 점검 출처·기준일 각주**
  - ※ 본 섹션의 라이브 상태·화면 수·기능 성숙도는 2026.6.2 plugnx-visaops.netlify.app(및 /workers·/dashboard·/dashboard/documents) 직접 접근 기준이며, 데모 사이트는 수시 업데이트됩니다. 스택 버전(Next.js 15·React 19·Tailwind CSS 4)의 양산 안정성은 각 공식 릴리스 기준입니다. 비자·환급·금융 판단은 법적 효력 없는 참고 정보이며 전문가 검증·최신 법령 확인이 필요합니다.

## 미해결
- /api/lead 리드 캡처·Slack/Resend 알림·분석 이벤트(diagnose_complete·lead_submit_success)의 실제 백엔드 동작은 UI만으로 확인 불가 — 네트워크 콜·코드 레벨 점검 필요
- GPT-4V OCR·ForeignID L1~L3 인증·외국인 신용스코어의 구현 단계(설계/프로토타입/라이브)를 내부 코드베이스·로드맵으로 확정 필요(공개 데모상 미노출)
- Supabase 백엔드·실데이터 vs 목업 데이터 여부 미확인 — /dashboard 샘플사 데이터가 하드코딩 시드인지 실 DB인지 코드 확인 필요
- '25페이지'의 정확한 정의(서브뷰·탭·미노출 라우트 포함 여부) 확정 후 본문 수치 동기화 필요
- 다국어 확대(중·태·우즈벡) 일정·환급 계산 정확도 검증(국가별 협정국 로직 반영 여부) 미확인
- 라이브 데모의 'Plug&X VisaOps/Crew' 표기·도메인 정정 일정 — IR 노출 전 시정 여부 확인 필요