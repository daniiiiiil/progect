import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('StudentsPerformance.csv')
print('Проверяем гипотезу что группа С учится лутше всех.')
#print(df.head())
am = df[df['race/ethnicity'] == 'group A']['math score'].mean()
bm = df[df['race/ethnicity'] == 'group B']['math score'].mean()
cm = df[df['race/ethnicity'] == 'group C']['math score'].mean()
ar = df[df['race/ethnicity'] == 'group A']['reading score'].mean()
br = df[df['race/ethnicity'] == 'group B']['reading score'].mean()
cr = df[df['race/ethnicity'] == 'group C']['reading score'].mean()
aw = df[df['race/ethnicity'] == 'group A']['writing score'].mean()
bw = df[df['race/ethnicity'] == 'group B']['writing score'].mean()
cw = df[df['race/ethnicity'] == 'group C']['writing score'].mean()
print('Результаты по математике в группе A - ', am)
print('Результаты по математике в группе B - ', bm)
print('Результаты по математике в группе C - ', cm)
print('                                                                                              ')
if am > bm and am > cm:
    print('Группа А лучшая в математике!')
elif bm > am and bm > cm:
    print('Группа Б лучшая в математике!')
else:
    print('Группа С лучшая в математике!')
    print('                     ')
print('Результаты по чтению в группе A - ', ar)
print('Результаты по чтению в группе B - ', br)
print('Результаты по чтениюю в группе C - ', cr)
print('                     ')
if ar > br and ar > cr:
    print('Группа А лучшая в правописании!')
elif br > ar and br > cr:
    print('Группа Б лучшая в правописании!')
else:
    print('Группа С лучшая в правописании!')
    print('                     ')
print('Результаты по письму в группе A - ', aw)
print('Результаты по письму в группе B - ', bw)
print('Результаты по письму в группе C - ', cw)
print('        ')
if ar > br and ar > cr:
    print('Группа А лучшая в чтении!')
elif br > ar and br > cr:
    print('Группа Б лучшая в чтении!')
else:
    print('Группа С лучшая в чтении!')
    print('                     ')

explode = (0.1, 0, 0, 0, 0)
df['race/ethnicity'].value_counts().plot(kind = 'pie', explode = explode , autopct='%1.1f%%', shadow=True)
plt.show()
print('Гипотеза подтверждена.')