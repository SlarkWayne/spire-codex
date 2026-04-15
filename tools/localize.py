#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
DEFAULT_LANG = "zhs"
ENTITY_TYPES = [
    "acts",
    "encounters",
    "monsters",
    "ascensions",
    "cards",
    "relics",
    "powers",
    "keywords",
    "events",
    "potions",
    "characters",
    "modifiers",
    "afflictions",
    "orbs",
    "epochs",
    "achievements",
]
ASCENSION_ENUM_TO_LEVEL = {
    "None": "LEVEL_00",
    "SwarmingElites": "LEVEL_01",
    "WearyTraveler": "LEVEL_02",
    "Poverty": "LEVEL_03",
    "TightBelt": "LEVEL_04",
    "AscendersBane": "LEVEL_05",
    "Gloom": "LEVEL_06",
    "Scarcity": "LEVEL_07",
    "ToughEnemies": "LEVEL_08",
    "DeadlyEnemies": "LEVEL_09",
    "DoubleBoss": "LEVEL_10",
}


@dataclass
class Candidate:
    input: str
    status: str
    entity_type: str
    id: str
    localized_name: str | None
    english_name: str | None
    source_file: str


@dataclass
class LookupResult:
    input: str
    status: str
    entity_type: str | None = None
    id: str | None = None
    localized_name: str | None = None
    english_name: str | None = None
    source_file: str | None = None
    candidates: list[Candidate] | None = None
    attempted: list[str] | None = None


def load_json(lang: str, name: str) -> Any:
    path = DATA_DIR / lang / f"{name}.json"
    if not path.exists():
        return {} if name == "translations" else []
    return json.loads(path.read_text(encoding="utf-8"))


def display_name(item: dict[str, Any]) -> str | None:
    value = item.get("name") or item.get("title") or item.get("term")
    return str(value) if value is not None else None


def pascal_to_id(value: str) -> str:
    value = value.split(".")[-1]
    if "_" in value or value.upper() == value:
        return value.upper()
    value = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", value)
    value = re.sub(r"(?<=[A-Z])(?=[A-Z][a-z])", "_", value)
    return value.upper()


def unique_attempts(raw_input: str) -> list[str]:
    attempts: list[str] = []
    for attempt in (raw_input.upper(), pascal_to_id(raw_input)):
        if attempt not in attempts:
            attempts.append(attempt)
    return attempts


def find_item(items: list[dict[str, Any]], attempts: list[str]) -> dict[str, Any] | None:
    for attempt in attempts:
        for item in items:
            if str(item.get("id", "")).upper() == attempt:
                return item
    return None


def make_candidate(
    raw_input: str,
    entity_type: str,
    entity_id: str,
    localized_name: str | None,
    english_name: str | None,
    source_file: str,
    status: str = "ok",
) -> Candidate:
    return Candidate(
        input=raw_input,
        status=status,
        entity_type=entity_type,
        id=entity_id,
        localized_name=localized_name,
        english_name=english_name,
        source_file=source_file,
    )


def candidate_to_result(candidate: Candidate) -> LookupResult:
    return LookupResult(
        input=candidate.input,
        status=candidate.status,
        entity_type=candidate.entity_type,
        id=candidate.id,
        localized_name=candidate.localized_name,
        english_name=candidate.english_name,
        source_file=candidate.source_file,
    )


def lookup_entity(lang: str, entity_type: str, raw_input: str) -> LookupResult:
    if entity_type not in ENTITY_TYPES:
        return LookupResult(
            input=raw_input,
            status="missing",
            entity_type=entity_type,
            attempted=[entity_type],
        )

    attempts = unique_attempts(raw_input)
    localized_items = load_json(lang, entity_type)
    english_items = load_json("eng", entity_type)
    localized_item = find_item(localized_items, attempts)
    english_item = find_item(english_items, attempts)

    if localized_item is not None:
        entity_id = str(localized_item["id"])
        english_name = display_name(english_item) if english_item else None
        return candidate_to_result(
            make_candidate(
                raw_input=raw_input,
                entity_type=entity_type,
                entity_id=entity_id,
                localized_name=display_name(localized_item),
                english_name=english_name,
                source_file=str(Path("data") / lang / f"{entity_type}.json"),
            )
        )

    if english_item is not None:
        return LookupResult(
            input=raw_input,
            status="missing",
            entity_type=entity_type,
            id=str(english_item["id"]),
            localized_name=None,
            english_name=display_name(english_item),
            source_file=str(Path("data") / "eng" / f"{entity_type}.json"),
            attempted=attempts,
        )

    return LookupResult(
        input=raw_input,
        status="missing",
        entity_type=entity_type,
        attempted=attempts,
    )


def lookup_glossary(lang: str, raw_input: str) -> LookupResult:
    attempts = unique_attempts(raw_input)
    localized_item = find_item(load_json(lang, "glossary"), attempts)
    english_item = find_item(load_json("eng", "glossary"), attempts)

    if localized_item is not None:
        term_id = str(localized_item["id"])
        return candidate_to_result(
            make_candidate(
                raw_input=raw_input,
                entity_type="glossary",
                entity_id=term_id,
                localized_name=display_name(localized_item),
                english_name=display_name(english_item) if english_item else None,
                source_file=str(Path("data") / lang / "glossary.json"),
            )
        )

    if english_item is not None:
        return LookupResult(
            input=raw_input,
            status="missing",
            entity_type="glossary",
            id=str(english_item["id"]),
            english_name=display_name(english_item),
            source_file=str(Path("data") / "eng" / "glossary.json"),
            attempted=attempts,
        )

    return LookupResult(
        input=raw_input,
        status="missing",
        entity_type="glossary",
        attempted=attempts,
    )


def lookup_translation(lang: str, group: str, key: str) -> LookupResult:
    localized = load_json(lang, "translations")
    english = load_json("eng", "translations")
    localized_group = localized.get(group, {}) if isinstance(localized, dict) else {}
    english_group = english.get(group, {}) if isinstance(english, dict) else {}
    term_id = f"{group}.{key}"

    if key in localized_group:
        return candidate_to_result(
            make_candidate(
                raw_input=term_id,
                entity_type="translations",
                entity_id=term_id,
                localized_name=str(localized_group[key]),
                english_name=str(english_group[key]) if key in english_group else None,
                source_file=str(Path("data") / lang / "translations.json"),
            )
        )

    if key in english_group:
        return LookupResult(
            input=term_id,
            status="missing",
            entity_type="translations",
            id=term_id,
            english_name=str(english_group[key]),
            source_file=str(Path("data") / "eng" / "translations.json"),
            attempted=[term_id],
        )

    return LookupResult(
        input=term_id,
        status="missing",
        entity_type="translations",
        attempted=[term_id],
    )


def lookup_term(lang: str, term_source: str, parts: list[str]) -> LookupResult:
    if term_source == "glossary":
        if len(parts) != 1:
            raise ValueError("--term glossary requires exactly one ID")
        return lookup_glossary(lang, parts[0])

    if term_source == "translations":
        if len(parts) != 2:
            raise ValueError("--term translations requires GROUP and KEY")
        return lookup_translation(lang, parts[0], parts[1])

    raise ValueError("--term source must be glossary or translations")


def result_as_candidate(
    result: LookupResult,
    include_missing_fallback: bool = False,
) -> Candidate | None:
    is_missing_fallback = (
        include_missing_fallback
        and result.status == "missing"
        and result.english_name is not None
    )
    if result.status != "ok" and not is_missing_fallback:
        return None

    if result.entity_type is None or result.id is None:
        return None
    return make_candidate(
        raw_input=result.input,
        entity_type=result.entity_type,
        entity_id=result.id,
        localized_name=result.localized_name,
        english_name=result.english_name,
        source_file=result.source_file or "",
        status=result.status,
    )


def translation_key_candidates(
    lang: str,
    raw_input: str,
    include_missing_fallback: bool = False,
) -> list[Candidate]:
    candidates: list[Candidate] = []
    translations = load_json(lang, "translations")
    english = load_json("eng", "translations")
    if not isinstance(translations, dict):
        translations = {}
    if not isinstance(english, dict):
        english = {}
    if not translations and not english:
        return candidates

    groups = list(translations)
    groups.extend(group for group in english if group not in translations)
    for group in groups:
        localized_values = translations.get(group, {})
        english_values = english.get(group, {})
        if not isinstance(localized_values, dict):
            localized_values = {}
        if not isinstance(english_values, dict):
            english_values = {}
        for key in (raw_input, raw_input.upper()):
            if key in localized_values or key in english_values:
                result = lookup_translation(lang, group, key)
                candidate = result_as_candidate(result, include_missing_fallback)
                if candidate and candidate not in candidates:
                    candidates.append(candidate)
    return candidates


def lookup_auto(lang: str, raw_input: str) -> LookupResult:
    if raw_input.startswith("AscensionLevel."):
        enum_name = raw_input.split(".", 1)[1]
        level_id = ASCENSION_ENUM_TO_LEVEL.get(enum_name)
        if level_id is None:
            return LookupResult(
                input=raw_input,
                status="missing",
                entity_type="ascensions",
                attempted=[enum_name],
            )
        result = lookup_entity(lang, "ascensions", level_id)
        result.input = raw_input
        return result

    candidates: list[Candidate] = []
    fallback_candidates: list[Candidate] = []
    for entity_type in ENTITY_TYPES:
        result = lookup_entity(lang, entity_type, raw_input)
        candidate = result_as_candidate(result)
        if candidate:
            candidates.append(candidate)
            continue
        fallback_candidate = result_as_candidate(result, include_missing_fallback=True)
        if fallback_candidate:
            fallback_candidates.append(fallback_candidate)

    glossary_result = lookup_glossary(lang, raw_input)
    glossary_candidate = result_as_candidate(glossary_result)
    if glossary_candidate:
        candidates.append(glossary_candidate)
    else:
        glossary_fallback = result_as_candidate(
            glossary_result,
            include_missing_fallback=True,
        )
        if glossary_fallback:
            fallback_candidates.append(glossary_fallback)

    for candidate in translation_key_candidates(
        lang,
        raw_input,
        include_missing_fallback=True,
    ):
        if candidate.status == "ok":
            candidates.append(candidate)
        else:
            fallback_candidates.append(candidate)

    if candidates:
        if len(candidates) == 1:
            result = candidate_to_result(candidates[0])
            result.input = raw_input
            return result

        return LookupResult(
            input=raw_input,
            status="ambiguous",
            candidates=candidates,
        )

    if fallback_candidates:
        if len(fallback_candidates) == 1:
            result = candidate_to_result(fallback_candidates[0])
            result.input = raw_input
            return result

        return LookupResult(
            input=raw_input,
            status="ambiguous",
            candidates=fallback_candidates,
        )

    return LookupResult(
        input=raw_input,
        status="missing",
        attempted=unique_attempts(raw_input),
    )


def to_jsonable(result: LookupResult | list[LookupResult]) -> Any:
    if isinstance(result, list):
        return [to_jsonable(item) for item in result]
    return asdict(result)


def markdown_rows(results: list[LookupResult]) -> list[Candidate | LookupResult]:
    rows: list[Candidate | LookupResult] = []
    for result in results:
        if result.status == "ambiguous" and result.candidates:
            rows.extend(
                Candidate(
                    input=c.input,
                    status="ambiguous",
                    entity_type=c.entity_type,
                    id=c.id,
                    localized_name=c.localized_name,
                    english_name=c.english_name,
                    source_file=c.source_file,
                )
                for c in result.candidates
            )
        else:
            rows.append(result)
    return rows


def render_markdown(results: list[LookupResult]) -> str:
    headers = [
        "input",
        "status",
        "entity_type",
        "id",
        "localized_name",
        "english_name",
        "source_file",
    ]
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in markdown_rows(results):
        values = []
        for header in headers:
            value = getattr(row, header, None)
            values.append("" if value is None else str(value))
        lines.append("| " + " | ".join(values) + " |")
    return "\n".join(lines)


def run_self_test() -> None:
    assert lookup_entity("zhs", "acts", "OVERGROWTH").localized_name == "密林"
    assert lookup_entity("zhs", "acts", "HIVE").localized_name == "巢穴"
    assert lookup_entity("zhs", "acts", "GLORY").localized_name == "荣耀"
    assert lookup_entity("zhs", "acts", "UNDERDOCKS").localized_name == "暗港"
    assert lookup_auto("zhs", "AscensionLevel.DoubleBoss").localized_name == "双重Boss"
    assert lookup_entity("zhs", "monsters", "NIBBIT").localized_name == "小啃兽"
    assert lookup_entity("zhs", "encounters", "RUBY_RAIDERS_NORMAL").localized_name == "红宝石劫掠者"
    assert lookup_term("zhs", "glossary", ["BLOCK"]).localized_name == "格挡"
    assert lookup_term("zhs", "translations", ["card_types", "Attack"]).localized_name == "攻击"
    ambiguous = lookup_auto("zhs", "BYRDPIP")
    assert ambiguous.status == "ambiguous"
    assert ambiguous.candidates is not None
    assert {candidate.entity_type for candidate in ambiguous.candidates} >= {"monsters", "relics"}
    fallback = lookup_auto("qqq", "NIBBIT")
    assert fallback.status == "missing"
    assert fallback.entity_type == "monsters"
    assert fallback.id == "NIBBIT"
    assert fallback.localized_name is None
    assert fallback.english_name == "Nibbit"
    assert fallback.source_file == "data/eng/monsters.json"
    assert lookup_auto("zhs", "LOCALIZE_MISSING_SENTINEL").status == "missing"
    print("self-test ok")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Look up localized STS2 names from data JSON.")
    parser.add_argument("--lang", default=DEFAULT_LANG, help="Language code, default: zhs")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of Markdown")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--entity", choices=ENTITY_TYPES, help="Entity JSON type to search")
    group.add_argument("--term", nargs="+", help="Term lookup: glossary ID, or translations GROUP KEY")
    group.add_argument("--auto", nargs="+", help="Automatically resolve ids, class names, or enum names")
    group.add_argument("--self-test", action="store_true", help="Run built-in validation checks")
    parser.add_argument("values", nargs="*", help="Values for --entity lookup")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)

    try:
        if args.self_test:
            if args.values:
                raise ValueError("--self-test does not accept values")
            run_self_test()
            return 0

        if args.entity:
            if not args.values:
                raise ValueError("--entity requires at least one value")
            results = [lookup_entity(args.lang, args.entity, value) for value in args.values]
        elif args.term:
            if args.values:
                raise ValueError("--term does not accept positional values")
            term_source, *parts = args.term
            results = [lookup_term(args.lang, term_source, parts)]
        elif args.auto:
            if args.values:
                raise ValueError("--auto does not accept positional values")
            results = [lookup_auto(args.lang, value) for value in args.auto]
        else:
            raise ValueError("no lookup mode selected")
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.json:
        payload: LookupResult | list[LookupResult] = results[0] if len(results) == 1 else results
        print(json.dumps(to_jsonable(payload), ensure_ascii=False, indent=2))
    else:
        print(render_markdown(results))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
