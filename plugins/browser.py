PLUGIN_NAME = "browser"
PLUGIN_DESCRIPTION = "Control a browser: open URLs, search Google, extract text from web pages"
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "browser",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "enum": ["open", "search", "extract", "screenshot"],
                    "description": "Action to perform"
                },
                "url": {
                    "type": "string",
                    "description": "URL to open or extract text from"
                },
                "query": {
                    "type": "string",
                    "description": "Search query for Google search"
                },
                "headless": {
                    "type": "boolean",
                    "description": "Run browser in background (no window). Default: true",
                    "default": True
                }
            },
            "required": ["action"]
        }
    }
}


def run(action: str, url: str = "", query: str = "", headless: bool = True) -> str:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return "ERROR: Playwright not installed. Run: pip3 install playwright && python3 -m playwright install chromium"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
        )
        page = context.new_page()

        try:
            if action == "open":
                if not url:
                    return "ERROR: URL required for open action"
                page.goto(url, timeout=15000)
                page.wait_for_load_state("domcontentloaded")
                title = page.title()
                return f"Opened: {url}\nTitle: {title}"

            elif action == "search":
                if not query:
                    return "ERROR: Query required for search action"
                page.goto(f"https://www.google.com/search?q={query}&hl=es", timeout=15000)
                page.wait_for_load_state("domcontentloaded")

                results = []
                items = page.query_selector_all("div.g")[:8]
                for item in items:
                    try:
                        title_el = item.query_selector("h3")
                        link_el = item.query_selector("a")
                        snippet_el = item.query_selector("div[data-sncf], div.VwiC3b, span.aCOpRe")

                        title = title_el.inner_text() if title_el else ""
                        link = link_el.get_attribute("href") if link_el else ""
                        snippet = snippet_el.inner_text() if snippet_el else ""

                        if title and link:
                            results.append(f"• {title}\n  {link}\n  {snippet[:150]}")
                    except Exception:
                        continue

                if not results:
                    return f"No results found for: {query}"
                return f"Search results for \'{query}\':\n\n" + "\n\n".join(results)

            elif action == "extract":
                if not url:
                    return "ERROR: URL required for extract action"
                page.goto(url, timeout=15000)
                page.wait_for_load_state("domcontentloaded")

                # Elimina scripts, styles y nav para limpiar el texto
                page.evaluate("""
                    document.querySelectorAll(\'script, style, nav, footer, header, aside\').forEach(e => e.remove())
                """)

                import re
                text = page.inner_text("body")
                # Limpia espacios múltiples
                text = re.sub(r'\n{3,}', '\n\n', text).strip()
                return text[:3000] + ("..." if len(text) > 3000 else "")

            elif action == "screenshot":
                if not url:
                    return "ERROR: URL required for screenshot action"
                from pathlib import Path
                page.goto(url, timeout=15000)
                page.wait_for_load_state("domcontentloaded")
                path = str(Path.home() / "workspace" / "screenshot.png")
                page.screenshot(path=path, full_page=False)
                return f"Screenshot saved: {path}"

            else:
                return f"ERROR: Unknown action \'{action}\'. Use: open, search, extract, screenshot"

        except Exception as e:
            return f"ERROR: {str(e)}"
        finally:
            browser.close()
