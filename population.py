from faker import Faker

myfactory = Faker('ar_EG')


print(dir(myfactory))

print(myfactory.name())