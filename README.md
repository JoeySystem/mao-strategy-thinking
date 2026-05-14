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

## Stability Notes and Troubleshooting

The skill itself is plain Markdown plus one standard-library Python script, so the core decision-analysis workflow should be stable after installation. Most issues come from local setup differences.

### Codex does not detect the skill

Check that the installed path is exactly:

```text
~/.codex/skills/mao-strategy-thinking/SKILL.md
```

If you cloned this repository, remember that the skill is nested under `skills/`:

```bash
mkdir -p ~/.codex/skills
cp -R skills/mao-strategy-thinking ~/.codex/skills/
```

Then start a new Codex conversation or explicitly invoke:

```text
Use $mao-strategy-thinking to analyze this decision: ...
```

### The skill works, but source search fails

Source search is optional. The decision framework works without local source text.

If search fails with:

```text
Provide --epub or set $MAOXUAN_EPUB_PATH to your local unpacked EPUB directory.
```

set the source path:

```bash
export MAOXUAN_EPUB_PATH="/path/to/your/unpacked/epub"
```

Or pass it directly:

```bash
python3 ~/.codex/skills/mao-strategy-thinking/scripts/search_maoxuan.py 主要矛盾 --epub "/path/to/your/unpacked/epub"
```

### My EPUB is a single `.epub` file

The search script expects an unpacked EPUB directory, not a zipped `.epub` file. An unpacked source should contain:

```text
OEBPS/Text/*.xhtml
OEBPS/toc.ncx
```

If your file is a normal EPUB archive, unpack it into a local directory first. Do not commit the unpacked book files to this repository.

### My EPUB has a different internal structure

Some EPUBs do not use `OEBPS/Text/*.xhtml` or `toc.ncx`. In that case:

- the skill still works as a decision framework
- the search script may need adaptation for your EPUB layout
- use `--epub` to point at the root directory that contains the book content
- inspect the EPUB directory and update `scripts/search_maoxuan.py` if text files live elsewhere

### Python issues

`search_maoxuan.py` uses only the Python standard library. It should run with Python 3.9+:

```bash
python3 --version
python3 ~/.codex/skills/mao-strategy-thinking/scripts/search_maoxuan.py --help
```

No pip dependencies are required.

### Public sharing and copyright

This repository intentionally excludes source book files. Users should provide their own legally obtained local copy if they want source search. Keep `.epub`, unpacked `OEBPS/`, and similar book files out of commits.

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
