try:
    f = open('tongxun.txt','r')
except:
    f = open('tongxun.txt','w')
    f.write('Person;PhoneNumber\n')
finally:
    f = open('tongxun.txt','r')
    line = f.readline()
    print(line)
    if line != 'Person;PhoneNumber\n':
        f = open('tongxun.txt','w')
        f.write('Person;PhoneNumber\n')
    f.close()
    f = open('tongxun.txt','r')
    tongXunLu = {}
    for each in f:
        bruh = {each.split(';')[0]:each.split(';')[1].strip('\n')}
        tongXunLu.update(bruh)
    f.close()    
    

name = ''
class ZhiLin:
    def getName():
        global name
        name = input('请输入联系人姓名:')
    def chaXun(name):
        if name in tongXunLu:
            print(name+':',tongXunLu[name])
        else:
            print('此用户不存在')
            
    def addPerson(name):
        phone_Number = input('请输入用户联系电话:')
        linShi = {name:phone_Number}
        tongXunLu.update(linShi)
            
    def chaRu(name):
        if name in tongXunLu:
            print('您输入的姓名在通讯录已存在 --> %s : %s' % (name,tongXunLu[name]))
            ShiFou = input('是否修改用户资料(YES/NO):')
            if ShiFou == 'YES':
                ZhiLin.addPerson(name)
        else:
            ZhiLin.addPerson(name)
    
    def shanChu(name):
        if name in tongXunLu:
            ShiFou = input('是否删除用户资料(YES/NO):')
            if ShiFou == 'YES': 
                tongXunLu.pop(name)
        else:
            print('此用户不存在于通讯录')
        
               

print('|--- 欢迎进入通讯录程序  ---|')
print('|---  1 :查询联系人资料  ---|')
print('|---  2 :插入新的联系人  ---|')
print('|---  3 :删除已有联系人  ---|')
print('|---  4 :退出并保存通讯录 ---|')
while True:
    code = input('请输入相关的指令代码:')
    if code.isdigit and '4' >= code >= '1' and len(code) == 1:  
        if code == '1':
            ZhiLin.getName()
            ZhiLin.chaXun(name)
            print('')
            continue
        elif code == '2':
            ZhiLin.getName()
            ZhiLin.chaRu(name)
            print('')
            continue
        elif code == '3':
            ZhiLin.getName()
            ZhiLin.shanChu(name)
            print('')
            continue
        else:
            print('|--- 感谢使用通讯录程序 ---|')
            f = open('tongxun.txt','w')
            for each in tongXunLu:
                f.write(each+';'+tongXunLu[each]+'\n')
            f.close()    
            break
    else:
        print('指令输入错误')

