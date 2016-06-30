from random import seed,shuffle
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'   #标准字母表
rotors=[]
alphabet_list=list(alphabet)    #列表化
for i in range(0,8):    #生成8个转子
    seed(i)    #加入伪随机数种子，使得每次生成的每个转子中字母表的替换是固定的
    shuffle(alphabet_list)    #随机洗牌
    rotors.append("".join(alphabet_list))    #8个转子保存在列表里

print('Rotors Initialized.\n'    #打印出所有转子的配置
      '=========================================\n'
      '   '+alphabet+'\n'
      '=========================================\n'
      'R1:'+rotors[0]+'\n'
      'R2:'+rotors[1]+'\n'
      'R3:'+rotors[2]+'\n'
      'R4:'+rotors[3]+'\n'
      'R5:'+rotors[4]+'\n'
      'R6:'+rotors[5]+'\n'
      'R7:'+rotors[6]+'\n'
      'R8:'+rotors[7]+'\n'
      '==========================================')

print('Input: '+alphabet[4])  #输入E
exchange_1=rotors[0].index(alphabet[4])    #第一次替换，搜索E在转子#1中的位置
print('Index in Rotor#1:',exchange_1)
print('Which is:',alphabet[exchange_1])    #变成K

exchange_2=rotors[5].index(alphabet[exchange_1])    #第二次替换
print('Index in Rotor#2:',exchange_2)
print('Which is:',alphabet[exchange_2])    #变成C

exchange_3=rotors[2].index(alphabet[exchange_2])    #第三次替换
print('Index in Rotor#2:',exchange_3)
print('Which is:',alphabet[exchange_3])    #变成Y
