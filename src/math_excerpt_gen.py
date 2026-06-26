import arxiv
from pathlib import Path

EXCERPTS_DIR = Path(__file__).parent.parent / "excerpts"

def collect_math_excerpts(num=20):
    client = arxiv.Client(page_size=100, delay_seconds=1)

    search = arxiv.Search(
        query="cat:math*",
        max_results=num,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    excerpts = [result.summary[:500] for result in client.results(search)]

    with open(EXCERPTS_DIR / "math_gen_output.md", 'w') as f:
        for excerpt in excerpts:
            f.write(excerpt + "\n")

    return " ".join(excerpts)