# Skills for Spire Codex

This directory contains custom skills for analyzing Slay the Spire 2 game mechanics.

## Available Skills

### analyze-sts2

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

**Structure**:
```
analyze-sts2/
├── SKILL.md                    # Main skill documentation
└── templates/                  # Analysis templates
    ├── combat_mechanics.md      # Combat systems analysis
    ├── card_mechanics.md        # Card mechanics analysis
    ├── monster_mechanics.md      # Monster behaviors analysis
    └── roguelike_mechanics.md  # Roguelike elements analysis
```

## Usage

When AI agents work on this repository, they can use the `analyze-sts2` skill to:

1. **Discover relevant source files** using provided file discovery patterns
2. **Extract exact values** from decompiled C# code
- **Generate technical documentation** with code references
4. **Compare base vs Ascension 10** mechanics

### Example Usage

**User Request**: "Analyze the card rarity odds system"

**AI Agent Process**:
1. Load `analyze-sts2` skill
2. Read `templates/card_mechanics.md` template
3. Discover files: `find extraction/decompiled -path "*/MegaCrit.Sts2.Core.Odds/*" -name "*.cs"`
4. Read `CardRarityOdds` class
5. Extract values using `AscensionHelper.GetValueIfAscension()` patterns
6. Generate documentation with tables and code references

## Repository Context

This skill is designed for the spire-codex repository structure:

- **extraction/decompiled/**: ~3,300 decompiled C# source files
- **backend/**: FastAPI backend with parsers
- **frontend/**: Next.js frontend
- **data/**: Parsed JSON data files (14 languages)

## Key Namespaces

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
