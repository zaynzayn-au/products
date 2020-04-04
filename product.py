import os # operating system

#读取文件
products = []
if os.path.isfile('products.csv'):#检查文件是否存在
	print('已找到文件')
	with open('products.csv','r', encoding = 'utf-8') as f:
		for line in f:
			if '名字,价格' in line:
				continue #继续loop
			name, price = line.strip().split(',')
			products.append([name,price])
	print(products)


else:
	print('文件不存在')

with open('products.csv','r', encoding = 'utf-8') as f:
	for line in f:
		if '名字,价格' in line:
			continue #继续loop
		name, price = line.strip().split(',')
		products.append([name,price])
print(products)

#使用者输入商品名字和价格
while True:
	name = input('请输入商品名称：')
	if name == 'q':
		break
	price = input('请输入商品价格：')

	products.append([name , price])
print(products)

#印出购买记录
for p in products:
	print(p[0],'的价格是', p[1])

#with是python独有功能，自动close已经打开的文档
with open('products.csv','w', encoding = 'utf-8') as f:
	f.write('名字,价格\n')#加入excel title 乱码要用excel data 导入
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')

