# Card Mechanics Analysis Template

## Template Structure

### 1. Card Rarity Odds System

**Source Files to Check:**
- `MegaCrit.Sts2.Core.Odds/CardRarityOdds.cs`
- `MegaCrit.Sts2.Core.Entities.Cards/CardRarity.cs`
- `MegaCrit.Sts2.Core.Entities.Ascension/AscensionHelper.cs`

**Analysis Points:**
- Base rarity probabilities for each encounter type
- Rarity growth system (how odds change over time)
- Ascension difficulty modifications
- Reset conditions (when odds reset)

**Output Format:**
```markdown
## Card Rarity Odds

**Source**: `MegaCrit.Sts2.Core.Odds/CardRarityOdds.cs`

### Base Rarity Probabilities

| Encounter Type | Common | Uncommon | Rare | Code Reference |
|---|---|---|---|---|
| Regular | [value]% | [value]% | [value]% | `CardRarityOdds.cs:line` |
| Elite | [value]% | [value]% | [value]% | `CardRarityOdds.cs:line` |
| Boss | [value]% | [value]% | [value]% | `CardRarityOdds.cs:line` |
| Shop | [value]% | [value]% | [value]% | `CardRarityOdds.cs:line` |

### Ascension 10 Changes

| Encounter Type | Common | Uncommon | Rare |
|---|---|---|---|
| Regular | [value]% | [value]% | [value]% |
| Elite | [value]% | [value]% | [value]% |
| Boss | [value]% | [value]% | [value]% |
| Shop | [value]% | [value]% | [value]% |

### Rarity Growth System

- **Base Growth Rate**: [value]% per card roll
- **Ascension 10 Growth Rate**: [value]% per card roll
- **Maximum Offset**: [value]%
- **Reset Condition**: [when odds reset]
- **Reset Value**: [value]%

**Code Reference**: `CardRarityOdds.cs:31,53-65`
```

### 2. Card Pool Composition

**Source Files to Check:**
- `MegaCrit.Sts2.Core.Models.CardPools/`
- Character-specific card pool classes
- `MegaCrit.Sts2.Core.Models.Cards/` - Individual card definitions

**Analysis Points:**
- Character-specific card pools
- Universal/common card pools
- Card color/type distribution
- Unlock conditions for cards

**Output Format:**
```markdown
## Card Pool Composition

### Character-Specific Pools

| Character | Card Count | Color | Card Types | Code Reference |
|---|---|---|---|---|
| [Character] | [count] | [color] | [types] | `file.cs:line` |

### Universal/Common Cards

| Category | Color | Card Count | Examples |
|---|---|---|---|
| [Category] | [color] | [count] | [examples] |

### Card Type Distribution

| Card Type | Percentage | Notes |
|---|---|---|
| Attack | [value]% | [notes] |
| Skill | [value]% | [notes] |
| Power | [value]% | [notes] |
| Status | [value]% | [notes] |
| Curse | [value]% | [notes] |
```

### 3. Card Upgrade Mechanics

**Source Files to Check:**
- Card implementation classes (look for upgrade methods)
- `MegaCrit.Sts2.Core.Entities.Cards/CardUpgradePreviewType.cs`
- Cost modification logic

**Analysis Points:**
- How card stats change on upgrade
- Cost changes (energy cost reduction)
- Effect changes (new effects, enhanced effects)
- Upgrade preview types

**Output Format:**
```markdown
## Card Upgrade Mechanics

### Upgrade Patterns

| Pattern Type | Description | Example Cards |
|---|---|---|
| [Pattern] | [description] | [examples] |

### Cost Changes

- **Standard Cost Reduction**: [explain]
- **Special Cases**: [list any cards with unique upgrade cost behavior]

### Effect Enhancements

| Enhancement Type | Description | Code Reference |
|---|---|---|
| [Type] | [description] | `file.cs:line` |

### Ascension 10 Changes

- [List any upgrade-related changes in Ascension 10]
```

### 4. Keyword System

**Source Files to Check:**
- `MegaCrit.Sts2.Core.Entities.Cards/CardKeyword.cs`
- `MegaCrit.Sts2.Core.Entities.Cards/CardKeywordExtensions.cs`
- Card implementations (keyword usage)

**Analysis Points:**
- All card keywords and their effects
- Keyword interactions
- Keywords that prevent card play
- Keywords that affect card lifetime

**Output Format:**
```markdown
## Keyword System

### Keyword Definitions

| Keyword | Effect | Prevents Play? | Affects Lifetime? | Code Reference |
|---|---|---|---|---|
| [Keyword] | [effect] | [yes/no] | [yes/no] | `file.cs:line` |

### Keyword Interactions

- [Keyword A] + [Keyword B]: [explain interaction]
- [Keyword C] prevents [Keyword D]: [explain prevention]

### Keyword Statistics

| Keyword | Card Count | Most Common On |
|---|---|---|
| [Keyword] | [count] | [card type/color] |
```

## Analysis Checklist

- [ ] Documented all rarity probabilities (base and Ascension 10)
- [ ] Mapped card pool composition by character
- [ ] Identified all upgrade patterns
- [ ] Listed all keywords and their effects
- [ ] Checked for Ascension 10 changes in card systems
- [ ] Verified code references for all claims
- [ ] Noted any special cases or exceptions
- [ ] Identified interactions between card mechanics
