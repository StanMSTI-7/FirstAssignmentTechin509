# AI Coding Agent Arena — Document Search Library

A small document-search exercise using synthetic data. Requires Python 3.10+.

## Task Specification

Implement `Library` in `search.py`.

### `Library(path)`
- Accepts a `path` to a JSON file containing a list of document objects. Each document has `source` and `text` string fields.
- Reads and stores documents **once during construction**. Subsequent searches must continue to work even if the original file becomes unavailable.
- Creating a new `Library` with an updated or different file must load the current data from that path.

### `search(query, limit=3)`
- Accepts a string `query` and an optional integer `limit`.
- Trims whitespace from the query string.
- Returns `[]` for blank, empty, or whitespace-only queries.
- Performs case-insensitive substring matching of the query against `doc["text"]`.
- Preserves the original input-file order of matching documents.
- Returns at most `limit` documents.
- Returns `[]` for non-positive limits (zero and negative).
- Preserves all result fields (`source` and `text`).

Assumptions: queries are strings, limits are integers, and JSON is valid.

## Acceptance Checks

Run all checks with:

```bash
python -m unittest -v
```

| # | Scenario | Expected Result | Test File |
|---|----------|-----------------|-----------|
| 1 | Normal query (`"vacation"`) | Returns matching document(s) | `test_search.py` |
| 2 | Unknown query (`"spaceship"`) | Returns `[]` | `test_search.py` |
| 3 | Case-insensitive query (`"PASSWORD"`) | Matches regardless of case | `test_search.py` |
| 4 | Padded query (`" password  "`) | Trimmed before matching | `test_search.py` |
| 5 | Blank query (`""` or `"   "`) | Returns `[]` | `test_search.py` |
| 6 | Limit enforced (`limit=1`) | Returns at most `limit` results | `test_search.py` |
| 7 | Zero limit (`limit=0`) | Returns `[]` | `test_search.py` |
| 8 | Negative limit (`limit=-1`) | Returns `[]` | `test_reveal.py` |
| 9 | File deleted after construction | Searches still work | `test_reveal.py` |
| 10 | New `Library` on updated file | Loads updated data independently | `test_reveal.py` |
| 11 | Multiple matches | Preserves input-file order | `test_reveal.py` |
| 12 | Result fields preserved | Each result contains `source` and `text` | `test_reveal.py` |

Add checks in a separate `test_*.py` file. Do not hard-code answers or add a model/API dependency.

## Verify Your Work

1. Follow your assigned workflow in the [session instructions](../README.md).
2. Read [the additional requirements](REVEAL.md), rotate roles, and update your checks.
3. Review the diff, rerun all checks, and test an additional case.
4. Complete the [Arena record](../templates/ARENA_RECORD.md). Explain the data flow: JSON → library → query → matching text and source.

If blocked, record the command, expected and observed result, likely cause, and next check. A supported diagnosis is an acceptable outcome.

## Data Flow

JSON file → `Library` loads once at construction → `search(query)` trims and lowercases the query → filters documents by case-insensitive substring match → slices to `limit` → returns ordered matches with preserved `source` and `text` fields.

## Quick Run

```bash
python search.py
```
