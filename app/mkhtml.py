import markdown_fastapi_rs


def markdown_to_html(input: str) -> str:
    return markdown_fastapi_rs.md_to_html(input)
