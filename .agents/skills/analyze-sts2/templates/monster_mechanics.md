# Monster Mechanics Analysis Template

## Template Structure

### 1. Monster AI State Machines

**Source Files to Check:**
- `MegaCrit.Sts2.Core.MonsterMoves/MonsterMoveStateMachine/`
- `MegaCrit.Sts2.Core.Models.Monsters/` - Look for `GenerateMoveStateMachine()` methods
- Individual monster model classes

**Analysis Points:**
- State machine types (loop, random, conditional, mixed)
- Move pattern definitions
- State transitions and conditions
- AI decision-making logic

**Output Format:**
```markdown
## Monster AI State Machines

**Source**: `MegaCrit.Sts2.Core.Monster/MonsterMoveStateMachine/`

### State Machine Types

| Type | Description | Example Monsters | Code Reference |
|---|---|---|---|
| Loop | [description] | [examples] | `file.cs:line` |
| Random | [description] | [examples] | `file.cs:line` |
| Conditional | [description] | [examples] | `file.cs:line` |
| Mixed | [description] | [examples] | `file.cs:line` |

### State Machine Analysis Example

**Monster**: [Monster Name]
**Type**: [State Machine Type]
**Source**: `MegaCrit.Sts2.Core.Models.Monsters/[MonsterName].cs:line`

**State Flow**:
1. [State 1] → [Action]
2. [State 2] → [Action]
3. [Transition Condition] → [Next State]

**Ascension 10 Changes**:
- [List any AI changes in Ascension 10]
```

### 2. Monster Move Patterns

**Source Files to Check:**
- `MegaCrit.Sts2.Core.MonsterMoves/`
- Monster move action classes
- Intent definitions

**Analysis Points:**
- Move types (attack, block, buff, debuff, summon, heal, status)
- Damage values and multipliers
- Block values
- Power applications
- Move timing and conditions

**Output Format:**
```markdown
## Monster Move Patterns

### Move Types

| Move Type | Description | Intent Icon | Code Reference |
|---|---|---|---|
| Attack | [description] | [icon] | `file.cs:line` |
| Block | [description] | [icon] | `file.cs:line` |
| Buff | [description] | [icon] | `file.cs:line` |
| Debuff | [description] | [icon] | `file.cs:line` |
| Summon | [description] | [icon] | `file.cs:line` |
| Heal | [description] | [icon] | `file.cs:line` |
| Status | [description] | [icon] | `file.cs:line` |

### Move Pattern Analysis

**Monster**: [Monster Name]
**Move**: [Move Name]

**Base Values**:
- Damage: [value]
- Block: [value]
- Hits: [value]
- Powers Applied: [list]

**Ascension 10 Changes**:
- Damage: [new value] (was [old value])
- Block: [new value] (was [old value])
- Hits: [new value] (was [old value])
- New Powers: [list]

**Code Reference**: `file.cs:line`
```

### 3. Ascension Difficulty Changes

**Source Files to Check:**
- `MegaCrit.Sts2.Core.Entities.Ascension/AscensionHelper.cs`
- Monster `GenerateMoveStateMachine()` methods
- Monster `AfterAddedToRoom()` methods

**Analysis Points:**
- Value changes (HP, damage, block)
- Behavior changes (new moves, different patterns)
- Entry powers (powers applied on spawn)
- Move frequency changes

**Output Format:**
```markdown
## Ascension Difficulty Changes

### Value Changes

| Monster | Stat | Base Value | Ascension 10 | Change Type | Code Reference |
|---|---|---|---|---|---|
| [Monster] | HP | [value] | [value] | [increase/decrease] | `file.cs:line` |
| [Monster] | Damage | [value] | [value] | [increase/decrease] | `file.cs:line` |
| [Monster] | Block | [value] | [value] | [increase/decrease] | `file.cs:line` |

### Behavior Changes

| Monster | Base Behavior | Ascension 10 Behavior | Code Reference |
|---|---|---|---|
| [Monster] | [description] | [description] | `file.cs:line` |

### Entry Powers

**Monsters with Ascension-Dependent Entry Powers**:

| Monster | Base Powers | Ascension 10 Powers | Code Reference |
|---|---|---|---|
| [Monster] | [list] | [list] | `file.cs:line` |

**Note**: Entry powers are applied in `AfterAddedToRoom()` method.
```

### 4. Encounter Pools

**Source Files to Check:**
- `MegaCrit.Sts2.Core.Models.Encounters/`
- Act definitions
- Encounter pool classes

**Analysis Points:**
- Encounter composition (monster groups)
- Act distribution (which encounters appear in which acts)
- Room type restrictions (monster room, elite room, boss room)
- Encounter weights and probabilities

**Output Format:**
```markdown
## Encounter Pools

### Encounter Composition

| Encounter | Monsters | Room Type | Acts | Code Reference |
|---|---|---|---|---|
| [Encounter] | [list] | [type] | [acts] | `file.cs:line` |

### Act Distribution

| Act | Monster Encounters | Elite Encounters | Boss Encounters |
|---|---|---|---|
| [Act 1] | [count] | [count] | [count] |
| [Act 2] | [count] | [count] | [count] |
| [Act 3] | [count] | [count] | [count] |

### Encounter Weights

**Note**: Some encounters may have different spawn weights.

| Encounter | Base Weight | Ascension 10 Weight | Notes |
|---|---|---|---|
| [Encounter] | [value] | [value] | [notes] |
```

## Analysis Checklist

- [ ] Identified all state machine types
- [ ] Analyzed move patterns for key monsters
- [ ] Documented all Ascension 10 changes
- [ ] Mapped encounter pools by act
- [ ] Checked for entry powers in `AfterAddedToRoom()`
- [ ] Verified code references for all claims
- [ ] Noted any special AI behaviors
- [ ] Identified monster-specific mechanics
