password=19880314
key=30
print("\n原密码：",password)
password=password<<key
print("\n加密后：",password)
password=password>>key
print("\n解密后：",password)
