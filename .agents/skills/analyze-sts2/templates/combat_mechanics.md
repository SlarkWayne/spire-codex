# Combat Mechanics Analysis Template

## Template Structure

### 1. Damage Calculation System

**Source Files to Check:**
- `MegaCrit.Sts2.Core.Combat/` - Combat logic
- `MegaCrit.Sts2.Core.Entities.Actions/` - Action implementations
- `MegaCrit.Sts2.Core.Entities.Powers/` - Power modifiers

**Analysis Points:**
- Base damage formula
- Damage modifiers (strength, dexterity, powers)
- Multi-hit damage calculation
- Damage reduction/blocking interaction
- Critical hit mechanics (if any)

**Output Format:**
```markdown
## Damage Calculation

**Core Formula**: [Explain the damage calculation formula]

**Modifiers**:
| Modifier Type | Effect | Code Reference |
|---|---|---|
| Strength | +1 damage per stack | `file.cs:line` |
| Dexterity | +1 block per stack | `file.cs:line` |
| [Power Name] | [Effect description] | `file.cs:line` |

**Ascension 10 Changes**:
- [List any damage-related changes in Ascension 10]
```

### 2. Blocking Mechanics

**Source Files to Check:**
- Combat action classes
- Block-related powers
- Creature health/block management

**Analysis Points:**
- Block calculation formula
- Block decay/retention mechanics
- Block vs damage interaction
- Powers that modify block

**Output Format:**
```markdown
## Blocking Mechanics

**Block Calculation**: [Explain how block is calculated]

**Block Behavior**:
- Block duration: [permanent/decays/turn-based]
- Damage absorption: [how damage reduces block]
- Overflow damage: [how excess damage is handled]

**Block Modifiers**:
| Power | Effect | Code Reference |
|---|---|---|
| [Power Name] | [Effect] | `file.cs:line` |

**Ascension 10 Changes**:
- [List any blocking-related changes]
```

### 3. Power System

**Source Files to Check:**
- `MegaCrit.Sts2.Core.Entities.Powers/PowerType.cs`
- `MegaCrit.Sts2.Core.Entities.Powers/PowerStackType.cs`
- Power implementation classes

**Analysis Points:**
- Power stacking types (DoesStackType enum)
- Power application/removal timing
- Power interaction rules
- Power duration/turn management

**Output Format:**
```markdown
## Power System

**Stacking Types**:
| Stack Type | Behavior | Example Powers |
|---|---|---|
| [Type] | [Description] | [Examples] |

**Power Application Flow**:
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Key Interactions**:
- [Power A] interacts with [Power B]: [Explain interaction]
- [Power C] prevents [Power D]: [Explain prevention]

**Ascension 10 Changes**:
- [List any power system changes]
```

### 4. Intent System

**Source Files to Check:**
- `MegaCrit.Sts2.Core.Entities.Intents/`
- Monster move classes
- Intent icon mappings

**Analysis Points:**
- Intent types and their meanings
- Intent icon associations
- Intent prediction mechanics
- Intent-changing powers

**Output Format:**
```markdown
## Intent System

**Intent Types**:
| Intent | Description | Icon | Code Reference |
|---|---|---|---|
| [Intent Name] | [Description] | [Icon name] | `file.cs:line` |

****Intent Prediction**:
- [Explain how players can predict monster intents]
- [List any powers that change/reveal intents]

**Ascension 10 Changes**:
- [List any intent system changes]
```

## Analysis Checklist

- [ ] Identified all damage calculation components
- [ ] Documented blocking mechanics completely
- [ ] Mapped power stacking behaviors
- [ ] Listed all intent types and icons
- [ ] Checked for Ascension 10 changes in each system
- [ ] Verified code references for all claims
- [ ] Noted interactions between combat systems
- [ ] Identified any special cases or edge conditions
