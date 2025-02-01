# print('a.py')
global_var = 1
# print(__name__)

def f():
    pass


# print('a.py end')

if __name__ == '__main__':
    print("a in retutning")
else:
    print("a is importing")