import random
import string


def get_random_name():
    letters = string.ascii_lowercase
    length = random.randint(2, 8)
    result_str = ''.join(random.choice(letters) for i in range(length))
    # print("Random string of length", length, "is:", result_str)
    return str(result_str)


def get_random_email():
    letters = string.ascii_lowercase
    length = random.randint(0, 8)
    result_str = ''.join(random.choice(letters) for i in range(length))
    result_email = ''.join(random.choice(letters) for i in range(length))
    result_tld = ''.join(random.choice(letters) for i in range(3))
    # print("Random email of length", length, "is:", result_str + '@' + result_email + '.' + result_tld)
    return str(result_str + '@' + result_email + '.' + result_tld)


def get_random_address():  # 1555 Lake Woodlands Dr
    letters = string.ascii_lowercase
    range1_3 = random.randint(2, 4)
    length = random.randint(0, 8)
    result_address = ''.join(str(random.randint(0, 9)) for i in range(4))
    result_name = ''.join(random.choice(letters) for i in range(length))
    result_street = ''.join(random.choice(letters) for i in range(range1_3))
    # print("Random email of length", length, "is:", result_address + ' ' + result_name + ' ' + result_street)
    return str(result_address + ' ' + result_name + ' ' + result_street)


def get_random_major():
    majors = []
    with open('major.txt') as fh:
        for line in fh:
            majors.append(line)
    number = random.randint(0, len(majors) - 1)
    return str(majors[number])


def create_csv(size):
    with open('temp.csv', 'a') as file:
        header = 'name,' + ' address,' + ' email,' + ' major' + '\n'
        file.write(header)
        for ii in range(size):
            name = get_random_name() + ', '
            address = get_random_address() + ', '
            email = get_random_email() + ', '
            major = get_random_major()
            print(name + address + email + major)
            data = name + address + email + major
            file.write(data)


create_csv(10000)
