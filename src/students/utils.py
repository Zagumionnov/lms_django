
def format_list(records):
    response = ''
    for entry in records:
        link = f"<a href=/students/update/{entry.id}>UPDATE</a>"
        response += f'{link} {entry} <br>'
    return response if response else '(Empty result)'
