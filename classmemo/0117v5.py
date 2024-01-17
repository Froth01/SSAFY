def create_user(name_in,age_in,address_in):
    user_info={}
    user_info['name']=name_in
    user_info['age']=age_in
    user_info['address']=address_in
    print(f'{name_in}님 환영합니다!')
    return user_info

def decrease_book(number):
    global number_of_book
    number_of_book -= number
    print(f'남은 책의 수 : {number_of_book}')

def rental_book(info):
    number = info[1]//10
    decrease_book(number)
    print(f'{info[0]}님이 {number}권의 책을 대여하였습니다.')

number_of_book = 100
name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']
many_user = list(map(create_user,name,age,address))
                 
info = dict(map(lambda user : (user['name'],user['age']), many_user))
list(map(rental_book,tuple(info.items())))



