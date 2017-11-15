# 传递元组
def get_error_details():
    return (2, 'details')


errnum, errstr = get_error_details()

# Lambda 表格
points = [
    {'x': 2, 'y': 3},
    {'x': 4, 'y': 1}
]
points.sort(key=lambda i: i['y'])
print(points)

# 列表推导
listone = [2, 3, 4]
listtwo = [2 * i for i in listone if i > 2]
print(listtwo)
