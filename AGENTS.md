# Spire Codex Agents Configuration

This file configures agent behavior for the spire-codex repository.

## Skills

Skills are located in `.agents/skills/` and provide specialized workflows for analyzing Slay the Spire 2 game mechanics.

### Available Skills

#### analyze-sts2
**Location**: `.agents/skills/analyze-sts2/`

**Purpose**: Analyze Slay the Spire 2 game mechanics by reading decompiled C# source code.

**When to Use**:
- Analyzing card mechanics (rarity odds, card pools, upgrades, keywords)
- Investigating combat systems (damage calculation, blocking, powers, intents)
- Studying monster behaviors (AI state machines, move patterns, ascension changes)
- Exploring roguelike elements (map generation, rewards, relic/potion drops)
- Comparing base mechanics vs Ascension 10 difficulty

**Key Features**:
- Code-first analysis (only uses `extraction/decompiled/` C# source)
- Multi-dimensional analysis (combat, cards, monsters, roguelike)
- Ascension difficulty comparison (base vs Ascension 10)
- Detailed technical documentation with code references

**Templates**:
- `templates/combat_mechanics.md` - Combat systems analysis
- `templates/card_mechanics.md` - Card mechanics analysis
- `templates/monster_mechanics.md` - Monster behaviors analysis
- `templates/roguelike_mechanics.md` - Roguelike elements analysis

## Repository Context

This repository contains:
- **extraction/decompiled/**: ~3,300 decompiled C# source files from Slay the Spire 2
- **backend/**: FastAPI backend with parsers for extracting game data
- **frontend/**: Next.js frontend for the spire-codex.com website
- **data/**: Parsed JSON data files (14 languages)

## Commit Hygiene

- Do not include temporary process artifacts such as `docs/superpowers/specs/` or `docs/superpowers/plans/` in final commits or merges unless the user explicitly asks to keep them.
- Before merging to `main`, squash or rewrite local work so final commits contain only repository behavior, tooling, source, and intentional documentation changes.

## Chinese Localization

When answering in Chinese, use Simplified Chinese localization from `data/zhs/*.json` for game entities and fixed game terms.

- Use `中文名（English/ClassName / ID）` on first mention when English/source identity helps trace code; after that, use the Chinese name.
- Prefer localized names from `data/zhs` over ad hoc translation. For example, `Overgrowth` is `密林`, and `Underdocks` is `暗港`.
- Use `进阶` for the game concept `Ascension`; use localized ascension names from `data/zhs/ascensions.json`, such as `阴郁` and `双重Boss`.
- Resolve fixed terms from `data/zhs/translations.json` and `data/zhs/glossary.json` before finalizing Chinese wording.
- Preserve code symbols in English/code form, such as `AscensionLevel.DoubleBoss`, `RoomType.Monster`, and `GenerateAllEncounters()`.
- If `data/zhs` has no entry, fall back to English data and the id, and explicitly mark the localized name as missing.

## Key Namespaces for Analysis

When using analyze-sts2 skill, focus on these namespaces:

| Mechanism Type | Key Namespaces | Key Classes |
|---|---|---|
| **Card Mechanics** | `MegaCrit.Sts2.Core.Odds`, `MegaCrit.Sts2.Core.Entities.Cards` | `CardRarityOdds`, `CardRarity`, `CardType` |
| **Combat Systems** | `MegaCrit.Sts2.Core.Combat`, `MegaCrit.Sts2.Core.Entities.Powers` | `PowerStackType`, `PowerType` |
| **Monster Behaviors** | `MegaCrit.Sts2.Core.MonsterMoves`, `MegaCrit.Sts2.Core.Models.Monsters` | `MonsterMoveStateMachine`, `GenerateMoveStateMachine()` |
| **Roguelike Elements** | `MegaCrit.Sts2.Core.Map`, `MegaCrit.Sts2.Core.Rewards` | `RunOddsSet`, `UnknownMapPointOdds` |
| **Ascension** | `MegaCrit.Sts2.Core.Entities.Ascension` | `AscensionLevel`, `AscensionHelper` |

## Analysis Guidelines

1. **Always use code sources**: Never use web search or game wikis
2. **Cite references**: All claims must include `file_path:line_number` references
3. **Compare ascension**: Always include base vs Ascension 10 comparisons
4. **Use templates**: Follow the structure in template files
5. **Complete checklists**: Verify all checklist items in templates are completed

## File Discovery Patterns

```bash
# Find all files in a namespace
find extraction/decompiled -path "*/MegaCrit.Sts2.Core.Odds/*" -name "*.cs"

# Find files containing specific class
find extraction/decompiled -name "*CardRarity*.cs"

# Search for specific methods or patterns
grep -r "AscensionHelper.GetValueIfAscension" extraction/decompiled/

# Find enum definitions
grep -r "enum.*AscensionLevel" extraction/decompiled/
```
