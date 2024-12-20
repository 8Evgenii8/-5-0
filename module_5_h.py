import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

class Video:
    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password ):
        for user in self.users:
            if user.nickname == nickname and user.password == password:
                self.current_user = user
                print('вошел в систему ', user)
                return


    def register(self,nickname, password, age):

        if nickname in self.users:
            print('ok')
        if nickname == nickname:
            print(f'Пользователь {nickname} уже существует')
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        if self.current_user == True:
            print('log_out')
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if any(v.title == video.title for v in self.videos):
                continue
            self.videos.append(video)

    def get_videos(self, vord):
        vord_lover = vord.lower()
        rizault = []
        for video in self.videos:
            if vord_lover in video.title.lower():
                rizault.append(video.title)
        return rizault


    def watch_video(self, title):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                print(f"Начинается воспроизведение: {title}")
                for secend in range(video.time_now +1, video.duration +1):
                    print(secend,end=" ", flush=True)
                    time.sleep(1)
                print('конец видио.')
                video.time_now = 0
                return
        print('видио не найдено.')

ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user.nickname)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

        
