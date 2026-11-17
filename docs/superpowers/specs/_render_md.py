#!/usr/bin/env python3
"""Render a markdown file to a styled, self-contained HTML file next to it."""
import sys
import pathlib
import markdown

src = pathlib.Path(sys.argv[1])
html_body = markdown.markdown(
    src.read_text(encoding="utf-8"),
    extensions=["tables", "fenced_code", "toc", "sane_lists"],
)

CSS = """
:root { color-scheme: light dark; }
body {
  font: 16px/1.65 -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  max-width: 860px; margin: 0 auto; padding: 3rem 1.5rem 6rem;
  color: #1a1a1a; background: #fbfbfa;
}
@media (prefers-color-scheme: dark) {
  body { color: #e6e6e6; background: #16171a; }
  code, pre { background: #22242a !important; }
  th { background: #22242a !important; }
  tr:nth-child(even) td { background: #1c1e22 !important; }
  a { color: #7db4ff; }
  blockquote { color: #aaa; border-color: #3a3d44; }
}
h1 { font-size: 2rem; border-bottom: 2px solid #e2624222; padding-bottom: .3rem; }
h2 { font-size: 1.4rem; margin-top: 2.4rem; border-bottom: 1px solid #8884; padding-bottom: .25rem; }
h3 { font-size: 1.12rem; margin-top: 1.8rem; }
code { font: 13.5px/1.5 "SF Mono", ui-monospace, Menlo, monospace; background: #f0f0ee; padding: .12em .4em; border-radius: 4px; }
pre { background: #f0f0ee; padding: 1rem 1.1rem; border-radius: 8px; overflow-x: auto; border: 1px solid #0001; }
pre code { background: none; padding: 0; }
table { border-collapse: collapse; width: 100%; margin: 1.2rem 0; font-size: 14.5px; }
th, td { border: 1px solid #8883; padding: .5rem .7rem; text-align: left; vertical-align: top; }
th { background: #f2f2f0; }
tr:nth-child(even) td { background: #f7f7f5; }
blockquote { margin: 1rem 0; padding: .2rem 1rem; border-left: 3px solid #e26242; color: #555; }
hr { border: none; border-top: 1px solid #8883; margin: 2rem 0; }
"""

html = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{src.stem}</title><style>{CSS}</style></head>
<body>{html_body}</body></html>"""

out = src.with_suffix(".html")
out.write_text(html, encoding="utf-8")
print(out)
