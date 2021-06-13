# ch08lab3.py
# 실습문제 3

zoo = ['곰','강아지','고양이','사자','호랑이','여우','늑대','원숭이',
       '뱀','코끼리']

like = []
hate = []

for one in zoo:
    usr = input(f'{one} 좋아하세요? ')

    if usr == '네':
        like.append(one)
    else:
        hate.append(one)

print('좋아하는 동물들:', like)
print('싫어하는 동물들:', hate)


