while True:
    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x/y)
    except Exception as ex:
        print("y'ye 0 değeri verilemez.", ex)
    else:
        break    