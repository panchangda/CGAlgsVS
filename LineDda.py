"""
1、已知直线的两端点坐标：(x1，y1)，(x2，y2)　　
2、已知画线的颜色：color　　
3、计算两个方向的变化量：dx=x2－x1 dy=y2－y1　　
4、求出两个方向最大变化量的绝对值：steps=max(|dx|，|dy|)　　
5、计算两个方向的增量(考虑了生成方向)：xin=dx/steps yin=dy/steps　　
6、设置初始象素坐标：x=x1,y=y1　　
7、用循环实现直线的绘制： 
"""

# 四舍五入函数
def ROUND(a):
    if a >= 0:
        return int(a + 0.5)
    else:
        # 由于 int(-1~-1.9999999) = -1
        # 负数 round(-1.5) = -1
        return int(a-0.5)

# DDA 算法实现
def generatePoints(x1, y1, x2, y2):
    pointlist = []

    #|k|<?>1
    if(abs(x2-x1) > abs(y2-y1)):
        steps = abs(x2-x1)
    else:
        steps = abs(y2-y1)

    increx = (x2-x1)/steps
    increy = (y2-y1)/steps

    x = x1
    y = y1

    # range(steps+1)
    for i in range(ROUND(steps)+1):
        pointlist.append([ROUND(x), ROUND(y)])
        x += increx
        y += increy

    return pointlist
