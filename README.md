# HelloChusquis-Plugins 🚀

Welcome to the official plugin repository for **HelloChusquis**! This collection features **20 essential (Tier 1) plugins**, refactored and optimized to extend the capabilities of your AI terminal agent, transforming it into an agile and robust productivity tool.

## 🛠️ Installation

To install any plugin from this repository, simply run the following command in your terminal:

```bash
hellochusquis install <plugin_name>
```

*Example: `hellochusquis install calculator`*

---

## ✨ New Capabilities & Highlights

HelloChusquis is constantly evolving. Here are some of the latest advancements that empower your agent:

### 🌐 Advanced Web Browsing (`browser` plugin)
The `browser` plugin provides your agent with real web interaction capabilities:
*   **Real Navigation**: Open any URL and wait for content to load.
*   **Brave Search Integration**: Perform searches using Brave Search, which is bot-friendly and provides structured results.
*   **Text Extraction**: Cleanly extract relevant text from web pages, removing clutter like scripts, styles, and ads.
*   **Screenshots**: Capture images of web content.

### 🛠️ Self-Building Agent (`core/builder.py`)
HelloChusquis can now build its own tools! The `core/builder.py` module enables the agent to:
*   **Investigate APIs**: Automatically search the web for API documentation for new functionalities.
*   **Generate Code**: Write new plugins following the official HelloChusquis standard.
*   **Self-Validation**: Test generated plugins locally and self-correct errors up to 3 times.
*   **Contribution Guidance**: Provide instructions for submitting new plugins via Pull Requests.

### 📈 Real-time Financial Data (`stocks` plugin)
The `stocks` plugin has been upgraded to provide real-time financial insights:
*   **`yfinance` Integration**: Access current prices, historical data, and technical analysis for any stock ticker (e.g., AAPL, TSLA).

---

## 🧩 Available Plugins (20)

| Plugin | Description |
| :--- | :--- |
| `calculator` | Performs mathematical operations with secure `eval`. |
| `worldclock` | Shows current time in any city using `pytz`. |
| `currency` | Currency converter using `https://api.exchangerate-api.com`. |
| `crypto` | Real-time cryptocurrency prices from `https://api.coinbase.com`. |
| `ip` | IP information lookup using `https://ipapi.co`. |
| `joke` | Fetches random jokes from `https://v2.jokeapi.dev`. |
| `qr` | Generates QR codes using the `qrcode` library. |
| `hash` | Generates MD5/SHA256 hashes using `hashlib`. |
| `base64encode` | Encodes/decodes Base64 strings using Python's standard library. |
| `password` | Generates secure passwords using Python's `secrets` module. |
| `sysinfo` | Provides system information using `psutil`. |
| `speedtest` | Performs internet speed tests using `speedtest-cli`. |
| `wikipedia` | Searches Wikipedia for information using the `wikipedia` library. |
| `translate` | Translates text using the `deep-translator` library. |
| `urlshortener` | Shortens URLs using `https://tinyurl.com`. |
| `webscrape` | Extracts main text content from any URL using `httpx` and `beautifulsoup4`. |
| `discord` | Sends messages to Discord via webhook. |
| `recipe` | Searches for recipes using `https://www.themealdb.com`. |
| `movie` | Fetches movie information using OMDb API. |
| `news` | Retrieves latest news using GNews API. |

---

## ✍️ Creating New Plugins

If you wish to contribute a new plugin, please follow this official structure:

```python
PLUGIN_NAME = "my_plugin"
PLUGIN_DESCRIPTION = "A useful description in English"
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "my_plugin",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "param": {"type": "string", "description": "Parameter description"}
            },
            "required": ["param"]
        }
    }
}

def run(param: str) -> str:
    try:
        # Your logic here
        return f"Result: {param}"
    except Exception as e:
        return f"Error: {e}"
```

---

## 🤝 Contributing

1.  **Fork** the project.
2.  Create a new branch for your feature: `git checkout -b feature/new-plugin`.
3.  **Commit** your changes: `git commit -m 'Add plugin X'`.
4.  Push to the branch: `git push origin feature/new-plugin`.
5.  Open a **Pull Request**.

---

## 📄 License

This project is licensed under the **MIT License**. See the `LICENSE` file for more details.

---
*Developed with ❤️ by aminoy77 and the HelloChusquis community.*
