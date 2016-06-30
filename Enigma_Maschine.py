#Try to rebuild an Enigma Maschine

class Keyboard:    #键盘部分（输入）
    def __init__(self):
        print('请输入要加密的内容（英文），请勿换行，或加入标点符号')
        plain_text=input('请输入')
        #加入函数来处理内容，去掉空格之类，用正则表达式去掉英文字母以外的


class Plugboard:    #接线板部分（两两交换字母）
    def __init__(self):
        print('【请设置接线板】')
        print('=========================================\n')
        #正则表达式来第一次替换明文

class Rotors:    #转子部分（进一步替换）
    
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'   #标准字母表
    alphabet_list=list(alphabet)    #列表化
    rotors=[]
    
    def __init__(self):    #初始化
        from random import seed,shuffle
        import re
        for i in range(0,8):    #生成8个转子
            seed(i)    #加入伪随机数种子，使得每次生成的每个转子的替换是固定的
            shuffle(Rotors.alphabet_list)    #随机洗牌
            Rotors.rotors.append("".join(Rotors.alphabet_list))    #8个转子保存在列表里

        print('【转子初始化完毕】\n'    #打印出所有转子的配置
              '=========================================\n'
              '   '+Rotors.alphabet+'\n'
              '=========================================\n'
              'R1:'+Rotors.rotors[0]+'\n'
              'R2:'+Rotors.rotors[1]+'\n'
              'R3:'+Rotors.rotors[2]+'\n'
              'R4:'+Rotors.rotors[3]+'\n'
              'R5:'+Rotors.rotors[4]+'\n'
              'R6:'+Rotors.rotors[5]+'\n'
              'R7:'+Rotors.rotors[6]+'\n'
              'R8:'+Rotors.rotors[7]+'\n'
              '==========================================\n')
        
        print('请选择转子（1-8）')
        invalid_entry='输入的值无效，请重新输入'
        #加入用正则表达式确保输入的是数字
        #这里输入空值会报错
        while True:
            i1=int(input('选择放入第一个插槽的转子：'))
            if 1 <= i1 <= 8:
                slot1=Rotors.rotors[i1-1]
                print('R'+str(i1)+':',slot1)
                break
            else:
                print(invalid_entry)

        while True:
            i2=int(input('选择放入第二个插槽的转子：'))
            if 1 <= i2 <= 8 and i2 != i1:
                slot2=Rotors.rotors[i2-1]
                print('R'+str(i2)+':',slot2)
                break
            else:
                print(invalid_entry)
            
        while True:
            i3=int(input('选择放入第三个插槽的转子：'))
            if 1 <= i3 <= 8 and i3 != i1 and i3 != i2:
                slot3=Rotors.rotors[i3-1]
                print('R'+str(i3)+':',slot3)
                break
            else:
                print(invalid_entry)
        '''
#    def rotate(self):    #转动功能
        print('Rotate rotors.')
        for i in range(0,8):
            print(i)
            list(slot1)[i]=list(slot1)[i-1]    #转子转动平移往前一位
            #不对
        print(''.join(slot1))
        '''
        

    def scramble(self):    #字母替换功能，要加参数
        #用for来遍历明文plain_text，一次加密一个
        print('Input: '+Rotors.alphabet[4])  #输入E
        exchange_1=Rotors.rotors[0].index(Rotors.alphabet[4])    #第一次替换，搜索E在转子#1中的位置
        print('Index in Rotor#1:',exchange_1)
        print('Which is:',Rotors.alphabet[exchange_1])    #变成K

        exchange_2=Rotors.rotors[5].index(Rotors.alphabet[exchange_1])    #第二次替换
        print('Index in Rotor#2:',exchange_2)
        print('Which is:',Rotors.alphabet[exchange_2])    #变成C

        exchange_3=Rotors.rotors[2].index(Rotors.alphabet[exchange_2])    #第三次替换
        print('Index in Rotor#2:',exchange_3)
        print('Which is:',Rotors.alphabet[exchange_3])    #变成Y
        return Rotors.alphabet[exchange_3]



class Reflector:    #反射器部分（返回信号）
    pass

class Enigma:    #主体部分（框架）
    
#    Plugboard()
    Rotors()
#    Keyboard()

    def __init__(self):    #初始化
        pass


class Lampboard:    #灯板部分（输出）
    pass
