# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

`judobase` is an async Python client (aiohttp + Pydantic v2) for the IJF Judobase API at `https://data.ijf.org/api/`. The API is unofficial and was reverse engineered, so the schemas reflect observed responses, not a published spec. Supports Python 3.10+ (CI tests 3.10-3.14).

## Commands

CI uses `uv`; run commands through it locally as well.

```bash
uv sync --extra tests          # install dev/test deps (add --extra docs for Sphinx)
uv run make lint               # ruff check + flake8 (wemake-python-styleguide) + mypy on judobase/
uv run make format             # ruff format + ruff check --fix
uv run make test               # pytest with coverage; fails under 99% coverage
uv run pytest tests/test_base.py::TestBase::test_get_json_success   # single test
uv run sphinx-build -b html docs/source docs/build/html              # build docs
uv build                       # build sdist/wheel
```

Lint and mypy only cover `judobase/`, not `tests/` or `examples/`. The 99% coverage gate means new code in `judobase/` needs tests. There is no `[tool.coverage]` config, so `--cov` also measures `tests/`, which sit at 100% and lift the total.

## Architecture

Three layers, each in its own module:

1. **`judobase/base.py`**: `_Base` owns the `aiohttp.ClientSession` (created in `__init__`, recreated in `__aenter__` if closed, closed in `__aexit__`/`close_session()`). Because `ClientSession()` runs in `__init__`, `JudoBase()` must be instantiated inside a running event loop; outside one it raises `RuntimeError: no running event loop`. Every request goes through `_get_json`, which issues `GET {BASE_URL}get_json` with PHP-style query params (`params[action]`, `params[id_person]`, ...). `_get_json_dict` / `_get_json_list` narrow the response shape and raise `TypeError` otherwise; non-200 raises `ConnectionError`. Thin per-domain subclasses (`CompetitionAPI`, `ContestAPI`, `JudokaAPI`, `RatingAPI`, `CountryAPI`) each map one Judobase `action` to a method that returns Pydantic models. IDs are passed as `str` at this layer.
2. **`judobase/judobase_api.py`**: `JudoBase` multiply inherits all the `*API` classes and adds user-friendly methods (accepting `int | str` IDs, date-range filtering, `WeightEnum` filtering, fan-out with `asyncio.gather` such as `all_contests`). Adding a new endpoint means a raw method on a `*API` class in `base.py`, then, if useful, a wrapper here; a new `*API` class must also be added to `JudoBase`'s bases.
3. **`judobase/schemas.py`**: Pydantic models for every response. Field validators normalize the API's inconsistent date formats to UTC-aware `datetime` (see `Competition.parse_date`). `WeightEnum` and `WEIGHT_ID_MAPPING` translate weight categories to Judobase weight IDs.

Public exports are listed in `judobase/__init__.py` (`__all__`); new public models must be added there. Version lives in `judobase/version.py` (`0.0.0` in the repo) and is read dynamically by setuptools; the publish and Sphinx workflows overwrite it with the GitHub release name on `release: published`. The package ships `py.typed` (PEP 561).

## Tests

- `tests/conftest.py` provides `mock_session` (an `AsyncMock` of `ClientSession`), `mock_api_response` (sets status and JSON on `session.get`), and `get_test_data` (loads `tests/test_data/*.json`).
- Fixture JSON files hold a `mock_response` (an API payload) plus the expected result, under `expected` in every file except `contests_by_competition_id.json`, which uses `dbn`. Tests never call the live API, so an upstream API change does not fail them.
- `base.py` tests patch `judobase.base.ClientSession` with the mock session; `JudoBase` tests patch the `*API` methods directly (e.g. `judobase.base.CompetitionAPI.get_competition_list`).
- Async tests use `@pytest.mark.asyncio` (pytest-asyncio, function-scoped loop per `pytest.ini`).

## Style

- Ruff with a broad rule set (see `pyproject.toml`): line length 100, double quotes, Google-style docstrings required, max McCabe complexity 6.
- flake8 runs `wemake-python-styleguide`; per-file suppressions use `# flake8: noqa: WPSxxx` at the top of the module, and ruff suppressions live in `[tool.ruff.lint.per-file-ignores]`.
- mypy runs on `judobase/` in CI.
