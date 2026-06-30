# VisaDesk 8주 PoC GTM·리서치 통합 산출물

작성일: 2026-06-15

## Executive Decision

**권고:** VisaDesk 8주 PoC는 **비수도권 제조 중소기업 중 외국인 10-80명을 고용하고, 전담 HR/컴플라이언스 담당자가 없는 사업장**을 1차 쐐기시장으로 잡는다.

이유:
- 시장은 충분히 크고 활성화되어 있다. 법무부 통계 기준 2025년 말 국내 체류외국인은 **2,783,247명**, 장기체류자는 **2,159,052명**, 취업자격 체류외국인은 **594,047명**이다.
- 정책 수요도 계속된다. 2030 이민정책 미래전략뿐 아니라 2023년 이후 **제4차 외국인정책 기본계획, Study Korea 300K, K-point E74, E-9 업종 확대, 지역특화형 비자, 외국인 돌봄·정주 정책**이 동시에 깔리며 "유입-취업-체류-정주-통합" 관리 수요를 키우고 있다.
- 기업 페인은 반복적이고 측정 가능하다. 고용허가, 등록, 교육, 고용변동 신고, 보험, 임금요건, 체류만료, 서류보관이 모두 운영 리스크다.
- 경쟁사는 대부분 B2C 생활·금융, 유학생 비자, 채용 매칭에 치우쳐 있다. **VisaDesk는 채용 이후 B2B 준법관리 시스템 오브 레코드**를 선점할 수 있다.

8주 PoC 목표는 SSOT 기준 **15개사 / 3,300만원**이다. 이는 확정 매출 전망이 아니라 검증 목표로 관리한다.

## 근거와 신뢰도

| 주장 | 출처 | 신뢰도 |
|---|---|---|
| 2025년 말 체류외국인 2,783,247명, 장기체류 2,159,052명, 취업자격 594,047명 | 법무부 출입국·외국인정책 통계 | 높음 |
| 2026년 E-9 도입 규모 8만 명 | 고용노동부 보도자료, 2025-12-22 | 높음 |
| 2026년 비전문 외국인력 도입 계획 19.1만 명 | 고용노동부 보도자료, 2025-12-22 | 높음 |
| 제4차 외국인정책 기본계획(2023~2027): 경제·안전·통합·인권·인프라 5대 정책목표 | 법무부 출입국·외국인정책본부 | 높음 |
| Study Korea 300K: 2027년 외국인 유학생 30만 명 유치, 지역-대학-기업 연계, D-2 규제 완화 | 교육부, 2023-08-16 | 높음 |
| K-point E74: 숙련기능인력 3만5천 명 확대, 기업추천·지역가점·E-9→E-7-4→F-2/F-5 경로 | 법무부, 2023-09-26 | 높음 |
| 2024년 E-9 16만5천 명 도입 및 음식점업·임업·광업 허용 | 고용노동부, 2023-11-27 | 높음 |
| K-CORE 등 지역 기반 중숙련 인재 정책 방향 | 출입국·외국인정책본부 2030 이민정책 미래전략 | 높음 |
| EPS 사업주 절차·보험 의무 | 고용허가제 공식 사이트 | 높음 |
| 국민연금 반환일시금 조건 | 국민연금공단 공식 페이지 | 높음 |
| 경쟁사 포지셔닝 | 공개 웹사이트·앱스토어·언론 | 중간 |
| PoC 퍼널 전환율 | PlugNX SSOT + GTM 가정 | 중간/가정 |

## 1. Due Diligence Snapshot

### 시장 수요

VisaDesk의 페인은 단순한 "있으면 좋은 기능"이 아니라 외국인력 확대와 세분화되는 체류정책이 만든 운영 공백이다. 2025년 말 취업자격 체류외국인 **594,047명**은 고용기업 시장의 가장 강한 상단 신호다. E-9, E-7, E-7-4, H-2, E-8 및 F/D 계열 전환은 각각 체류만료, 임금요건, 신고, 보험, 서류 관리 기준이 다르다.

### 정책 순풍

2030 이민정책 미래전략은 가장 최신의 큰 방향이지만, VisaDesk의 GTM 근거는 그 전략 하나에만 기대면 약하다. 실제로는 2023년부터 여러 부처의 외국인 대상 정책이 이미 **유입 확대, 취업 전환, 지역 정주, 숙련 전환, 돌봄 개방, 행정 디지털화**를 향해 움직였다.

정책 전수 스캔 범위: 2023년 이후 중앙부처가 발표·공표한 외국인 대상 **기본계획, 시행계획, 대책, 비자/고용허가 운영계획, 시범사업** 중 VisaDesk·BackWon·ForeignID에 직접 영향을 주는 항목. 단순 행사·일회성 홍보·개별 지자체 공고는 제외했다.

| 정책 레이어 | 주무/시점 | 핵심 내용 | VisaDesk/BackWon/ForeignID 시사점 |
|---|---|---|---|
| **제4차 외국인정책 기본계획(2023~2027)** | 법무부, 2024-01 게시(2023~2027 계획) | 경제·안전·통합·인권·협력/인프라 5대 목표. 특히 "우리 경제에 필요한 이민자 유치와 육성", "지역기반 이민정책 체계", "기술혁신 기반 이민행정 고도화"가 핵심이다. | 2030 전략의 전 단계이자 범정부 마스터 플랜. VisaDesk는 기업 운영 레이어, ForeignID는 행정·신원 인프라, BackWon은 정주·권익 레이어로 정렬된다. |
| **2023년 외국인정책 시행계획** | 법무부, 2024-09 게시 | 중앙행정기관과 광역 지자체 단위로 외국인정책 시행계획을 분리 공표. 정책 실행 주체가 법무부 단독이 아니라 교육부·고용부·여가부·복지부·지자체로 분산되어 있음을 확인. | GTM에서 "정부 정책 하나"가 아니라 지자체·대학·기업·전문가 파트너를 묶는 다중 채널 접근이 필요하다. |
| **Study Korea 300K Project** | 교육부, 2023-08-16 | 2027년 외국인 유학생 30만 명 유치. 지역-대학-기업-지자체 TF, 해외인재특화형 교육국제화특구, 유학생 D-2 현장실습·아르바이트·인턴십 규제 완화, E-9 근로자의 대학 진학·학위 취득→E-7 숙련 전환 통로, GKS/BK21 이공계 인재 확대. | 유학생은 단순 B2C 고객이 아니라 미래 취업·정주 풀이다. ForeignID는 유학생 인증/eKYC, VisaDesk는 D-2→E-7/E-7-4 전환과 지역기업 채용관리, BackWon은 생활금융·환급 접점으로 확장 가능. |
| **과학·기술 우수인재 영주·귀화 패스트트랙** | 법무부, 2023-01-02 | 국내에서 수학한 과학·기술 우수 외국인의 영주·국적 취득 절차를 단축해 2023년부터 본격 추진. | 고급인재 쪽은 B2B 구매자는 대학·연구기관·첨단기업이다. 초기 ICP는 아니지만 ForeignID/비자전환 관리의 상위 세그먼트가 된다. |
| **조선업 외국인력 도입 애로 해소** | 법무부 등, 2023-01 | 산업현장 인력난 대응으로 조선업 외국인력 도입 절차 개선. | 제조·조선 협력사는 외국인 고용관리 페인이 이미 정책으로 인정된 산업군이다. 제조 ICP의 하위 vertical로 우선 테스트할 수 있다. |
| **K-point E74 숙련기능인력 3만5천 명 확대** | 법무부, 2023-09-26 | 4년 이상 체류, 한국어, 기업추천, 점수요건 등을 바탕으로 E-9 등 단순노무 인력이 E-7-4 숙련기능인력으로 전환 가능. 지역가점, 기업 추천권 박탈 조건, 향후 F-2/F-5 경로가 포함된다. | VisaDesk의 킬러 기능은 "체류만료 알림"을 넘어 E-9→E-7-4 전환 후보 관리, 기업추천 증빙, 임금·체납·인권침해 리스크 기록 관리가 되어야 한다. |
| **2024년 E-9 도입·운용계획** | 고용노동부, 2023-11-27 | 2024년 E-9 도입 규모 16만5천 명. 음식점업, 임업, 광업 등 신규 업종 허용. 업종별 교육·체류관리TF·지자체 역할 분담 언급. | 제조 외에 외식·임업·광업도 실험 셀로 열리지만, 초기에는 제조를 기준모델로 만들고 업종 확대는 채널별 랜딩/체크리스트로 분화한다. |
| **지역특화형 비자 사업 공모** | 법무부, 2023-12-08 | 인구감소 대응과 지역경제 활력을 위한 지역특화형 비자 사업 공모. 지자체가 외국인의 유치·정착에 직접 관여. | 지역 기업·지자체·대학을 묶는 outbound가 중요하다. VisaDesk는 "지역특화 비자 참여기업 준법관리 패키지"로 제안 가능. |
| **제4차 다문화가족정책 기본계획(2023~2027)** | 여성가족부, 2023-05-03 | 다문화 아동·청소년 출발선 보장, 안정적 생활환경 조성 등 가족·정주 관점의 정책. | BackWon/ForeignID의 B2C 확장에서는 근로자뿐 아니라 결혼이민·자녀·가족 단위의 인증, 금융, 정보 접근성도 장기 시장이 된다. |
| **외국인 가사관리사·돌봄 시범사업** | 고용노동부·서울시, 2024-07 본격 신청(2023년 논의·계획) | E-9 기반 외국인 가사관리사 100명 소규모 시범, 서비스 제공기관 직접고용, 신원검증·교육·고충처리 체계 운영. | 돌봄은 제조 다음의 확장 ICP다. 다만 가정 내 서비스 특성상 신원검증, 교육, 고충처리, 근무환경 관리가 강해 VisaDesk보다 ForeignID+운영관리 패키지가 먼저 먹힐 수 있다. |
| **2030 이민정책 미래전략** | 법무부/출입국·외국인정책본부, 2026 | K-CORE, K-STAR, 비자체계 단순화, 디지털 사전심사, AI 분류심사, 임금자문위, 요양보호사·농어업 숙련 등 후속 전략. | 위 정책 흐름을 한 단계 더 제품화하는 신호. "채용 이후 모든 것"을 민간 SaaS로 묶는 PlugNX 포지셔닝을 강화한다. |

정책 해석:
- **제조 ICP는 더 강해진다.** E-9 확대, E-7-4 숙련 전환, 조선업·제조업 인력난 정책이 모두 "채용 이후 준법관리" 문제를 만든다.
- **유학생/지역대학은 별도 GTM 축이다.** Study Korea 300K는 지금 당장 제조 outbound보다 전환이 느리지만, D-2→E-7, 지역기업 취업, 전문대 기반 숙련화 흐름 때문에 중기 파트너 채널로 중요하다.
- **돌봄은 2차 ICP로 남긴다.** 정책 수요는 크지만 가정·서비스 제공기관·노동권·신원검증 리스크가 커서 PoC 이후 전용 플로우가 필요하다.
- **제품 메시지는 "정책 수혜"가 아니라 "정책 리스크 대응"이어야 한다.** 정부가 유입을 늘릴수록 기업은 체류, 임금, 보험, 추천, 신고, 교육, 고충처리 기록을 더 정교하게 남겨야 한다.

### 경쟁 지형

| 플레이어 | 장악 영역 | VisaDesk 대비 빈틈 |
|---|---|---|
| VIVISA / YesFuture | 유학생 비자, 어학원 신청, 대학 중심 외국인 라이프사이클 | B2C·학생·기관 지원에 가깝고, 고용기업 준법관리 SaaS는 아님 |
| glow / 클링커즈 | 외국인 근로자 생활금융, 대출 비교, 송금, 비자·생활 가이드, 5만+ MAU 주장 | B2C 금융 쐐기는 강하지만, 고용기업 준법 기록은 약함 |
| VIVISA x glow 제휴 | 비자·행정 데이터 + 금융을 결합한 대안신용·정착 패키지 | 비자 데이터가 금융으로 이어지는 길목이 경쟁화되고 있다는 신호 |
| Vijob | 외국인 구인구직, 번역 채용공고, 고용주 매뉴얼, 번역 채팅, Google Play 10만+ 다운로드 | 채용 전후방 중 채용·정착 입구 중심, 채용 이후 준법 운영 시스템은 아님 |
| DAGACHI | 다국어 커뮤니티·생활정보 | 커뮤니티/생활정보 중심, 컴플라이언스 시스템 아님 |
| 행정사/노무사 | 고신뢰 인적 전문가 처리 | 사건·건별·사후대응 중심, 상시 모니터링과 데이터 축적이 약함 |
| HiKorea/EPS/정부 | 공식 절차·권한 | 기업 운영 레이어가 아니며 SMB가 워크플로 도구로 쓰기 어려움 |

Right-to-win:
- **VisaDesk:** 비자, 임금, 서류, 알림을 묶는 고용기업 데이터 원장.
- **BackWon:** 동일 고용 데이터를 활용한 근로자 환급·금융 결과.
- **ForeignID:** B2B와 B2C 모두에서 재사용 가능한 외국인 본인인증/eKYC 레이어.
- 결합 효과: B2B 획득이 근로자 저CAC 유입을 만들고, B2C 만족이 기업 유지율을 강화한다.

주요 리스크:
- 법률·규정 정확도 책임: 카피는 반드시 "운영 보조, 법률 자문 아님"을 명시해야 한다.
- 연동 리스크: 공식 시스템 API가 제한적일 수 있다.
- 신뢰 장벽: SMB 대표는 기존 행정사를 선호할 수 있으므로 전문가 에스컬레이션을 상품 안에 넣어야 한다.
- 경쟁 제휴 리스크: VIVISA x glow는 비자 데이터 → 금융 길목 경쟁의 신호다.

## 2. 브랜드 DNA와 포지셔닝

### 브랜드 구조

**PlugNX**는 외국인 고용·체류·금융을 연결하는 신뢰 운영 레이어다.

| 제품 | 한 줄 정의 | 주요 구매자/사용자 | 핵심 약속 |
|---|---|---|---|
| VisaDesk | 고용기업용 외국인 고용 준법관리 SaaS | 대표, HR/총무, 관리자 | 비자, 임금, 서류, 신고 실수를 사고 전에 막는다 |
| BackWon | 외국인 근로자 환급·금융 회수 도우미 | 외국인 근로자 | 연금, 보험, 퇴직금, 미수령금을 모국어 흐름으로 찾는다 |
| ForeignID | 외국인 본인인증·eKYC 인프라 | 두 제품과 미래 파트너 | 여권/ARC/통신/계좌/전자서명을 묶은 신뢰 레이어 |

### 포지셔닝

**카테고리:** 외국인 고용 준법관리 + 근로자 금융회수 통합 플랫폼.

**포지셔닝 문장:**  
PlugNX VisaDesk는 외국인 근로자를 고용한 기업이 체류만료, 비자별 임금요건, 서류 미비, 신고 누락 리스크를 상시 모니터링하도록 돕고, 등록된 근로자를 BackWon 환급·금융 흐름으로 자동 연결하는 ForeignID 기반 B2B2C 플랫폼이다.

### 차별점

- 고용기업 B2B 준법 기록과 근로자 B2C 금융 결과를 한 데이터 플라이휠로 연결한다.
- 행정사/노무사의 사후 처리가 아니라 예방형 모니터링을 제공한다.
- ForeignID를 통해 신원확인을 반복 업무가 아니라 재사용 가능한 인프라 자산으로 만든다.
- 범용 HR SaaS가 아니라 "외국인 채용 이후 운영"에 특화된 쐐기 포지션이다.

### 메시지 기둥

1. **손실 회피:** "만료일이나 임금요건 한 건만 놓쳐도 1년치 구독료보다 큰 비용이 납니다."
2. **수작업 대체:** "엑셀, 캘린더, 기억에 맡기던 외국인 고용관리를 멈추세요."
3. **정책 준비:** "K-Trust/K-CORE형 인센티브가 본격화되기 전, 평소 기록을 먼저 쌓으세요."
4. **근로자 신뢰:** "회사가 등록하면 근로자는 BackWon으로 받을 수 있는 돈을 확인합니다."

## 3. ICP 우선순위

점수: 5점 = 가장 강함.

| 세그먼트 | 페인 | 접근성 | 지불의사 | 반복성 | 리스크 | 총점 | 판단 |
|---|---:|---:|---:|---:|---:|---:|---|
| 제조 중소기업, 외국인 10-80명 | 5 | 4 | 4 | 5 | 3 | 21 | **1차 ICP** |
| 요양·돌봄 사업자 | 5 | 3 | 4 | 4 | 4 | 20 | 정책 세부 안정 후 2차 |
| 농축산 법인 | 5 | 3 | 3 | 3 | 4 | 18 | 직접영업보다 파트너 주도 |
| 외식·프랜차이즈 | 3 | 4 | 2 | 3 | 3 | 15 | 다점포·고용 규모 큰 곳만 선별 |

주요 구매자 페르소나:
- 대표/사업주: 과태료, 인력 공백, 고용제한을 줄이고 싶다.
- HR/총무 담당자: 체류만료와 서류 누락 알림을 자동화하고 싶다.
- 재무/관리 담당자: 예측 가능한 SaaS 비용으로 예측 불가능한 사고비용을 줄이고 싶다.
- 전문가 파트너: 반복 모니터링 수익과 정리된 고객 데이터를 원한다.

제외 기준:
- 외국인 근로자 5명 미만, 단 다점포 그룹은 예외.
- 행정 소유자가 없는 초소형 계절 사업장.
- 기본 직원/비자/서류 메타데이터 업로드를 거부하는 기업.

## 4. 8주 PoC GTM Plan

### 목표 결과

| 지표 | 8주 목표 | 비고 |
|---|---:|---|
| 타깃 계정 소싱 | 400개 | 제조업 중심, 요양·농축산 실험 셀 포함 |
| 검증된 의사결정자 연락처 | 240개 | 대표, HR/총무, 공장관리, 재무/관리 |
| 자가진단 완료 | 35건 | 셀프 진단 또는 어시스트 진단 |
| Qualified PoC 기회 | 20건 | 외국인 10명 이상 또는 긴급 준법 공백 |
| PoC 시작/LOI | 15건 | SSOT 목표 |
| PoC 매출 | 3,300만원 | SSOT 목표 |
| 온보딩 근로자 기록 | 450-900명 | 가정: 회사당 30-60명 |

### 채널 믹스

| 채널 | 역할 | 주간 액션 | KPI |
|---|---|---|---|
| 산업단지/상공회의소 세미나 | 신뢰와 긴급성 형성 | 20-30개사 규모 소규모 세션 3회 | 참석 80명, 진단 25건 |
| 행정사/노무사 파트너 | 신뢰 보강과 추천 | 파트너 인터뷰 10건, 추천 파일럿 3건 | 추천 계정 10개 |
| 직접 outbound | 계정 커버리지 확보 | 검증 연락처 240개, 3단계 이메일 + 전화 | 답장률 8-12%, 미팅 20건 |
| 협회/지자체 인접 채널 | 공신력 | "외국인 고용 리스크 점검" 공동 세션 제안 | 공동 마케팅 훅 2개 |
| BackWon 근로자 훅 | B2B2C 증명 | PoC 온보딩 시 근로자 환급 확인 제공 | 근로자 opt-in 60% 가정 |

### 타임라인

| 주차 | 워크스트림 | 산출 |
|---|---|---|
| 1주차 | ICP/list setup | 400개 계정 Clay 테이블, scoring rubric, 랜딩 진단 이벤트 추적 |
| 2주차 | 파트너 proof | 전문가 10명 통화, quote 가능한 advisor 2명, 세미나 deck |
| 3주차 | Outbound wave 1 | 연락처 120개, 대표/HR variant, 미팅 10건 |
| 4주차 | Seminar wave | 세션 2회, 진단 20건, 첫 PoC 5건 |
| 5주차 | Onboarding sprint | 직원 샘플 데이터 업로드, 리스크 리포트, 전문가 티켓 흐름 |
| 6주차 | Outbound wave 2 | 연락처 120개, 경쟁/과태료 angle, 추가 PoC 7건 |
| 7주차 | Worker flywheel proof | BackWon 동의 흐름, 근로자 benefit report, 기업 retention story |
| 8주차 | Conversion | PoC/LOI 15건, 가격 실험, before/after case-study metric |

### KPI Stack

획득:
- 연락처 검증률 > 60%
- 답장률 > 8%
- 미팅 전환율 > 4%
- 미팅 후 진단 완료율 > 50%

활성화:
- 첫 리스크 리포트까지 48시간 이내
- PoC 계정의 80% 이상이 근로자 10명 이상 등록
- 활성 PoC 계정당 actionable alert 3건 이상

매출:
- Qualified opportunity → PoC close rate > 75%
- 8주 내 paid conversion 또는 LOI 확보
- Plan mix 목표: Starter 40%, Growth 50%, Compliance 10%

제품 proof:
- 회사당 발견된 체류/임금/서류 리스크 수
- 전문가 티켓 handoff 수
- 근로자 BackWon opt-in rate
- 관리자 self-reported 절감 시간

## 5. 키워드 클러스터

Ahrefs/Semrush 데이터가 없으므로 정성 기반 1차안이며, 추후 실제 볼륨 검증이 필요하다.

| 키워드 | 의도 | 우선순위 | 클러스터 | 페이지 |
|---|---|---|---|---|
| 외국인 고용 | commercial | target | employer_compliance | Pillar |
| 외국인 채용 | commercial | target | employer_compliance | Pillar |
| 외국인 고용관리 | commercial | easy_win | employer_compliance | Product |
| 고용허가제 | informational | target | eps_compliance | Guide |
| E-9 고용 | commercial | target | eps_compliance | Guide |
| 외국인근로자 보험 | informational | easy_win | eps_compliance | Guide |
| 비자 만료 | informational | easy_win | visa_monitoring | Guide |
| 체류기간 연장 | informational | target | visa_monitoring | Guide |
| 자격외 활동 | informational | target | visa_monitoring | Guide |
| 불법고용 과태료 | commercial | easy_win | penalty_risk | Calculator |
| 외국인 임금 | informational | target | wage_compliance | Guide |
| E-7 임금 | commercial | easy_win | wage_compliance | Guide |
| 국민연금 반환일시금 | informational | target | worker_refund | BackWon |
| 출국만기보험 | informational | target | worker_refund | BackWon |
| 외국인 본인인증 | commercial | content | foreignid | ForeignID |

콘텐츠 공백:
- "외국인 고용 리스크 자가진단" evergreen landing page.
- "E-9/E-7/E-7-4 고용 체크리스트" guide pages.
- "출국만기보험 vs 퇴직금" employer/worker explainer.
- "불법고용/체류만료 비용 계산기" lead magnet.
- `llms.txt`, FAQ schema, Product schema, Organization schema, 출처 링크가 있는 정책 페이지.

## 6. VisaDesk 랜딩 AEO/GEO 감사

감사 URL: https://plugnx-visaops.netlify.app  
결과 JSON: `scratch/aeo-visadesk/aeo-audit.json`

### 점수

| 항목 | 점수 |
|---|---:|
| Foundational deterministic checks | 55/100 |
| Intelligence manual score | 57/100 |
| 최종 | **56/100, Grade C-** |

수동 intelligence 평가:
- Answer readiness: 3/5. 홈페이지는 제품 문제를 설명하지만, 대시보드 페이지 다수가 공개 답변형 콘텐츠가 아니라 UI 데모다.
- Quotability: 3/5. 표와 수치는 좋지만, 40-60단어짜리 인용 가능한 answer block이 부족하다.
- Evidence density: 3/5. 일부 법령/통계 주장이 있으나 source link와 structured citation이 약하다.
- Content depth: 3/5. 홈페이지는 충실하지만, supporting public guide가 부족하다.
- Freshness: 2/5. 2026 예시는 있으나 업데이트일, RSS, changelog, article metadata가 없다.
- Structural clarity: 3/5. 메인 페이지는 읽히지만, dashboard route에는 중복 H1과 schema 부재가 있다.

주요 deterministic 실패:
- canonical URL 없음.
- 여러 페이지에서 H1 규칙 미흡.
- JSON-LD structured data 및 recognized schema type 없음.
- Open Graph basics 없음.
- 유효한 `llms.txt` 없음.
- RSS/Atom feed 없음.

가장 중요한 개선:
1. `Organization`, `SoftwareApplication`, `Product`, `FAQPage`, `Article` JSON-LD 추가.
2. 모든 template에 canonical과 OG tag 추가.
3. canonical product, policy, pricing, FAQ, guide URL을 담은 `llms.txt` 발행.
4. dashboard/demo route의 one-H1-per-page와 heading hierarchy 수정.
5. marketing section뿐 아니라 source-linked guide page 추가.
6. current law/source가 다른 벌금 상한을 확인하면 "2,000만원" 카피 재검증.

## 7. Research Fields 추가안

외국인 환급/준법 리서치용 `fields.yaml` 추가 필드:

```yaml
policy_risk_level:
  description: 현재 또는 예정 정책 변화가 제품 자격, 가격, 법적 문구에 영향을 줄 가능성.
  type: enum
  values: [low, medium, high]

official_source_url:
  description: 주장을 뒷받침하는 1차 정부/기관 출처 URL.
  type: url

source_effective_date:
  description: 인용 규정 또는 통계의 시행일/게시일.
  type: date_or_text

channel_accessibility_score:
  description: 협회, 디렉토리, 파트너, 직접 outbound로 구매자에게 접근하기 쉬운 정도.
  type: integer_1_to_5

channel_owner:
  description: 세그먼트 접근권을 가진 사람 또는 기관. 예: 상공회의소, 협회, 전문가 파트너, 플랫폼.
  type: text

cac_assumption:
  description: 예상 고객획득비용 가정과 계산 로직.
  type: text

cac_evidence:
  description: CAC 가정을 뒷받침하는 outbound benchmark, 세미나 비용, 파트너 수수료, 과거 캠페인 데이터.
  type: text

employer_penalty_exposure:
  description: 구매 동기를 만드는 예상 벌금 또는 운영 손실 노출.
  type: text

refund_monetization_fit:
  description: 해당 세그먼트가 BackWon 환급/금융 회수 흐름으로 자연스럽게 이어지는 정도.
  type: enum
  values: [low, medium, high]

evidence_confidence:
  description: 출처 품질과 최신성에 따른 근거 신뢰도.
  type: enum
  values: [low, medium, high]
```

## 8. Clay List-Building Workflow

### 계정 소스

합법적인 사업자/연락처 데이터만 사용하고, 반드시 source URL을 보관한다.

1. 산업단지 디렉토리, 상공회의소/협회 회원사 페이지.
2. E-9, E-7, 외국인 근로자, 베트남어/태국어/필리핀어 필요 등 신호가 있는 공개 채용공고.
3. 지자체/협회 세미나 참석자 opt-in.
4. 행정사/노무사 파트너 추천 고객, 단 동의 기반.
5. Google Maps/local directories는 company-level enrichment에만 사용하고, 개인 스크래핑은 피한다.

### Clay Table Columns

| Column | 용도 |
|---|---|
| company_name | 계정 식별 |
| website_domain | enrichment key |
| region | 비수도권 우선순위 |
| industry | 제조/요양/농축산/외식 |
| foreign_worker_signal | 외국인 고용 증거 문장 |
| visa_signal | E-9/E-7/E-7-4/H-2/E-8 언급 |
| worker_count_estimate | 근로자 수 추정과 confidence |
| compliance_pain_signal | 만료, 임금, 채용, 숙소, admin, quota signal |
| decision_maker_title | 대표, HR/총무, 재무/관리 |
| contact_email | 검증 완료 이메일만 |
| source_url | 필수 |
| icp_score | 0-100 |
| message_angle | expiry, wage, document, expert, worker refund |
| sequence_status | queued/sent/replied/booked/disqualified |

### Workflow

1. 회사 리스트 import.
2. 도메인과 company summary를 저비용 모델로 enrichment.
3. CEO/HR/admin 연락처 탐색.
4. 이메일을 `final_email`로 merge.
5. 모든 이메일 verify. valid/deliverable만 발송.
6. 아래 프롬프트로 account scoring.

```text
You are scoring whether this Korean company is a fit for PlugNX VisaDesk.
Return only JSON with icp_score, tier, primary_pain, message_angle, evidence.
Fit signals: 10+ foreign workers, manufacturing/care/agri, E-9/E-7/E-7-4/H-2 mentions,
non-metropolitan location, no dedicated HR team, public hiring activity, compliance-risk language.
```

7. Tier A/B 계정만 Smartlead/Instantly로 push.
8. bounce, role-based, unknown, free-mail, 동의 없는 연락처는 suppress.

운영 기준:
- 이메일은 100% verify.
- bounce rate는 1% 미만.
- 30일 지난 리스트는 재검증.
- 전체 실행 전 10-row test를 먼저 수행.

## 9. Cold Email 4-Step Sequence

ColdIQ 권장 구조는 3-email sequence이므로, 4단계는 즉시 네 번째 이메일이 아니라 **전화/LinkedIn touch 또는 3개월 후 re-engagement**로 운영한다.

### Step 1: 대표/사업주 대상

Subject: 외국인 고용 리스크

```text
{{first_name}} 대표님,

외국인 직원 체류만료나 임금요건 한 건만 놓쳐도 벌금·고용제한·대체채용 비용이 한 번에 터질 수 있습니다.

PlugNX VisaDesk는 외국인 직원의 체류일, 비자별 임금요건, 서류 미비를 매일 점검해 위험 리포트로 보여드립니다.

{{similar_company}}처럼 외국인 10명 이상 고용 중인 사업장에 1분 무료 진단을 열어두고 있는데, 이번 주에 확인해보실까요?
```

### Step 2: HR/총무 담당자 follow-up, 같은 thread, Day 3

```text
{{first_name}}님, 참고로 진단 결과는 바로 이런 형태입니다.

- 90일 내 체류만료자
- 임금요건 미달/주의
- 여권·ARC·계약서 등 핵심서류 누락
- 행정사/노무사 검토가 필요한 케이스

엑셀 파일 없이도 현재 리스크를 48시간 안에 정리해드릴 수 있습니다.
담당자분께 전달드려도 괜찮을까요?
```

### Step 3: 새 subject, Day 17

Subject: 외국인 직원 관리 체크리스트

```text
{{first_name}}님,

외국인 고용 사업장은 채용보다 "채용 이후"가 더 자주 문제 됩니다.

체류기간, 고용변동 신고, 출국만기보험, 임금요건, 서류 보관이 각각 다른 곳에 흩어져 있어서 담당자가 바뀌면 리스크가 그대로 남습니다.

외국인 직원 {{worker_count_estimate}}명 기준 체크리스트를 만들어드릴까요?
```

### Step 4: Call / LinkedIn / Re-engagement

```text
{{first_name}}님, 제가 잘못 짚었다면 편하게 무시해주세요.

다만 외국인 직원 관리가 대표님이 아니라 다른 담당자분 업무라면, 어느 분께 전달드리는 게 좋을까요?
```

벤치마크:
- 최소 답장률 기준: 5%.
- signal-based list가 좋으면 10-20% 기대.
- bounce > 2% 또는 reply < 3%면 타깃/리스트/카피를 즉시 재검토.
- 본사 primary domain으로 cold email 발송 금지. 별도 warmed outreach domain 사용.

## 10. 법률·준법 고지

본 산출물은 사업기획·운영 참고자료다. 비자 자격, 고용 준법, 연금/환급 가능성, 세무, 노무, KYC/AML, 전자서명 효력은 반드시 소관 기관의 최신 1차 출처와 행정사·노무사·변호사·세무사·컴플라이언스 전문가 검토가 필요하다. 여권번호, 외국인등록번호, 계좌, 생체정보는 목적, 동의, 보관기간, 암호화, 접근통제, 파기정책이 명확하지 않으면 수집·저장하지 않는다.

## 출처 링크

- 법무부 체류외국인 통계: https://www.moj.go.kr/moj/2412/subview.do
- 제4차 외국인정책 기본계획(2023~2027): https://www.immigration.go.kr/immigration/1607/subview.do
- 제4차 외국인정책 기본계획 정책목표 및 중점과제: https://www.immigration.go.kr/immigration/1609/subview.do
- 2023년 외국인정책 시행계획: https://www.immigration.go.kr/bbs/immigration/226/587262/artclView.do
- 교육부 Study Korea 300K Project 보도자료: https://www.moe.go.kr/boardCnts/viewRenew.do?boardID=294&boardSeq=96027&lev=0&searc=
- 로컬 원문 PDF: C:\Users\admin\Downloads\[교육부+08-16(수)+브리핑시(15시30분)+보도자료]+[별첨]유학생+교육경쟁력+제고+방안(Study+Korea+300k+Project).hwp.pdf
- 법무부 과학·기술 우수인재 영주·귀화 패스트트랙: https://www.moj.go.kr/bbs/moj/182/566218/artclView.do
- 법무부 K-point E74 숙련기능인력 3만5천 명 확대: https://www.moj.go.kr/moj/228/subview.do?enc=Zm5jdDF8QEB8JTJGYmJzJTJGbW9qJTJGMTg5JTJGNTc1NTM3JTJGYXJ0Y2xWaWV3LmRvJTNGcGFzc3dvcmQlM0QlMjZyZ3NCZ25kZVN0ciUzRCUyNmJic0NsU2VxJTNEJTI2cmdzRW5kZGVTdHIlM0QlMjZpc1ZpZXdNaW5lJTNEZmFsc2UlMjZwYWdlJTNEMTAlMjZiYnNPcGVuV3JkU2VxJTNEJTI2c3JjaENvbHVtbiUzRCUyNnNyY2hXcmQlM0QlMjY%3D
- 고용노동부 2024년 E-9 16만5천 명 도입 및 신규 업종 허용: https://www.moel.go.kr/news/enews/report/enewsView.do?news_seq=15860
- 법무부 2024년도 지역특화형 비자 사업 공모: https://www.immigration.go.kr/bbs/immigration/47/577980/artclView.do
- 여성가족부 제4차 다문화가족정책기본계획: https://www.mogef.go.kr/mp/pcd/mp_pcd_s001d.do?bbtSn=704956&mid=plc503
- 고용노동부 외국인 가사관리사 시범사업: https://www.moel.go.kr/news/enews/report/enewsView.do?news_seq=16825
- 2030 이민정책 미래전략 PDF: https://www.immigration.go.kr/bbs/immigration/214/491432/download.do
- 고용노동부 2026년 E-9 도입규모: https://www.moel.go.kr/news/enews/report/enewsView.do?news_seq=18774
- 고용노동부 2026년 비전문 외국인력 도입계획: https://www.moel.go.kr/news/enews/report/enewsView.do?news_seq=18773
- EPS 보험 안내: https://www.eps.go.kr/eo/EmployPerSystem.eo?tabGb=06
- EPS 사업주 절차 안내: https://www.eps.go.kr/eo/process.eo
- 국민연금 외국인 급여 안내: https://www.nps.or.kr/pnsinfo/ntpsklg/getOHAF0084M0.do
- YesFuture 서비스: https://yesfuture.co.kr/service
- VIVISA x glow 기사: https://www.newsprime.co.kr/news/article.html?no=717061
- 클링커즈 glow: https://clinkers.io/
- Vijob Google Play: https://play.google.com/store/apps/details?hl=ko&id=net.vijob.app
- DAGACHI App Store: https://apps.apple.com/kr/app/dagachi/id6749035814
