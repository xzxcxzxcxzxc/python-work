#!python3

import pyautogui,shelve,random,copy

xCoordinate = []
yCoordinate = []
time = []
randomXYT = []
setting = shelve.open('按键预设')
randomSetting = shelve.open('随机按键预设')
randomNum = []

def getCoordinate():
    print('将鼠标移动至要点击的位置，键入数字以记录')
    xCoordinate.clear()
    yCoordinate.clear()
    time.clear()
    while True:
        print('输入整数为间隔时间(ms)，其余为退出')
        a = input()
        if a.isdecimal():
            x, y =pyautogui.position()
            xCoordinate.append(x) 
            yCoordinate.append(y)
            time.append(int(a)/1000)
        elif time != []:
            while True:
                print('已有预设' + str(list(setting.keys())))
                print('输入预设名称')
                a = input()  #TODO输入重复报错
                if a in setting.keys():
                    print('已有此预设！')
                    continue
                else:
                    setting[a] = [xCoordinate,yCoordinate,time]
                    break
            break
        else:
            print('输入为空！')
            break

def callSetting():
    global xCoordinate
    global yCoordinate
    global time
    global randomXYT
    print('已有预设' + str(list(setting.keys())))
    print('已有随机预设' + str(list(randomSetting.keys())))
    print('请输入需要调用的设定')
    print('请输入预设类型 "a": 为精确预设 "b": 为随机预设')
    model = input()
    if model == 'a':
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
    elif model == 'b':
        print('请输入需要调用的随机设定')
        model = input()
        if model in randomSetting.keys():
            randomXYT = randomSetting[model]
            print('已成功调用预设')
        else:
            print('没有此预设')
    else:
        print('请输入正确指令!')

def click(x,y,t):
    for i in range(len(x)):
        pyautogui.moveTo(x[i],y[i],duration=float(t[i]))
        pyautogui.click()
    print('')

def deleteSetting():
    print('已有预设' + str(list(setting.keys())))
    print('已有随机预设' + str(list(randomSetting.keys())))
    print('请输入要删除的预设类型 "a": 为精确预设 "b": 为随机预设')
    delete = input()
    if delete == 'a':
        print('已有预设' + str(list(setting.keys())))
        delete = input()
        if delete in setting.keys():
            del setting[delete]
            print('已成功删除')
        else:
            print('没有此预设')
    elif delete == 'b':
        print('已有随机预设' + str(list(randomSetting.keys())))
        delete = input()
        if delete in randomSetting.keys():
            del randomSetting[delete]
            print('已成功删除')
        else:
            print('没有此预设')
    else:
        print('请输入正确指令!')

def randomClickSetting():
    print('使每次的点击位置在一个矩形位置中随机，防止多次点击相同位置导致被检测')
    randomXYT.clear()
    a = ''
    b = ''
    c = False
    while True:
        if c:
            break
        for i in range(0,2):
            if c:
                break
            if i == 0:
                print('输入整数为间隔时间(ms)，其余为退出')
            else:
                print('请键入任意符号已确认随机区域')
            a = input()
            if (a.isdecimal() and i == 0) or i == 1:
                x,y =pyautogui.position()
                randomXYT.append(x)
                randomXYT.append(y)
                if i == 0:
                    randomXYT.append(int(a)/1000)
            elif randomXYT != []:
                while True:
                    print('已有随机预设' + str(list(randomSetting.keys())))
                    print('输入预设名称')
                    a = input()  
                    if a in randomSetting.keys():
                        print('已有此预设！')
                        continue
                    else:
                        randomSetting[a] = randomXYT
                        c = True
                        break
            else:
                print('输入为空！')
                c = True
                break

def randomClick():
    print(len(randomXYT))
    for i in range(len(randomXYT)//5):
        RX = [randomXYT[i * 5],randomXYT[i * 5 + 3]]
        RY = [randomXYT[i * 5 + 1],randomXYT[i * 5 + 4]]
        RX.sort()
        RY.sort()
        pyautogui.moveTo(random.randint(RX[0],RX[1]),random.randint(RY[0],RY[1]),randomXYT[i * 5 + 2])
        pyautogui.click()

def main():
    modelName = ''
    while True:
        print('''指令
        'a': 设置预设
        'b'：调用预设
        'c'：精确点击
        'd': 删除预设
        'f': 随机预设
        'g': 随机点击
        'h': 关闭程序
        ''')
        command = input()
        if command == 'a':
            getCoordinate()
        elif command == 'b':
            callSetting()
        elif command == 'c':
            if xCoordinate == []:
                print('未添加预设!')
                continue
            try:
                print('请输入点击次数：')
                t = input()
                for i in range(1,int(t) + 1):
                    click(xCoordinate,yCoordinate,time)
                    print('已运行' + str(i) + '次' )
                print('运行完毕')
            except ValueError:
                print('请输入数字！')
        elif command == 'd':
            deleteSetting()
        elif command == 'f':
            randomClickSetting()
        elif command == 'g':
            if randomXYT == []:
                print('未添加预设!')
                continue
            try:
                print('请输入点击次数：')
                t = input()
                for i in range(1,int(t) + 1):
                    randomClick()
                    print('已运行' + str(i) + '次' )
                print('运行完毕')
            except ValueError():
                    print('请输入数字！')
        elif command == 'h':
            setting.close()
            randomSetting.close()
            break
        else:
            print(randomSetting['a'])
            print(randomXYT)
            print('请输入正确指令!')

if __name__ == '__main__':
    main()