#!python3

import pyautogui,shelve,random

xCoordinate = []
yCoordinate = []
time = []
setting = shelve.open('setting')

def getCoordinate():
    print('将鼠标移动至要点击的位置，键入数字以记录')
    while True:
        print('输入整数为间隔时间(ms)，其余为退出')
        a = input()
        if a.isdecimal():
            x, y =pyautogui.position()
            xCoordinate.append(x) 
            yCoordinate.append(y)
            time.append(int(a)/1000)
        else:
            print('输入预设名称')
            a = input()
            setting[a] = [xCoordinate,yCoordinate,time]
            break

def callSetting():
    global xCoordinate
    global yCoordinate
    global time
    print('已有预设' + str(list(setting.keys())))
    print('请输入需要调用的设定')
    model = input()
    if model in setting.keys():
        xCoordinate.clear()
        yCoordinate.clear()
        time.clear()
        xCoordinate = setting[model][0]
        yCoordinate = setting[model][1]
        time = setting[model][2]
        print('已成功调用预设')
    else:
        print('没有此预设')

def click():
    for i in range(len(xCoordinate)):
        pyautogui.moveTo(xCoordinate[i],yCoordinate[i],duration=float(time[i]))
        pyautogui.click()

def deleteSetting():
    print('已有预设' + str(list(setting.keys())))
    print('请输入要删除的预设')
    delete = input()
    if delete in setting.keys():
        del setting[delete]
        print('已成功删除')
    else:
        print('没有此预设')

def main():
    while True:
        print('''指令
        'a': 设置按键
        'b'：调用预设
        'c'：开始点击
        'd': 删除预设
        'f': 关闭程序
        ''')
        command = input()
        if command == 'a':
            getCoordinate()
        elif command == 'b':
            callSetting()
        elif command == 'c':
            click()
        elif command == 'd':
            deleteSetting()
        elif command == 'f':
            setting.close()
            break
        else:
            print('请输入正确指令')

if __name__ == '__main__':
    main()