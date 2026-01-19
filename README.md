

<p align="left"> <img src="https://komarev.com/ghpvc/?username=facebook-auto-unfriend&label=Repository%20views&color=0e75b6&style=flat" alt="facebook-auto-unfriend" /> </p>

# Facebook Auto-Unfriend Tool 🤖



[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-✓-green)](https://pyautogui.readthedocs.io/)

An automated tool that helps clean up your Facebook friend list using Python and PyAutoGUI. Use responsibly and at your own risk.

> ⚠️ **Important Disclaimer**: This tool is for educational purposes only. Use in accordance with Facebook's Terms of Service.

## 📋 Features

- 🔍 **Image Recognition**: Automatically identifies Facebook UI elements using screenshot matching
- ⚡ **Batch Processing**: Unfriend multiple friends in sequence
- 📜 **Smart Scrolling**: Automatically scrolls through friend lists
- 🛡️ **Error Handling**: Graceful error recovery and logging
- ⚙️ **Configurable**: Adjustable confidence levels and timing delays

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- Facebook account (logged in)
- Stable internet connection

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/shishirRsiam/facebook-auto-unfriend.git
cd facebook-auto-unfriend
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Prepare image files**
   - Take screenshots of these Facebook UI elements (at 100% zoom):
     - `three_dots.png` - The "..." menu button on friend cards
     - `unfriend_button.png` - The "Unfriend" option
     - `confirm_unfriend_button.png` - The confirmation button
   - Save them in the project directory

### Usage

1. **Configure your settings** (optional)
   - Open the script and adjust:
     - `confidence` level (0.8-0.95 for better matching)
     - `time.sleep()` values for your internet speed

2. **Prepare Facebook**
   - Log into Facebook in your browser
   - Navigate to your Friends list
   - Make sure the browser window is visible and not minimized

3. **Run the script**
```bash
python unfriend_automation.py
```

4. **Quickly switch to your browser**
   - You have 5 seconds to click on the browser window
   - The script will start from the top of your friend list

## 📁 Project Structure

```
facebook-auto-unfriend/
├── unfriend_automation.py    # Main automation script
├── three_dots.png            # Screenshot of menu button
├── unfriend_button.png       # Screenshot of unfriend option
├── confirm_unfriend_button.png # Screenshot of confirmation
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── .gitignore               # Git ignore file
```

## ⚙️ Customization

### Adjust Scroll Speed
```python
# In the script, modify:
pg.scroll(-120)  # Change -120 to scroll more/less
time.sleep(0.5)  # Adjust delay after scrolling
```

### Adjust Click Confidence
```python
# For better/worse image matching:
click_image('three_dots.png', confidence=0.8)  # More lenient
click_image('three_dots.png', confidence=0.95) # More strict
```

### Adjust Timing Delays
```python
# If actions are too fast/slow:
time.sleep(1.0)  # Increase for slower internet
time.sleep(0.2)  # Decrease for faster response
```

## ⚠️ Important Warnings

1. **Rate Limiting**: Facebook may temporarily block accounts for rapid unfriending
2. **Terms of Service**: Violating Facebook's ToS may result in account suspension
3. **Irreversible Action**: Unfriending cannot be automatically undone
4. **Test First**: Run with 1-2 friends first to ensure it works correctly
5. **Supervision Required**: Never leave the script running unattended

## 🛡️ Safety Recommendations

- **Start Small**: Test with 5-10 friends first
- **Monitor Closely**: Watch the script to catch errors
- **Take Breaks**: Run in short sessions (e.g., 50 friends per session)
- **Check Limits**: Facebook may have daily unfriend limits
- **Backup First**: Consider downloading your friend list first

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| "Image not found" | Ensure screenshots match exactly (zoom level, theme) |
| Clicking wrong area | Adjust confidence level or retake screenshots |
| Script too fast | Increase time.sleep() values |
| Script too slow | Decrease time.sleep() values |
| Scroll not working | Adjust scroll amount (try -100 to -200) |

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [PyAutoGUI](https://pyautogui.readthedocs.io/) for the automation framework
- Inspired by the need for digital decluttering

## ⭐ Support

If you find this project useful, please give it a star! ⭐

---

**Disclaimer**: This tool is for educational purposes. The author is not responsible for any account restrictions or consequences from using this tool. Use at your own risk and in accordance with all applicable laws and platform terms of service.
```

## Additional Files to Include

### `.gitignore`
```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
.venv/
ENV/
env.bak/
venv.bak/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Custom
*.log
test_screenshots/
```

### `requirements.txt`
```txt
PyAutoGUI==0.9.54
opencv-python==4.8.1.78
pillow==10.1.0
```

### `LICENSE` (MIT License)
```text
MIT License

Copyright (c) 2026 [shishirRsiam]
Permission is hereby granted, free of charge, to any person obtaining a copy
... [standard MIT license text] ...


<p align="left"> <img src="https://komarev.com/ghpvc/?username=shishirrsiam&label=Profile%20views&color=0e75b6&style=flat" alt="shishirrsiam" /> </p>
