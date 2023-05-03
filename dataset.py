import praw

# utwórz obiekt praw, podając swoje dane logowania
reddit = praw.Reddit(client_id='EuotFvMTAV1Sdn8pvS-yog', client_secret='v6qKmbKFIzlQd-amcpYej4B7sWvE6Q',
                     username='D__', password='', user_agent='simple sentiment analysis')

# pobierz nazwę użytkownika, którego posty chcesz pobrać
uzytkownik = input("Podaj nazwę użytkownika, którego posty chcesz pobrać: ")

# pobierz 10 najnowszych postów danego użytkownika
for post in reddit.redditor(uzytkownik).comments.top(time_filter='all'):
    # print(post.title)
    print(f'{post.body}\n-------------\n')
