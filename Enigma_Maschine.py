#Try to rebuild an Enigma Maschine

class Keyboard:    #键盘部分（输入）
    pass

class Plugboard:    #接线板部分（两两交换字母）
    pass

class Rotors:    #转子部分（进一步替换）
    
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'   #标准字母表
    alphabet_list=list(alphabet)    #列表化
    rotors=[]
    
    def __init__(self):    #初始化
        from random import seed,shuffle
        for i in range(0,8):    #生成8个转子
            seed(i)    #加入伪随机数种子，使得每次生成的每个转子的替换是固定的
            shuffle(Rotors.alphabet_list)    #随机洗牌
            Rotors.rotors.append("".join(Rotors.alphabet_list))    #8个转子保存在列表里

        print('Rotors Initialized.\n'    #打印出所有转子的配置
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
        slot1=int(input('选择第一个转子：'))
        if 0 <= slot1 <= 8:
            print('R'+str(slot1)+':',Rotors.rotors[slot1-1])
        slot2=int(input('选择第二个转子：'))
        if 0 <= slot2 <= 8 and slot2 != slot1:
            print('R'+str(slot2)+':',Rotors.rotors[slot2-1])
        slot3=int(input('选择第三个转子：'))
        if 0 <= slot3 <= 8 and slot3 != slot2 != slot1:
            print('R'+str(slot3)+':',Rotors.rotors[slot3-1])
        
    def rotate(self):    #转动功能
        pass    #暂时不知道怎么写
        print('Rotate rotors.')

    def scramble(self):    #字母替换功能，要加参数
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
    
    slot1=slot2=slot3=None
    Rotors()
#    Keyboard()
#    Plugboard()

    def __init__(self):    #初始化
        pass


class Lampboard:    #灯板部分（输出）
    pass
