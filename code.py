# видео
video_1_title = "Concrete Candle Holder How To Make"
video_1_link = "Z_8Ss94fgZc"
video_2_title = "How To Make a Concrete Fire Bowl"
video_2_link = "uSSp3X07Vls"
video_3_title = "Diy LED Desk Lamp With Concrete Base"
video_3_link = "a5yiMhJaGCo"
# теги
tags = "concrete, table ,wood, furniture, accessorizes, metal"
# плейлисты
playlist_1_title = "Работа по дереву"
playlist_2_title = "Литье"
playlist_3_title = "Оборудование мастерской"    

print('Приложение в разработке.\nВведите ”videos” чтобы посмотреть список видео.\nВведите “tags” чтобы посмотреть список тегов.\nВведите “playlists” чтобы посмотреть список тегов.\nВведите “about” чтобы получить информацию.')
razd = str(input())
if razd == 'videos':
    print('''У нас есть 3 видео:
    Concrete Candle Holder How To Make: youtu.be/Z_8Ss94fgZc
    How To Make a Concrete Fire Bowl: youtu.be/uSSp3X07Vls
    Diy LED Desk Lamp With Concrete Base: youtu.be/a5yiMhJaGCo''')
elif razd == 'tags':
    print('У нас есть 6 тегов: concrete, table ,wood, furniture, accessorizes, metal')
elif razd == 'playlists':
    print('У нас есть 3 плейлиста: Работа по дереву, Литье, Оборудование мастерской')
 