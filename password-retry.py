ans = 'a123456'
n = 3
while n>0:
    password = input('請輸入密碼 :')
    if password == ans:
        print('登入成功')
        break
    elif password != ans:
        if n >= 2:
            print('密碼錯誤, 還有', n - 1, '次機會')
        else:
            break
    n = n - 1 
    