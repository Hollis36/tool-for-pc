# tool-for-pc

这是一个用于将剪贴板中的文本自动逐字输入到无法直接粘贴的输入框中的 Python 小工具。

## 使用说明

1. 安装依赖：`pyautogui` 和 `pyperclip`
2. 运行：`python auto_type_from_clipboard.py`
3. 在 5 秒内切换到目标输入框并点击它
4. 脚本会读取剪贴板内容并逐字输入

## 文件说明

- `auto_type_from_clipboard.py`: 主脚本，使用 `pyautogui` 模拟键盘输入

