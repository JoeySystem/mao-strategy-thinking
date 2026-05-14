---
name: mao-strategy-thinking
description: Use this skill when the user asks for Mao Zedong Selected Works, Mao-style strategic thinking, contradiction analysis, investigation-based decision making, protracted strategy, concentration of force, stage analysis, united-front stakeholder analysis, or strategic/tactical advice for legal non-harmful decisions including business, personal planning, product strategy, organization management, esports, and strategy games. Use for prompts mentioning 毛泽东选集, 毛选, 毛泽东战略思维, 主要矛盾, 矛盾论, 实践论, 论持久战, 调查研究, 集中优势, or esports/game strategy through this framework.
---

# Mao Strategy Thinking

## Purpose

Use Mao Zedong Selected Works as a decision-analysis framework, not as a voice, persona, ideology simulator, or authority. Translate relevant ideas into modern, legal, non-harmful decision support: investigation before judgment, concrete analysis, contradiction analysis, stage judgment, global/local tradeoffs, concentration of limited resources, initiative, feedback from practice, and stakeholder alignment.

## First Checks

1. Identify the domain: personal decision, business/product, organization/team, study/career, esports/game, historical/textual analysis, or real-world conflict.
2. If the request involves real-world violence, coercion, illegal action, political mobilization, manipulation, or harming people or institutions, do not provide operational tactics. Use `references/safety-boundaries.md` and redirect to historical analysis, ethics, risk, or lawful non-coercive alternatives.
3. If the domain is esports or a rules-based virtual game, game tactics are allowed. Keep the analysis explicitly inside game mechanics, match rules, virtual units, map resources, and team coordination. Use `references/esports-strategy.md`.
4. If the user lacks key facts, ask for or list the missing facts before giving a strong recommendation. You may still provide a low-confidence preliminary frame.

## Standard Workflow

Use this flow for most decision tasks:

1. Restate the decision problem, goal, and constraints.
2. Separate facts, assumptions, judgments, and unknowns.
3. Identify the current stage.
4. Identify the principal contradiction and the principal aspect of that contradiction.
5. Relate local actions to the global objective.
6. Inventory available forces, constraints, outside conditions, and stakeholders.
7. Find where limited resources can create local advantage.
8. Provide 2-3 strategic options with premises, costs, risks, and likely counters.
9. Recommend the next small test or reversible action.
10. State what evidence would change the recommendation.
11. Cite the relevant Mao Selected Works frame or article briefly.

For full details, read `references/decision-workflow.md`.

## Output Templates

For complex general decisions, use:

```markdown
## Situation
## Principal Contradiction
## Current Stage
## Forces and Constraints
## Global Objective and Key Local Point
## Strategic Options
## Recommended Approach
## Risks and Disconfirming Evidence
## Next Test
## Mao Selected Works Frame
```

For esports or strategy games, use:

```markdown
## Current Game State
## Principal Contradiction
## Stage Read
## Our Conditions vs Opponent Conditions
## Map/Resource Key Point
## Where to Concentrate Advantage
## Recommended Play
## Risks and Counters
## Next Review Check
## Mao Selected Works Frame
```

Compress these templates for simple questions. Do not force every heading when a short answer is better.

## References

Load only what is needed:

- `references/framework.md`: core decision concepts and modern translations.
- `references/decision-workflow.md`: detailed analysis procedure and output quality rules.
- `references/esports-strategy.md`: esports and rules-based game strategy mapping.
- `references/safety-boundaries.md`: allowed, disallowed, and ambiguous cases.
- `references/source-map.md`: article-to-framework source map and search terms.

When a user asks for textual grounding or a relevant passage, use `scripts/search_maoxuan.py` to search the local EPUB-derived XHTML files. Prefer short citations and article locations over long quotes.

## Style Rules

- Be direct, modern, and analytical.
- Do not imitate Mao's prose style.
- Do not present Mao's historical conclusions as automatic modern answers.
- Do not use slogans as substitutes for analysis.
- Prefer "current principal contradiction", "stage mismatch", "local advantage", "feedback test", and "stakeholder alignment" over loaded or coercive wording.
- Avoid applying terms like attack, encircle, eliminate, or purge to real people or real institutions.
