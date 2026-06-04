# GTM 엔게이지먼트 — 병렬 워크스트림 산출물

이 폴더는 **GTM 전략본부**(맥킨지형 병렬 워크스트림 팀)의 산출물 저장소다.
총괄(`gtm-engagement-lead`)이 8개 워크스트림 에이전트를 **동시에 소환**하고,
각 에이전트는 **자기 파일에만** 기록한다. → 동시 실행 시 쓰기 충돌 0.
8개 세부 워크스트림은 중복 skill 없이 **agent-only**로 운영하며, 공통 워크플로우는 `gtm-engagement`가 책임진다.

## 파일 점유 규칙 (한 에이전트 = 한 파일)

| 파일 | 담당 에이전트 | 내용 |
|---|---|---|
| `00-engagement-brief.md` | gtm-engagement-lead | 공통 입력(문제정의·목표·제약·SSOT 핵심수치). **모든 워크스트림이 먼저 읽는다.** |
| `01-segmentation.md` | gtm-segmentation-agent | 세그멘테이션·비치헤드·ICP·세그먼트별 TAM/SAM/SOM |
| `02-customer-insight.md` | gtm-customer-insight-agent | JTBD·구매여정·DMU·페인 정량화 |
| `03-competitive-positioning.md` | gtm-competitive-positioning-agent | 경쟁지형·포지셔닝 2×2·해자·win-theme |
| `04-value-pricing.md` | gtm-value-pricing-agent | 가치제안·패키징·가격 아키텍처·수익모델 |
| `05-channel-partnership.md` | gtm-channel-partnership-agent | 채널 믹스·RTM·파트너십·채널 경제성 |
| `06-sales-motion.md` | gtm-sales-motion-agent | 세일즈 모션·퍼널·전환·인에이블먼트 |
| `07-launch-pilot.md` | gtm-launch-pilot-agent | 런치 플랜·PoC 설계·30/60/90·KPI |
| `08-business-case.md` | gtm-business-case-agent | 유닛이코노믹스·ARR 빌드·시나리오 |
| `99-storyline.md` | gtm-engagement-lead | 통합 스토리라인(SCQA/Pyramid)·임원 readout |

## 병렬 철칙
1. **자기 파일만 쓴다.** 다른 워크스트림 파일·`PROJECT.md`는 **읽기 전용**.
2. **공통 입력은 `00-engagement-brief.md` + `PROJECT.md`(SSOT).** 핵심수치는 여기서만 가져온다.
3. **표준 산출 스키마**(아래)를 지켜야 총괄이 기계적으로 통합한다.
4. 워크스트림 간 정보가 필요하면 **추정으로 진행하고 ⑤ 의존성/오픈이슈에 기록** — 다른 에이전트를 기다리지 않는다.

## 표준 산출 스키마 (모든 워크스트림 공통)
```
# <워크스트림명> — <헤드라인 한 줄>
## ① 핵심 질문        (이 워크스트림이 답하는 질문)
## ② 분석             (프레임워크·표·근거. 출처/가정 표기)
## ③ So-what          (전략적 함의)
## ④ 권고             (실행 가능한 결정 — 누가/무엇을/언제)
## ⑤ 의존성·오픈이슈   (다른 워크스트림에 넘길 것 / 확인 필요)
## ⑥ 헤드라인          (총괄 신디시스용 한 줄, 액션 동사로)
```

> ⚠️ 모든 산출물은 법적 효력 없는 **참고 정보**다. 재무 수치는 **목표·가정**으로 라벨링하고,
> 비자·정책·환급 사실은 1차 출처와 전문가 검증이 필요함을 말미에 명시한다.
