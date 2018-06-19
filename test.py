# Code Walkthrough Lec 2

x = 1
y = 2
z = x + y
print z


# 1. when executing, python first compile the source code by calling the `compile` function:
c = compile('test.py', 'test.py', 'exec')
bytestring = c.co_code  #output: 'e\x00\x00j\x01\x00\x01d\x00\x00S'

#Bash
# $ python2.7 -m dis test.py

# 2. then, when code is running, the following happens
''' Output


  1           0 LOAD_CONST               0 (1)     # Pushing object 1 onto the value stack
              3 STORE_NAME               0 (x)     # Pop value 1 off the stack, and puts it into a spot in memory associated with the name

  2           6 LOAD_CONST               1 (2)     # same
              9 STORE_NAME               1 (y)

  3          12 LOAD_NAME                0 (x)     # Load whatever 'x' contains, grab its value and push it onto the stack
             15 LOAD_NAME                1 (y)     # Load whatever 'y' contains, grab its value and push it onto the stack
             18 BINARY_ADD                         # Find the top 2 on the stack, pops them and put the added value back on stack
             19 STORE_NAME               2 (z)

  4          22 LOAD_NAME                2 (z)
             25 PRINT_ITEM
             26 PRINT_NEWLINE

 42          27 LOAD_CONST               2 (None)
             30 RETURN_VALUE
'''



# 3. ceval.c里面是如何实现上面这些操作的？
'''
1.
        case LOAD_CONST:
            x = GETITEM(consts, oparg);
            Py_INCREF(x);
            PUSH(x);
            goto fast_next_opcode;
'''
