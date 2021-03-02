from services import school_service

# result = school_service.getSchools()
# print(result)

school_name = input('Enter school name ')
school_email = input('Enter email ')
school_pin = int(input('Enter pin '))
school_pwd = input('Enter password ')
school_address = input('Enter address ')

if school_service.isSchoolEmailExists(school_email=school_email) == False:
    result = school_service.insertSchool(school_name=school_name, school_email=school_email, school_pin=school_pin,
                                         school_pwd=school_pwd, school_address=school_address)
    print('School created successfully. School Id is {}'.format(result))
else:
    print('School Email already exists')


