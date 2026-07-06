# BackWon B2C 웹사이트 AEO/GEO 감사 — AI 엔진 발견·인용 가능성

감사일: 2026-06-15 · 대상: BackWon 기존 임시 도메인 https://moneeback.vercel.app (라이브 접근 성공) · 프레임워크: `audit-website-aeo`(16 결정 체크 + 6차원) · `improve-aeo-geo`(우선순위 수정)

---

## 핵심 결론 (Answer-first)

1. **등급 F (최종 35/100, 실측 기반 산정).** BackWon 랜딩은 **사람에게는 잘 읽히지만 AI 엔진에는 사실상 보이지 않는다.** 본문은 좋은데(약 800단어, 깔끔한 H2/H3 위계) **기계가 읽는 신호가 0에 가깝다** — `<title>` 없음, meta description 없음, canonical 없음, JSON-LD 없음, Open Graph 없음, hreflang 없음, `robots.txt`/`sitemap.xml`/`llms.txt` 모두 404 [출처:WebFetch 2026-06-15].
2. **가장 중요한 단일 권고:** 지금 ChatGPT·Perplexity·Claude·Google AI Overviews가 "외국인 국민연금 환급" 류 질문에 BackWon을 **인용할 근거 자체가 없다.** 첫 스프린트에서 `<head>` 6종(title·meta·canonical·OG·hreflang·lang)과 JSON-LD 3종(Organization·SoftwareApplication·FAQPage), `llms.txt`만 넣어도 35 → 67+ 점프가 가능하다(저비용·고효과 — §5 점수 시뮬 참조) [추정/목표].
3. **치명적 결손 1순위는 H1 중복과 다국어(hreflang) 부재.** H1이 2개("You Earned It…"/"Protect your money")라 주제 신호가 흐려지고, **6개 언어 제품**[SSOT]인데 hreflang/언어별 URL이 없어 비영어 AI 질의(베트남어·크메르어 등은 예시[가정])에서 **0 노출**이다 — 이게 B2C 환급 시장의 최대 손실 지점.
4. **이 팩이 #10 대비 더하는 것:** 팩 #10 §6은 VisaDesk(B2B 영문 랜딩) 감사였다. 본 팩은 **BackWon(B2C·환급·6개 언어) 특화** — 다국어 hreflang 전략, 환급 FAQPage 스키마, SPA 클라이언트 렌더링 리스크, 환급 수치의 규제 안전 문구를 새로 다룬다.

> ⚠️ 라이브 접근은 **성공**했으므로 진단의 기술 신호는 [출처:WebFetch 2026-06-15] 실측이다. 단, 단일 페이지(홈) n=1 크롤이며 alt-text·일부 라우트는 미확인 → 해당 항목은 [추정]으로 라벨한다.

---

## 1. 점수 요약

| 구분 | 점수 | 근거 |
|---|---:|---|
| Foundational (16 결정 체크) | **32/100** | 46/142점 → 100점 환산, 16개 중 5개만 통과 (실측) |
| Intelligence (6차원 수동) | **37/100** | 평균 1.83/5 × 20 = 36.7 → 37 |
| **최종** = 0.5×32 + 0.5×37 | **35/100** | **Grade F** (0.5×32 + 0.5×37 = 34.5 → 35) |

**한 줄 평결:** 콘텐츠 자산은 B등급감인데, 기계 판독 레이어가 비어 있어 AI 인용 가능성은 사실상 0 — "콘텐츠는 있는데 봉투(메타데이터)가 없는" 전형적 SPA 결손.

> 점수 산정 노트: foundational은 `audit-website-aeo`의 16체크 배점(총 142점)에 실측 결과를 매핑했다. 단일 홈페이지 기준이므로 사이트 전체 크롤(최대 30p) 시 internal-links·text-depth가 더 떨어질 수 있어 32점은 **낙관적 상한**으로 본다.

---

## 2. Foundational — 16개 결정 체크 (실측)

실패를 위에 모음. (P=통과, F=실패, ?=미확인→보수적 처리)

| 체크 | 배점 | 결과 | 실측 상세 [출처:WebFetch 2026-06-15] |
|---|---:|:---:|---|
| `title` | 10 | **F (0)** | `<title>` 태그 **ABSENT** — AI가 페이지 주제를 한 줄로 못 잡음 |
| `meta-description` | 10 | **F (0)** | meta description **ABSENT** — 스니펫 근거 없음 |
| `canonical` | 8 | **F (0)** | `<link rel=canonical>` **ABSENT** — 중복/언어 URL 정규화 불가 |
| `h1` | 8 | **F (0)** | **H1 2개** ("You Earned It. Korea Still Has It." + "Protect your money") — 정확히 1개 규칙 위반 |
| `schema` | 8 | **F (0)** | JSON-LD 블록 **0개** |
| `schema-types` | 8 | **F (0)** | 인식 가능한 `@type` 없음 |
| `og` | 8 | **F (0)** | og:title/og:description **ABSENT** — 공유·미리보기·일부 AI 카드 0 |
| `internal-links` | 10 | **F (0)** | 단일 페이지 앵커 위주, 크롤 가능한 5+ 내부링크 **부재** [추정] |
| `image-alt` | 8 | **? → F (0)** | alt 커버리지 미확인, 아이콘 위주로 추정 → 보수적 0 [추정] |
| `text-depth` | 12 | **P (12)** | 본문 약 800단어 (250+ 충족) |
| `indexability` | 10 | **P (10)** | `noindex` 미발견 |
| `ai-meta-tags` | 6 | **P (6)** | `nosnippet`/`noai`/`noimageai` 미발견 |
| `heading-hierarchy` | 6 | **P (6)** | H2/H3 2+ 레벨, 스킵 없음 (단 H1 중복은 별도 감점) |
| `llms-txt` | 10 | **F (0)** | `/.well-known/llms.txt` **404** |
| `ai-bot-access` | 12 | **P (12)** | `robots.txt` **404** = 기본 전체 허용 (AI 봇 차단 없음). *주의: sitemap 라인도 없음* |
| `rss-feed` | 8 | **F (0)** | RSS/Atom **ABSENT** — 신선도 신호 없음 |

**합계: 46/142 = 32/100.**
**통과 5개:** text-depth, indexability, ai-meta-tags, heading-hierarchy, ai-bot-access.
**실패 11개:** title, meta-description, canonical, h1, schema, schema-types, og, internal-links, image-alt, llms-txt, rss-feed.

부수 확인: `robots.txt` 404 · `sitemap.xml` 404 · `llms.txt` 404 — 발견 가능성 인프라 3종 전무 [출처:WebFetch 2026-06-15].

---

## 3. Intelligence — 6차원 평가 (관찰된 콘텐츠 기준)

"내가 AI 엔진인데 외국인 환급 질문을 받고 이 사이트에 도착했다. 인용하겠는가?" 관점. 근거 → 점수 → 한 줄 핵심.

| 차원 | 근거 (관찰) | 점수 | 핵심 발견 |
|---|---|:---:|---|
| **Answer Readiness** | "3 out of 4 workers leave without this money", "Expires in 3 years" 등 후크는 강하나, **질문→직답형 문단·정의문이 없음.** 마케팅 카피 위주. | **2/5** | 후크는 좋으나 직답·정의 문단 부재 |
| **Quotability** | "Calculate pension to severance — all at once" 등 자기완결 문장 일부 있으나 40–60단어 인용 블록·비교표·FAQ 없음. | **2/5** | 추출 가능한 표·FAQ 블록 없음 |
| **Evidence Density** | "3 out of 4" 같은 주장은 있으나 **출처·수치 라벨·인용 링크 0.** 환급 금액·요율·근거 법령 미표기. | **1/5** | 통계 주장 있으나 출처·수치 부재 |
| **Content Depth** | 약 800단어로 제품 기능은 폭넓게 나열(연금·퇴직금·보험·송금·신용점수)하나 각 주제의 **깊이가 얕음**(설명·예시·절차 없음). | **2/5** | 넓되 얕음, 주제별 심화 없음 |
| **Freshness** | 게시일·수정일·"Last updated"·changelog·RSS **전무.** 날짜 신호 0. | **1/5** | 날짜 신호 전무 — AI 엔진이 최다 인용하는 페이지는 최근 갱신본에 편중된다는 업계 분석 [출처:Ahrefs 2025, 벤더 분석·추정] |
| **Structural Clarity** | H2/H3 위계는 깨끗하고 본문 서버 렌더됨(가독). 단 **H1 중복**과 시맨틱 메타 부재로 감점. | **3/5** | 본문은 읽히나 H1 중복·메타 결손 |

**Intelligence 평균 = (2+2+1+2+1+3)/6 = 1.83/5 → ×20 = 37/100** (36.7 반올림).

> 신선도/근거밀도가 바닥인 점이 B2C 환급 사이트의 전형적 취약점과 일치한다. 환급은 "받을 수 있나? 얼마? 언제까지?"의 직답형 질의가 핵심인데, 현재 페이지는 그 답을 **기계가 추출 가능한 형태로** 담고 있지 않다.

---

## 4. 결정적 실패 목록 (Critical Failures, 우선순위순)

1. **`<title>`·meta description 완전 부재** — AI/검색이 페이지를 한 줄로 식별할 근거가 없음. 모든 인용의 0단계.
2. **JSON-LD 구조화 데이터 0** — Organization/SoftwareApplication/FAQPage 어느 것도 없어, AI가 "BackWon = 외국인 환급 서비스"라는 엔터티 사실을 못 가져감.
3. **hreflang·언어별 URL 부재 (B2C 최대 손실)** — 6개 언어 제품인데 `lang` 속성조차 ABSENT. 비영어 AI 질의에서 0 노출.
4. **H1 2개** — 주제 신호 분산. 정확히 1 H1 규칙 위반.
5. **`llms.txt`·`sitemap.xml`·`robots.txt`(+Sitemap 라인) 전무** — AI 크롤러에 사이트 지도·핵심 페이지 안내 0.
6. **Open Graph 부재** — 공유 카드·일부 AI 미리보기 근거 없음.
7. **canonical 부재** — vercel.app 임시 도메인 + 향후 커스텀 도메인(backwon.kr 등) 전환 시 중복 URL 위험.
8. **신선도 신호 0** — 게시/수정일·RSS 없음. 환급 한도·요율은 매년 바뀌므로 날짜 부재는 신뢰도 직격.
9. **근거·출처 라벨 0** — "3 out of 4" 등 통계가 출처 없이 떠 있어 AI가 인용을 꺼림. 본문 내 인용(in-text citation)·통계·인용구를 더한 콘텐츠가 가시성을 유의하게(원논문 최대 +115%) 끌어올린다는 통제 실험 결과가 있다 [출처:GEO 논문, Aggarwal et al., KDD 2024, arXiv:2311.09735].
10. **클라이언트 렌더링 리스크 [추정]** — 현재 홈은 서버 렌더 본문이 보이나, SPA 라우트(`/check` 등 404 확인)가 CSR이면 AI 크롤러가 빈 셸을 볼 수 있음 → SSR/SSG 또는 프리렌더 필요.

---

## 5. 우선순위 코드 수정안 (`improve-aeo-geo` 기반)

스택 [추정]: Vercel 배포 → Next.js 가능성 높음. 아래는 Next.js(App Router) 기준 드롭인이며, 다른 스택이면 `improve-aeo-geo` SKILL의 프레임워크별 패턴으로 치환.

### Priority 1 — Blockers (스프린트 1, 반나절)

**(a) `app/robots.ts` — AI 봇 명시 허용 + Sitemap 선언**
```typescript
import type { MetadataRoute } from 'next'
export default function robots(): MetadataRoute.Robots {
  return {
    rules: [
      { userAgent: '*', allow: '/' },
      ...['GPTBot','ClaudeBot','PerplexityBot','Google-Extended',
          'OAI-SearchBot','anthropic-ai','ChatGPT-User','Bytespider','CCBot']
        .map(ua => ({ userAgent: ua, allow: '/' })),
    ],
    sitemap: 'https://backwon.kr/sitemap.xml', // 커스텀 도메인 확정 후 교체
  }
}
```
*현재는 404라 "기본 허용"이지만, Sitemap 미선언으로 크롤 효율이 낮다. 명시 파일로 전환 권장.*

**(b) `public/.well-known/llms.txt`** (환급 도메인 특화)
```markdown
# BackWon

> 한국 체류·퇴직 외국인 근로자의 미수령 환급(국민연금 반환일시금·퇴직금·출국만기보험·고용보험)을
> 모국어로 확인·청구하도록 돕는 B2C 서비스. 6개 언어 지원[SSOT]. PlugNX의 ForeignID 본인인증 기반.

## 핵심 페이지
- [환급 확인 / Check your refund](https://backwon.kr/check)
- [국민연금 반환일시금 안내](https://backwon.kr/guide/pension-lump-sum)
- [퇴직금·출국만기보험 안내](https://backwon.kr/guide/severance)
- [급여 적정성 진단](https://backwon.kr/guide/wage-check)
- [자주 묻는 질문 / FAQ](https://backwon.kr/faq)

## 정책
- [개인정보 처리방침](https://backwon.kr/privacy)
- [이용약관](https://backwon.kr/terms)
```

### Priority 2 — `<head>` 메타 + JSON-LD (스프린트 1, 핵심)

**(c) `app/layout.tsx` 또는 `app/page.tsx` 메타데이터**
```typescript
import type { Metadata } from 'next'
export const metadata: Metadata = {
  title: 'BackWon — 한국 떠나기 전 못 받은 환급금 찾기 (외국인 근로자)',
  description:
    '국민연금 반환일시금·퇴직금·출국만기보험 등 한국에서 일한 외국인이 받을 수 있는 미수령 환급을 모국어로 확인하세요. 급여명세서 사진 한 장이면 AI가 계산합니다. 6개 언어 지원.',
  metadataBase: new URL('https://backwon.kr'),
  alternates: {
    canonical: '/',
    // hreflang — B2C 다국어 핵심. SSOT는 "6개 언어"만 확정[SSOT]; 아래 구체 언어 코드는
    // 예시[가정] — 실제 지원 언어셋으로 교체할 것(주요 송출국 기준: ko/en + 추가 4종).
    languages: {
      'ko-KR': '/ko', 'en': '/en', 'vi': '/vi',
      'km': '/km', 'ne': '/ne', 'id': '/id', 'x-default': '/',
    },
  },
  openGraph: {
    title: 'BackWon — 못 받은 한국 환급금, 모국어로 확인',
    description: '국민연금·퇴직금·보험 미수령금 확인. 급여명세서 한 장으로 AI 계산.',
    url: 'https://backwon.kr', type: 'website',
    images: [{ url: '/og-backwon.png', width: 1200, height: 630 }],
  },
  robots: { index: true, follow: true },
}
```
*`<html lang>`도 언어별로 세팅: 영어 진입은 `lang="en"`, 한국어는 `lang="ko"`. 현재 lang 속성 ABSENT가 다국어 AEO의 1차 결손.*

**(d) Organization + SoftwareApplication + FAQPage JSON-LD** (`page.tsx`에 `<script type="application/ld+json">`로 주입)
```json
[
  {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "BackWon",
    "url": "https://backwon.kr",
    "parentOrganization": { "@type": "Organization", "name": "PlugNX" },
    "description": "한국 체류·퇴직 외국인 근로자의 미수령 환급 확인·청구 B2C 서비스",
    "availableLanguage": ["ko","en","vi","km","ne","id"]
  },
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "BackWon",
    "applicationCategory": "FinanceApplication",
    "operatingSystem": "Web, iOS, Android",
    "inLanguage": ["ko","en","vi","km","ne","id"],
    "offers": { "@type": "Offer", "price": "0", "priceCurrency": "KRW" }
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "한국을 떠나는 외국인은 어떤 환급을 받을 수 있나요?",
        "acceptedAnswer": { "@type": "Answer",
          "text": "근무 형태에 따라 국민연금 반환일시금, 퇴직금, 출국만기보험금, 고용보험 등을 받을 수 있습니다(추정). 실제 수령 가능 여부와 금액은 국민연금공단·고용센터·보험사 조회로만 확정됩니다." }
      },
      {
        "@type": "Question",
        "name": "환급 청구는 언제까지 해야 하나요?",
        "acceptedAnswer": { "@type": "Answer",
          "text": "환급 항목별로 소멸시효가 다릅니다. 일부 항목은 청구권에 기한이 있으므로 출국 전·후 가능한 빨리 확인하는 것이 안전합니다(참고용, 최신 법령 확인 필요)." }
      }
    ]
  }
]
```
*FAQ는 **콘텐츠로도 본문에 노출**해야 인용된다(스키마만으론 부족). 질문→직답형 FAQ 본문을 갖춘 페이지가 AI 인용률이 뚜렷이 높다는 업계 분석 [출처:AirOps 2025, 벤더 분석·추정].*

### Priority 3 — 콘텐츠 구조 (스프린트 2)

- **H1 1개로 통합:** `<h1>한국에서 일한 외국인을 위한 환급금 확인 — BackWon</h1>` 하나만. "Protect your money"는 H2로 강등.
- **Answer-first 재구성:** 각 H2/H3 아래 첫 1–2문장에 직답 + 수치/출처. 예: "국민연금 반환일시금이란? — 한국에서 국민연금을 낸 외국인이 출국·자격상실 시 낸 보험료에 이자를 더해 일시금으로 돌려받는 제도입니다(추정·참고용)." AI 인용은 페이지 상단부 콘텐츠에 편중되는 경향이 있다는 분석이 있다 [출처:Growth Memo 2026, 벤더 분석·추정].
- **환급별 정의/비교 블록 + 표:** 항목·대상·근거·시효를 표로. 구조화된 비교표는 추출·인용에 유리하다 [출처:AirOps 2025, 벤더 분석·추정].
- **신선도:** 각 가이드에 "최종 업데이트: YYYY-MM-DD" 가시 노출 + `article:modified_time`. 요율·한도는 매년 변동.
- **출처 라벨:** "3 out of 4" 류 통계에 1차 출처(국민연금공단·고용노동부) 링크. 본문 내 인용 추가는 가시성을 유의하게 끌어올린다(원논문 최대 +115%) [출처:GEO 논문, KDD 2024, arXiv:2311.09735].

### Priority 4 — 다국어 GEO (B2C 차별 포인트, 스프린트 2–3)

- **언어별 정적 URL + hreflang 상호참조:** `/ko /en /vi /km /ne /id`, 각 페이지 `<head>`에 6개+`x-default` `<link rel="alternate" hreflang>`. 현재 0 → 비영어 AI 질의 노출의 전제.
- **번역은 메타·H1·FAQ까지:** title/description/FAQ를 언어별 번역(MT 후 모국어 검수). 다국어 GEO는 로컬라이즈된 메타+크롤 가능 구조가 핵심 [출처:RWS 2025, betterdocs 2025].
- **SSR/SSG 확인:** 언어별 페이지가 CSR이면 크롤러가 빈 셸을 봄. Next.js `generateStaticParams`로 프리렌더.
- **sitemap.xml에 hreflang 엔트리 + lastmod:** 언어별 URL 전부 포함.

### 수정 후 예상 점수 [추정/목표]

| 단계 | Foundational | Intelligence | 최종 | 등급 |
|---|---:|---:|---:|---|
| 현재 (실측) | 32 | 37 | **35** | F |
| P1+P2 적용 후 [추정/목표] | ~78 | ~55 | **~67** | C+ |
| P3+P4 적용 후 [추정/목표] | ~90 | ~75 | **~83** | B+ |

목표는 80+(B+). P1+P2만으로 title·meta·canonical·OG·schema·llms.txt·robots 7체크가 한 번에 통과되어 점프 폭이 가장 크다(80/20).

---

## 6. 팩 #10 대비 새 가치 (중복 회피)

| 구분 | 팩 #10 §6 (VisaDesk) | 본 팩 (BackWon) |
|---|---|---|
| 대상 | B2B 영문 랜딩(VisaDesk 데모) | **BackWon B2C 환급·금융 랜딩(기존 moneeback.vercel.app)** |
| 언어 | 단일(영문) | **6개 언어 → hreflang·언어별 URL 전략 신규** |
| 스키마 초점 | Organization/SoftwareApplication/Product/Article | **FAQPage(환급 Q&A)·SoftwareApplication(FinanceApplication)** |
| 고유 리스크 | 대시보드 라우트 중복 H1 | **H1 2개·SPA CSR 빈 셸·환급 수치 규제 안전문구** |
| 점수 | C- (56) | **F (35)** — 더 낮음, 그래서 P1+P2 ROI가 더 큼 |

본 팩이 **새로 더하는 3가지:** (1) 다국어 hreflang/lang 결손을 B2C 최대 손실로 정량화, (2) 환급 도메인 특화 FAQPage·llms.txt 드롭인, (3) "환급 금액·시효는 추정·참고용" 규제 안전 문구를 스키마/카피에 내장하는 법.

---

## 참고·한계 (Caveats)

- **법적 효력 없는 참고 정보:** 본 감사는 웹 발견성(AEO/GEO) 진단이며, 환급 가능 여부·금액·시효, 비자·노무·세무·KYC 판단은 **행정사·노무사·변호사·세무사 검증과 1차 출처(국민연금공단·고용노동부·하이코리아 등) 최신 확인**이 필요하다. 제안 카피·FAQ·스키마의 모든 환급 표현은 "추정·참고용, 확정은 소관기관 조회"를 병기해야 한다.
- **민감정보:** 본 산출물에는 여권번호·외국인등록번호·계좌·생체정보 실제 값을 일절 쓰지 않았다. 제품 구현 시 급여명세서·신분증 이미지의 수집·OCR·보관에는 목적·동의·보관기간·암호화·접근통제·파기정책이 선결되어야 한다.
- **측정 범위:** foundational 신호는 [출처:WebFetch 2026-06-15] 실측이나 **단일 홈페이지(n=1) 크롤**이며, image-alt·internal-links·SPA 하위 라우트 렌더링은 미확인 → 해당 항목은 [추정]으로 보수 처리했다. 사이트 전체 크롤(`audit-website-aeo` 스크립트, 최대 30p) 시 점수가 하향 조정될 수 있다.
- **수치 라벨:** 모든 점수·예상 개선치는 [추정/목표(가정)]이며 확정 매출·성과 전망이 아니다. SSOT 사업 수치는 본 감사 범위 밖이다.
- **GEO 통계 출처 구분:** 통제 실험 1차 근거는 [출처:GEO 논문, Aggarwal et al., KDD 2024, arXiv:2311.09735](본문 내 인용·통계·인용구가 가시성을 유의하게 향상, 최대 +115%) 하나다. [출처:Growth Memo 2026]·[출처:AirOps 2025]·[출처:Ahrefs 2025]의 구체 수치(상단부 인용 편중·FAQ/비교표 인용률·30일 신선도 등)는 **벤더 블로그 분석·추정**으로, 방향성은 일관되나 절대 수치는 독립 검증되지 않았으므로 단정하지 않고 directional 근거로만 사용한다. 다국어 GEO는 [출처:RWS 2025](https://www.rws.com/blog/generative-engine-optimization-geo-for-multilingualbrands/)·[출처:betterdocs 2025](https://betterdocs.co/optimize-multilingual-documentation-for-geo) 참고. 모든 출처는 본 스킬(`audit-website-aeo`·`improve-aeo-geo`) SKILL.md에 인용된 자료다.
- **재측정:** P1+P2 적용 후 동일 URL로 본 감사를 재실행해 32→목표 점수 도달을 검증할 것(`improve-aeo-geo` Step 5).
