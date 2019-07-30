'''
用Pillow操作图像
'''

from PIL import Image, ImageFilter
image = Image.open('C:/Users/asu1/Desktop/素材/girl.jpg')
# print(image.format, image.size, image.mode)

# #剪裁图片
# rect = 150, 100, 380, 350    #左上右下
# image.crop(rect).show()

# #缩略图
# size = 128, 128
# image.thumbnail(size)
# image.show()

#缩放和黏贴头像
image1 = Image.open('C:/Users/asu1/Desktop/素材/girl.jpg')
image2 = Image.open('C:/Users/asu1/Desktop/素材/girl2.jpg')
rect = 150, 100, 380, 350
girl2_head = image2.crop(rect)
width, height = girl2_head.size
image1.paste(girl2_head.resize((int(width / 1.5), int(height / 1.5))), (172, 40))

# #旋转和翻转
# image.rotate(180).show()
# image.transpose(Image.FLIP_LEFT_RIGHT).show()

#操作像素
# # for x in range(150, 380):
# #      for y in range(100, 350):
# #          image.putpixel((x, y), (128, 128, 128))
# # image.show()

#滤镜效果
image.filter(ImageFilter.EMBOSS).show()