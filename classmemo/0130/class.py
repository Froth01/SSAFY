
def create_user(name_in,age_in,address_in):
    user_info={}
    user_info['name']=name_in
    user_info['age']=age_in
    user_info['address']=address_in
    print(f'{name_in}님 환영합니다!')
    return user_info

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']
many_user = list(map(create_user,name,age,address))

info = dict(map(lambda user : (user['name'],user['age']), many_user))
print(info)


