import pygetwindow as gw
import pyautogui

# 지금 활성화된 창이 어떤 게 있는지 찾기
# print(gw.getAllTitles())

# 특정 윈도우 타이틀 찾기
window = gw.getWindowsWithTitle('Microsoft Excel.app')[0]

#해당 창 활성화
window.activate()

# 찾은 윈도우의 좌표 및 크기 가져오기
x, y, width, height = window.left, window.top, window.width, window.height

window.activate()

# 해당 영역의 스크린샷 찍기
screenshot = pyautogui.screenshot(region=(x, y, width, height))

# 이미지 파일로 저장
screenshot.save('screenshot.png')
