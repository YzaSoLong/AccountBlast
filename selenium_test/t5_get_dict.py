# 输入数字为 行数*10

def get_merchant_code_dic_generator():
    with open('dictionary/merchant_code_dic', 'r') as f:
        while True:
            lines = f.readlines(1000)
            if not lines:
                break
            for line in lines:
                yield line.replace("\n", "")

def get_user_name_dic_generator():
    with open('dictionary/user_name_dic', 'r') as f:
        while True:
            lines = f.readlines(1000)
            if not lines:
                break
            for line in lines:
                yield line.replace("\n", "")


def get_user_pwd_dic_generator():
    with open('dictionary/user_pwd_dic', 'r') as f:
        while True:
            lines = f.readlines(1000)
            if not lines:
                break
            for line in lines:
                yield line.replace("\n", "")

def test_next():
    print(1)

merchant_code_dic_generator = get_merchant_code_dic_generator()

user_name_dic_generator = get_user_name_dic_generator()

user_name_pwd_generator = get_user_pwd_dic_generator()

single_row_dict = {}

# for i in range(0,5):
#
#     if True:
#
#         if True:
#             try:
#                 #while True:
#                     single_row_dict['merchant_code_dic'] = next(merchant_code_dic_generator)
#                     print(single_row_dict['merchant_code_dic'])
#                     test_next()
#
#
#             except StopIteration:
#                 print("no merchant_code data")
t1={'1':1,'2':2,'3':3}
t2=[]
t2.append(t1)
t2.append(t1)
t3={}
t3[1]=t1
t3[2]=t1
print(t3)

# try:
#     while True:
#         single_row_dict['user_name_dic'] = next(user_name_dic_generator)
#
# except StopIteration:
#     print("no user_name data")
#
# try:
#     while True:
#         single_row_dict['user_pwd_dic'] = next(user_name_pwd_generator)
# except StopIteration:
#     print("no user_pwd data")
#
# print(single_row_dict)


