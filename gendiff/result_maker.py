from string import Template


def transform_to_json(value):
    if value is True:
        value = 'true'
    elif value is False:
        value = 'false'
    elif value is None:
        value = 'null'
    return value


def get_string_result(items):
    diff = ''
    temp = Template('  $flag $key: $value\n')
    for item in items:
        value = transform_to_json(item[2])
        diff += temp.substitute(flag=item[0], key=item[1], value=value)
    return '{{\n{}}}'.format(diff)
