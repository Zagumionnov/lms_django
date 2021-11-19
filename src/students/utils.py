
def format_list(records):
    response = ''
    for entry in records:
        response += '<br>' + str(entry)
    return response if response else '(Empty result)'
