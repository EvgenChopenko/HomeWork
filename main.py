import Validator.Validator

conf = Validator.Validator.Validator.get_instance('email')
print(conf.validate('evg!chopepko@mail.com'),'False')
print(conf.validate('evg-chopepko@mail.com'),'true')
print(conf.validate('evg+chopepko@mail.com'),'false')
print(conf.validate('evg:chopepko@mail.com'),'false')
print(conf.validate('evg.chopepko@mail.com'),'true')
print(conf.validate('info@itmo-it.org'),'TRUE')
print(conf.validate('unknown'),'FALSE')


conf = Validator.Validator.Validator.get_instance('datetime')
print(conf.validate('2017-09-01'))
print(conf.validate('2017-09-1'))
print(conf.validate('2017-9-1'))
print(conf.validate('2017-09-01 12:00'))
print(conf.validate('2017-09-01 12:00:00'))
print(conf.validate('1.9.2017'))
print(conf.validate('1.09.2017'))
print(conf.validate('01.09.2017'))
print(conf.validate('1.9.2017 12:00'))
print(conf.validate('1.9.2017 12:00:00'))
print(conf.validate('1/9/2017'))
print(conf.validate('1/09/2017'))
print(conf.validate('01/09/2017'))
print(conf.validate('1/9/2017 12:00'))
print(conf.validate('1/9/2017 12:00:00'))
