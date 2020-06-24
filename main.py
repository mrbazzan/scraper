
from getRank import get_rank
from theScraper import eachPageLink
from review import get_review


the_input = input('Enter Profile URL \n>')
user_review = get_review(the_input)
print(f'User has {user_review} reviews')

print('...')

stored = set()
total_review_list = []

the_link = '/s/Melbourne--Victoria--Australia/homes'  # Area to get data to be compared against
for i in range(15):
    # print(the_link)
    # print(i)
    each_detail, the_link = eachPageLink(the_link)
    for value in each_detail:
        stored.add(value)

print('...')
for value in stored:
    total_review_list.append(get_review(value))


print(f'Top {get_rank(user_review, total_review_list)}%  of melbourne-based users')

# import sys
# user_review = sys.argv[1]
# print(f'User has {get_review(user_review)} reviews')
