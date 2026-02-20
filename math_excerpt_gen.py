import arxiv
import time

def collect_math_excerpts(num = 20):

    client = arxiv.Client(page_size=100, delay_seconds=1)

    search = arxiv.Search(
        query="cat:math*",
        max_results=num,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    excerpts = []
    for result in client.results(search):
        excerpt = result.summary[:500]  # Get the first 200 characters of the summary
        excerpts.append(excerpt)
        time.sleep(1)  # To avoid hitting the API rate limit
    
    with open('math_gen_output.md', 'w') as f:
        for excerpt in excerpts:
            f.write(excerpt + "\n")  # Separate excerpts by two newlines

    return " ".join(excerpts)