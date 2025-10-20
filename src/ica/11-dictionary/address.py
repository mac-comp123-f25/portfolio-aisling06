betsy_info = {'Name': 'Betsy Foobar',
              'Phone': 'x8012',
              'Street': '1600 Grand Avenue',
              'City': 'Saint Paul',
              'State': 'MN',
              'Email': 'bfoobar@macalester.edu'}

tom_info = {'Name': 'Tom Riddle',
            'Phone': 'x8512',
            'Street': '1600 Grand Avenue',
            'City': 'Saint Paul',
            'State': 'MN',
            'Email': 'triddle@macalester.edu'}

address_book = [ betsy_info, tom_info,
                {'Name': 'Susan Fox',
                 'Phone': 'x6553',
                 'Street': '1600 Grand Avenue',
                 'City': 'Saint Paul',
                 'State': 'MN',
                 'Email': 'fox@macalester.edu'} ]
print(address_book)

carrie_info = {'Name': 'Carrie Bradshaw',
              'Phone': 'x112',
              'Street': 'Fifth Avenue',
              'City': 'New York',
              'State': 'New York',
              'Email': 'carrie123@gmail.com'}
charlotte_info = {'Name': 'Charlotte York',
              'Phone': 'x113',
              'Street': 'Fifth Avenue',
              'City': 'New York',
              'State': 'New York',
              'Email': 'charlotteyork@gmail.com'}
address_book = [betsy_info, tom_info, carrie_info, charlotte_info]
print(address_book)

def filter_by_city(name_city, address_book):
    result = []
    for info in address_book:
        if info['City'] == name_city:
            result.append(info)
    return result

print(filter_by_city('Saint Paul', address_book))