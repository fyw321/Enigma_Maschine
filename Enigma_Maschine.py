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
def set_plugboard():    #设置接线板
    from random import seed,sample

    print('='*(len(alphabet)+3))
    seed(input('请输入设置接线板的随机数种子：'))
    invalid_value='输入的值无效，请重新输入0-20的数字'

    while True:
        number=input('请选择要交换多少对字符（0-20）：')    #设置需要交换多少对字符，加入number这个中间变量来防止int()处理非数字或者空值时报错
        if number.isdigit():    #判断是否是数字
            plugs=int(number)
            if 0 <= plugs <= len(alphabet)//2:    #判断数字是否在范围内，字母表长40
                break
            else:
                print(invalid_value)
        else:
            print(invalid_value)
            
    plugboard_sample=sample(alphabet, plugs*2)    #从字母表随机选出2倍plugs长度的字符，生成一个接线板的配置列表，前半部分作为front，后半部分作为back

    front=plugboard_sample[0:plugs]    #front列表
    temp=[]    #建立一个过度用的临时字符序列temp，实现front-->temp-->back, back-->front   
    for i in front:
        temp.append(i+'&')
    back=plugboard_sample[plugs:2*plugs]    #back列表
    plugboard_setting=[front,temp,back]
    
    print('接线板设置：\n'+
          str(plugboard_setting[0])+'\n'+
          str(plugboard_setting[2]))
    print('='*(len(alphabet)+3)+'\n')

    
    return plugboard_setting

def divert(text,plugboard_setting,is_coming_in):    #接线板交换字符功能，前两个参数是输入内容和接线板设定,第三个参数判断是第一次调用（数据往里）还是第二次调用（数据往外）

    diverted=list(text)    #列表化所输入的文本方便修改
    if is_coming_in:    #如果是第一次调用（往里走），正着来
        front=plugboard_setting[0]
        temp=plugboard_setting[1]
        back=plugboard_setting[2]

    else:    #如果不是第一次调用（往外走），反着来
        front=plugboard_setting[2]
        temp=plugboard_setting[1]
        back=plugboard_setting[0]
    
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
def set_rotors():    #设置转子
    from random import seed,shuffle
    
    alphabet_list=list(alphabet)    #列表化
    rt=[]
    print('='*(len(alphabet)+3))
    seed(input('请输入生成转子的随机数种子：'))    #加入伪随机数种子，使得每次生成的每个转子的替换是固定的
    for i in range(0,8):    #生成8个转子
        shuffle(alphabet_list)    #随机洗牌
        rt.append("".join(alphabet_list))    #8个转子保存在列表里
    
    print('='*(len(alphabet)+3))
    print('【转子初始化完毕】\n'+    #打印出所有转子的配置
          '='*(len(alphabet)+3)+'\n'+
          '   '+alphabet+'\n'+
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
    while True:
        i=input('选择放入第一个插槽的转子：')    #加入i这个中间变量来防止int()处理非数字或者空值时报错
        if i.isdigit():    #判断是否是数字
            i1=int(i)
            if 1 <= i1 <= 8:    #判断数字是否在范围内
                slot1=rt[i1-1]
                break
            else:
                print(invalid_entry)
        else:
            print(invalid_entry)

    while True:
        i=input('选择放入第二个插槽的转子：')
        if i.isdigit():
            i2=int(i)
            if 1 <= i2 <= 8 and i2 != i1:
                slot2=rt[i2-1]
                break
            else:
                print(invalid_entry)
        else:
            print(invalid_entry)
            
    while True:
        i=input('选择放入第三个插槽的转子：')
        if i.isdigit():
            i3=int(i)
            if 1 <= i3 <= 8 and i3 != i1 and i3 != i2:
                slot3=rt[i3-1]
                break
            else:
                print(invalid_entry)
        else:
            print(invalid_entry)
            
    print('\n'+'转子设置：')
    print('R'+str(i1)+':'+str(slot1)+'\n'+
          'R'+str(i2)+':'+str(slot2)+'\n'+
          'R'+str(i3)+':'+str(slot3))
    print('='*(len(alphabet)+3)+'\n')
    return slot1,slot2,slot3
          
def scramble(text,rotors_setting,is_coming_in):    #转子加密功能，前两个参数是输入内容和转子设定,第三个参数判断是第一次调用（数据往里）还是第二次调用（数据往外）

    scrambled=[]
    ein=zwei=drei=0    #三个转子的偏移量
    
    if is_coming_in:    #如果是第一次调用
        for char in text:    #用for来遍历text，一次加密一个
            exchange_1=rotors_setting[0][alphabet.index(char) - ein]    #使用第1个转子加密，搜索字符在转子1中的位置，并每加密一个字符向前平移一位
                        
            exchange_2=rotors_setting[1][rotors_setting[0].index(exchange_1) - zwei]    #使用第2个转子加密
            
            exchange_3=rotors_setting[2][rotors_setting[1].index(exchange_2) - drei]    #使用第3个转子加密

            ein+=1    #转子1偏移量+1
            if ein == len(alphabet):    #当转子1转到一圈时
                ein=0    #转子1偏移量归零
                zwei+=1    #转子2偏移量+1
            if zwei == len(alphabet):    #当转子2转到一圈时
                zwei=0    #转子2偏移量归零
                drei+=1    #转子3偏移量+1
            if drei == len(alphabet):    #当转子2转到一圈时
                drei=0

            scrambled.append(exchange_3)
            
    else:    #如果不是第一次调用
        for char in text:
            exchange_4=rotors_setting[1][rotors_setting[2].index(char) - (len(alphabet) - drei)]

            exchange_5=rotors_setting[0][rotors_setting[1].index(exchange_4) - (len(alphabet) - zwei)]

            exchange_6=alphabet[rotors_setting[0].index(exchange_5) - (len(alphabet) - ein)]
           
            ein+=1    #转子1偏移量+1
            if ein == len(alphabet):    #当转子1转到一圈时
                ein=0    #转子1偏移量归零
                zwei+=1    #转子2偏移量+1
            if zwei == len(alphabet):    #当转子2转到一圈时
                zwei=0    #转子2偏移量归零
                drei+=1    #转子3偏移量+1
            if drei == len(alphabet):    #当转子2转到一圈时
                drei=0
            
            scrambled.append(exchange_6)

                
    scrambled_text=''.join(scrambled)
    
    return scrambled_text

#==========Reflector==========
def set_reflector():    #设置反射器
    from random import seed,shuffle

    print('='*(len(alphabet)+3))
    seed(input('请输入生成反射器的随机数种子：'))
    alphabet_list=list(alphabet)
    shuffle(alphabet_list)
    front=alphabet_list[0:len(alphabet)//2]
    back=alphabet_list[len(alphabet)//2:len(alphabet)]
    a=''.join(front+back)
    b=''.join(back+front)
      
    print('反射器设置：\n'+
          ' '*3+a+'\n'+
          ' '*3+b+'\n')
    print('='*(len(alphabet)+3)+'\n')
    
    return a,b

def reflect(scrambled_in,reflector_setting):    #反射器功能，把从转子进来的字符转换为另一个字符再返回转子
    a=reflector_setting[0]
    b=reflector_setting[1]
    reflected = []

    for char in scrambled_in:    #遍历scrambled_in中每一个字符
        index=a.index(char)    #在反射器序列中找到这个字符的位置
        reflected.append(b[index])    #并替换为字母表中相同位置的字符
        
    reflected_text = ''.join(reflected)
    return reflected_text
            
#==========Lampboard==========
def lampboard(diverted_out):    #灯板部分（输出）
    from tkinter import Tk

    print('='*(len(alphabet)+3))
    output_text = '输出的内容为：\n'+diverted_out
    print(output_text)

    clip = Tk()    #这一堆代码是调用tkinter来把程序输出的内容复制到剪贴板里
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(diverted_out)
    clip.destroy()
    print('输出内容已复制到剪贴板')
    print('='*(len(alphabet)+3)+'\n')
    
    return output_text

#==========Enigma==========
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_,.?'   #标准字母表+数字+空格+少数标点
while True:
    print('='*(len(alphabet)+3))
    print('请选择操作：\n'+
          '1. 设置恩尼格玛机\n'+
          '2. 输入内容\n'+
          '3. 退出程序')
    print('='*(len(alphabet)+3))
    command=input('请选择：')
    
    if command == '1':     
        plugboard_setting = set_plugboard()    #设置接线板，调用plugboard()方法，返回一个经过接线板初次替换字符顺序的文本
        rotors_setting = set_rotors()    #设置转子，调用rotors()方法，返回一个列表
        reflector_setting = set_reflector()    #设置反射器，调用reflector()方法，返回一个列表
        set_completed = 'yes'
        
    elif command == '2':
        try:
            set_completed == 'yes'
        except NameError:    #捕捉异常，通过判断set_completed变量是否存在，判断程序是否已经设置完成
            print('请先设置完成后再输入内容')
        else:
            input_text = keyboard()    #输入内容

            diverted_in = divert(input_text, plugboard_setting,1)    #调用diverte()方法，使字符进入接线板进行第一次交换
            scrambled_in = scramble(diverted_in, rotors_setting,1)    #调用scramble()方法，使字符第一次进入转子进一步加密
            reflected_text = reflect(scrambled_in, reflector_setting)    #调用reflect()功能，使字符进入反射器内部交换，并返回转子
            scrambled_out=scramble(reflected_text,rotors_setting,0)    #再次调用scramble()方法，使字符第二次进入转子进一步加密
            diverted_out=divert(scrambled_out,plugboard_setting,0)    #再次调用diverte()方法，使字符进入接线板进行第二次交换
            output_text = lampboard(diverted_out)    #调用lampboard()方法，输出结果，其实这一步完全没必要，但是为了整个程序在结构上看起来像真的Enigma机于是就加上去了

    elif command == '3':
        break
