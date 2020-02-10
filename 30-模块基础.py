# 每一个以.py作为扩展名的文件都是一个模块结
hi = 'hello world'
def pstar(n=50):
    print('*'*n)

if __name__ == '__main__':
    pstar()
    pstar(30)
# 在当前模块中调用star模块
import star
print(star.hi)
star.pstar
star.pstar(30)
