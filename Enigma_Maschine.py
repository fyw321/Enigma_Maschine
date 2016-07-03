#Try to rebuild an Enigma Maschine

#==========Keyboard==========
def keyboard():    #键盘部分（输入）
    import re
    
    print('='*(len(alphabet)+3))
    raw_text=input('请输入要处理的内容（英文）\n')
    no_space=re.sub(r'\s',r'_',raw_text.strip())    #去掉文字两边的空格，把文中空格替换为下划线
    pattern=re.compile(r'[a-zA-Z0-9_.,?]')    #匹配数字、大小写字母、逗号句号、空格、问号
    formatted_text=(''.join(re.findall(pattern, no_space))).upper()    #把匹配结果联合成一个字符串，并把字母全大写
    print('='*(len(alphabet)+3)+'\n')
    return formatted_text

#==========Plugboard==========
def plugboard(input_text):    #接线板部分（两两交换字母）
    from random import seed,sample
    import re

    ##这里加入一个if判断，是输入时（第一次）还是输出时（第二次）的替换，以免重复设置
    print('='*(len(alphabet)+3))
    seed(input('请输入设置接线板的随机数种子：'))
    invalid_value='输入的值无效，请重新输入0-20的数字'
    while True:
        plugs=int(input('请选择要交换多少对字符：'))    #设置需要交换多少对字符
        if 0 <= plugs <= len(alphabet)//2:    #字母表长40
            break
        else:
            print(invalid_value)
    plugboard_setting=sample(alphabet, plugs*2)    #从字母表随机选出2倍plugs长度的字符，用一部分替换另一部分
    
    print('接线板设置：\n ',plugboard_setting)    #生成一个接线板的配置列表，前半部分作为front，后半部分作为back

    front=[]
    back=[]
    for i in range(plugs):
        front.append(plugboard_setting[i])
        back.append(plugboard_setting[i+plugs])
    temp=[]    #建立一个过度用的临时字符序列temp，实现front-->temp-->back, back-->front   
    for i in front:
        temp.append(i+'&')
    print('='*(len(alphabet)+3)+'\n')

    diverted=list(input_text)    #复制所输入的文本方便修改

    for char in diverted:    #遍历输入的文本中的每一个字符
        i=diverted.index(char)
        if char in front:    #检查是否有front中的字符
            bingo_index=front.index(char)    #找到匹配项在front中的位置
            bingo=temp[bingo_index]    #找到匹配项在temp中对应的位置
            diverted[i]=bingo    #将文本中的匹配front的字符替换为temp中的临时字符

    for char in diverted:
        i=diverted.index(char)
        if char in back:    #检查是否有back中的字符
            bingo_index=back.index(char)    #找到匹配项在back中的位置
            bingo=front[bingo_index]    #找到匹配项在front中对应的位置
            diverted[i]=bingo    #将文本中的匹配back的字符替换为front中的字符

    for char in diverted:
        i=diverted.index(char)
        if char in temp:    #检查是否有temp中的字符
            bingo_index=temp.index(char)    #找到匹配项在temp中的位置
            bingo=back[bingo_index]    #找到匹配项在back中对应的位置
            diverted[i]=bingo    #将文本中的匹配temp的字符替换为back中的字符，去掉所有临时字符


    diverted_text=''.join(diverted)    #输出转换后的文本
    return diverted_text

#==========Rotors==========
def rotors():    #转子部分（进一步替换）
    from random import seed,shuffle
    import re
    
    alphabet_list=list(alphabet)    #列表化
    rt=[]
    seed(input('请输入生成转子的随机数种子：'))    #加入伪随机数种子，使得每次生成的每个转子的替换是固定的
    for i in range(0,8):    #生成8个转子
        shuffle(alphabet_list)    #随机洗牌
        rt.append("".join(alphabet_list))    #8个转子保存在列表里
    
    print('='*(len(alphabet)+3))
    print('【转子初始化完毕】\n'+    #打印出所有转子的配置
          '='*(len(alphabet)+3)+'\n'+
          '   '+alphabet+'\n'+
          #''*(len(alphabet)+3)+'\n'+
          'R1:'+rt[0]+'\n'+
          'R2:'+rt[1]+'\n'+
          'R3:'+rt[2]+'\n'+
          'R4:'+rt[3]+'\n'+
          'R5:'+rt[4]+'\n'+
          'R6:'+rt[5]+'\n'+
          'R7:'+rt[6]+'\n'+
          'R8:'+rt[7]+'\n'+
          '='*(len(alphabet)+3)+'\n')
    
    print('='*(len(alphabet)+3))
    print('请选择转子（1-8）')
    invalid_entry='输入的值无效，请重新输入1-8的数字'
    ##加入用正则表达式确保输入的是数字
    ##这里输入空值会报错！
    while True:
        i1=int(input('选择放入第一个插槽的转子：'))
        if 1 <= i1 <= 8:
            slot1=rt[i1-1]
            print('R'+str(i1)+':'+str(slot1))
            break
        else:
            print(invalid_entry)

    while True:
        i2=int(input('选择放入第二个插槽的转子：'))
        if 1 <= i2 <= 8 and i2 != i1:
            slot2=rt[i2-1]
            print('R'+str(i2)+':'+str(slot2))
            break
        else:
            print(invalid_entry)
            
    while True:
        i3=int(input('选择放入第三个插槽的转子：'))
        if 1 <= i3 <= 8 and i3 != i1 and i3 != i2:
            slot3=rt[i3-1]
            print('R'+str(i3)+':'+str(slot3))
            break
        else:
            print(invalid_entry)
    
    print('='*(len(alphabet)+3)+'\n')
    return slot1,slot2,slot3
          
def scramble(diverted_text,rotors_setting):    #转子加密功能，参数是输入内容和转子设定
    print(rotors_setting[0])
    print(rotors_setting[1])
    print(rotors_setting[2])
    
    for char in diverted_text:    #用for来遍历diverted_text，一次加密一个
        print('输入: '+char)
        print(alphabet.index[char])
        ##这里这个有问题
        exchange_1=rotors_setting[0][alphabet.index[char]]    #使用第1个转子加密，搜索E在转子#1中的位置
        print(exchange_1)

    scrambled='scrambled'
    return scrambled_text

##每加密一个字符便转动slot1中的转子一格，slot1转一圈slot2中的转一格，slot3以此类推
'''
    print('Rotate rotors.')
    for i in range(0,8):
        print(i)
        list(slot1)[i]=list(slot1)[i-1]    #转子转动平移往前一位
        ##不对！
        print(''.join(slot1))
'''


#==========Reflector==========
def reflector():    #反射器部分（返回信号）
    pass

#==========Lampboard==========
def lampboard():    #灯板部分（输出）
    output_text = 'output text here'
    return output_text

#==========Enigma==========
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_,.?'   #标准字母表+数字+空格+少数标点

rotors_setting = rotors()    #设置转子，调用rotors()方法，返回一个列表
input_text = keyboard()    #输入内容
diverted_text = plugboard(input_text)    #设置接线板，调用plugboard()方法，返回一个经过接线板初次替换字符顺序的文本
scrambled_text = scramble(diverted_text,rotors_setting)    #调用scramble()方法，使字符进入转子进一步加密
output_text=lampboard()
print('输出的内容为：\n')
#print(output_text)
