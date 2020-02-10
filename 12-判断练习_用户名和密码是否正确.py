# getpass模块中有一个getpass方法，这个方法的输入是不会对外显示的，因此以它作为密码的设置
import getpass  # 导入模块
def main():
    username = input("username: ")
    password = getpass.getpass('passworld: ')
    if username == 'xiaohei' and password == '0':
        print('登陆成功')
    else:
        print('用户名或密码错误')

if __name__ == '__main__':
    main()

# 给用户三次输入的机会
# 此处省去导入模块的部分
def main():
    count = 0
    while count < 3:
        username = input('username: ')
        password = getpass.getpass('password: ')
        if username == 'xiaohei' and password == '666':
            print("登陆成功")
            break
        else:
            print('密码或用户名错误，请重新输入')
            count += 1
    if count == 3:
        print("冻结账户，退出程序")





if __name__ == '__main__':
    main()
