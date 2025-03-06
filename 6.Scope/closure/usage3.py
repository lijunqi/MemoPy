"""
以一个类似棋盘游戏的例子来说明:
假设棋盘大小为50*50, 左上角为坐标系原点(0,0), 我需要一个函数, 接收2个参数,
分别为方向(direction), 步长(step), 该函数控制棋子的运动.
这里需要说明的是, 每次运动的起点都是上次运动结束的终点
"""

"""
* 在这段代码中, player实际上就是闭包go函数的一个实例对象
它一共运行了三次,
第一次是沿X轴前进了10来到[10,0],
第二次是沿Y轴前进了20来到 [10, 20],
第三次是反方向沿X轴退了10来到[0, 20]
"""
def create(pos=None):
    if pos is None:
        pos = [0,0]

    def go(direction, step):
        new_x = pos[0]+direction[0]*step
        new_y = pos[1]+direction[1]*step
        pos[0] = new_x
        pos[1] = new_y
        return pos

    return go

def main():
    player = create()
    print(player([1,0],10))
    print(player([0,1],20))
    print(player([-1,0],10))

if __name__ == "__main__":
    main()
