# References

Google Search String: [chromium python](https://www.google.com/search?q=chromium+python&rlz=1C1YTUH_enIE1084IE1084&oq=chromium+python&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIHCAEQABiABDIHCAIQABiABDIICAMQABgWGB4yCAgEEAAYFhgeMggIBRAAGBYYHjIICAYQABgWGB4yCAgHEAAYFhgeMggICBAAGBYYHjIKCAkQABgKGBYYHtIBCDQyNDZqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8)

```text
I recommend using selenium to automate this process although you could use webbrowser too:
```

```python
from selenium.webdriver import *;

chrome = Chrome() # create browser
chrome.get('http://www.google.com')
```

Result: [](https://stackoverflow.com/questions/30123632/using-python-to-start-a-browser-chromium-and-change-the-url)
