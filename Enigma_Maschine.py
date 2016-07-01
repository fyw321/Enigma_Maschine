#Try to rebuild an Enigma Maschine

##需要改，把不需要的类都去掉


def keyboard():    #键盘部分（输入）

    print('请输入要加密的内容（英文）')
    input_text=input('请输入')
    ##改进：加入正则表达式来处理内容，去掉换行符号，把空格用下划线代替，包容数字与少数标点

def plugboard():    #接线板部分（两两交换字母）
    print('【请设置接线板】')
    ##加入一个输入功能来设置字符交换
    print('=========================================\n')
    ##正则表达式来第一次替换明文

def rotors():    #转子部分（进一步替换）
    from random import seed,shuffle
    import re
    
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'   #标准字母表
    ##加入数字与少数标点的支持
    alphabet_list=list(alphabet)    #列表化
    rt=[]

    for i in range(0,8):    #生成8个转子
        seed(i)    #加入伪随机数种子，使得每次生成的每个转子的替换是固定的
        shuffle(alphabet_list)    #随机洗牌
        rt.append("".join(alphabet_list))    #8个转子保存在列表里

    print('【转子初始化完毕】\n'    #打印出所有转子的配置
          '=========================================\n'
          '   '+alphabet+'\n'
          '=========================================\n'
          'R1:'+rt[0]+'\n'
          'R2:'+rt[1]+'\n'
          'R3:'+rt[2]+'\n'
          'R4:'+rt[3]+'\n'
          'R5:'+rt[4]+'\n'
          'R6:'+rt[5]+'\n'
          'R7:'+rt[6]+'\n'
          'R8:'+rt[7]+'\n'
          '=========================================\n')
        
    print('请选择转子（1-8）')
    invalid_entry='输入的值无效，请重新输入1-8的数字'
    ##加入用正则表达式确保输入的是数字
    ##这里输入空值会报错！
    while True:
        i1=int(input('选择放入第一个插槽的转子：'))
        if 1 <= i1 <= 8 and str(i1).isdigit():
            slot1=rt[i1-1]
            print('R'+str(i1)+':',slot1)
            break
        else:
            print(invalid_entry)

    while True:
        i2=int(input('选择放入第二个插槽的转子：'))
        if 1 <= i2 <= 8 and i2 != i1:
            slot2=rt[i2-1]
            print('R'+str(i2)+':',slot2)
            break
        else:
            print(invalid_entry)
            
    while True:
        i3=int(input('选择放入第三个插槽的转子：'))
        if 1 <= i3 <= 8 and i3 != i1 and i3 != i2:
            slot3=rt[i3-1]
            print('R'+str(i3)+':',slot3)
            break
        else:
            print(invalid_entry)

def rotate():    #转动功能
    print('Rotate rotors.')
    for i in range(0,8):
        print(i)
        list(slot1)[i]=list(slot1)[i-1]    #转子转动平移往前一位
        ##不对！
        print(''.join(slot1))
                
def scramble():    #字母替换功能，要加参数
    #用for来遍历明文plain_text，一次加密一个
    print('Input: '+self.alphabet[4])  #输入E
    exchange_1=self.rotors[0].index(self.alphabet[4])    #第一次替换，搜索E在转子#1中的位置
    print('Index in Rotor#1:',exchange_1)
    print('Which is:',self.alphabet[exchange_1])    #变成K

    exchange_2=self.rotors[5].index(self.alphabet[exchange_1])    #第二次替换
    print('Index in Rotor#2:',exchange_2)
    print('Which is:',self.alphabet[exchange_2])    #变成C

    exchange_3=self.rotors[2].index(self.alphabet[exchange_2])    #第三次替换
    print('Index in Rotor#2:',exchange_3)
    print('Which is:',self.alphabet[exchange_3])    #变成Y
    return self.alphabet[exchange_3]



def reflector():    #反射器部分（返回信号）
    pass

def enigma():    #主体部分（框架）
    pass

def lampboard():    #灯板部分（输出）
    pass
