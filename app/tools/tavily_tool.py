from tavily import TavilyClient
from config import api_key


client = TavilyClient(
    api_key =api_key.TAVILY_API_KEY
)

def tavily_search(query):
    response = client.search(
        query=query,
        max_results=5
    )

    search_result = []
    for id,result in enumerate(response['result'],1):
        title = result.get('title', "unknown")
        url = result.get('url','')
        content = result.get('content','').strip()

        if len(content) >300:
            content = content[:300].rsplit(" ",1)[0] + "..."
        
        search_result.append(
            f'{id}. **{title}**\n {url}\n {content}'
        )

    return search_result
