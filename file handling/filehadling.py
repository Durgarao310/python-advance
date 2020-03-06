# f = open('test.txt','r')
# print(f.mode)
# f.close()
# output: r(reading mode)

# with open('test.txt','r') as f:
#     print(f.name)
#     print(f.mode)
# output: test.txt(filename)
#         r(reading mode)

# with open('test.txt','r') as f:
#     content = f.read()
#     print(content)
# # output:     1.'django.middleware.security.SecurityMiddleware',
#             # 2.'django.contrib.sessions.middleware.SessionMiddleware',
#             # 3.'django.middleware.common.CommonMiddleware',
#             # 4.'django.middleware.csrf.CsrfViewMiddleware',
#             # 5.'django.contrib.auth.middleware.AuthenticationMiddleware',
#             # 6.'django.contrib.messages.middleware.MessageMiddleware',
#             # 7.'django.middleware.clickjacking.XFrameOptionsMiddleware',
# with open('test.txt','r') as f:
#     content = f.readline()
#     print(content)

# # output: 1.'django.middleware.security.SecurityMiddleware',

# with open('test.txt','r') as f:
#     content = f.readlines()
#     print(content)
# # output: ["1.'django.middleware.security.SecurityMiddleware',\n", "2.'django.contrib.sessions.middleware.SessionMiddleware',\n", "3.'django.middleware.common.CommonMiddleware',\n", "4.'django.middleware.csrf.CsrfViewMiddleware',\n", "5.'django.contrib.auth.middleware.AuthenticationMiddleware',\n", "6.'django.contrib.messages.middleware.MessageMiddleware',\n", "7.'django.middleware.clickjacking.XFrameOptionsMiddleware',"]

# with open('test.txt','r') as f:
#     for i in f:
#         print(i,end="")
# output: 1.'django.middleware.security.SecurityMiddleware',
#         2.'django.contrib.sessions.middleware.SessionMiddleware',
#         3.'django.middleware.common.CommonMiddleware',
#         4.'django.middleware.csrf.CsrfViewMiddleware',
#         5.'django.contrib.auth.middleware.AuthenticationMiddleware',
#         6.'django.contrib.messages.middleware.MessageMiddleware',
#         7.'django.middleware.clickjacking.XFrameOptionsMiddleware'


# with open('test.txt','r') as f:
#     content = f.read(100)#it will reads 100 chars only of the file
#     print(content)

# with open('test.txt','r') as f:
#     content = f.readlines()
#     print(content[4]) 
# # output: 5.'django.contrib.auth.middleware.AuthenticationMiddleware',

# with open('test.txt','r') as f:
#     content = f.readlines()
#     print(content[0:4]) # it will returns the first to N lines  here N=4


# with open('test1.txt','w') as f:
#     f.write('sai')
#     f.seek(0)
#     f.write('b')

# with open('test.txt','r') as rf:
#     with open('test_copy1.txt','w') as wf:
#         for line in rf:
#             wf.write(line)
