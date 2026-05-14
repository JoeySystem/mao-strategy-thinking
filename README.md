# Mao Strategy Thinking

A Codex skill that translates selected strategic decision-making frameworks from *Mao Zedong Selected Works* into modern analysis workflows.

The skill supports contradiction analysis, investigation-first decision making, stage judgment, strategic endurance with tactical resolution, concentration of limited resources, stakeholder alignment, and esports or strategy-game analysis.

## What It Does

- Analyze decisions through principal contradiction and stage judgment.
- Separate facts, assumptions, judgments, and unknowns.
- Connect local actions to global objectives.
- Find where limited resources can create local advantage.
- Design small feedback tests instead of treating plans as fixed doctrine.
- Apply the framework to legal, non-harmful domains such as business, product strategy, personal planning, organization management, and esports.

## What It Does Not Do

- It does not include or distribute *Mao Zedong Selected Works* text.
- It does not simulate Mao Zedong's voice, personality, or ideology.
- It does not provide operational advice for real-world violence, coercion, illegal action, political targeting, or harming people or institutions.
- It does not treat historical military conclusions as directly applicable to modern real-world conflicts.

## Install

Copy the skill into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R skills/mao-strategy-thinking ~/.codex/skills/
```

Then invoke it in Codex:

```text
Use $mao-strategy-thinking to analyze this decision: ...
```

Natural prompts can also trigger it when they mention concepts such as `毛选`, `主要矛盾`, `矛盾论`, `实践论`, `论持久战`, `调查研究`, `集中优势`, or esports strategy through this framework.

## Optional Local Source Search

The repository does not ship source text. If you have a legally obtained local unpacked EPUB directory, configure:

```bash
export MAOXUAN_EPUB_PATH="/path/to/毛泽东选集.epub"
```

Then search:

```bash
python3 ~/.codex/skills/mao-strategy-thinking/scripts/search_maoxuan.py 主要矛盾 --max 5
```

Or pass the path directly:

```bash
python3 ~/.codex/skills/mao-strategy-thinking/scripts/search_maoxuan.py 全局 局部 --epub "/path/to/毛泽东选集.epub"
```

The script expects an unpacked EPUB directory containing `OEBPS/Text/*.xhtml`.

## Repository Layout

```text
skills/
└── mao-strategy-thinking/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    ├── references/
    │   ├── decision-workflow.md
    │   ├── esports-strategy.md
    │   ├── framework.md
    │   ├── safety-boundaries.md
    │   └── source-map.md
    └── scripts/
        └── search_maoxuan.py
```

## License

This repository's original code and documentation are licensed under the MIT License. The license does not cover any third-party source texts, including user-provided copies of *Mao Zedong Selected Works*.
