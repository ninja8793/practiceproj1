def foo(required,*args,**kwargs):
    print('req args.......',required)
    if args:
        for i in args:
            a=i+i
        print(a)
        print('second args...',args)
        print('total arguments passed in args...',len(args))
    if kwargs:
        print('third kwrgs...',kwargs)


foo(0,1,1,1,1)
