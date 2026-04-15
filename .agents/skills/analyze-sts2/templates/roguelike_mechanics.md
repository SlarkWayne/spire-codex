# Roguelike Mechanics Analysis Template

## Template Structure

### 1. Map Generation System

**Source Files to Check:**
- `MegaCrit.Sts2.Core.Map/`
- `MegaCrit.Sts2.Core.Odds/UnknownMapPointOdds.cs`
- `MegaCrit.Sts2.Core.Odds/RunOddsSet.cs`
- Act definitions

**Analysis Points:**
- Map structure (nodes, paths, layers)
- Room type distribution (monster, elite, treasure, shop, rest, event, boss)
- Path generation algorithms
- Map size and complexity by act

**Output Format:**
```markdown
## Map Generation System

**Source**: `MegaCrit.Sts2.Core.Map/`

### Map Structure

| Element | Description | Code Reference |
|---|---|---|
| Nodes | [description] | `file.cs:line` |
| Paths | [description] | `file.cs:line` |
| Layers | [description] | `file.cs:line` |

### Room Type Distribution

**Base Probabilities**:
| Room Type | Base Probability | Ascension 10 | Code Reference |
|---|---|---|---|
| Monster | [value]% | [value]% | `UnknownMapPointOdds.cs:line` |
| Elite | [value]% | [value]% | `UnknownMapPointOdds.cs:line` |
| Treasure | [value]% | [value]% | `UnknownMapPointOdds.cs:line` |
| Shop | [value]% | [value]% | `UnknownMapPointOdds.cs:line` |
| Rest | [value]% | [value]% | `UnknownMapPointOdds.cs:line` |
| Event | [value]% | [value]% | `UnknownMapPointOdds.cs:line` |
| Boss | [value]% | [value]% | `UnknownMapPointOdds.cs:line` |

### Map Size by Act

| Act | Node Count | Path Length | Special Features |
|---|---|---|---|
| [Act 1] | [count] | [length] | [features] |
| [Act 2] | [count] | [length] | [features] |
| [Act 3] | [count] | [length] | [features] |

### Path Generation

- **Algorithm**: [explain path generation algorithm]
- **Branching**: [explain how branches are created]
- **Boss Path**: [explain boss path generation]
```

### 2. Reward Allocation System

**Source Files to Check:**
- `MegaCrit.Sts2.Core.Rewards/`
- `MegaCrit.Sts2.Core.Odds/CardRarityOdds.cs`
- `MegaCrit.Sts2.Core.Odds/PotionRewardOdds.cs`
- Reward room implementations

**Analysis Points:**
- Card reward generation (quantity, rarity, options)
- Relic reward distribution
- Potion drop mechanics
- Gold reward amounts
- Reward types by room type

**Output Format:**
```markdown
## Reward Allocation System

### Card Rewards

**Reward Quantities**:
| Room Type | Card Count | Options | Code Reference |
|---|---|---|---|
| Monster | [count] | [options] | `file.cs:line` |
| Elite | [count] | [options] | `file.cs:line` |
| Boss | [count] | [options] | `file.cs:line` |
| Event | [count] | [options] | `file.cs:line` |

**Card Rarity**: See Card Mechanics section for detailed rarity odds.

### Relic Rewards

**Relic Distribution**:
| Source | Pool Type | Quantity | Code Reference |
|---|---|---|---|
| Boss Room | Boss Relics | [count] | `file.cs:line` |
| Elite Room | Elite Relics | [count] | `file.cs:line` |
| Treasure Room | Common Relics | [count] | `file.cs:line` |
| Shop | Shop Relics | [variable] | `file.cs:line` |
| Event | Event Relics | [variable] | `file.cs:line` |

**Ascension 10 Changes**:
- [List any relic reward changes]

### Potion Drops

**Drop Probabilities**:
| Encounter Type | Drop Chance | Code Reference |
|---|---|---|
| Monster | [value]% | `PotionRewardOdds.cs:line` |
| Elite | [value]% | `PotionRewardOdds.cs:line` |
| Boss | [value]% | `PotionRewardOdds.cs:line` |

**Potion Slots**: [max potion slots per character]

**Ascension 10 Changes**:
- [List any potion drop changes]

### Gold Rewards

**Gold Amounts**:
| Source | Base Range | Ascension 10 Range | Code Reference |
|---|---|---|---|
| Monster | [min-max] | [min-max] | `file.cs:line` |
| Elite | [min-max] | [min-max] | `file.cs:line` |
| Treasure | [min-max] | [min-max] | `file.cs:line` |
| Event | [variable] | [variable] | `file.cs:line` |
```

### 3. Relic Pool System

**Source Files to Check:**
- `MegaCrit.Sts2.Core.Models.RelicPools/`
- `MegaCrit.Sts2.Core.Models.Relics/` - Individual relic definitions
- Character-specific relic pools

**Analysis Points:**
- Boss relic pools (by act)
- Common relic pools
- Shop relic pools
- Character-specific relics
- Starter relics

**Output Format:**
```markdown
## Relic Pool System

### Boss Relic Pools

| Act | Boss Relic Count | Example Relics | Code Reference |
|---|---|---|---|
| [Act 1] | [count] | [examples] | `file.cs:line` |
| [Act 2] | [count] | [examples] | `file.cs:line` |
| [Act 3] | [count] | [examples] | `file.cs:line` |

### Common Relic Pools

| Pool | Relic Count | Rarity Distribution | Code Reference |
|---|---|---|---|
| [Pool Name] | [count] | [distribution] | `file.cs:line` |

### Shop Relics

**Shop Relic Pool**:
- **Total Relics**: [count]
- **Price Range**: [min-max] gold
- **Refresh Cost**: [cost] gold

**Code Reference**: `file.cs:line`

### Character-Specific Relics

| Character | Starter Relics | Exclusive Relics | Code Reference |
|---|---|---|---|
| [Character] | [list] | [list] | `file.cs:line` |

### Ascension 10 Changes

- [List any relic pool changes in Ascension 10]
```

### 4. Potion Pool System

**Source Files to Check:**
- `MegaCrit.Sts2.Core.Models.PotionPools/`
- `MegaCrit.Sts2.Core.Models.Potions/` - Individual potion definitions
- Character-specific potion pools

**Analysis Points:**
- Universal potion pool
- Character-specific potion pools
- Potion rarity distribution
- Potion effects and mechanics

**Output Format:**
```markdown
## Potion Pool System

### Universal Potion Pool

**Total Potions**: [count]
**Examples**: [list common potions]

**Code Reference**: `file.cs:line`

### Character-Specific Potions

| Character | Exclusive Potions | Shared Potions | Code Reference |
|---|---|---|---|
| [Character] | [list] | [list] | `file.cs:line` |

### Potion Rarity Distribution

| Rarity | Percentage | Examples |
|---|---|---|
| Common | [value]% | [examples] |
| Uncommon | [value]% | [examples] |

### Potion Mechanics

**Potion Use Rules**:
- **Targeting**: [explain targeting rules]
- **Timing**: [explain when potions can be used]
- **Limits**: [explain usage limits]

**Ascension 10 Changes**:
- [List any potion pool changes]
```

## Analysis Checklist

- [ ] Documented map generation algorithms
- [ ] Mapped room type probabilities (base and Ascension 10)
- [ ] Analyzed reward allocation for all room types
- [ ] Identified all relic pools and compositions
- [ ] Mapped potion pools by character
- [ ] Checked for Ascension 10 changes in all systems
- [ ] Verified code references for all claims
- [ ] Noted any special cases or exceptions
- [ ] Identified interactions between roguelike systems
