import pyautogui
import pyperclip
import time

def auto_type_from_clipboard():
    print("=== 键盘输入模拟器已启动 ===")
    print("请在 5 秒内，切换到目标网页，并用鼠标点击一下那个无法粘贴的输入框...")
    
    # 倒计时 5 秒，给你时间切换窗口
    for i in range(5, 0, -1):
        print(f"倒计时: {i} 秒")
        time.sleep(1)
        
    print("开始输入！请不要触碰键盘和鼠标...")
    
    # 从剪贴板获取你刚才复制的英文文本
    text = pyperclip.paste()
    
    if not text:
        print("错误：剪贴板是空的，请先复制一段文字！")
        return

    # 核心代码：模拟键盘逐字输入
    # interval 是每个字符之间的输入间隔（秒）
    # 0.02 秒比较像人类较快打字的速度，也能防止网页因为输入过快而卡死
    pyautogui.write(text, interval=0.02)
    
    print("\n输入完成！")

if __name__ == "__main__":
    auto_type_from_clipboard()