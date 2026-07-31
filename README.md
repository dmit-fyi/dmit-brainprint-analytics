# DMIT BrainPrint Analytics 🧠👆

[![npm](https://img.shields.io/npm/v/@dmit-fyi/brainprint-analytics)](https://npmjs.com/package/@dmit-fyi/brainprint-analytics)
[![PyPI](https://img.shields.io/pypi/v/dmit-brainprint-analytics)](https://pypi.org/project/dmit-brainprint-analytics)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21721771.svg)](https://doi.org/10.5281/zenodo.21721771)

DMIT BrainPrint Analytics is an intelligent assessment platform for fingerprint analysis, cognitive profiling, learning preferences, personality insights, and career guidance. Built by [DMIT.fyi](https://dmit.fyi) — guided by Mrs. Priyanka Swain, Founder of Merit Teacher.

## Features

- BrainPrint Score — fingerprint-based multiple intelligence profiling
- Cognitive Profile Score — evaluates cognitive strengths and learning potential
- Learning Style Score — identifies preferred learning modalities and academic strengths
- Personality Insight Score — reveals personality traits and behavioural tendencies
- Career Pathway Score — maps natural talents to suitable career and stream options
- Leadership & Workplace Score — assesses leadership style and work environment fit
- Assessment Types — student DMIT, adult DMIT, career DMIT, leadership DMIT
- CLI support in Node.js and Python
- Benchmark dataset included (20 DMIT assessment cases)
- Lightweight, publish-ready, minimal dependencies

## Quick Start

### Node.js

```bash
npm install @dmit-fyi/brainprint-analytics
npx dmit-brainprint "student-profile" student-dmit 88 82 85 78 90 80
```

### Python

```bash
pip install dmit-brainprint-analytics
python -m brainprint "student-profile" student-dmit 88 82 85 78 90 80
```

## Output

```
Profile: student-profile
Assessment Type: Student DMIT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BrainPrint Score:              88 / 100  [Excellent]
Cognitive Profile Score:       82 / 100  [Healthy]
Learning Style Score:          85 / 100  [Excellent]
Personality Insight Score:     78 / 100  [Healthy]
Career Pathway Score:          90 / 100  [Excellent]
Leadership & Workplace Score:  80 / 100  [Healthy]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Overall BrainPrint Index:      84 / 100
Priority Action:               Personality Insight (lowest — act first)

Multiple Intelligence Profile:
  Logical-Mathematical:    88 / 100
  Linguistic:              82 / 100
  Spatial-Visual:          85 / 100
  Interpersonal:           80 / 100
```

## Assessment Types

| Type | Description |
|------|-------------|
| student-dmit | Student fingerprint and intelligence profiling |
| adult-dmit | Adult cognitive and personality DMIT assessment |
| career-dmit | Career pathway and stream selection assessment |
| leadership-dmit | Leadership style and workplace strengths DMIT |
| early-dmit | Early childhood intelligence and learning assessment |
| entrepreneur-dmit | Entrepreneurship aptitude and business personality |

## Multiple Intelligence Areas

| Intelligence | Description |
|-------------|-------------|
| Logical-Mathematical | Reasoning, analysis, and problem solving |
| Linguistic | Language, communication, and verbal ability |
| Spatial-Visual | Visual thinking, creativity, and design |
| Interpersonal | Social skills, empathy, and teamwork |
| Intrapersonal | Self-awareness and emotional regulation |
| Musical | Rhythm, pattern recognition, and auditory skills |
| Kinesthetic | Physical coordination and hands-on learning |
| Naturalistic | Pattern observation and environmental sensitivity |

## Project Structure

```
dmit-brainprint-analytics/
├── index.ts                  # TypeScript BrainPrint analytics
├── brainprint.py             # Python BrainPrint analytics
├── setup.py                  # PyPI setup config
├── pyproject.toml            # PyPI build config
├── package.json              # NPM package config
├── package-lock.json         # NPM lock file
├── tsconfig.json             # TypeScript config
├── schema.json               # JSON-LD structured data
├── zenodo.json               # Zenodo metadata
├── heartbeat.txt             # Auto-updated daily
├── mkdocs.yml                # ReadTheDocs config
├── .readthedocs.yaml         # ReadTheDocs build config
├── docs/
│   ├── index.md              # Documentation
│   └── requirements.txt
├── dataset/
│   └── dmit_benchmarks.csv
├── .github/workflows/
│   ├── heartbeat.yml
│   ├── npm-publish.yml
│   └── pypi-publish.yml
├── README.md
└── LICENSE
```

## Score Interpretation

| Score | Status | Action |
|-------|--------|--------|
| 0–30 | Critical | Immediate DMIT assessment required |
| 31–60 | At Risk | Active guidance and profiling needed |
| 61–80 | Healthy | On track with targeted development |
| 81–100 | Excellent | Strong brainprint — leverage strengths |

## Keywords

DMIT · Dermatoglyphics · Multiple Intelligence Test · Fingerprint Analysis · BrainPrint · Cognitive Profiling · Learning Style · Career Guidance · Merit Teacher · DMIT.fyi

## Links

| Platform | URL |
|----------|-----|
| Website | https://dmit.fyi |
| GitHub | https://github.com/dmit-fyi/dmit-brainprint-analytics |
| GitHub Pages | https://dmit-fyi.github.io/dmit-brainprint-analytics/ |
| NPM | https://npmjs.com/package/@dmit-fyi/brainprint-analytics |
| PyPI | https://pypi.org/project/dmit-brainprint-analytics |
| Hugging Face | https://huggingface.co/datasets/dmit-fyi/brainprint-benchmarks |
| Zenodo | https://zenodo.org/records/21721771 |
| Docs | https://dmit-brainprint-analytics.readthedocs.io |
| Medium | https://medium.com/@dmit-fyi |
| Quora | https://www.quora.com/profile/Dmit-Fyi |
| SlideShare | https://www.slideshare.net/slideshow/dmit-fyi-understanding-dermatoglyphics-multiple-intelligence-testing-dmit/288912143 |
| Pinterest | https://www.pinterest.com/DMITfyi/_profile/ |

## About DMIT.fyi

DMIT.fyi develops technology and digital resources for Dermatoglyphics Multiple Intelligence Testing. Our repositories include tools, APIs, datasets, documentation, and web applications supporting fingerprint analysis, assessment reports, and personalised insights into learning preferences, personality traits, multiple intelligences, and career development. Guided by Mrs. Priyanka Swain, Founder of Merit Teacher.

## License

MIT — [DMIT.fyi](https://dmit.fyi)
