#Try to rebuild an Enigma Maschine

#==========Keyboard==========
def keyboard():    #键盘部分（输入）
    import re
    
    input_text=input('请输入要加密的内容（英文）')
    no_space=re.sub(r'\s',r'_',input_text.strip())    #去掉文字两边的空格，把文中空格替换为下划线
    pattern=re.compile(r'[a-zA-Z0-9_.,?]')    #匹配数字、大小写字母、逗号句号、空格、问号
    formatted_text=(''.join(re.findall(pattern, no_space))).upper()    #把匹配结果联合成一个字符串，并把字母全大写
    print('=========================================\n')
    return formatted_text

#==========Plugboard==========
def plugboard(input_text):    #接线板部分（两两交换字母）
    print('【请设置接线板】')
    ##加入一个输入功能来设置字符交换
    print('=========================================\n')
    diverted_text='test'    #输出一个替换过的内容
    ##正则表达式来交换字母，输入交换一次，输出交换一次
    return diverted_text

#==========Rotors==========
def rotors():    #转子部分（进一步替换）
    from random import seed,shuffle
    import re
    
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_,.?'   #标准字母表+数字+空格+少数标点
    alphabet_list=list(alphabet)    #列表化
    rt=[]

    for i in range(0,8):    #生成8个转子
        seed(i)    #加入伪随机数种子，使得每次生成的每个转子的替换是固定的
        shuffle(alphabet_list)    #随机洗牌
        rt.append("".join(alphabet_list))    #8个转子保存在列表里

    print('【转子初始化完毕】\n'+    #打印出所有转子的配置
          '='*(len(alphabet)+3)+'\n'+
          '   '+alphabet+'\n'+
          '='*(len(alphabet)+3)+'\n'+
          'R1:'+rt[0]+'\n'+
          'R2:'+rt[1]+'\n'+
          'R3:'+rt[2]+'\n'+
          'R4:'+rt[3]+'\n'+
          'R5:'+rt[4]+'\n'+
          'R6:'+rt[5]+'\n'+
          'R7:'+rt[6]+'\n'+
          'R8:'+rt[7]+'\n'+
          '='*(len(alphabet)+3)+'\n')
        
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
            
    return slot1,slot2,slot3

def rotate(slot_number):    #转动转子功能
    print('Rotate rotors.')
    for i in range(0,8):
        print(i)
        list(slot1)[i]=list(slot1)[i-1]    #转子转动平移往前一位
        ##不对！
        print(''.join(slot1))
    ##也许这一部分应该加入到scramble()里
                
def scramble(input_text,set_rotors):    #字母替换功能，参数是输入内容和转子设定
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

    return scrambled_text

#==========Reflector==========
def reflector():    #反射器部分（返回信号）
    pass

#==========Lampboard==========
def lampboard():    #灯板部分（输出）
    output_txt = 'output text here'
    return output_text

#==========Enigma==========
set_rotors = rotors()    #设置转子，调用rotors()方法，返回一个列表
input_text = keyboard()    #输入内容
set_plugboard = plugboard(input_text)    #设置接线板，调用plugboard()方法，返回一个？
