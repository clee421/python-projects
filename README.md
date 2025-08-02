# Python

Python repository for building somethig with the usage of the standard libraries.

NOTE: The repository has not been verified. I spent $0.82 in creating the code with claude.

## Setup

```shell
uv venv python-project --python 3.10
source python-project/bin/activate
```

## Prompt

Prompted claude to create the repository with:

```
Build a Python project called `webscrape-reporter` using a `src/` layout and only a `pyproject.toml` for packaging (no setup.py). The project scrapes a given URL, extracts hyperlinks,
  summarizes statistics, and outputs a report in text, JSON, or CSV format.

  Use the following structure:
  - `src/webscrape_reporter/scraper/fetcher.py`: `fetch_url(url: str) -> str` that fetches the raw HTML using `urllib.request` with error handling.
  - `src/webscrape_reporter/scraper/parser.py`: `parse_html(html: str) -> list[str]` that parses the HTML and returns a list of href links using `html.parser.HTMLParser`.
  - `src/webscrape_reporter/reports/formatter.py`: `save_report(links, summary, output_format)` that writes the links and summary to a file in CSV, JSON, or text based on a CLI argument.
  - `src/webscrape_reporter/reports/statistics.py`: `summarize(links) -> dict` that returns total links, unique domains, and top 5 most common domains using `urllib.parse` and
  `collections.Counter`.
  - `src/webscrape_reporter/cli/main.py`: CLI entrypoint using `argparse`. It should take a URL and optional `--format` argument, call the above modules, and save a report.
  - Use `pyproject.toml` with `[project.scripts] webscrape-report = "webscrape_reporter.cli.main:main"` and a `[tool.setuptools] package-dir = {"" = "src"}` config.
  - Create an example test in `tests/test_parser.py` that validates `parse_html`.
  Avoid using third-party libraries unless necessary.

  Using it would look like:
  ```
  webscrape-report https://news.ycombinator.com/ --format csv
  ```

  Example output:
  ```
  Summary:
  total_links: 30
  unique_domains: 12
  top_domains: [('example.com', 5), ('github.com', 4), ('nytimes.com', 3), ...]

  Links:
  https://example.com/article1
  https://github.com/project
  ```
```

### Cost

```
Total cost:            $0.90
Total duration (API):  4m 55.9s
Total duration (wall): 16m 58.2s
Total code changes:    318 lines added, 39 lines removed
Usage by model:
    claude-3-5-haiku:  22.6k input, 1.6k output, 0 cache read, 0 cache write
       claude-sonnet:  97 input, 15.5k output, 1.5m cache read, 55.2k cache write
```

## How to run

Run the command `webscrape-report https://news.ycombinator.com/ --format csv`

```text
Fetching URL: https://news.ycombinator.com/
Parsing HTML for links...
Generating statistics...

Summary:
total_links: 227
unique_domains: 50
top_domains: [('item', 59), ('from', 30), ('hide', 30), ('vote', 29), ('user', 29)]

Links:
https://news.ycombinator.com
news
newest
front
newcomments
ask
show
jobs
submit
login?goto=news
... and 217 more links

Saving report in csv format...
Report saved to report.csv
```

## How to test

Run `cd webscrape-reporter` and then `python -m pytest tests/ -v`

```
================================================================================================================ test session starts ================================================================================================================
platform darwin -- Python 3.10.16, pytest-8.4.1, pluggy-1.6.0 -- /Users/calvin/Projects/python-projects/python-project/bin/python
cachedir: .pytest_cache
rootdir: /Users/calvin/Projects/python-projects/webscrape-reporter
configfile: pyproject.toml
collected 5 items

tests/test_parser.py::TestParser::test_parse_html_basic PASSED                                                                                                                                                                                [ 20%]
tests/test_parser.py::TestParser::test_parse_html_empty PASSED                                                                                                                                                                                [ 40%]
tests/test_parser.py::TestParser::test_parse_html_empty_href PASSED                                                                                                                                                                           [ 60%]
tests/test_parser.py::TestParser::test_parse_html_mixed_content PASSED                                                                                                                                                                        [ 80%]
tests/test_parser.py::TestParser::test_parse_html_no_href PASSED                                                                                                                                                                              [100%]

================================================================================================================= 5 passed in 0.04s =================================================================================================================
```