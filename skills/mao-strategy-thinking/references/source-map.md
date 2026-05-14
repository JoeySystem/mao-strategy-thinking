# Source Map

Use this map to connect decision frames to Mao Zedong Selected Works articles.

This repository does not include Mao Zedong Selected Works source text. To use local source search, provide your own legally obtained unpacked EPUB directory with XHTML files under `OEBPS/Text/`, then pass it with `--epub` or set `MAOXUAN_EPUB_PATH`.

## High-Value Articles

| Framework | Article | Local file hint | Use |
| --- | --- | --- | --- |
| Investigation, anti-dogmatism | 反对本本主义 | `Section0205.xhtml` | Start from actual conditions, not copied doctrine |
| Practice feedback | 实践论 | `Section0215.xhtml` | Knowledge-action-feedback cycle |
| Contradiction analysis | 矛盾论 | `Section0216.xhtml` | Principal contradiction and principal aspect |
| Strategic/global thinking | 中国革命战争的战略问题 | `Section0211.xhtml` | Global/local, concentration, stage, initiative |
| Protracted strategy | 论持久战 | `Section0309.xhtml` | Long-cycle strategy and stage development |
| Strategic guerrilla/game mobility | 抗日游击战争的战略问题 | `Section0308.xhtml` | Mobility, initiative, conditions for flexible tactics |
| Leadership method | 关于领导方法的若干问题 | `Section0413.xhtml` | From practice to concentrated guidance and back |
| Policy and flexibility | 论政策 | `Section0337.xhtml` | Principle and flexibility |
| Team/communication discipline | 反对自由主义 | `Section0303.xhtml` | Avoid harmful internal drift and unprincipled behavior |
| Learning/work style | 改造我们的学习 | `Section0402.xhtml` | Anti-empty-talk, evidence-based study |
| Communication quality | 反对党八股 | `Section0407.xhtml` | Avoid formulaic language |

## Search Terms

Useful Chinese search terms:

- 调查
- 本本主义
- 具体
- 矛盾
- 主要矛盾
- 实践
- 全局
- 局部
- 战略
- 战术
- 持久战
- 速决战
- 集中兵力
- 优势
- 主动
- 阶段
- 政策
- 领导方法
- 群众

## Search Script

Use:

```bash
python3 scripts/search_maoxuan.py 矛盾 --max 8
python3 scripts/search_maoxuan.py 全局 局部 --article 中国革命战争的战略问题
python3 scripts/search_maoxuan.py --list
```

The script returns article titles, file names, approximate line numbers, and short snippets. Use snippets for orientation; open the source file if exact context matters.

## Citation Practice

Prefer:

- article title
- short paraphrase
- one short quote when useful
- file location from search results

Avoid:

- long verbatim excerpts
- treating historical military contexts as direct modern commands
- quoting without explaining modern transfer limits
