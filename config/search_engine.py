import json
import os

SETTINGS_FILE = os.path.join(os.path.dirname(__file__), "settings.json")

BUILTIN_ENGINES = {
    "DuckDuckGo": "https://duckduckgo.com/?q=",
    "Google": "https://www.google.com/search?q=",
    "Bing": "https://www.bing.com/search?q=",
    "Yandex": "https://yandex.com/search/?text=",
}

def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "default_search_engine": "DuckDuckGo",
        "custom_search_url": ""
    }

def save_settings(settings):
    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=4)

def get_search_url(engine_name, custom_url=None):
    if engine_name == "Özel..." and custom_url:
        return custom_url
    return BUILTIN_ENGINES.get(engine_name)
