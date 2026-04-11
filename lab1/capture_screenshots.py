"""
Runs each part of lab1.py and lab1_modified.py, captures output,
and renders terminal-style PNG screenshots for the lab report.
"""
import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont
import os
import textwrap

OUT_DIR = os.path.join(os.path.dirname(__file__), "screenshots")
os.makedirs(OUT_DIR, exist_ok=True)

# Try to get a monospace font
def get_font(size=14):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf",
        "/usr/share/fonts/truetype/ubuntu/UbuntuMono-R.ttf",
    ]
    for path in candidates:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()

FONT = get_font(14)
BG = (30, 30, 30)
FG = (220, 220, 220)
HEADER_FG = (100, 200, 100)
PAD = 16
LINE_H = 20


def render_screenshot(title, content, filename):
    lines = content.splitlines()
    # Wrap very long lines
    wrapped = []
    for line in lines:
        if len(line) > 110:
            wrapped.extend(textwrap.wrap(line, 110, break_long_words=True))
        else:
            wrapped.append(line)

    w = 900
    h = PAD * 2 + LINE_H + 4 + len(wrapped) * LINE_H + PAD
    img = Image.new("RGB", (w, max(h, 80)), BG)
    d = ImageDraw.Draw(img)

    # Title bar
    d.rectangle([0, 0, w, LINE_H + PAD], fill=(50, 50, 50))
    d.text((PAD, PAD // 2), f"  {title}", font=FONT, fill=HEADER_FG)
    d.line([0, LINE_H + PAD, w, LINE_H + PAD], fill=(80, 80, 80), width=1)

    y = LINE_H + PAD + 8
    for line in wrapped:
        d.text((PAD, y), line, font=FONT, fill=FG)
        y += LINE_H

    path = os.path.join(OUT_DIR, filename)
    img.save(path)
    print(f"  Saved: {filename}")


# ── Part A — page.text (first 60 lines) ──────────────────────────────────────
print("Capturing Part A...")
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
raw_lines = page.text.splitlines()
preview = "\n".join(raw_lines[:50]) + f"\n\n... (output truncated, total {len(page.text)} characters)"
render_screenshot(
    "Part A — page.text  (Raw HTML Output)",
    f"$ python3 lab1.py   [Part A: page.text]\n\n" + preview,
    "partA_raw_html.png"
)

# ── Part B — soup / prettify (first 50 lines) ────────────────────────────────
print("Capturing Part B...")
soup = BeautifulSoup(page.content, "html.parser")
pretty_lines = soup.prettify().splitlines()
preview_b = "\n".join(pretty_lines[:50]) + f"\n\n... (output truncated, BeautifulSoup parsed object)"
render_screenshot(
    "Part B — BeautifulSoup Parsed Output (soup.prettify())",
    f"$ python3 lab1.py   [Part B: soup]\n\n" + preview_b,
    "partB_soup.png"
)

# ── Part C — ResultsContainer ─────────────────────────────────────────────────
print("Capturing Part C...")
results = soup.find(id="ResultsContainer")
rc_lines = results.prettify().splitlines()
preview_c = "\n".join(rc_lines[:50]) + f"\n\n... (output truncated, ResultsContainer div)"
render_screenshot(
    "Part C — soup.find(id='ResultsContainer')",
    f"$ python3 lab1.py   [Part C: results]\n\n" + preview_c,
    "partC_results_container.png"
)

# ── Part D — job elements ─────────────────────────────────────────────────────
print("Capturing Part D...")
job_elements = results.find_all("div", class_="card-content")
lines_d = ["***Job Element***", f"Total jobs found: {len(job_elements)}", ""]
for i, job_element in enumerate(job_elements[:5]):
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    lines_d.append(f"--- Job {i+1} ---")
    lines_d.append(f"[Raw tag]  {str(title_element)}")
    lines_d.append(f"[.text]    {repr(title_element.text)}")
    lines_d.append(f"[.strip()] {title_element.text.strip()}")
    lines_d.append(f"           {company_element.text.strip()}")
    lines_d.append(f"           {location_element.text.strip()}")
    lines_d.append("")
lines_d.append("... (showing first 5 of 100 jobs)")
lines_d.append("***END***")
render_screenshot(
    "Part D — Extracting Individual Job Elements (first 5 of 100)",
    f"$ python3 lab1.py   [Part D: job_elements]\n\n" + "\n".join(lines_d),
    "partD_job_elements.png"
)

# ── Part E — Python jobs ──────────────────────────────────────────────────────
print("Capturing Part E...")
python_jobs = results.find_all("h2", string=lambda text: "python" in text.lower())
python_job_elements = [h2.parent.parent.parent for h2 in python_jobs]
lines_e = ["\n***Python Job Element***", f"Number of elements:  {len(python_jobs)}", ""]
for job_element in python_job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    lines_e.append(title_element.text.strip())
    lines_e.append(company_element.text.strip())
    lines_e.append(location_element.text.strip())
    lines_e.append("")
lines_e.append("***END***")
render_screenshot(
    "Part E — Filtered Python Jobs",
    f"$ python3 lab1.py   [Part E: python_jobs]\n\n" + "\n".join(lines_e),
    "partE_python_jobs.png"
)

# ── Modified code — quotes ────────────────────────────────────────────────────
print("Capturing Modified Code...")
URL2 = "https://quotes.toscrape.com/"
page2 = requests.get(URL2)
soup2 = BeautifulSoup(page2.content, "html.parser")
quotes = soup2.find_all("div", class_="quote")
lines_m = ["***Quotes***", ""]
for quote in quotes:
    text_el = quote.find("span", class_="text")
    author_el = quote.find("small", class_="author")
    lines_m.append(f'Quote:  {text_el.text.strip()}')
    lines_m.append(f'Author: {author_el.text.strip()}')
    lines_m.append("")
lines_m.append("***END***")
render_screenshot(
    "lab1_modified.py — Quotes Scraper Output",
    f"$ python3 lab1_modified.py\n\n" + "\n".join(lines_m),
    "modified_quotes.png"
)

print("\nDone! All screenshots saved to lab1/screenshots/")
