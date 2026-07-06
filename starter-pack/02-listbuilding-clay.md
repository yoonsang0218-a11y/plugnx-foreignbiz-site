# 02 · 리스트빌딩 전략 + Clay Enrichment 워크플로 — 비수도권 제조 중소기업(E-9·E-7 다수 고용)

작성일: 2026-06-15 · 대상: VisaDesk 8주 PoC 영업 엔진 · 적용 스킬: `list-building` · `clay` · `clay-enrichment-9step` · `lead-sources-guide`

---

## 핵심 결론 (Answer-first)

1. **리드 소스는 "공개 채용공고 시그널"을 1순위 엔진으로 삼는다.** 워크넷·EPS 구인·잡코리아 등 공개 채용공고에서 "베트남어/태국어 가능, E-9, 외국인 가능, 기숙사 제공" 신호를 잡으면 **외국인 고용 식별 수율이 산단공·협회 회원사 명부 대비 3~5배 높다(추정).** 명부는 모집단(universe), 채용공고는 적격 신호(qualifier)로 역할 분리한다.
2. **개인정보 가드레일이 전략을 규정한다 — 한국은 미국식 "개인 이메일 스크래핑"이 불법 리스크.** 회사 대표메일(info@·hr@)·공개 채용 담당자만 수집하고, **개인 휴대폰/개인메일 스크래핑은 전면 금지.** 모든 행은 `source_url` 필수 보관, opt-out 즉시 처리.
3. **ICP 스코어 0~100점은 "외국인 규모 35점 + 준법 페인 25점 + 접근성 20점 + 핏 20점"** 가중치로 운영하고, **80점 이상만 Smartlead push.**
4. **Clay 9-step waterfall은 한국 데이터 환경에 맞춰 재배치** — 글로벌 이메일 파인더(Apollo/Prospeo) 커버리지가 한국 SMB에서 40% 미만(추정)이므로, **Claygent 회사 리서치 → 도메인 추론 → 패턴 이메일 + 단일 검증(MillionVerifier, $37/10K·99%+ [출처: list-building data-validation])** 조합으로 크레딧을 절약하고 바운스 <1%[출처: data-validation]를 맞춘다.
5. **이 문서가 팩 #10에 더하는 것:** 팩 #10 §8은 13컬럼 Clay 테이블·6-step 골격만 제시했다. 본 문서는 (a) 한국 합법 소스 12종 수율·비용·리스크 매트릭스, (b) 항목별 가중치가 명시된 100점 스코어링 룰, (c) 컬럼·공급자·조건식까지 박힌 9-step waterfall, (d) 즉시 붙여쓰는 Claygent 프롬프트 2종, (e) 국내법 가드레일을 **실행 가능 수준**으로 확장한다.

---

## 1. 전략 프레임 — 모집단 vs 적격 신호 (2-레이어 소싱)

리스트빌딩 실패의 대부분[가정]은 "명부 한 곳을 통째로 import → 외국인 고용 여부 모름 → 전수 enrichment로 크레딧 소진"에서 온다. `list-building` 마스터 원칙인 "Mix sources"(단일 소스로는 TAM 일부만, 다중 소스로 커버리지↑) [출처: list-building skill]를 한국 제조 SMB에 맞게 2레이어로 재구성한다.

```text
[레이어 A: 모집단 — 비수도권 제조 SMB 전수]
  산단공 입주기업 디렉토리 · 지방상의 회원사 · KOSIS 사업체 · 지자체 향토기업
        ↓ (회사 단위, source_url 보관)
[레이어 B: 적격 신호 — "이 회사가 외국인을 고용한다"는 증거]
  워크넷/EPS 공개 채용공고 · 잡코리아·사람인 다국어 공고 · 보도/홈페이지 "외국인 근로자"
        ↓ (외국인 고용 시그널 1개 이상 매칭된 회사만 enrichment 진입)
[레이어 C: Clay enrichment + ICP 스코어 → 80점+ 만 Smartlead]
```

핵심: **레이어 B를 통과한 회사만 Clay 유료 enrichment에 넣는다.** 레이어 A 전수를 enrichment하면 외국인 미고용 회사에 크레딧을 태운다. 이 게이트 하나가 Clay 크레딧을 60~70% 절약한다(추정).

---

## 2. (a) 합법적 리드 소스맵 — 수율·비용·개인정보/법적 리스크

> 라벨: 수율·비용·리스크는 모두 [추정] (실제 측정 전 1차안). 출처가 있는 사실만 [출처] 표기.
> 모든 소스 공통 원칙: **회사 단위 공개정보만 수집, `source_url` 필수 보관, 개인 식별정보(개인 휴대폰·개인메일) 스크래핑 금지.**

### 2.1 레이어 A — 모집단 소스 (비수도권 제조 SMB universe)

| # | 소스 | 무엇을 얻나 | 외국인 식별 수율 [추정] | 비용 | 개인정보/법적 리스크 | 수집 방식 |
|---|---|---|---|---|---|---|
| A1 | **한국산업단지공단(KICOX) 입주기업 디렉토리** (factoryon / 클러스터별 입주사) | 회사명·업종·주소·단지 | 낮음(고용여부 미표시) — 그러나 **비수도권 제조 모집단 정밀** | 무료(공개) | 낮음 — 회사 공개정보. 대량 자동수집 시 robots/이용약관 확인 | 페이지네이션 스크래핑 또는 공개 목록 export |
| A2 | **지방상공회의소 회원사 명부**(창원·구미·울산·여수·아산 등) | 회사명·업종·대표연락처 | 낮음 | 무료/일부 회원전용 | 낮음 — 단 회원전용 DB 무단수집 금지 | 공개 회원 디렉토리만 |
| A3 | **KOSIS 사업체 통계 / 통계청 사업체 DB** | 지역×업종×규모 사업체 수(집계) | N/A(개별기업 식별 불가) | 무료 [출처:KOSIS] | 없음(집계통계) | TAM 사이징·셀 우선순위용 |
| A4 | **공공데이터포털(data.go.kr) 사업장/공장등록 오픈데이터** | 공장등록현황·사업장명·소재지·업종코드 | 낮음 | 무료(오픈API) | 낮음 — 라이선스(이용허락범위) 준수 | 오픈API → Clay webhook import |
| A5 | **국세청 사업자등록 상태조회**(nts-business-registration) | 사업자번호 유효성·과세유형 | N/A(검증용) | 무료 | 없음 | enrichment 단계 사업자 유효성 검증 |
| A6 | **DART 공시기업**(opendart, 외감 이상) | 종업원수·재무·임원 | 중간(종업원수로 규모 필터) | 무료(오픈API) [출처:OpenDART] | 없음(공시정보) | 제조 중소기업은 대부분 비공시 → 커버리지 제한 |

### 2.2 레이어 B — 적격 신호 소스 (외국인 고용 증거)

| # | 소스 | 외국인 식별 시그널 | 수율 [추정] | 비용 | 개인정보/법적 리스크 | 비고 |
|---|---|---|---|---|---|---|
| B1 | **워크넷(work.go.kr) 공개 채용공고** | "외국인 가능", 직무·근무지, 기숙사, 교대 | **높음** | 무료(공개) | 중간 — 채용 담당자 개인정보가 아닌 **회사 대표연락처만** 수집. 자동수집은 이용약관·robots 확인 | 가장 강한 단일 신호 |
| B2 | **EPS(고용허가제) 구인·도입 관련 공개정보**(eps.go.kr) | E-9 고용허가 사업장 관련 공개 안내 | 높음(E-9 직격) | 무료 | 중간 — 사업장 개별 명단은 비공개일 수 있음(공개범위 확인 필요) | 개별 사업장 DB는 정부 비공개 → 추정 신호로만 |
| B3 | **잡코리아·사람인·알바몬 공개 채용공고** | 다국어 공고, "베트남어/태국어/네팔어 가능", "E-7-4", "외국인 환영" | **높음** | 무료(공개 표면) | 중간 — 공고의 회사 연락처만, 개인 이력서 DB 접근 금지 | 제조 생산직 다국어 공고 = 강신호 |
| B4 | **회사 홈페이지/보도자료/지역언론** | "외국인 근로자 OO명", "글로벌 인재", 다문화 행사 | 중간 | 무료 | 낮음 | Claygent로 회사 도메인 크롤 |
| B5 | **네이버 뉴스·지역지**(naver-news-search) | "외국인 고용 우수기업", 산단 외국인 관련 기사 | 중간 | 무료 | 낮음 | 보조 신호·세미나 타겟 발굴 |
| B6 | **세미나·협회 행사 opt-in 명단** | 본인 동의 제출 연락처 | 매우 높음(동의 기반) | 행사비 | **가장 낮음(동의 확보)** | §6.2 동의 가드레일 충족 — 최우선 합법 채널 |

### 2.3 소스 운영 룰 (80/20)

- **1차 가동 = B1(워크넷) + B3(잡코리아/사람인) + A1(산단공)** 3개 소스로 80% 커버. 나머지는 보강.
- **금지 소스(N): 개인 SNS 프로필 스크래핑, 이력서 DB, 개인 휴대폰 수집 서비스, 동의 없는 명함 데이터 구매.** → §6.2 레드라인.
- 모든 행에 `source_url` + `source_captured_date` 보관 → 30일 경과 시 재검증(B2B 데이터 decay 평균 약 2.1%/월·연 ~25% [출처: list-building data-validation]).

---

## 3. (b) 외국인 고용 식별 시그널 → ICP 스코어링 룰 (0~100)

`clay-enrichment-9step` Step 8(100점)과 `list-building` 가중 ICP를 한국 외국인 고용 맥락으로 재설계. **항목·가중치 명시, Tier A(80-100)만 즉시 outreach.**

### 3.1 외국인 고용 식별 시그널 사전 (Claygent/공고 파싱이 잡는 단서)

| 시그널 카테고리 | 구체 단서(키워드/패턴) | 강도 |
|---|---|---|
| 직접 비자 명시 | "E-9", "E-7", "E-7-4", "H-2", "E-8", "고용허가제", "특정활동" | 강 |
| 다국어 요건 | "베트남어/태국어/네팔어/인도네시아어/우즈벡어/몽골어 가능" | 강 |
| 외국인 직접 언급 | "외국인 근로자", "외국인 가능", "외국인 환영", "다문화" | 강 |
| 생산직 운영 단서 | "기숙사 제공", "3교대", "단순노무", "생산직 다수 채용" | 중 |
| 규모·업종 | 제조 표준산업분류(C), 종업원 10~300명, 비수도권 소재 | 중 |
| 준법 페인 단서 | "체류만료", "비자 연장", "고용변동 신고", "임금요건", "보험 가입" 언급/문의 | 중 |

### 3.2 ICP 스코어링 룰 — 0~100점, 항목·가중치

| 대분류 | 항목 | 배점 | 채점 기준 |
|---|---|---:|---|
| **① 외국인 고용 규모·확실성** | 외국인 고용 증거 강도 | 20 | 비자/다국어 직접명시 20 · 외국인 언급 14 · 생산직 단서만 8 · 추정뿐 0 |
| (소계 35) | 추정 외국인 수 | 15 | 30명+ 15 · 10~29명 11 · 5~9명 6 · <5명 0 |
| **② 준법 페인** | 준법 리스크 신호 수 | 15 | 만료/임금/신고/보험 단서 1개당 5점(상한 15) |
| (소계 25) | 비자 다양성(E-9+E-7 혼재 등) | 10 | 2종+ 10 · 1종 5 · 불명 0 |
| **③ 접근성** | 의사결정자 연락 가능성 | 12 | 검증 대표/HR 이메일 확보 12 · 대표메일만 7 · 없음 0 |
| (소계 20) | 채널 근접성 | 8 | 세미나/협회/파트너 접점 8 · 산단 동일권역 5 · 없음 2 |
| **④ 핏·수익성** | 지역·업종 핏 | 10 | 비수도권 제조 10 · 비수도권 비제조 6 · 수도권 제조 4 |
| (소계 20) | 플라이휠 적합(BackWon 연계) | 10 | 외국인 30명+ & 환급 모멘텀 추정 10 · 중간 6 · 낮음 2 |
| **합계** | | **100** | |

### 3.3 Tier 컷 & 액션 (`list-building` Tier 체계 + 한국 SMB 보정)

> 컷 라인은 [가정]이다. `list-building` 표준 컷은 A:90-100/B:70-89/C:50-69/D:<50 [출처: list-building skill]이나, 한국 비수도권 제조 SMB는 공개 데이터가 얕아 만점 도달이 어려우므로 80점=A로 **10점 하향 보정**했다(가동 후 응답률·전환율로 재보정).

| 점수 | Tier | 액션 | 회사당 컨택 수 |
|---|---|---|---|
| 80~100 | **A** | 즉시 Smartlead push + 대표/HR 멀티스레드 | 2~3 |
| 60~79 | **B** | 2차 nurture, 세미나 초대 우선 | 1~2 |
| 40~59 | **C** | long-term nurture(분기) | 1 |
| <40 | **D** | suppress(제외) | 0 |

### 3.4 Clay 스코어링 형식 (Clayscript, 0 크레딧)

스코어는 **AI가 아니라 Formula 컬럼으로 계산**(스킬 원칙: "Formulas cost 0 credits"). 각 시그널은 Claygent가 enum/숫자로 정규화한 뒤 가산:

```javascript
// Clay Formula 컬럼: icp_score (0 크레딧)
// 입력은 앞단 Claygent/파싱이 채운 정규화 필드
let s = 0;
const sig = {visa_explicit:20, foreigner_mention:14, prod_only:8, none:0};
s += sig[r.evidence_strength] ?? 0;                  // ①-1
s += r.worker_est>=30?15 : r.worker_est>=10?11 : r.worker_est>=5?6 : 0; // ①-2
s += Math.min(15, (r.compliance_signal_count||0)*5); // ②-1
s += r.visa_diversity>=2?10 : r.visa_diversity==1?5:0;// ②-2
s += r.dm_email_verified?12 : r.company_email?7:0;    // ③-1
s += r.channel=="event"?8 : r.channel=="cluster"?5:2; // ③-2
s += (r.region=="non_metro"&&r.is_mfg)?10 : (r.region=="non_metro")?6:4; // ④-1
s += r.flywheel=="high"?10 : r.flywheel=="mid"?6:2;   // ④-2
return s;
```

---

## 4. (c) Clay 9-Step Waterfall — 컬럼·공급자·크레딧 절약 로직

`clay-enrichment-9step`의 9단계를 한국 제조 SMB 환경에 맞춰 **공급자 재배치 + 조건식**으로 구현. 글로벌 이메일 파인더(Apollo/Prospeo/LeadMagic)는 한국 SMB 커버리지가 낮으므로(추정 <40%), **Claygent 회사 리서치 → 도메인 추론 → 패턴 이메일 → 단일 검증**을 메인 경로로 둔다.

### 4.1 단계별 매핑

| Step | 액션 | 한국향 공급자/방법 | 크레딧 절약 조건식 |
|---|---|---|---|
| 1 | Upload & Clean | A1/B1/B3 CSV·webhook import, 도메인 정규화 | 중복(도메인) dedupe 먼저 — `deduplicate` |
| 2 | Company Enrichment | **Claygent**(도메인·업종·소재지·종업원) + DART(opendart, 외감만) + 사업자검증(nts) | `if domain empty → skip`. DART는 외감 매칭 시만 |
| 3 | People(의사결정자) | Claygent 회사 홈페이지/공고에서 **대표·HR 직함만**, LinkedIn은 공개 회사페이지 한정 | 개인메일/개인폰 탐색 금지(§6.2) |
| 4 | **Email Waterfall** | **회사 패턴 이메일 생성**(info@·hr@·대표도메인) → Findymail(회사) → Apollo(보조) | 단계별 `if previous found → stop`. 회사 대표메일 우선이라 파인더 호출 최소화 |
| 5 | **Email Verification** | **MillionVerifier**($37/10K·99%+ [출처: list-building data-validation]) — valid/deliverable만 통과 | catch-all/unknown/role 분기 처리(§6) |
| 6 | Phone(선택) | 회사 대표 유선번호만(공개 디렉토리). **개인 휴대폰 enrichment 비활성** | 기본 OFF — 개인정보 리스크(§6.2) |
| 7 | Custom Data | **Claygent 리서치 프롬프트**(§5) — 외국인 규모·비자 추정 | 레이어 B 통과 행만 실행 |
| 8 | Scoring | §3.4 Formula 컬럼(0 크레딧) | AI 미사용 |
| 9 | Export | Tier A만 Smartlead/Instantly push, 나머지 Supabase 저장(재사용) | suppression 동기화 |

### 4.2 실제 Clay 테이블 컬럼 (팩 #10 §8의 13컬럼 → 확장)

> 팩 #10 컬럼은 유지하고 **enrichment·검증·거버넌스 컬럼을 추가**(중복 생성 아님, 운영 가능 수준 확장).

| 컬럼 | 타입 | 채우는 단계 | 비고 |
|---|---|---|---|
| company_name / website_domain / region / industry | text | 1~2 | 팩 #10 유지 |
| corp_reg_status | enum | 2 | nts 사업자 유효성(active/closed) |
| headcount_total | int | 2 | DART 또는 Claygent 추정 |
| foreign_worker_signal / visa_signal | text | 7 | 팩 #10 유지, Claygent가 근거 문장 |
| worker_est / evidence_strength | int/enum | 7 | 스코어 입력(정규화) |
| compliance_signal_count / visa_diversity | int | 7 | 스코어 입력 |
| decision_maker_title | text | 3 | 대표/HR/총무만 |
| final_email | email | 4 | 패턴+파인더 merge |
| email_status | enum | 5 | valid/risky/invalid/role |
| icp_score / tier | int/enum | 8 | Formula(0크레딧) |
| message_angle | enum | 8 | expiry/wage/document/expert/refund |
| source_url / source_captured_date | url/date | 1 | **필수**(거버넌스) |
| consent_basis | enum | 1 | public_business / event_optin / partner_referral |
| sequence_status | enum | 9 | queued/sent/replied/booked/disqualified |
| suppression_flag | bool | 9 | opt-out·bounce 즉시 true |

### 4.3 크레딧 절약 5대 로직 (스킬 Universal Principles 적용)

1. **레이어 B 게이트** — 외국인 신호 0인 행은 Step 7 유료 Claygent 미실행(가장 큰 절약).
2. **조건식 필수** — 모든 유료 enrichment에 `if field already filled → skip`. (스킬: "never run paid without checking").
3. **GPT-4 mini로 90%** — 회사요약·정규화는 mini, 외국인 규모 추론(§5)만 상위 모델.
4. **Formula 우선** — 스코어·도메인 정규화·이메일 패턴은 0 크레딧 Formula.
5. **소량 테스트 → 배치 실행** — 전체 실행 전 10~50행으로 검증(팩 #10 "10-row test"와 일치). 검증 후 배치 단위(약 250행[가정])로 확대.
6. **유료 데이터 저장** — Supabase에 적재해 재구매 방지(스킬: "never pay twice").

---

## 5. (d) Claygent 리서치 프롬프트 — 외국인 고용 규모·비자 추정

> 출력은 **JSON 고정**(스코어 입력 정규화). 추정은 반드시 `confidence`와 `evidence`(근거 문장+URL) 동반. 개인정보 추출 금지.

### 5.1 메인 프롬프트 — 외국인 고용 규모·비자 추정

```text
You are researching a Korean company to estimate its FOREIGN-WORKER employment for a B2B
compliance-SaaS targeting fit. Use ONLY public sources: the company website, public job
postings (워크넷/잡코리아/사람인), news, and association/industrial-complex pages.

DO NOT collect or output any individual's personal data (no personal phone, personal email,
resident/foreigner ID, passport). Company-level public info only. Always cite source URLs.

Company: {{company_name}}
Domain: {{website_domain}}
Region/Industry: {{region}} / {{industry}}

Assess and return ONLY this JSON:
{
  "foreign_employment": "yes" | "likely" | "unknown",
  "worker_est": <integer or null>,            // best estimate of foreign workers; null if unknown
  "worker_est_range": "<e.g. 10-29>" | null,
  "visa_types": ["E-9"|"E-7"|"E-7-4"|"H-2"|"E-8"...],   // mentioned or strongly implied
  "visa_diversity": <count of distinct visa types>,
  "evidence_strength": "visa_explicit" | "foreigner_mention" | "prod_only" | "none",
  "compliance_signals": ["expiry"|"wage"|"report"|"insurance"|"housing"...],
  "evidence": [ {"quote":"<short public snippet>","url":"<source url>"} ],
  "confidence": "high" | "medium" | "low"
}

Rules:
- If you cannot find foreign-employment evidence, set "foreign_employment":"unknown" and worker_est:null.
- Never fabricate numbers. Estimates must trace to a cited public snippet.
- Korean manufacturing SMBs hiring 생산직 with 다국어/기숙사/3교대 strongly imply E-9; flag as "likely".
```

### 5.2 보조 프롬프트 — 의사결정자(직함만) 식별

```text
From the company's PUBLIC website/about/contact and public job postings only, identify the
decision-maker FUNCTION for foreign-worker compliance. Output JOB TITLE/ROLE and a COMPANY
contact channel (info@/hr@/대표전화) ONLY. Never output a named individual's personal email
or mobile. Return JSON:
{ "decision_maker_title": "<대표|HR/총무|공장장|관리이사|unknown>",
  "company_email": "<role-based company email or null>",
  "evidence_url": "<url>" }
```

---

## 6. (e) 이메일 검증·바운스(<1%)·동의/개인정보 가드레일

### 6.1 검증 파이프라인 (data-validation 적용, 바운스 <1% 목표)

| 단계 | 처리 | 도구/기준 |
|---|---|---|
| 발송 전 100% 검증 | 전 리스트 캠페인 직전 검증 | **MillionVerifier $37/10K·99%+** [출처: list-building data-validation] (catch-all/disposable/role 탐지) |
| 결과 분류 | valid→발송 · invalid→즉시제거 · risky/catch-all→보류 또는 대체 · role(info@,hr@)→**B2B 특성상 조건부 허용**[가정](표준 권고는 role 메일 skip [출처: data-validation]이나 한국 SMB는 대표메일이 실채널이므로 보정) | data-validation 카테고리 |
| 바운스 핸들링 | soft 3회 재시도→hard 전환 · hard 즉시 suppression·재발송 금지·소스 품질 플래그 | 바운스 워크플로 [출처: data-validation] |
| 리스트 위생 | 발송 전 매번 검증 · 주간 바운스 모니터 · 30일 경과 재검증(decay 약 2.1%/월 [출처: data-validation]) | 위생 스케줄 |

**KPI 가드(danger zone):** 바운스 <1%(>3% 즉시 중단) · 스팸신고 <0.1% · 딜리버러빌리티 95%+ [출처: list-building data-validation].
**인프라:** 본사 primary 도메인 발송 금지 — 별도 warmed outreach 도메인(팩 #10 §9과 일치).

### 6.2 동의·개인정보 가드레일 (국내법 유의 — 개인 스크래핑 금지)

> 참고용 정리이며 법적 효력 없음. 실제 적용 전 변호사·개인정보 전문가 검증 필수.

| 레드라인 | 규칙 |
|---|---|
| **개인정보 스크래핑 금지** | 개인 휴대폰·개인 이메일·SNS 프로필·이력서 DB 수집 금지. **회사 공개 대표연락처(info@/hr@/대표전화)만.** |
| **영리목적 광고성 정보(정보통신망법)** | 영리 광고성 전송 시 사전 수신동의·야간 제한·수신거부 표기 등 의무 고려. cold B2B는 **회사 업무용 채널 + 즉시 opt-out** 전제로 보수적 운용, 발송 전 법률 검토. |
| **수집 근거 라벨** | `consent_basis` 컬럼: public_business(공개 사업자정보) · event_optin(동의) · partner_referral(동의기반 추천)만 허용. |
| **목적·보관** | 영업 목적 외 사용 금지, 보관기간 설정, opt-out 시 즉시 suppression + 글로벌 억제 리스트. |
| **민감정보 절대 금지** | 외국인등록번호·여권번호·계좌·생체정보는 리드 데이터에 **수집·저장·예시 금지**. |
| **최우선 합법 채널** | B6 세미나/협회 opt-in = 동의 확보된 가장 안전한 소스 → 비중 확대. |

---

## 7. 8주 PoC 실행 연결 (팩 #10 퍼널과 정합)

- **목표 정합:** **PoC/LOI 15사 · 3,300만원 [SSOT]** (PROJECT.md). 퍼널 상단 수치 — 타깃 계정 400 · 검증 연락처 240 — 은 SSOT가 아니라 **팩 #10 GTM 플랜의 목표치 [출처: 팩 #10 §4]**다.
- **본 엔진 기여:** 레이어 A 모집단 800~1,000사[가정] → 레이어 B 신호 게이트 → Tier A 80점+ 약 240사[가정](팩 #10 검증 연락처 목표와 정렬) → Smartlead.
- **주차 연결:** W1 테이블·스코어링 셋업(팩 #10 1주차) → W3·W6 outbound wave에 Tier A 공급 → W4·W7 세미나 opt-in(B6)으로 동의 리드 보강.
- **플라이휠:** Tier A(외국인 30명+) = BackWon 자동유입(전환 60%+·CAC 0) [SSOT] 잠재 최대 셀 → `message_angle=refund` 우선.

---

## 8. 이 문서가 팩 #10 §8에 더한 것 (중복 회피 명시)

| 항목 | 팩 #10 §8 | 본 문서 추가분 |
|---|---|---|
| 소스 | 5개 나열 | **12종 매트릭스 + 수율·비용·리스크 + 2-레이어 게이트** |
| 스코어 | "icp_score 0-100" 컬럼만 | **항목·가중치 명시 100점 룰 + 0크레딧 Formula** |
| 워크플로 | 6-step 골격 | **9-step waterfall + 공급자 재배치 + 5대 크레딧 절약 조건식** |
| 프롬프트 | scoring 프롬프트 1개 | **Claygent 외국인 규모·비자 추정 + 의사결정자 식별 2종(JSON 고정)** |
| 거버넌스 | "동의 기반·개인 스크래핑 회피" 한 줄 | **국내법 레드라인 표 + consent_basis 컬럼 + 검증 KPI 가드** |

---

## 참고·한계 (Caveats)

- 본 산출물은 **사업 운영 참고자료**이며 법적 효력이 없다. 외국인 고용 식별·비자 추정·채용공고 해석은 모두 [추정]이며, 비자 자격·고용 준법·개인정보·정보통신망법(영리 광고성 정보 전송) 적용은 **행정사·노무사·변호사·개인정보 전문가의 최신 1차 출처 검증**이 필요하다.
- 수율·비용·전환 수치는 측정 전 1차 가정([추정])이다. 실제 가동 후 소스별 수율·바운스·답장률로 재보정한다(30일 재검증 원칙).
- **개인정보 레드라인:** 개인 휴대폰·개인 이메일·이력서 DB·SNS 프로필 스크래핑 금지. 회사 공개 대표연락처만 수집하고, 외국인등록번호·여권번호·계좌·생체정보는 수집·저장·예시 어디에도 남기지 않는다.
- EPS 사업장 개별 명단, 채용공고 자동수집 등은 각 사이트 **이용약관·robots·공개범위**를 발송 전 확인한다. 동의 기반(세미나 opt-in·파트너 추천)을 최우선 채널로 운용한다.
- SSOT 수치(체류외국인 약 278.3만 명, 요금제, PoC 목표 15사/3,300만원, TAM B2B 49만·B2C 216만)는 PROJECT.md 정본을 따른다. 바뀌면 정본을 먼저 갱신한다. 정밀 인구수(2025년 말 2,783,247명)는 정본의 반올림값(278.3만)을 뒷받침하는 1차 통계 [출처: 법무부 출입국·외국인정책 통계, 팩 #10 §1 재인용]이다.
