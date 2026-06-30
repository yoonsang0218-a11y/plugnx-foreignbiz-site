# WS16 — BackWon 실제 구축 기능상세서

> 작성 기준일: 2026-06-30 KST
> 연결 문서: `15-a-to-z-worker-service-blueprint.md`
> 목적: BackWon을 실제 제품으로 만들 때 필요한 유저플로우, 환급연계, 금융레이어, 데이터/동의/보안 요구사항을 개발 가능한 수준으로 정의한다.
> 사용 스킬: `moneeback-refund` · `foreignid-auth` · `foreign-visa-kb` · `pm-execution:create-prd`
> 면책: 비자·노무·세무·법률·금융 판단은 법적 효력 없는 참고 정보다. 제품화 전 행정사·노무사·세무사·변호사·금융규제 전문가 검토와 최신 1차 출처 확인이 필요하다.

---

## 1. Summary

BackWon은 외국인 재직자와 구직자가 한국에서 필요한 **구직·신원·체류·재직·급여·보험·환급·금융 준비**를 한 곳에서 관리하는 서비스다. 직접 환급 대행이나 신용점수 산출이 아니라, 사용자에게는 무료에 가까운 정리/체크/라우팅을 제공하고, 그 결과로 생기는 본인 동의 기반의 **점수 없는 신용 보강 리포트**를 금융권에 제공한다.

구축 범위는 3개 레이어로 나눈다.

1. **User App**: 외국인 재직자용 BackWon Passport
2. **Decision & Document Engine**: 환급 가능성, 급여 적정성, 금융 준비도, 레드플래그 판정
3. **Partner Layer**: CB/은행/카드/보험/송금사 조회 API와 전문가/공식기관 라우팅

### 1.1 Value-First Product Principle

제품 우선순위는 금융권 수익이 아니라 외국인 개인 가치다.

```text
외국인 재직자·구직자 가치
→ 사업자 운영·복지 가치
→ 신뢰 가능한 Work Passport 데이터
→ 금융권/CB 신호 리포트 수익
```

따라서 MVP도 "금융권에 팔 데이터"를 먼저 설계하지 않는다. 외국인이 매월 돌아와 서류와 급여, 체류상태를 업데이트할 만큼 실질 가치가 있는 기능을 먼저 만든다.

---

## 2. Contacts

| 역할 | 담당 | 코멘트 |
|---|---|---|
| Product Owner | PlugNX BackWon | 전체 범위·우선순위·릴리즈 책임 |
| Compliance Owner | 외부 법무/금융규제 자문 | 신용정보법, 개인정보보호법, 전자금융, 자격사법 검토 |
| Domain Reviewer | 행정사/노무사/세무사/변호사 | 비자·노무·세무·법률 문구와 라우팅 기준 검토 |
| Engineering Lead | PlugNX 개발 | Next.js, Supabase, OCR, API, 보안 구현 |
| Data Partner Lead | 금융권/CB 제휴 | 리포트 필드, 과금, 조회 동의, 파일럿 검증 |

---

## 3. Background

### 3.1 왜 지금인가

외국인 근로자는 EPS, 국민연금공단, 하이코리아, 정부24, 고용센터, 보험사 등 공식 경로가 이미 있어도 실제로는 다음 병목에 막힌다.

- 한국어와 행정 용어를 이해하기 어렵다.
- 본인이 대상자인지 판단하기 어렵다.
- 서류를 잃어버리거나 최신 상태로 유지하지 못한다.
- 출국, 이직, 체류만기, 급여지연처럼 중요한 시점을 놓친다.
- 은행/카드/대출 심사에서는 thin-file로 취급되어 재직·소득을 충분히 증명하지 못한다.

BackWon은 공식기관을 대체하지 않는다. 공식기관으로 보내기 전에 **내 상태를 정리하고, 필요한 서류를 모으고, 금융권이 이해할 수 있는 신호로 번역**한다.

### 3.2 제품 원칙

| 원칙 | 설명 |
|---|---|
| 직접 대행보다 라우팅 | 신청/신고/소송/세무 대행이 아니라 체크, 증빙 패키지, 공식 경로 안내 |
| 무료 유저 경험 우선 | 하단 유저에게 과금하면 데이터 축적이 줄어든다 |
| 점수 없는 금융 신호 | 신용점수/등급 대신 원천 신호와 최신성 제공 |
| 동의 기반 제공 | 금융권·전문가·공식기관 제공은 목적별 동의 후 진행 |
| 최소 수집 | ForeignID L0-L3 step-up 구조로 필요한 순간에만 민감정보 수집 |
| 다국어 기본 | 쉬운 한국어 + 6개 언어 번역을 기본 UX로 설계 |

---

## 4. Objective

### 4.1 제품 목표

BackWon MVP의 목표는 환급 수수료 매출이 아니다. 외국인 재직자·구직자가 자발적으로 증빙을 쌓고 매월 갱신할 만큼 유용한 **Work Passport**를 만들고, 그 결과 금융권이 유료로 조회할 만한 **재직·소득·체류·보험 신호 DB**를 만드는 것이다.

### 4.2 Key Results

| 구분 | KR | 파일럿 목표 |
|---|---|---:|
| 첫 가치 | 가입 후 첫 유용한 결과 도달 | 10분 이내 |
| 유저 획득 | 초대/방문 대비 가입률 | 30%+ |
| 인증 | ForeignID L1 완료율 | 70%+ |
| 증빙 | 급여·재직·체류 중 2종 이상 업로드율 | 40%+ |
| 환급 | 환급 체크리스트 생성률 | 35%+ |
| 금융 | Readiness Report 생성률 | 30%+ |
| 동의 | 금융권 제공 opt-in율 | 20%+ |
| 파트너 | 금융권/CB 유료 PoC | 1곳 이상 |
| 반복 | 월 1회 이상 정보 갱신률 | 25%+ |

---

## 5. Market Segments

| 세그먼트 | 문제 | MVP 우선순위 | 요구 인증 |
|---|---|---:|---|
| 외국인 구직자 | 지원 가능 직무, 필요서류, 안전한 사업장, 입사 전 증빙 | 0 | L0-L2 |
| E-9 제조·농축산·어업 재직자 | 급여, 보험, 환급, 출국정산, 송금, 금융접근 | 1 | L1-L3 |
| H-2 방문취업 동포 | 보험, 체류지 신고, 노동분쟁, 금융접근 | 2 | L1-L3 |
| E-7/E-7-4 전환 희망자 | 장기체류, 경력증빙, 재직·소득 안정성 증명 | 3 | L2-L3 |
| E-8 계절근로 | 단기 출국정산, 보험, 반복 입국 | 4 | L1-L2 |
| F계열 재직 외국인 | 금융상품 접근, 증빙 패키지 | 5 | L2-L3 |

---

## 6. Value Propositions

### 6.1 외국인 재직자

| Job | 제공 가치 |
|---|---|
| 내가 받을 돈이 있는지 알고 싶다 | 국민연금, 퇴직금, 출국만기보험, 귀국비용보험, 고용보험 가능성 체크 |
| 은행에서 거절되지 않고 싶다 | 재직·급여·체류·보험 증빙을 묶은 금융 준비도 리포트 |
| 회사나 기관에 설명하기 어렵다 | 다국어 상태 설명, 증빙 패키지, 상담 전 intake |
| 체류·주소·출국 일정을 놓치고 싶지 않다 | D-day 알림, 공식기관 링크, 해야 할 일 자동 생성 |

### 6.2 외국인 구직자

| Job | 제공 가치 |
|---|---|
| 내가 지원할 수 있는 일을 알고 싶다 | 비자별 취업 가능 범위와 필요서류 체크 |
| 위험한 일자리나 불리한 계약을 피하고 싶다 | 채용공고·계약서 위험 키워드와 급여 조건 체크 |
| 좋은 일자리에 더 빨리 지원하고 싶다 | 다국어 경력 프로필, 교육·자격 기록, 서류 패키지 |
| 입사 후 금융 접근을 준비하고 싶다 | 첫 급여부터 재직·소득 증빙이 쌓이는 Work Passport |

### 6.3 사업자

| Job | 제공 가치 |
|---|---|
| 외국인 직원 온보딩을 줄이고 싶다 | 직원 self-service 서류 월렛과 다국어 안내 |
| 체류·서류·보험 누락을 줄이고 싶다 | 직원별 완료율과 위험 플래그 |
| 직원에게 월급 외 복지를 주고 싶다 | 금융 준비도, 환급/정산 안내, 생활 안정 도구 |
| 좋은 구직자를 선별하고 싶다 | Job Passport 기반 서류 완성도와 준비도 |

### 6.4 금융권/CB

| Job | 제공 가치 |
|---|---|
| 외국인 thin-file 리스크를 줄이고 싶다 | 자행 계좌 밖의 재직·소득·체류·보험 신호 조회 |
| 심사에 쓸 수 있는 최신 증빙이 필요하다 | 최신성, 출처, 사용자 동의, 문서 원본성 플래그 |
| 직접 외국인 데이터를 모으기 어렵다 | BackWon Passport 기반 opt-in 데이터 파이프라인 |

### 6.5 전문가/공식기관

| Job | 제공 가치 |
|---|---|
| 상담 전 상황 파악 시간이 길다 | 다국어 intake와 증빙 패키지 |
| 같은 질문을 반복해서 받는다 | 공식기관 라우팅과 체크리스트로 단순 문의 감소 |

---

## 7. End-to-End User Flow

### 7.1 전체 플로우

```text
초대/유입
→ 언어 선택
→ L0 가입
→ 핵심 가치 카드 노출
→ ForeignID L1 인증
→ 내 상태 입력
→ 서류/급여/보험 업로드
→ 환급 체크 + 금융 준비도 생성
→ 부족 서류 안내
→ L2/L3 step-up
→ 금융권 제공 동의
→ 파트너 조회/API 제공
→ 공식기관/전문가/금융사 라우팅
→ 월간 갱신 리마인드
```

### 7.2 온보딩 플로우

| Step | 화면 | 사용자 행동 | 시스템 처리 | 성공 기준 |
|---|---|---|---|---|
| 1 | 언어 선택 | 모국어 선택 | `preferred_language` 저장 | 선택 완료 |
| 2 | 가치 선택 | 받을 돈, 금융준비, 서류관리 중 관심사 선택 | 첫 대시보드 우선순위 결정 | 관심사 1개 이상 |
| 3 | L0 가입 | 이메일/소셜/휴대폰 중 하나 | 약관·기본 동의 저장 | 계정 생성 |
| 4 | L1 인증 | 여권+셀카 제출 | OCR, MRZ, 라이브니스, 얼굴대조 | L1 pass 또는 재시도 |
| 5 | 상태 입력 | 국적, 비자, 직장, 급여, 출국예정 입력 | `profile_completeness` 산출 | 60% 이상 |
| 6 | 첫 할 일 생성 | 대시보드 확인 | 체류, 급여, 보험, 환급, 금융 카드 생성 | 할 일 3개 이상 |

### 7.3 환급연계 플로우

```text
환급 체크 시작
→ 국적·비자·가입이력·재직기간·출국예정 입력
→ 항목별 가능성 판정
→ 추정액 범위 또는 "확인 필요" 표시
→ 필요한 증빙 체크리스트 생성
→ 공식기관 링크/연락처 제공
→ 유저가 신청 진행상태 기록
→ 완료/보류/불가 사유 저장
```

| 항목 | 입력 | 판정 | 출력 | 공식 경로 |
|---|---|---|---|---|
| 국민연금 반환일시금 | 국적, 가입 여부, 출국 사유, 납부 이력 | 사회보장협정/상호주의 + 가입이력 + 지급 사유 | 가능성, 필요서류, NPS 확인 안내 | 국민연금공단 |
| 퇴직금 | 재직기간, 급여, 근무시간, 퇴직 여부 | 1년 이상, 주 15시간 이상, 평균임금 | 추정액 범위, 체불 신호 | 고용노동부/노무사 |
| 출국만기보험 | E-9/H-2 여부, 사업주 가입, 출국/사업장변경 | EPS 보험 가입 여부 | 보험금 확인 체크 | EPS/보험사 |
| 귀국비용보험 | EPS 가입 여부, 본인 납입 | 본인 납입 이력 | 환급 가능성 | EPS/보험사 |
| 고용보험 | 체류자격, 가입여부, 이직 사유 | 가입·수급 요건 | 확인 필요 또는 가능성 | 고용센터 |

**중요 UX 문구**

- "예상액은 추정입니다. 확정액은 국민연금공단·고용센터·보험사 조회로만 확인됩니다."
- "BackWon은 신청을 대행하지 않습니다. 필요한 서류와 공식 경로를 정리합니다."
- "퇴직금과 출국만기보험은 중복 수령이 아니라 차액 정산될 수 있습니다."

### 7.4 금융레이어 플로우

```text
금융 준비도 보기
→ 부족 신호 안내
→ 급여명세/입금내역/재직/체류/보험 증빙 업로드
→ L2 또는 L3 step-up
→ 점수 없는 Readiness Report 생성
→ 금융권 제공 목적별 동의
→ 파트너가 리포트 조회
→ 조회 로그와 철회 경로 제공
```

| Step | 사용자 화면 | 시스템 산출 | 파트너 제공 여부 |
|---|---|---|---|
| 1 | 금융 준비도 홈 | missing docs list | 없음 |
| 2 | 증빙 업로드 | OCR 필드, 원본성/최신성 플래그 | 없음 |
| 3 | 리포트 미리보기 | scoreless report snapshot | 사용자만 |
| 4 | 제공 동의 | partner_access_grant | 선택 파트너만 |
| 5 | 파트너 조회 | partner_query_log | 동의 범위 내 제공 |
| 6 | 철회/만료 | grant revoked/expired | 이후 조회 차단 |

---

## 8. Functional Requirements

### 8.1 F0. 다국어·약관·동의 기반

| 항목 | 상세 |
|---|---|
| 목적 | 하단 유저가 이해 가능한 언어로 가입·동의·결과 확인 |
| 기능 | 언어 선택, 쉬운 문장 모드, 약관/개인정보/고유식별정보/생체/금융제공 분리동의 |
| 입력 | 언어, 국가, 약관 동의, 목적별 동의 |
| 출력 | `user_locale`, `consent_scope`, `consent_version` |
| 예외 | 동의 철회 시 해당 목적 데이터 제공 중단 |
| Acceptance | 동의 항목별 버전, 시각, IP/기기 요약, 철회 이력이 감사로그에 남는다 |

### 8.2 F1. ForeignID 인증

| 레벨 | 필요 기능 | 허용 행위 |
|---|---|---|
| L0 | 계정 생성, 기본 약관 | 공개 콘텐츠, 기본 체크 시작 |
| L1 | 여권 OCR, MRZ 검증, 셀카 라이브니스, 얼굴대조 | 개인화 대시보드, 기본 환급 체크 |
| L2 | ARC OCR, 체류자격/만료일 추출, 통신 본인확인 | 체류 기반 서비스, 금융 준비도 상세 |
| L3 | 본인 명의 계좌 확인, 전자서명 | 금융권 제공 동의, 환급 수령 계좌 등록, 전자계약 |

**Acceptance**

- 각 인증 단계는 `pass`, `retry`, `manual_review`, `failed` 상태를 가진다.
- 문서번호, 외국인등록번호, 계좌번호는 평문 로그에 남지 않는다.
- L3 행위는 L1/L2가 유효해야 가능하다.

### 8.3 F2. 홈 대시보드

| 카드 | 표시 정보 | CTA |
|---|---|---|
| 오늘 해야 할 일 | 체류만기, 급여명세, 보험, 환급, 금융 준비 | 상세 보기 |
| 내 돈 | 급여, 송금, 보험, 환급 가능성 | 업데이트 |
| 내 서류 | 신분, 재직, 급여, 보험, 주거 | 업로드 |
| 금융 준비도 | 신원, 체류, 소득, 보험, 부족서류 | 리포트 보기 |
| 도움받기 | 공식기관, 전문가, 긴급상황 | 연결 |

**Acceptance**

- 신규 유저는 할 일 3개 이상을 본다.
- 각 카드에는 `complete`, `needs_update`, `missing`, `red_flag` 상태가 있다.
- 사용자가 무슨 행동을 해야 하는지 1개 CTA로 끝나야 한다.

### 8.4 F3. Document Wallet

| 문서 | OCR 필드 | 유효성 |
|---|---|---|
| 여권 | 성명, 국적, 생년월일, 만료일, MRZ | 만료/형식/얼굴대조 |
| ARC | 성명, 체류자격, 만료일, 외국인등록번호 마스킹 | 만료/교차일치 |
| 근로계약서 | 회사, 직무, 기간, 임금, 근로시간 | 서명/날짜/임금 필드 |
| 급여명세서 | 지급월, 총급여, 공제, 실수령 | 월별 연속성 |
| 입금내역 | 입금일, 금액, 입금자 | 급여명세와 매칭 |
| 보험/NPS 증빙 | 가입 여부, 납부/적립 힌트 | 최신성 |
| 주거/월세 | 주소, 계약기간, 월세/보증금 | 체류지 일치 |

**Acceptance**

- 모든 문서는 `source`, `uploaded_at`, `extracted_at`, `freshness`, `confidence`를 가진다.
- OCR 신뢰도 미달 시 사용자 정정 UI와 수기 검토 큐가 열린다.
- 파트너에게는 원본 전체가 아니라 동의된 필드와 플래그만 제공한다.

### 8.5 F4. Refund Check Engine

| 기능 | 상세 |
|---|---|
| 항목별 판정 | 국민연금, 퇴직금, 출국만기보험, 귀국비용보험, 고용보험 |
| 가능성 등급 | 높음, 조건부, 낮음, 확인 필요 |
| 추정액 | 범위로 표시. 공단/보험사 조회 전 확정 금액 금지 |
| 체크리스트 | 필요서류, 공식기관, 예상 순서, 유의문구 |
| 상태관리 | not_started, checking, ready_to_apply, submitted_by_user, paid, blocked |

**Acceptance**

- 국적이 없으면 국민연금 반환일시금 가능성을 확정하지 않는다.
- EPS 여부가 없으면 출국만기보험/귀국비용보험을 확정하지 않는다.
- 퇴직금과 출국만기보험 관계는 "중복 수령 아님" 안내를 표시한다.
- 모든 결과에 "추정/확인 필요" 라벨이 붙는다.

### 8.6 F5. Wage Adequacy Engine

| 기능 | 상세 |
|---|---|
| 최저임금 체크 | 해당 연도 최저임금은 설정값으로 관리, 하드코딩 금지 |
| 급여 연속성 | 최근 3개월 급여명세/입금내역 매칭 |
| 공제 위험 | 숙식비, 식비, 기타공제 과다/불명확 플래그 |
| 체불 신호 | 지급지연, 일부지급, 명세서-입금 불일치 |
| 라우팅 | 노동청/노무사 안내, 상담 전 패키지 생성 |

**Acceptance**

- "위법 확정" 표현을 쓰지 않는다.
- 위험 플래그와 근거 문서를 함께 보여준다.
- 사용자에게 회사와 공유할지 여부를 별도 선택하게 한다.

### 8.7 F6. Financial Readiness Report

| 섹션 | 필드 | 점수화 여부 |
|---|---|---|
| Identity | verified_level, document_freshness | 점수 아님 |
| Stay | visa_type, months_to_expiry, address_match | 점수 아님 |
| Employment | employer_verified, employment_duration, contract_verified | 점수 아님 |
| Income | salary_continuity_3m, income_volatility, payslip_bank_match | 점수 아님 |
| Contribution | pension/insurance evidence flags | 점수 아님 |
| Stability | residence_duration, rent_burden, remittance_ratio | 점수 아님 |
| Flags | missing_docs, red_flags, expired_docs | 점수 아님 |

**Acceptance**

- 리포트는 `score`, `grade`, `rank`, `approval probability`를 제공하지 않는다.
- 각 필드는 출처와 최신성을 가진다.
- 파트너 조회용 snapshot은 생성 후 변경되지 않고 버전이 남는다.

### 8.8 F7. Partner API

| API | 설명 | 요구 인증/동의 |
|---|---|---|
| `POST /partner/report-requests` | 금융사 조회 요청 생성 | 파트너 인증 |
| `GET /users/{id}/readiness-report` | 동의된 리포트 조회 | 사용자 동의 + L2/L3 |
| `POST /users/{id}/consents` | 제공 동의 생성/갱신 | 사용자 인증 |
| `DELETE /users/{id}/consents/{grant_id}` | 제공 철회 | 사용자 인증 |
| `GET /partner/query-logs` | 조회 로그 확인 | 파트너/관리자 |

**Acceptance**

- 파트너는 동의 범위 밖 필드를 조회할 수 없다.
- 모든 조회는 `partner_id`, `purpose`, `fields`, `timestamp`, `result`를 남긴다.
- 동의 만료 또는 철회 후 API는 403을 반환한다.

### 8.9 F8. Help Router & Expert Workspace

| 기능 | 상세 |
|---|---|
| 레드플래그 분류 | 체류만기, 임금체불, 산재, 세무, 고액 주거분쟁, 출국 D-30 |
| 공식기관 우선 | 하이코리아, NPS, EPS, 고용노동부, 고용센터, 보험사 |
| 전문가 디렉토리 | 노무사, 세무사, 행정사, 변호사 |
| 상담 전 intake | 유저가 직접 전달할 증빙 패키지 생성 |
| 과금 경계 | 수임 성공보수/소개료가 아닌 광고/디렉토리/SaaS 월정액 검토 |

**Acceptance**

- 법률/세무/노무 판단을 확정적으로 말하지 않는다.
- 전문가 연결은 사용자가 직접 선택한다.
- 전문가에게 제공되는 정보는 별도 동의와 최소 필드 원칙을 따른다.

### 8.10 F9. Notification & Retention

| 트리거 | 알림 |
|---|---|
| 체류만기 D-90/D-30/D-7 | 하이코리아/출입국 예약 안내 |
| 월급일 + 3일 | 급여명세/입금내역 업로드 요청 |
| 출국예정 D-90/D-30 | 환급 체크리스트 |
| 문서 만료 | 재제출 요청 |
| 금융 리포트 30일 경과 | 최신화 요청 |
| 파트너 조회 발생 | 조회 알림과 철회 링크 |

**Acceptance**

- 알림은 언어별로 제공한다.
- 민감 정보는 푸시/문자 본문에 노출하지 않는다.
- 사용자는 알림 채널과 빈도를 조정할 수 있다.

---

## 9. Data Model

### 9.1 핵심 테이블

| 테이블 | 목적 | 주요 필드 |
|---|---|---|
| `users` | 계정 | id, locale, nationality, created_at |
| `identity_verifications` | ForeignID 상태 | user_id, level, status, expires_at, evidence_refs |
| `consents` | 목적별 동의 | user_id, purpose, fields, partner_id, version, status, expires_at |
| `documents` | 원본 문서 메타 | user_id, type, storage_ref, hash, uploaded_at, retention_until |
| `document_extractions` | OCR 결과 | document_id, extracted_fields_masked, confidence, status |
| `employment_records` | 재직/계약 | user_id, employer_name_masked, visa_type, start_date, status |
| `payroll_records` | 급여명세 | user_id, pay_month, gross_pay, deductions, net_pay, confidence |
| `bank_income_records` | 입금내역 | user_id, month, amount, payer_hint, match_status |
| `insurance_records` | 보험/NPS 증빙 | user_id, type, status, source, evidence_date |
| `refund_cases` | 환급 체크 | user_id, item_type, likelihood, status, next_action |
| `refund_estimates` | 추정액 | refund_case_id, min_amount, max_amount, assumptions |
| `readiness_reports` | 리포트 snapshot | user_id, version, fields, freshness, created_at |
| `partner_access_grants` | 파트너 제공권한 | user_id, partner_id, purpose, fields, status, expires_at |
| `partner_query_logs` | 조회 감사 | grant_id, partner_id, fields, result, queried_at |
| `risk_flags` | 레드플래그 | user_id, type, severity, evidence_ref, status |
| `notifications` | 알림 | user_id, trigger_type, channel, status, sent_at |
| `audit_logs` | 보안/감사 | actor_id, action, object_type, object_id, timestamp |

### 9.2 데이터 보안 기본값

| 데이터 | 저장 원칙 |
|---|---|
| 여권/ARC 이미지 | 암호화 저장, 원본 단기 보관 지향, 접근 감사 |
| 외국인등록번호/여권번호 | 평문 저장 금지, 필요 시 암호화/토큰화/마스킹 |
| 계좌번호 | 평문 로그 금지, 최소 저장, L3 목적 한정 |
| 생체/라이브니스 | 원본/특징값 보관 최소화, 가능하면 즉시 파기 |
| OCR 로그 | 실제 번호/이미지 제외, confidence와 플래그만 |
| 파트너 제공 | snapshot + 필드 단위 동의 + 조회 로그 |

---

## 10. Technical Architecture

```text
Next.js Web/App
  ├─ Auth & Locale
  ├─ ForeignID Capture
  ├─ BackWon Dashboard
  ├─ Document Wallet
  ├─ Refund Checker
  ├─ Readiness Report
  └─ Help Router

API Layer
  ├─ Identity Service
  ├─ Document OCR Service
  ├─ Refund Rule Engine
  ├─ Wage Adequacy Engine
  ├─ Report Builder
  ├─ Consent Service
  ├─ Partner API Gateway
  └─ Notification Service

Data Layer
  ├─ Supabase Postgres
  ├─ Encrypted Object Storage
  ├─ Audit Log
  └─ Partner Query Logs
```

### 10.1 Rule Engine 원칙

- 요율, 최저임금, 협정국/상호주의 국가, 보험 산식은 코드에 하드코딩하지 않는다.
- `ruleset_version`을 두고 결과마다 어떤 규칙 버전으로 판정했는지 남긴다.
- "확정" 대신 `likelihood`와 `needs_official_confirmation`을 사용한다.

### 10.2 Report Builder 원칙

- 원천 문서에서 바로 파트너에게 제공하지 않는다.
- 사용자에게 미리보기 제공 후 동의된 필드만 snapshot으로 만든다.
- snapshot은 변경 불가하고 새 데이터가 들어오면 새 버전을 만든다.

---

## 11. Compliance Guardrails

| 영역 | 금지/주의 | 제품 방어선 |
|---|---|---|
| 신용평가 | 점수, 등급, 승인확률 제공 | 점수 없는 신호 리포트 |
| 대출중개 | 직접 대출 비교/모집/권유 | MVP에서는 금융사 연결 전 동의 리포트만 |
| 세무 | 세금환급 대행/수임 알선 | 홈택스/세무사 디렉토리 라우팅 |
| 법률 | 사건 알선 수수료, 법률 판단 | 전문가 디렉토리/상담 전 패키지 |
| 노무 | 회사 상대 대리·교섭 | 노동청/노무사 라우팅 |
| 환급 | 확정액 보장, 대행 오인 | 추정/확인 필요 라벨, 공식기관 링크 |
| 개인정보 | 과다 수집, 로그 노출 | step-up, 분리동의, 암호화, 감사로그 |

---

## 12. MVP Scope

### 12.1 V0.1 - 8주 파일럿

| 주차 | 구축 범위 | 산출 |
|---|---|---|
| 1-2 | 언어, 약관, L0/L1 인증, 동의센터 | 가입/여권+셀카 인증 |
| 2-3 | 내 상태 대시보드, 기본 프로필 | 비자·직장·급여·출국예정 카드 |
| 3-4 | 문서 월렛, 급여명세/계약서 OCR | 증빙 업로드/정정 |
| 4-5 | 환급 체크엔진 | 5개 항목 가능성/체크리스트 |
| 5-6 | 금융 준비도 리포트 | scoreless report v1 |
| 6-7 | 파트너 동의/조회 로그 | 수동 PoC용 report link/API |
| 7-8 | Help Router, 알림, 파일럿 운영 | 유저 100명, 금융권 2곳 RFI |

### 12.2 V0.1 제외 범위

- 직접 대출중개, 직접 송금, 지갑/선불충전
- 직접 환급 신청 대행
- 직접 세무신고/법률문서/노무대리
- 신용점수/등급 산출
- 전문가 수임 성공보수 쉐어
- 정부/보험사 실시간 데이터 연동 확정 표현

---

## 13. Acceptance Test Scenarios

| 시나리오 | Given | When | Then |
|---|---|---|---|
| L1 인증 성공 | 여권과 셀카가 선명함 | 사용자가 제출 | L1 pass, 대시보드 진입 |
| OCR 실패 | 급여명세 이미지가 흐림 | 업로드 | 재촬영 가이드와 수기입력 제공 |
| 국민연금 판정 보류 | 국적 없음 | 환급 체크 | "국적 입력 필요"와 NPS 확인 안내 |
| 출국만기보험 보류 | EPS 여부 없음 | 환급 체크 | E-9/H-2 여부 입력 요청 |
| 금융 리포트 생성 | L2, 급여 3개월, 체류만기 입력됨 | 리포트 생성 | 점수 없는 signal report 생성 |
| 파트너 조회 | 사용자 동의 있음 | 은행이 API 조회 | 동의 필드만 반환, 조회 로그 생성 |
| 동의 철회 | 사용자가 철회 | 파트너 재조회 | 403 또는 접근 차단 |
| 체불 플래그 | 입금 2개월 지연 | 급여 진단 | 체불 가능성, 노동청/노무사 라우팅 |
| 문서 만료 | ARC 만료일 경과 | 홈 진입 | L2 유효성 재확인 요청 |

---

## 14. Open Questions

| 질문 | 왜 중요한가 | 검증 방법 |
|---|---|---|
| 금융권이 어떤 필드에 돈을 낼까 | 리포트 상품성 | CB/은행 5곳 인터뷰 |
| 조회 단가는 얼마가 가능한가 | BM 핵심 | PoC 제안서와 RFI |
| L2/L3 인증 비용과 이탈률은 얼마인가 | 유닛이코노믹스 | 100명 파일럿 퍼널 |
| NPS/EPS/보험 증빙을 어느 수준까지 자동화할 수 있나 | 환급 UX | 공식기관별 절차 확인 |
| 전문가 연결 과금은 어디까지 안전한가 | 법률 리스크 | 자격사별 법무 검토 |
| 외국어 번역 품질을 어떻게 보증할까 | 신뢰와 민원 | 주요 6개 언어 검수자 운영 |

---

## 15. 주요 출처와 기준

- `[1차]` 국민연금공단 — [외국인 반환일시금 FAQ](https://www.nps.or.kr/pnsinfo/ntpsklg/getOHAF0100M0.do), [외국인에 대한 급여](https://www.nps.or.kr/pnsinfo/ntpsklg/getOHAF0084M0.do)
- `[1차]` EPS — [고용/취업절차](https://www.eps.go.kr/eo/EmployJobProc.eo?tabGb=01), [각종 보험가입 및 혜택](https://www.eps.go.kr/eo/EmployPerSystem.eo?tabGb=06), [외국인 근로자 출국준비 안내](https://www.eps.go.kr/eo/BusiPsttOutInfoM.eo?natNm=kr&pageGb=04)
- `[1차]` 하이코리아 — [전자민원 신청](https://www.hikorea.go.kr/cvlappl/CvlapplStep1.pt)
- `[1차]` 정부24/외국인서비스 — [외국인 체류지변경신고](https://www.gov.kr/mw/AA020InfoCappView.do?CappBizCD=12700000026)
- `[1차]` 국가법령정보센터 — 신용정보법, 개인정보보호법, 근로기준법, 근로자퇴직급여 보장법, 외국인근로자의 고용 등에 관한 법률
- `[내부]` `15-a-to-z-worker-service-blueprint.md`, `13-three-party-workflow-bm-review.md`, `14-worker-services-credit-signal-opportunities.md`, `.agents/skills/moneeback-refund/`, `.agents/skills/foreignid-auth/`
