# Nimblet

Nimblet is a lightweight background agent that monitors clipboard content and suggests context-aware snippets and code completions.

Nimblet addresses the problem where developers waste keystrokes re‑typing boilerplate loops and configuration templates copied from memory or search engines, lacking proactive clipboard assistance by not automatically surfacing relevant snippets when needed, forcing manual lookup and copy‑paste.

## Example

```bash
$ python -c "from nimblet.suggester import suggest_snippet; print(suggest_snippet('for loop'))"
for item in iterable:
    print(item)
```

## Install

```bash
pip install -e .
```

## Usage

- `suggest_snippet(text)`: Check clipboard text or user input against known trigger phrases to fetch a matched snippet.

## How it works

- Matches input text against known trigger phrases like "for loop".
- Emits pre-defined hard-coded code snippets for matching triggers.
- Returns `None` when no trigger phrase matches the input text.

## Limitations

- Currently supports only a hard-coded set of trigger phrases (e.g., "for loop").
- Does not monitor actual system clipboard yet; operates on explicit string input.

## Development

```bash
pip install -e ".[dev]"
pytest -q
```

## License

MIT -- see [LICENSE](LICENSE).
