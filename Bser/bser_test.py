from bser_client import BserAPIClient

my_token = 'iE0bUkwlG53g4tXG4lszR2P2Q7kgr4Jn7rpKnGWX'

api_client = BserAPIClient(api_key=my_token, version='v1')

characters = api_client.fetch_meta_data(meta_type='Character')

# for character in characters:
#     print(character.get('굄우지헌'))

user_number = api_client.get_user_number_by_nickname(nickname='굄우지헌')
# user_info = api_client.get_user_games('1595274')
print(user_number)
# print(user_info)
temp = api_client.fetch_user_games(user_number)
print(temp)