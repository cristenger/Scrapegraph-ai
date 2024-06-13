from scrapegraphai.graphs import SmartScraperGraph

graph_config = {
    "llm": {
        "model": "ollama/qwen2:7b-instruct-q8_0",
        "temperature": 0,
        "format": "json",
        "base_url": "http://localhost:11434",
    },
    "embeddings": {
        "model": "ollama/nomic-embed-text",
        "base_url": "http://localhost:11434",
    },
    "verbose": True,
}

smart_scraper_graph = SmartScraperGraph(
    prompt="List me all the titles with their urls in the titleline elements",
    source="https://news.ycombinator.com/",
    config=graph_config
)

result = smart_scraper_graph.run()
print(result)