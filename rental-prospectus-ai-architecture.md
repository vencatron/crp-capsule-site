# Rental Property AI Prospectus Platform
## Innovative Technical Architecture Document

**Version:** 1.0 Draft
**Date:** December 2024
**Status:** Concept Architecture

---

## Table of Contents

1. [Executive Vision](#1-executive-vision)
2. [Architectural Philosophy](#2-architectural-philosophy)
3. [System Overview](#3-system-overview)
4. [Data Intelligence Layer](#4-data-intelligence-layer)
5. [Multi-Agent AI System](#5-multi-agent-ai-system)
6. [Analysis Engine](#6-analysis-engine)
7. [Report Generation Pipeline](#7-report-generation-pipeline)
8. [Real-Time Processing](#8-real-time-processing)
9. [B2B Integration Architecture](#9-b2b-integration-architecture)
10. [Infrastructure & DevOps](#10-infrastructure--devops)
11. [Security & Compliance](#11-security--compliance)
12. [Phased Implementation Roadmap](#12-phased-implementation-roadmap)

---

## 1. Executive Vision

### The Problem Space

Retail real estate investors face a paradox: they have access to more property data than ever, yet making informed investment decisions remains difficult. Existing tools offer either:

- **Shallow analysis** (quick calculators with basic metrics)
- **Raw data dumps** (overwhelming without interpretation)
- **Expensive human expertise** (appraisers, analysts at $500+ per report)

### The Innovation Opportunity

We're building an **AI Investment Analyst** — not just a calculator, but a system that thinks like a seasoned real estate investor with access to comprehensive data and unlimited patience for analysis.

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   "Transform any property address into an institutional-grade  │
│    investment prospectus in under 60 seconds"                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Core Innovation Pillars

| Pillar | Innovation | Competitor Gap |
|--------|------------|----------------|
| **Intelligence** | Multi-agent AI reasoning, not templates | Others use simple formulas |
| **Context** | Property Intelligence Graph connecting all data | Others treat properties as isolated |
| **Confidence** | Uncertainty quantification on all predictions | Others give false precision |
| **Adaptability** | Living reports that update with market | Others are point-in-time snapshots |

---

## 2. Architectural Philosophy

### Guiding Principles

```
┌──────────────────────────────────────────────────────────────────────┐
│                     ARCHITECTURAL PRINCIPLES                         │
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  1. DATA AS FIRST-CLASS CITIZEN                                     │
│     └─ Quality over quantity; every data point has provenance       │
│                                                                      │
│  2. INTELLIGENCE AT THE EDGE                                        │
│     └─ Pre-compute what's predictable, reason in real-time on rest │
│                                                                      │
│  3. EXPLAINABLE BY DEFAULT                                          │
│     └─ Every recommendation traces back to evidence                 │
│                                                                      │
│  4. CONFIDENCE-AWARE                                                │
│     └─ Uncertainty is information, not a bug to hide               │
│                                                                      │
│  5. HEADLESS FIRST                                                  │
│     └─ API-first design enables any consumption pattern            │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

### Architecture Style: Event-Driven Intelligence Mesh

Rather than a traditional monolith or microservices spaghetti, we employ an **Intelligence Mesh** pattern:

```
                    ┌─────────────────────────────────────┐
                    │         EVENT BACKBONE              │
                    │   (Kafka / AWS EventBridge)         │
                    └──────────────┬──────────────────────┘
                                   │
        ┌──────────────────────────┼──────────────────────────┐
        │                          │                          │
        ▼                          ▼                          ▼
┌───────────────┐        ┌─────────────────┐        ┌────────────────┐
│  DATA AGENTS  │        │ ANALYSIS AGENTS │        │ DELIVERY AGENTS│
│               │        │                 │        │                │
│ • Ingest      │───────▶│ • Financial     │───────▶│ • Report Gen   │
│ • Validate    │        │ • Risk          │        │ • API          │
│ • Enrich      │        │ • Market        │        │ • Webhooks     │
│ • Store       │        │ • Comparable    │        │ • Embeds       │
└───────────────┘        └─────────────────┘        └────────────────┘
        │                          │                          │
        └──────────────────────────┴──────────────────────────┘
                                   │
                    ┌──────────────▼──────────────────────┐
                    │     PROPERTY INTELLIGENCE GRAPH     │
                    │        (Central Knowledge Base)     │
                    └─────────────────────────────────────┘
```

**Benefits:**
- Agents evolve independently
- New data sources plug in without rewiring
- Analysis scales horizontally
- Real-time and batch processing unified

---

## 3. System Overview

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                              PRESENTATION LAYER                                  │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│   ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    │
│   │  Web App    │    │  B2B Portal │    │  Embeddable │    │  API/SDK    │    │
│   │  (Next.js)  │    │  Dashboard  │    │  Widgets    │    │  (REST/GQL) │    │
│   └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘    │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
                                        │
                                        ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                              GATEWAY LAYER                                       │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│   ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐           │
│   │  API Gateway    │    │  Auth Service   │    │  Rate Limiter   │           │
│   │  (Kong/AWS)     │    │  (Clerk/Auth0)  │    │  & Metering     │           │
│   └─────────────────┘    └─────────────────┘    └─────────────────┘           │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
                                        │
                                        ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           INTELLIGENCE LAYER                                     │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│   ┌───────────────────────────────────────────────────────────────────────┐   │
│   │                    MULTI-AGENT ORCHESTRATOR                            │   │
│   │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐    │   │
│   │  │Financial │ │  Risk    │ │  Market  │ │  Comp    │ │  Writer  │    │   │
│   │  │ Analyst  │ │ Analyst  │ │ Analyst  │ │ Analyst  │ │  Agent   │    │   │
│   │  └──────────┘ └──────────┘ └──────────┘ └──────────┘ └──────────┘    │   │
│   └───────────────────────────────────────────────────────────────────────┘   │
│                                                                                 │
│   ┌───────────────────────────────────────────────────────────────────────┐   │
│   │                    ANALYSIS ENGINE                                     │   │
│   │  • Cash Flow Models    • Risk Scoring    • Valuation Models           │   │
│   │  • Scenario Engine     • Comp Matching   • Trend Analysis             │   │
│   └───────────────────────────────────────────────────────────────────────┘   │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
                                        │
                                        ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                              DATA LAYER                                          │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│   ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    │
│   │  Property   │    │  Knowledge  │    │   Vector    │    │   Cache     │    │
│   │  Graph DB   │    │  Store      │    │   Store     │    │   Layer     │    │
│   │  (Neo4j)    │    │ (Postgres)  │    │ (Pinecone)  │    │  (Redis)    │    │
│   └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘    │
│                                                                                 │
│   ┌─────────────────────────────────────────────────────────────────────────┐ │
│   │                     DATA INGESTION PIPELINE                              │ │
│   │  Property APIs → Enrichment → Validation → Storage → Indexing           │ │
│   └─────────────────────────────────────────────────────────────────────────┘ │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Data Intelligence Layer

### The Property Intelligence Graph

Instead of flat database tables, we model real estate as an interconnected knowledge graph. This enables sophisticated queries and relationship-based insights.

```
                              ┌─────────────┐
                              │   MARKET    │
                              │  (Austin)   │
                              └──────┬──────┘
                                     │ contains
                    ┌────────────────┼────────────────┐
                    ▼                ▼                ▼
            ┌───────────┐    ┌───────────┐    ┌───────────┐
            │SUBMARKET  │    │SUBMARKET  │    │SUBMARKET  │
            │(Downtown) │    │ (Mueller) │    │ (Domain)  │
            └─────┬─────┘    └─────┬─────┘    └─────┬─────┘
                  │                │                │
                  ▼                ▼                ▼
            ┌───────────┐    ┌───────────┐    ┌───────────┐
            │NEIGHBORHOOD│   │NEIGHBORHOOD│   │NEIGHBORHOOD│
            │ (Rainey)  │    │(Mueller E)│    │ (Arboretum)│
            └─────┬─────┘    └─────┬─────┘    └─────┬─────┘
                  │                │                │
        ┌─────────┼─────────┐     │          ┌─────┴─────┐
        ▼         ▼         ▼     ▼          ▼           ▼
    ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐
    │PROPERTY│ │PROPERTY│ │PROPERTY│ │PROPERTY│ │PROPERTY│ │PROPERTY│
    │  #1   │ │  #2   │ │  #3   │ │  #4   │ │  #5   │ │  #6   │
    └───┬───┘ └───────┘ └───┬───┘ └───────┘ └───────┘ └───────┘
        │                   │
        │ similar_to        │ similar_to
        └───────────────────┘
```

### Graph Relationships

| Relationship | Description | Example Query |
|-------------|-------------|---------------|
| `LOCATED_IN` | Property → Neighborhood | Find all properties in a neighborhood |
| `SIMILAR_TO` | Property ↔ Property | Find comparable properties |
| `SOLD_AS` | Property → Transaction | Track price history |
| `RENTED_AS` | Property → Lease | Track rental history |
| `NEAR` | Property ↔ Amenity | Walkability analysis |
| `AFFECTED_BY` | Property → Risk Factor | Risk propagation |
| `TRENDING_LIKE` | Neighborhood ↔ Neighborhood | Pattern matching |

### Data Schema: Core Entities

```typescript
// Property Node
interface Property {
  id: string;
  address: Address;
  characteristics: {
    bedrooms: number;
    bathrooms: number;
    sqft: number;
    lotSize: number;
    yearBuilt: number;
    propertyType: 'SFH' | 'Condo' | 'Townhouse' | 'Multi';
    stories: number;
    garage: number;
    pool: boolean;
    // ... 50+ attributes
  };
  condition: ConditionAssessment;  // AI-derived from photos
  valuations: Valuation[];
  rentalEstimates: RentalEstimate[];
  riskProfile: RiskProfile;
  lastUpdated: DateTime;
  dataProvenance: DataSource[];    // Track where each data point came from
}

// Neighborhood Node
interface Neighborhood {
  id: string;
  name: string;
  boundaries: GeoJSON;
  demographics: Demographics;
  economics: {
    medianIncome: number;
    employmentRate: number;
    primaryEmployers: string[];
  };
  schools: School[];
  crime: CrimeStats;
  amenities: Amenity[];
  marketMetrics: {
    medianHomePrice: number;
    medianRent: number;
    daysOnMarket: number;
    inventoryLevel: number;
    pricePerSqft: number;
  };
  trends: TrendData[];
  riskFactors: RiskFactor[];
}

// Transaction Edge
interface Transaction {
  property: Property;
  date: DateTime;
  salePrice: number;
  pricePerSqft: number;
  daysOnMarket: number;
  saleType: 'Market' | 'Foreclosure' | 'ShortSale' | 'Auction';
  financing: 'Cash' | 'Conventional' | 'FHA' | 'VA';
  seller: Entity;
  buyer: Entity;
}
```

### Multi-Source Data Fusion

**The Challenge:** Different data sources have different strengths, freshness, and accuracy. We need intelligent fusion.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                       DATA FUSION PIPELINE                               │
└─────────────────────────────────────────────────────────────────────────┘

  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
  │ Attom    │   │RealtyMole│   │ Public   │   │ MLS/IDX  │
  │ Data     │   │   API    │   │ Records  │   │  Feed    │
  └────┬─────┘   └────┬─────┘   └────┬─────┘   └────┬─────┘
       │              │              │              │
       ▼              ▼              ▼              ▼
  ┌─────────────────────────────────────────────────────────────────────┐
  │                     INGESTION LAYER                                  │
  │  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐               │
  │  │ Adapter │  │ Adapter │  │ Adapter │  │ Adapter │               │
  │  │   A     │  │   B     │  │   C     │  │   D     │               │
  │  └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘               │
  │       └────────────┼───────────┼───────────┘                       │
  │                    ▼           ▼                                    │
  │              ┌─────────────────────────┐                           │
  │              │   CANONICAL SCHEMA      │                           │
  │              │   TRANSFORMATION        │                           │
  │              └───────────┬─────────────┘                           │
  └──────────────────────────┼──────────────────────────────────────────┘
                             ▼
  ┌─────────────────────────────────────────────────────────────────────┐
  │                    FUSION ENGINE                                     │
  │                                                                      │
  │  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐        │
  │  │   CONFLICT     │  │   CONFIDENCE   │  │   FRESHNESS    │        │
  │  │   RESOLUTION   │  │   WEIGHTING    │  │   SCORING      │        │
  │  └───────┬────────┘  └───────┬────────┘  └───────┬────────┘        │
  │          └───────────────────┼───────────────────┘                  │
  │                              ▼                                       │
  │                   ┌─────────────────────┐                           │
  │                   │   GOLDEN RECORD     │                           │
  │                   │   CREATION          │                           │
  │                   └─────────────────────┘                           │
  └─────────────────────────────────────────────────────────────────────┘
```

**Fusion Rules Example:**

```python
# Pseudocode for intelligent data fusion
class PropertyFusion:

    SOURCE_CONFIDENCE = {
        'mls': 0.95,      # Most accurate, most fresh
        'attom': 0.85,    # Comprehensive, slight lag
        'public_records': 0.99,  # Official but delayed
        'realtymole': 0.80,      # Good coverage, varied quality
    }

    def fuse_property(self, property_id: str) -> GoldenRecord:
        records = self.fetch_all_sources(property_id)

        golden = GoldenRecord()

        for field in PROPERTY_FIELDS:
            values = [(r.source, r.get(field), r.timestamp) for r in records]

            # Weighted voting with freshness decay
            golden[field] = self.resolve_field(
                values,
                conflict_strategy=self.get_strategy(field),
                freshness_weight=0.3
            )

            # Track provenance and confidence
            golden.provenance[field] = self.compute_provenance(values)
            golden.confidence[field] = self.compute_confidence(values)

        return golden

    def get_strategy(self, field: str) -> str:
        # Different fields need different resolution strategies
        strategies = {
            'bedrooms': 'mode',           # Most common value wins
            'sqft': 'weighted_average',   # Average with confidence weights
            'price': 'most_recent',       # Latest value wins
            'yearBuilt': 'authoritative', # Public records wins
        }
        return strategies.get(field, 'weighted_average')
```

### Alternative Data Sources (Innovation Opportunity)

Beyond traditional property data, we can incorporate alternative signals:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    ALTERNATIVE DATA ENRICHMENT                          │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌─────────────────┐                                                   │
│  │ PERMIT DATA     │  → Renovation activity, neighborhood investment  │
│  │ (Local govt)    │    Signal: Rising permits = appreciation coming  │
│  └─────────────────┘                                                   │
│                                                                         │
│  ┌─────────────────┐                                                   │
│  │ BUSINESS DATA   │  → New businesses, closures, foot traffic        │
│  │ (Yelp, Google)  │    Signal: Coffee shops appearing = gentrifying  │
│  └─────────────────┘                                                   │
│                                                                         │
│  ┌─────────────────┐                                                   │
│  │ SATELLITE IMG   │  → Construction, parking, green space changes    │
│  │ (Mapbox, Google)│    Signal: New development = supply increase     │
│  └─────────────────┘                                                   │
│                                                                         │
│  ┌─────────────────┐                                                   │
│  │ RENTAL LISTINGS │  → Actual asking rents, days on market           │
│  │ (Apartments.com)│    Signal: Real-time rent validation            │
│  └─────────────────┘                                                   │
│                                                                         │
│  ┌─────────────────┐                                                   │
│  │ SOCIAL SIGNALS  │  → Reddit/Twitter sentiment, neighborhood vibe  │
│  │ (Reddit, X)     │    Signal: Community perception, safety feels   │
│  └─────────────────┘                                                   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 5. Multi-Agent AI System

### The Innovation: Specialized Reasoning Agents

Instead of a single monolithic prompt, we orchestrate **specialized AI agents** that collaborate like an investment committee.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     INVESTMENT COMMITTEE AI                              │
│                     (Multi-Agent Orchestration)                          │
└─────────────────────────────────────────────────────────────────────────┘

                         ┌──────────────────┐
                         │   ORCHESTRATOR   │
                         │     AGENT        │
                         │                  │
                         │ • Task routing   │
                         │ • Synthesis      │
                         │ • Conflict res.  │
                         └────────┬─────────┘
                                  │
            ┌─────────────────────┼─────────────────────┐
            │                     │                     │
            ▼                     ▼                     ▼
   ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
   │   FINANCIAL     │  │     RISK        │  │    MARKET       │
   │   ANALYST       │  │   ANALYST       │  │   ANALYST       │
   │                 │  │                 │  │                 │
   │ • Cash flow     │  │ • Property risk │  │ • Neighborhood  │
   │ • NOI/Cap rate  │  │ • Market risk   │  │ • Comp analysis │
   │ • Financing     │  │ • Tenant risk   │  │ • Trend forecast│
   │ • Scenarios     │  │ • Macro risk    │  │ • Supply/demand │
   │                 │  │                 │  │                 │
   │ Personality:    │  │ Personality:    │  │ Personality:    │
   │ Conservative,   │  │ Skeptical,      │  │ Data-driven,    │
   │ numbers-focused │  │ worst-case      │  │ pattern seeker  │
   └─────────────────┘  └─────────────────┘  └─────────────────┘
            │                     │                     │
            └─────────────────────┼─────────────────────┘
                                  ▼
                    ┌───────────────────────┐
                    │      WRITER           │
                    │      AGENT            │
                    │                       │
                    │ • Synthesize findings │
                    │ • Generate narrative  │
                    │ • Ensure consistency  │
                    │ • Format report       │
                    └───────────────────────┘
```

### Agent Specifications

```python
# Agent Definition Schema

class FinancialAnalystAgent:
    """
    Specializes in property-level financial analysis.
    Thinks like a conservative real estate accountant.
    """

    role = "Financial Analyst"

    personality = """
    You are a conservative financial analyst specializing in rental
    properties. You've seen too many investors overlook expenses and
    overestimate income. Your job is to provide realistic, defensible
    financial projections. When in doubt, be conservative.
    """

    capabilities = [
        "cash_flow_analysis",
        "financing_scenarios",
        "expense_estimation",
        "return_calculations",
        "sensitivity_analysis",
    ]

    tools = [
        MortgageCalculator(),
        ExpenseEstimator(),
        RentComparator(),
        CapRateAnalyzer(),
    ]

    output_schema = FinancialAnalysisReport


class RiskAnalystAgent:
    """
    Specializes in identifying and quantifying investment risks.
    Thinks like a skeptical insurance underwriter.
    """

    role = "Risk Analyst"

    personality = """
    You are a risk analyst who has seen countless real estate
    investments go wrong. Your job is to identify every possible
    risk and quantify its potential impact. You're not a pessimist—
    you're a realist who helps investors make informed decisions.
    """

    capabilities = [
        "property_risk_assessment",
        "market_risk_analysis",
        "tenant_risk_profiling",
        "environmental_risk",
        "regulatory_risk",
    ]

    risk_categories = {
        "property": ["deferred_maintenance", "functional_obsolescence", "foundation", "roof"],
        "market": ["oversupply", "demand_decline", "rate_sensitivity", "recession"],
        "tenant": ["vacancy", "credit_risk", "turnover", "eviction"],
        "location": ["crime_trend", "school_quality", "employer_dependency"],
        "regulatory": ["rent_control", "zoning", "tax_changes"],
    }


class MarketAnalystAgent:
    """
    Specializes in neighborhood and market analysis.
    Thinks like a local real estate expert with data superpowers.
    """

    role = "Market Analyst"

    personality = """
    You are a market analyst who combines deep local knowledge with
    rigorous data analysis. You understand that real estate is hyper-local—
    two blocks can make all the difference. Your job is to contextualize
    this property within its market and identify trends.
    """

    capabilities = [
        "neighborhood_analysis",
        "comparable_selection",
        "trend_identification",
        "supply_demand_analysis",
        "appreciation_forecasting",
    ]
```

### Agent Communication Protocol

Agents communicate through structured messages with clear handoffs:

```typescript
interface AgentMessage {
  from: AgentRole;
  to: AgentRole | 'orchestrator';
  type: 'analysis' | 'question' | 'disagreement' | 'synthesis';
  content: {
    findings: Finding[];
    confidence: number;  // 0-1
    caveats: string[];
    dataUsed: DataReference[];
    questionsForOthers?: Question[];
  };
}

// Example: Risk agent disagrees with Financial agent's vacancy assumption
const disagreementMessage: AgentMessage = {
  from: 'risk_analyst',
  to: 'orchestrator',
  type: 'disagreement',
  content: {
    findings: [{
      topic: 'vacancy_rate',
      position: 'Financial analyst used 5% vacancy, but neighborhood data shows 8% average with increasing trend',
      evidence: ['neighborhood_vacancy_data', 'recent_listing_duration'],
      recommendation: 'Adjust vacancy assumption to 8-10%'
    }],
    confidence: 0.85,
    caveats: ['Based on last 12 months; seasonal adjustment not applied'],
    dataUsed: [
      { source: 'rentometer', field: 'vacancy_rate', value: 0.082 },
      { source: 'census', field: 'rental_vacancy', value: 0.079 }
    ]
  }
};
```

### Orchestration Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    ANALYSIS ORCHESTRATION FLOW                           │
└─────────────────────────────────────────────────────────────────────────┘

  User Request: "Analyze 123 Main St"
          │
          ▼
  ┌───────────────────────────────────────────────────────────────────┐
  │  PHASE 1: DATA GATHERING                                          │
  │  • Pull property data from graph                                  │
  │  • Retrieve neighborhood context                                   │
  │  • Fetch comparables                                               │
  │  • Gather market data                                              │
  │  Time: ~2 seconds                                                  │
  └───────────────────────────────────────────────────────────────────┘
          │
          ▼
  ┌───────────────────────────────────────────────────────────────────┐
  │  PHASE 2: PARALLEL ANALYSIS (Agents work simultaneously)          │
  │                                                                    │
  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐            │
  │  │ Financial    │  │    Risk      │  │   Market     │            │
  │  │  Analysis    │  │   Analysis   │  │  Analysis    │            │
  │  │   (5 sec)    │  │   (5 sec)    │  │   (5 sec)    │            │
  │  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘            │
  │         └─────────────────┼─────────────────┘                     │
  │                           ▼                                        │
  │  Total Time: ~5 seconds (parallel)                                 │
  └───────────────────────────────────────────────────────────────────┘
          │
          ▼
  ┌───────────────────────────────────────────────────────────────────┐
  │  PHASE 3: SYNTHESIS & CONFLICT RESOLUTION                         │
  │  • Orchestrator reviews all analyses                               │
  │  • Identifies conflicts (e.g., different assumptions)             │
  │  • Requests clarification if needed                                │
  │  • Synthesizes unified view                                        │
  │  Time: ~3 seconds                                                  │
  └───────────────────────────────────────────────────────────────────┘
          │
          ▼
  ┌───────────────────────────────────────────────────────────────────┐
  │  PHASE 4: REPORT GENERATION                                        │
  │  • Writer agent crafts narrative                                   │
  │  • Incorporates all findings                                       │
  │  • Generates recommendations                                       │
  │  • Formats output (HTML/PDF/JSON)                                  │
  │  Time: ~8 seconds                                                  │
  └───────────────────────────────────────────────────────────────────┘
          │
          ▼
  Total End-to-End: ~18 seconds
```

---

## 6. Analysis Engine

### Cash Flow Model

```typescript
interface CashFlowAnalysis {
  // Income
  grossPotentialRent: MonthlyAmount;
  otherIncome: MonthlyAmount;        // Laundry, parking, storage
  vacancyAllowance: Percentage;       // Data-driven, not assumed
  effectiveGrossIncome: MonthlyAmount;

  // Expenses
  operatingExpenses: {
    propertyTax: AnnualAmount;        // From public records
    insurance: AnnualAmount;          // Estimated by property type/location
    propertyManagement: Percentage;   // Typically 8-10%
    maintenance: AnnualAmount;        // Age/condition-based model
    utilities: MonthlyAmount;         // If landlord-paid
    hoa: MonthlyAmount;               // If applicable
    capexReserve: Percentage;         // For roof, HVAC, etc.
  };
  netOperatingIncome: AnnualAmount;

  // Debt Service
  mortgage: {
    principal: Amount;
    interestRate: Percentage;
    term: Years;
    monthlyPayment: MonthlyAmount;
    annualDebtService: AnnualAmount;
  };

  // Returns
  cashFlow: {
    monthly: MonthlyAmount;
    annual: AnnualAmount;
  };
  metrics: {
    capRate: Percentage;
    cashOnCashReturn: Percentage;
    dscr: Ratio;                      // Debt Service Coverage Ratio
    breakEvenOccupancy: Percentage;
  };

  // Confidence
  confidence: {
    overall: Percentage;
    rentEstimate: Percentage;
    expenseEstimate: Percentage;
  };
}
```

### Expense Estimation Model

```python
class ExpenseEstimator:
    """
    Data-driven expense estimation based on property characteristics
    and local market data.
    """

    def estimate_maintenance(self, property: Property) -> ExpenseEstimate:
        """
        Maintenance costs vary significantly by age, condition, and type.
        We use a regression model trained on actual expense data.
        """

        base_rate = 0.01  # 1% of property value baseline

        # Age adjustment (older = higher maintenance)
        age = current_year - property.year_built
        age_factor = 1.0 + (age / 100) * 0.5  # +50% at 100 years

        # Condition adjustment (from photo analysis)
        condition_factors = {
            'excellent': 0.7,
            'good': 0.9,
            'fair': 1.2,
            'poor': 1.8,
        }
        condition_factor = condition_factors[property.condition]

        # Property type adjustment
        type_factors = {
            'sfh': 1.0,
            'condo': 0.6,    # HOA covers some
            'townhouse': 0.8,
            'multi': 1.3,    # More systems
        }
        type_factor = type_factors[property.type]

        # Local labor cost adjustment
        labor_factor = self.get_local_labor_index(property.zip_code)

        # Calculate estimate with confidence interval
        point_estimate = (
            property.value *
            base_rate *
            age_factor *
            condition_factor *
            type_factor *
            labor_factor
        )

        return ExpenseEstimate(
            low=point_estimate * 0.7,
            expected=point_estimate,
            high=point_estimate * 1.5,
            confidence=self.calculate_confidence(property)
        )
```

### Risk Scoring Framework

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         RISK SCORING MODEL                               │
└─────────────────────────────────────────────────────────────────────────┘

  OVERALL RISK SCORE = Weighted combination of category scores

  ┌───────────────────────────────────────────────────────────────────────┐
  │  PROPERTY RISK (25% weight)                                           │
  │  ├─ Age Score: f(year_built, renovations)                            │
  │  ├─ Condition Score: f(photo_analysis, maintenance_history)          │
  │  ├─ Functional Score: f(layout, parking, amenities vs market)        │
  │  └─ CapEx Score: f(roof_age, hvac_age, major_systems)               │
  └───────────────────────────────────────────────────────────────────────┘

  ┌───────────────────────────────────────────────────────────────────────┐
  │  MARKET RISK (25% weight)                                             │
  │  ├─ Supply Score: f(inventory_levels, new_construction)              │
  │  ├─ Demand Score: f(population_growth, job_growth)                   │
  │  ├─ Volatility Score: f(price_variance, rent_variance)               │
  │  └─ Affordability Score: f(price_to_income, rent_to_income)          │
  └───────────────────────────────────────────────────────────────────────┘

  ┌───────────────────────────────────────────────────────────────────────┐
  │  LOCATION RISK (25% weight)                                           │
  │  ├─ Crime Score: f(crime_rate, crime_trend)                          │
  │  ├─ School Score: f(school_ratings, school_trend)                    │
  │  ├─ Economic Score: f(employer_diversity, unemployment)              │
  │  └─ Amenity Score: f(walkability, transit, services)                 │
  └───────────────────────────────────────────────────────────────────────┘

  ┌───────────────────────────────────────────────────────────────────────┐
  │  TENANT RISK (25% weight)                                             │
  │  ├─ Vacancy Score: f(market_vacancy, seasonal_pattern)               │
  │  ├─ Tenant Quality Score: f(area_income, credit_distribution)        │
  │  ├─ Turnover Score: f(avg_tenancy, moving_patterns)                  │
  │  └─ Rent Collection Score: f(eviction_rates, economic_stability)     │
  └───────────────────────────────────────────────────────────────────────┘

                                    │
                                    ▼
                    ┌───────────────────────────────┐
                    │      COMPOSITE RISK SCORE     │
                    │                               │
                    │   1-3: Low Risk    (Green)    │
                    │   4-5: Moderate    (Yellow)   │
                    │   6-7: Elevated    (Orange)   │
                    │   8-10: High Risk  (Red)      │
                    │                               │
                    │   + Confidence Interval       │
                    │   + Key Risk Factors List     │
                    │   + Mitigation Suggestions    │
                    └───────────────────────────────┘
```

### Comparable Property Matching Algorithm

```python
class CompAnalyzer:
    """
    Intelligent comparable property selection using weighted similarity
    and market relevance scoring.
    """

    def find_comparables(
        self,
        subject: Property,
        comp_type: Literal['sales', 'rentals'],
        limit: int = 10
    ) -> List[Comparable]:

        # Phase 1: Candidate Selection (fast filter)
        candidates = self.graph.query("""
            MATCH (subject:Property {id: $subject_id})
            MATCH (comp:Property)-[:LOCATED_IN]->(n:Neighborhood)
            WHERE comp.id <> subject.id
              AND distance(subject.location, comp.location) < 2 miles
              AND comp.bedrooms >= subject.bedrooms - 1
              AND comp.bedrooms <= subject.bedrooms + 1
              AND comp.sqft >= subject.sqft * 0.8
              AND comp.sqft <= subject.sqft * 1.2
              AND comp.property_type = subject.property_type
              AND comp.last_transaction_date > date() - duration({months: 6})
            RETURN comp
            LIMIT 100
        """, subject_id=subject.id)

        # Phase 2: Similarity Scoring
        scored = []
        for comp in candidates:
            similarity = self.calculate_similarity(subject, comp)
            recency = self.calculate_recency_score(comp)
            relevance = self.calculate_market_relevance(comp)

            total_score = (
                similarity * 0.5 +
                recency * 0.3 +
                relevance * 0.2
            )
            scored.append((comp, total_score))

        # Phase 3: Selection with diversity
        # Don't just take top N; ensure geographic and feature diversity
        selected = self.diverse_selection(scored, limit)

        return selected

    def calculate_similarity(self, subject: Property, comp: Property) -> float:
        """
        Multi-dimensional similarity using weighted features.
        """
        weights = {
            'sqft': 0.20,
            'bedrooms': 0.15,
            'bathrooms': 0.10,
            'year_built': 0.10,
            'lot_size': 0.10,
            'condition': 0.15,
            'location': 0.20,
        }

        similarities = {}

        # Continuous features - gaussian similarity
        similarities['sqft'] = gaussian_similarity(
            subject.sqft, comp.sqft, sigma=200
        )
        similarities['year_built'] = gaussian_similarity(
            subject.year_built, comp.year_built, sigma=10
        )

        # Exact match features
        similarities['bedrooms'] = 1.0 if subject.bedrooms == comp.bedrooms else 0.5
        similarities['bathrooms'] = 1.0 if subject.bathrooms == comp.bathrooms else 0.5

        # Location - decay function based on distance
        distance = haversine(subject.location, comp.location)
        similarities['location'] = math.exp(-distance / 0.5)  # Half-mile decay

        # Condition - from photo analysis
        similarities['condition'] = self.condition_similarity(
            subject.condition, comp.condition
        )

        return sum(
            weights[k] * similarities[k]
            for k in weights
        )
```

---

## 7. Report Generation Pipeline

### Report Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    REPORT GENERATION PIPELINE                            │
└─────────────────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────────────┐
  │  STRUCTURED DATA                                                     │
  │  (From Analysis Engine)                                              │
  │                                                                      │
  │  • Financial Analysis JSON                                           │
  │  • Risk Assessment JSON                                              │
  │  • Market Analysis JSON                                              │
  │  • Comparable Data JSON                                              │
  │  • Property Data JSON                                                │
  └──────────────────────────────┬──────────────────────────────────────┘
                                 │
                                 ▼
  ┌─────────────────────────────────────────────────────────────────────┐
  │  NARRATIVE GENERATION                                                │
  │  (Writer Agent + LLM)                                                │
  │                                                                      │
  │  For each section:                                                   │
  │  1. Select relevant data points                                      │
  │  2. Generate narrative with context                                  │
  │  3. Ensure consistency with other sections                           │
  │  4. Add caveats and confidence statements                            │
  └──────────────────────────────┬──────────────────────────────────────┘
                                 │
                                 ▼
  ┌─────────────────────────────────────────────────────────────────────┐
  │  TEMPLATE HYDRATION                                                  │
  │                                                                      │
  │  ┌─────────────────────────────────────────────────────────────┐   │
  │  │  REPORT TEMPLATE (React Components)                          │   │
  │  │                                                              │   │
  │  │  <CoverPage property={} metrics={} />                       │   │
  │  │  <ExecutiveSummary narrative={} highlights={} />            │   │
  │  │  <FinancialAnalysis data={} charts={} narrative={} />       │   │
  │  │  <RiskAssessment scores={} factors={} narrative={} />       │   │
  │  │  <MarketAnalysis trends={} comps={} narrative={} />         │   │
  │  │  ...                                                         │   │
  │  └─────────────────────────────────────────────────────────────┘   │
  └──────────────────────────────┬──────────────────────────────────────┘
                                 │
           ┌─────────────────────┼─────────────────────┐
           ▼                     ▼                     ▼
  ┌─────────────┐       ┌─────────────┐       ┌─────────────┐
  │   WEB VIEW  │       │     PDF     │       │    JSON     │
  │  (HTML/CSS) │       │  (Puppeteer)│       │   (API)     │
  └─────────────┘       └─────────────┘       └─────────────┘
```

### Report Sections Detailed

```typescript
interface InvestmentProspectus {
  metadata: {
    generatedAt: DateTime;
    version: string;
    propertyId: string;
    requestedBy: string;
    confidenceLevel: 'high' | 'medium' | 'low';
  };

  sections: {
    coverPage: {
      propertyAddress: Address;
      heroImage: URL;
      keyMetrics: {
        askingPrice: Currency;
        estimatedRent: Currency;
        capRate: Percentage;
        cashOnCash: Percentage;
        riskScore: Score;
      };
      generatedDate: Date;
    };

    executiveSummary: {
      investmentThesis: string;          // 2-3 paragraph narrative
      keyHighlights: string[];           // Bullet points
      keyRisks: string[];                // Top 3 risks
      recommendation: 'strong_buy' | 'buy' | 'hold' | 'avoid';
      suggestedOfferRange: { low: Currency; high: Currency };
    };

    propertyOverview: {
      basicInfo: PropertyDetails;
      photos: Photo[];
      conditionAssessment: {
        overall: Rating;
        exterior: Rating;
        interior: Rating;
        systems: Rating;
        narrative: string;
      };
      features: Feature[];
      improvements: Improvement[];        // Known renovations
    };

    financialAnalysis: {
      purchaseAnalysis: {
        askingPrice: Currency;
        estimatedMarketValue: Currency;
        pricePerSqft: Currency;
        priceVsMarket: Percentage;
      };
      incomeAnalysis: {
        estimatedMonthlyRent: { low: Currency; expected: Currency; high: Currency };
        rentPerSqft: Currency;
        rentVsMarket: Percentage;
        vacancyAllowance: Percentage;
        effectiveGrossIncome: Currency;
      };
      expenseAnalysis: {
        propertyTax: Currency;
        insurance: Currency;
        maintenance: Currency;
        management: Currency;
        utilities: Currency;
        hoa: Currency;
        reserves: Currency;
        totalExpenses: Currency;
        expenseRatio: Percentage;
      };
      cashFlowAnalysis: {
        noi: Currency;
        debtService: Currency;
        cashFlow: Currency;
        capRate: Percentage;
        cashOnCashReturn: Percentage;
        dscr: Ratio;
      };
      financingScenarios: FinancingScenario[];  // Multiple down payment options
      sensitivityAnalysis: SensitivityMatrix;    // Rent vs vacancy impact
      charts: {
        cashFlowProjection: Chart;
        expenseBreakdown: Chart;
        returnComparison: Chart;
      };
    };

    riskAssessment: {
      overallScore: Score;
      categoryScores: {
        property: Score;
        market: Score;
        location: Score;
        tenant: Score;
      };
      keyRiskFactors: RiskFactor[];
      mitigationStrategies: Strategy[];
      riskNarrative: string;
      charts: {
        riskRadar: Chart;
        riskTrend: Chart;
      };
    };

    comparableAnalysis: {
      salesComps: Comparable[];
      rentalComps: Comparable[];
      adjustmentGrid: AdjustmentGrid;
      compMap: Map;
      narrative: string;
    };

    neighborhoodProfile: {
      overview: string;
      demographics: Demographics;
      economics: {
        medianIncome: Currency;
        incomeGrowth: Percentage;
        unemployment: Percentage;
        majorEmployers: Employer[];
      };
      schools: School[];
      crime: {
        overallScore: Score;
        trend: 'improving' | 'stable' | 'declining';
        details: CrimeStats;
      };
      amenities: {
        walkScore: Score;
        transitScore: Score;
        nearbyAmenities: Amenity[];
      };
      charts: {
        demographicBreakdown: Chart;
        incomeDistribution: Chart;
        crimeHeatmap: Map;
      };
    };

    marketOutlook: {
      currentConditions: string;
      supplyDemandAnalysis: string;
      priceTrends: TrendData;
      rentTrends: TrendData;
      forecast: {
        appreciation: { oneYear: Percentage; threeYear: Percentage; fiveYear: Percentage };
        rentGrowth: { oneYear: Percentage; threeYear: Percentage; fiveYear: Percentage };
        confidence: Percentage;
      };
      charts: {
        priceHistory: Chart;
        rentHistory: Chart;
        forecastCone: Chart;
      };
    };

    investmentRecommendation: {
      summary: string;
      pros: string[];
      cons: string[];
      suggestedOfferPrice: Currency;
      expectedReturns: {
        yearOne: Returns;
        yearThree: Returns;
        yearFive: Returns;
      };
      exitStrategies: ExitStrategy[];
      finalThoughts: string;
    };

    appendices: {
      methodology: string;
      dataSources: DataSource[];
      assumptions: Assumption[];
      glossary: Term[];
      disclaimer: string;
    };
  };
}
```

### Interactive Report Features (Innovation)

Beyond static PDFs, we offer **Living Reports**:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    INTERACTIVE REPORT FEATURES                          │
└─────────────────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────────────┐
  │  SCENARIO SLIDERS                                                    │
  │                                                                      │
  │  Down Payment:  [████████░░░░░░░░░░░░]  25%                         │
  │  Interest Rate: [██████░░░░░░░░░░░░░░]  6.5%                        │
  │  Vacancy Rate:  [████░░░░░░░░░░░░░░░░]  8%                          │
  │  Rent Growth:   [██████░░░░░░░░░░░░░░]  3%                          │
  │                                                                      │
  │  ───────────────────────────────────────────────────────────────    │
  │  Live Recalculation:                                                 │
  │                                                                      │
  │  Monthly Cash Flow:   $287  →  $412  (+$125)                        │
  │  Cash-on-Cash Return: 6.2%  →  8.4%  (+2.2%)                        │
  │  Cap Rate:            5.8%  →  5.8%  (unchanged)                    │
  │                                                                      │
  └─────────────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────────────┐
  │  CONVERSATIONAL EXPLORATION                                          │
  │                                                                      │
  │  You: "What if I put only 20% down?"                                │
  │                                                                      │
  │  AI: "With 20% down ($60,000), your monthly payment increases to    │
  │       $1,847, reducing cash flow to $153/month. Your cash-on-cash   │
  │       return drops to 3.1%. However, you'd have $20,000 more        │
  │       liquid capital for reserves or another investment..."         │
  │                                                                      │
  │  You: "What's the breakeven occupancy?"                             │
  │                                                                      │
  │  AI: "With 20% down, you need 89% occupancy to break even. That's   │
  │       about 11 months occupied per year. Given this neighborhood's  │
  │       7% historical vacancy rate, you have a reasonable buffer..."  │
  │                                                                      │
  └─────────────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────────────┐
  │  LIVING UPDATES                                                      │
  │                                                                      │
  │  📊 Market Update (Dec 3, 2024)                                     │
  │                                                                      │
  │  Since this report was generated (Nov 15):                          │
  │  • 2 comparable properties sold (+4.2% vs estimates)                │
  │  • Neighborhood median rent increased 1.8%                          │
  │  • 1 new listing within 0.5 miles at $295,000                       │
  │                                                                      │
  │  [Regenerate Report with Latest Data]                               │
  │                                                                      │
  └─────────────────────────────────────────────────────────────────────┘
```

---

## 8. Real-Time Processing

### Event-Driven Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    REAL-TIME EVENT PROCESSING                           │
└─────────────────────────────────────────────────────────────────────────┘

                        EXTERNAL EVENTS
  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐
  │New Listing│ │Price Drop│ │Property  │ │Market    │ │User      │
  │ Detected │ │ Detected │ │  Sold    │ │Data Upd. │ │Portfolio │
  └─────┬────┘ └─────┬────┘ └─────┬────┘ └─────┬────┘ └─────┬────┘
        │            │            │            │            │
        └────────────┴────────────┴────────────┴────────────┘
                                  │
                                  ▼
        ┌─────────────────────────────────────────────────────────┐
        │                    EVENT ROUTER                          │
        │                   (AWS EventBridge)                      │
        └─────────────────────────────────────────────────────────┘
                                  │
          ┌───────────────────────┼───────────────────────┐
          ▼                       ▼                       ▼
  ┌───────────────┐     ┌───────────────┐     ┌───────────────┐
  │  ALERT        │     │  ANALYSIS     │     │  CACHE        │
  │  PROCESSOR    │     │  REFRESH      │     │  INVALIDATOR  │
  │               │     │               │     │               │
  │ Match user    │     │ Re-run models │     │ Clear stale   │
  │ criteria,     │     │ for affected  │     │ cached data   │
  │ send notifs   │     │ properties    │     │ and reports   │
  └───────────────┘     └───────────────┘     └───────────────┘
          │                       │                       │
          ▼                       ▼                       ▼
  ┌───────────────┐     ┌───────────────┐     ┌───────────────┐
  │ Push Notif    │     │ Graph Update  │     │ CDN Purge     │
  │ Email         │     │ Vector Update │     │ Report Regen  │
  │ Webhook       │     │ Pre-compute   │     │ API Response  │
  └───────────────┘     └───────────────┘     └───────────────┘
```

### Deal Alert Engine

```python
class DealAlertEngine:
    """
    Intelligent deal detection that goes beyond simple price alerts.
    """

    async def process_new_listing(self, listing: Listing) -> List[Alert]:
        alerts = []

        # 1. Instant Analysis
        quick_analysis = await self.quick_analyzer.analyze(listing)

        # 2. Find matching investor criteria
        matching_criteria = await self.match_investor_criteria(
            listing,
            quick_analysis
        )

        for criteria in matching_criteria:
            # 3. Score the deal for this investor
            deal_score = self.score_deal(listing, quick_analysis, criteria)

            if deal_score.is_notable:
                # 4. Generate personalized alert
                alert = Alert(
                    investor_id=criteria.investor_id,
                    listing=listing,
                    analysis_summary=quick_analysis,
                    deal_score=deal_score,
                    why_matched=self.explain_match(listing, criteria),
                    suggested_action=self.suggest_action(deal_score),
                )
                alerts.append(alert)

        return alerts

    def score_deal(
        self,
        listing: Listing,
        analysis: QuickAnalysis,
        criteria: InvestorCriteria
    ) -> DealScore:
        """
        Multi-factor deal scoring relative to investor preferences.
        """

        factors = {
            # Price vs value
            'value_score': self.calculate_value_score(
                listing.price,
                analysis.estimated_value
            ),

            # Returns vs target
            'return_score': self.calculate_return_score(
                analysis.estimated_cash_on_cash,
                criteria.target_cash_on_cash
            ),

            # Risk vs tolerance
            'risk_score': self.calculate_risk_alignment(
                analysis.risk_score,
                criteria.risk_tolerance
            ),

            # Market timing
            'timing_score': self.calculate_timing_score(
                listing.days_on_market,
                analysis.market_conditions
            ),

            # Anomaly detection
            'anomaly_score': self.detect_anomaly(listing, analysis),
        }

        overall = self.weighted_average(factors, self.DEAL_WEIGHTS)

        return DealScore(
            overall=overall,
            factors=factors,
            is_notable=overall > 0.7 or factors['anomaly_score'] > 0.9,
            explanation=self.generate_explanation(factors)
        )
```

---

## 9. B2B Integration Architecture

### API-First Design

```yaml
# OpenAPI Specification (excerpt)

openapi: 3.0.3
info:
  title: Property Prospectus API
  version: 2.0.0
  description: |
    AI-powered rental property investment analysis API.
    Generate institutional-grade investment reports programmatically.

paths:
  /v2/properties/search:
    post:
      summary: Search properties with investment criteria
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PropertySearchRequest'
      responses:
        200:
          description: Matching properties with basic metrics
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PropertySearchResponse'

  /v2/properties/{propertyId}/analyze:
    post:
      summary: Generate full investment analysis
      parameters:
        - name: propertyId
          in: path
          required: true
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AnalysisRequest'
      responses:
        200:
          description: Complete investment analysis
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/InvestmentAnalysis'

  /v2/reports/{reportId}:
    get:
      summary: Retrieve generated report
      parameters:
        - name: format
          in: query
          schema:
            type: string
            enum: [json, html, pdf]
      responses:
        200:
          description: Report in requested format

  /v2/webhooks:
    post:
      summary: Register webhook for real-time updates
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/WebhookRegistration'

components:
  schemas:
    PropertySearchRequest:
      type: object
      properties:
        location:
          oneOf:
            - $ref: '#/components/schemas/BoundingBox'
            - $ref: '#/components/schemas/ZipCode'
            - $ref: '#/components/schemas/City'
        priceRange:
          $ref: '#/components/schemas/Range'
        bedrooms:
          $ref: '#/components/schemas/Range'
        propertyTypes:
          type: array
          items:
            type: string
            enum: [sfh, condo, townhouse, multi]
        investmentCriteria:
          type: object
          properties:
            minCapRate:
              type: number
            minCashOnCash:
              type: number
            maxRiskScore:
              type: integer
        limit:
          type: integer
          default: 20
```

### Embeddable Components

```typescript
// React SDK for B2B customers

import { PropertyProspectus } from '@prospectus/react';

// Embed full report viewer
function InvestmentPortal() {
  return (
    <PropertyProspectus
      apiKey={process.env.PROSPECTUS_API_KEY}
      propertyId="prop_abc123"
      theme={{
        primaryColor: '#your-brand-color',
        fontFamily: 'Your Brand Font',
        logo: '/your-logo.svg',
      }}
      features={{
        interactiveScenarios: true,
        chat: true,
        pdfExport: true,
      }}
      onAnalysisComplete={(analysis) => {
        // Handle completed analysis
        trackEvent('analysis_viewed', { propertyId: analysis.id });
      }}
    />
  );
}

// Embed mini-widget for property cards
function PropertyCard({ property }) {
  return (
    <div className="property-card">
      <img src={property.photo} />
      <h3>{property.address}</h3>
      <p>${property.price.toLocaleString()}</p>

      {/* Embed quick metrics widget */}
      <ProspectusQuickMetrics
        apiKey={process.env.PROSPECTUS_API_KEY}
        propertyId={property.id}
        metrics={['capRate', 'cashOnCash', 'riskScore']}
      />

      <button onClick={() => openFullAnalysis(property.id)}>
        View Full Analysis
      </button>
    </div>
  );
}
```

### White-Label Configuration

```typescript
interface WhiteLabelConfig {
  branding: {
    companyName: string;
    logo: URL;
    favicon: URL;
    colors: {
      primary: HexColor;
      secondary: HexColor;
      accent: HexColor;
    };
    fonts: {
      heading: FontFamily;
      body: FontFamily;
    };
  };

  customization: {
    reportSections: {
      // Enable/disable sections
      executiveSummary: boolean;
      financialAnalysis: boolean;
      riskAssessment: boolean;
      marketAnalysis: boolean;
      // Add custom sections
      customSections?: CustomSection[];
    };

    terminology: {
      // Replace our terms with client's preferred terms
      'investment prospectus': string;  // e.g., "Property Analysis"
      'risk score': string;             // e.g., "Investment Grade"
    };

    methodology: {
      // Customize calculation assumptions
      defaultVacancyRate: Percentage;
      defaultManagementFee: Percentage;
      capExReserveRate: Percentage;
    };
  };

  integration: {
    ssoProvider?: 'okta' | 'auth0' | 'custom';
    webhookEndpoints: WebhookConfig[];
    customDataSources?: DataSourceConfig[];
  };
}
```

---

## 10. Infrastructure & DevOps

### Cloud Architecture (AWS)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         AWS INFRASTRUCTURE                               │
└─────────────────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────────────┐
  │  EDGE LAYER                                                          │
  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                 │
  │  │ CloudFront  │  │    WAF      │  │   Shield    │                 │
  │  │    CDN      │  │  Firewall   │  │   DDoS      │                 │
  │  └─────────────┘  └─────────────┘  └─────────────┘                 │
  └─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
  ┌─────────────────────────────────────────────────────────────────────┐
  │  APPLICATION LAYER                                                   │
  │                                                                      │
  │  ┌─────────────────────────────────────────────────────────────┐   │
  │  │  ECS Fargate Cluster                                         │   │
  │  │  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐           │   │
  │  │  │ API     │ │ Worker  │ │ Analysis│ │ Report  │           │   │
  │  │  │ Service │ │ Service │ │ Service │ │ Service │           │   │
  │  │  └─────────┘ └─────────┘ └─────────┘ └─────────┘           │   │
  │  └─────────────────────────────────────────────────────────────┘   │
  │                                                                      │
  │  ┌─────────────────────────────────────────────────────────────┐   │
  │  │  Lambda Functions                                            │   │
  │  │  ├─ Data Ingestion Handlers                                  │   │
  │  │  ├─ Event Processors                                         │   │
  │  │  ├─ Alert Generators                                         │   │
  │  │  └─ Report PDF Generator                                     │   │
  │  └─────────────────────────────────────────────────────────────┘   │
  └─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
  ┌─────────────────────────────────────────────────────────────────────┐
  │  DATA LAYER                                                          │
  │                                                                      │
  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                 │
  │  │  Aurora     │  │  Neptune    │  │ ElastiCache │                 │
  │  │ PostgreSQL  │  │  Graph DB   │  │   Redis     │                 │
  │  │ (Primary)   │  │ (Prop Graph)│  │  (Cache)    │                 │
  │  └─────────────┘  └─────────────┘  └─────────────┘                 │
  │                                                                      │
  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                 │
  │  │ OpenSearch  │  │     S3      │  │  Pinecone   │                 │
  │  │ (Search)    │  │  (Storage)  │  │ (Vectors)   │                 │
  │  └─────────────┘  └─────────────┘  └─────────────┘                 │
  └─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
  ┌─────────────────────────────────────────────────────────────────────┐
  │  EVENTING & MESSAGING                                                │
  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                 │
  │  │EventBridge  │  │    SQS      │  │    SNS      │                 │
  │  │  (Events)   │  │  (Queues)   │  │ (Pub/Sub)   │                 │
  │  └─────────────┘  └─────────────┘  └─────────────┘                 │
  └─────────────────────────────────────────────────────────────────────┘
```

### Infrastructure as Code

```hcl
# Terraform excerpt

module "prospectus_platform" {
  source = "./modules/platform"

  environment = var.environment

  # Networking
  vpc_cidr = "10.0.0.0/16"
  availability_zones = ["us-west-2a", "us-west-2b", "us-west-2c"]

  # Compute
  ecs_cluster = {
    name = "prospectus-${var.environment}"

    services = {
      api = {
        cpu = 1024
        memory = 2048
        desired_count = 3
        auto_scaling = {
          min = 2
          max = 20
          target_cpu = 70
        }
      }

      analysis = {
        cpu = 2048
        memory = 4096
        desired_count = 5
        auto_scaling = {
          min = 3
          max = 50
          target_cpu = 80
        }
      }

      worker = {
        cpu = 512
        memory = 1024
        desired_count = 2
        auto_scaling = {
          min = 1
          max = 10
          target_queue_depth = 100
        }
      }
    }
  }

  # Databases
  aurora = {
    engine = "aurora-postgresql"
    engine_version = "15.4"
    instance_class = "db.r6g.xlarge"
    instances = 3
  }

  neptune = {
    instance_class = "db.r5.large"
    cluster_size = 2
  }

  elasticache = {
    node_type = "cache.r6g.large"
    num_cache_nodes = 3
  }

  # AI/ML
  bedrock = {
    models = ["anthropic.claude-3-sonnet", "anthropic.claude-3-haiku"]
  }
}
```

---

## 11. Security & Compliance

### Security Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                       SECURITY ARCHITECTURE                              │
└─────────────────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────────────┐
  │  IDENTITY & ACCESS                                                   │
  │                                                                      │
  │  ┌─────────────────────────────────────────────────────────────┐   │
  │  │  Auth0 / Clerk                                               │   │
  │  │  ├─ B2C: Email/Password, Social, MFA                        │   │
  │  │  ├─ B2B: SSO (SAML, OIDC), SCIM provisioning               │   │
  │  │  └─ API: JWT tokens, API keys with scopes                   │   │
  │  └─────────────────────────────────────────────────────────────┘   │
  │                                                                      │
  │  ┌─────────────────────────────────────────────────────────────┐   │
  │  │  Authorization                                               │   │
  │  │  ├─ RBAC: Admin, Analyst, Viewer, API-Only                  │   │
  │  │  ├─ ABAC: Org-based, Geo-based, Feature-based              │   │
  │  │  └─ Rate Limits: Per plan, per endpoint                     │   │
  │  └─────────────────────────────────────────────────────────────┘   │
  └─────────────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────────────┐
  │  DATA PROTECTION                                                     │
  │                                                                      │
  │  ┌─────────────────────────────────────────────────────────────┐   │
  │  │  Encryption                                                  │   │
  │  │  ├─ At Rest: AES-256 (AWS KMS managed keys)                 │   │
  │  │  ├─ In Transit: TLS 1.3                                     │   │
  │  │  └─ Application: Field-level encryption for PII             │   │
  │  └─────────────────────────────────────────────────────────────┘   │
  │                                                                      │
  │  ┌─────────────────────────────────────────────────────────────┐   │
  │  │  Data Handling                                               │   │
  │  │  ├─ No PII stored unnecessarily                             │   │
  │  │  ├─ User data isolated per organization                     │   │
  │  │  ├─ Audit logging for all data access                       │   │
  │  │  └─ Data retention policies enforced                        │   │
  │  └─────────────────────────────────────────────────────────────┘   │
  └─────────────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────────────┐
  │  COMPLIANCE CONSIDERATIONS                                           │
  │                                                                      │
  │  ├─ SOC 2 Type II (future goal for enterprise customers)           │
  │  ├─ CCPA compliance for California users                            │
  │  ├─ Financial disclaimers on all reports                            │
  │  └─ Data source attribution and licensing compliance                │
  └─────────────────────────────────────────────────────────────────────┘
```

---

## 12. Phased Implementation Roadmap

### Phase 1: Foundation (Prototype)

**Goal:** Working prototype demonstrating core value proposition

```
┌─────────────────────────────────────────────────────────────────────────┐
│  PHASE 1: FOUNDATION                                                     │
│  Target: Working Prototype                                               │
└─────────────────────────────────────────────────────────────────────────┘

  SCOPE:
  ├─ Single metro market (e.g., Austin, TX)
  ├─ Property search with basic filters
  ├─ Single property deep analysis
  ├─ AI-generated 10-page report (PDF)
  └─ Basic web interface

  TECH STACK:
  ├─ Frontend: Next.js 14 + Tailwind
  ├─ Backend: Node.js / Python FastAPI
  ├─ Database: PostgreSQL (Supabase)
  ├─ AI: Claude API (Anthropic)
  ├─ Data: 1-2 property data APIs
  └─ Hosting: Vercel + Railway/Render

  DELIVERABLES:
  ├─ Property search returning 20+ properties
  ├─ Property detail page with key metrics
  ├─ Full analysis report generation (<60s)
  ├─ PDF export of report
  └─ Basic user auth

  VALIDATION:
  ├─ Generate 10 sample reports
  ├─ Review with 3-5 real estate professionals
  ├─ Measure report accuracy vs manual analysis
  └─ Gather feedback on value proposition
```

### Phase 2: Intelligence

**Goal:** Differentiated AI capabilities

```
┌─────────────────────────────────────────────────────────────────────────┐
│  PHASE 2: INTELLIGENCE                                                   │
│  Target: Differentiated Analysis                                         │
└─────────────────────────────────────────────────────────────────────────┘

  SCOPE:
  ├─ Multi-agent AI system (Financial, Risk, Market analysts)
  ├─ Advanced risk scoring model
  ├─ Comparable property matching algorithm
  ├─ Interactive scenario modeling
  └─ Confidence scoring on all predictions

  ADDITIONS:
  ├─ Graph database for property relationships
  ├─ Vector store for semantic search
  ├─ Data fusion from multiple sources
  ├─ Agent orchestration framework
  └─ Streaming report generation

  DELIVERABLES:
  ├─ Multi-agent analysis with cited reasoning
  ├─ Risk scores with factor breakdown
  ├─ 5+ comparable properties per analysis
  ├─ Scenario sliders in web report
  └─ Confidence intervals on key metrics
```

### Phase 3: Scale

**Goal:** Production-ready platform

```
┌─────────────────────────────────────────────────────────────────────────┐
│  PHASE 3: SCALE                                                          │
│  Target: Production Platform                                             │
└─────────────────────────────────────────────────────────────────────────┘

  SCOPE:
  ├─ Multi-metro expansion (5-10 markets)
  ├─ Portfolio tracking and monitoring
  ├─ Deal alerts and notifications
  ├─ API for B2B integrations
  └─ Usage-based billing system

  ADDITIONS:
  ├─ Event-driven architecture
  ├─ Real-time data pipeline
  ├─ Webhook infrastructure
  ├─ Admin dashboard for B2B
  └─ API documentation portal

  DELIVERABLES:
  ├─ Stable API with <200ms latency
  ├─ 99.9% uptime SLA
  ├─ Self-serve B2B onboarding
  ├─ Usage analytics dashboard
  └─ Billing integration (Stripe)
```

### Phase 4: Enterprise

**Goal:** Enterprise-grade B2B platform

```
┌─────────────────────────────────────────────────────────────────────────┐
│  PHASE 4: ENTERPRISE                                                     │
│  Target: Enterprise B2B                                                  │
└─────────────────────────────────────────────────────────────────────────┘

  SCOPE:
  ├─ White-label solution
  ├─ SSO / SCIM integration
  ├─ Custom methodology configuration
  ├─ Embeddable React components
  └─ SOC 2 Type II compliance

  ADDITIONS:
  ├─ Multi-tenant architecture
  ├─ Custom branding engine
  ├─ Enterprise admin controls
  ├─ Audit logging
  └─ SLA monitoring

  DELIVERABLES:
  ├─ White-label deployment toolkit
  ├─ Enterprise security documentation
  ├─ Custom integration support
  ├─ Dedicated success management
  └─ Volume pricing tiers
```

---

## Appendix A: Technology Decision Matrix

| Decision | Options Considered | Recommendation | Rationale |
|----------|-------------------|----------------|-----------|
| **Frontend** | Next.js, Remix, SvelteKit | **Next.js 14** | Best ecosystem, Vercel deployment, RSC for performance |
| **Backend** | Node/Express, FastAPI, Go | **FastAPI** | Python ecosystem for ML, async support, auto-docs |
| **Primary DB** | PostgreSQL, MySQL, Supabase | **Supabase** | Postgres + auth + realtime, fast prototyping |
| **Graph DB** | Neo4j, Neptune, Dgraph | **Neo4j** | Best query language, managed cloud option |
| **Vector Store** | Pinecone, Weaviate, pgvector | **Pinecone** | Managed, fast, good free tier |
| **Cache** | Redis, Memcached, Upstash | **Upstash Redis** | Serverless, per-request pricing |
| **LLM** | Claude, GPT-4, Llama | **Claude 3** | Best for structured output, reasoning |
| **Hosting** | Vercel, Railway, AWS | **Vercel + Railway** | Fast iteration, then AWS for scale |
| **Property Data** | Attom, RealtyMole, Estated | **RealtyMole** (start) | Best price/coverage for prototype |

---

## Appendix B: Data Provider Comparison

| Provider | Coverage | Rental Est. | API Quality | Pricing | Recommended For |
|----------|----------|-------------|-------------|---------|-----------------|
| **Attom** | National | Yes | Excellent | $$$ | Production/Scale |
| **RealtyMole** | National | Yes | Good | $$ | Prototype/Growth |
| **Estated** | National | No | Good | $$ | Property details |
| **Rentometer** | National | Specialized | Good | $$ | Rental validation |
| **HouseCanary** | National | Yes | Excellent | $$$$ | Enterprise |
| **CoreLogic** | National | Yes | Excellent | $$$$$ | Enterprise |

---

## Appendix C: Glossary

| Term | Definition |
|------|------------|
| **Cap Rate** | Net Operating Income / Property Value |
| **Cash-on-Cash** | Annual Cash Flow / Total Cash Invested |
| **NOI** | Net Operating Income = Gross Income - Operating Expenses |
| **DSCR** | Debt Service Coverage Ratio = NOI / Annual Debt Payments |
| **GRM** | Gross Rent Multiplier = Property Price / Annual Gross Rent |
| **1% Rule** | Monthly rent should be ≥ 1% of purchase price |

---

*Document generated during brainstorming session. Subject to refinement based on stakeholder feedback and technical validation.*
