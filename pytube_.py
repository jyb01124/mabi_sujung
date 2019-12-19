from pytube import YouTube

a = [
    "https://www.youtube.com/watch?v=dZ4vw6v3LcA&list=PLlMkM4tgfjnKsCWav-Z2F-MMFRx-2gMGG&t=0s&index=2",
    "https://www.youtube.com/watch?v=xgoO54qN4lY&list=PLlMkM4tgfjnKsCWav-Z2F-MMFRx-2gMGG&t=0s&index=3",
    "https://www.youtube.com/watch?v=xvDAURQVDhk&list=PLlMkM4tgfjnKsCWav-Z2F-MMFRx-2gMGG&t=5s&index=4",
    "https://www.youtube.com/watch?v=Vd-gmo-qO5E&list=PLlMkM4tgfjnKsCWav-Z2F-MMFRx-2gMGG&t=0s&index=5",
    "https://www.youtube.com/watch?v=yOBKtGU6CG0&list=PLlMkM4tgfjnKsCWav-Z2F-MMFRx-2gMGG&t=0s&index=6",
    "https://www.youtube.com/watch?v=MQ-3QScrFSI&list=PLlMkM4tgfjnKsCWav-Z2F-MMFRx-2gMGG&t=0s&index=7",
    "https://www.youtube.com/watch?v=VYOq-He90bE&list=PLlMkM4tgfjnKsCWav-Z2F-MMFRx-2gMGG&t=0s&index=8",
    "https://www.youtube.com/watch?v=6KSf-j4LL-c&list=PLlMkM4tgfjnKsCWav-Z2F-MMFRx-2gMGG&t=0s&index=9",
    "https://www.youtube.com/watch?v=ZCumo_6qTsU&list=PLlMkM4tgfjnKsCWav-Z2F-MMFRx-2gMGG&t=0s&index=10",
    "https://www.youtube.com/watch?v=B-CZv9WD5eM&list=PLlMkM4tgfjnKsCWav-Z2F-MMFRx-2gMGG&t=0s&index=11",
    "https://www.youtube.com/watch?v=w9GwqPx7LW8&list=PLlMkM4tgfjnKsCWav-Z2F-MMFRx-2gMGG&t=0s&index=12",
    "https://www.youtube.com/watch?v=Fcmgl8ow2Uc&list=PLlMkM4tgfjnKsCWav-Z2F-MMFRx-2gMGG&t=0s&index=13",
    "https://www.youtube.com/watch?v=MF_Wllw9VKk&list=PLlMkM4tgfjnKsCWav-Z2F-MMFRx-2gMGG&t=0s&index=14",
    "https://www.youtube.com/watch?v=S1Y9eys2bdg&list=PLlMkM4tgfjnKsCWav-Z2F-MMFRx-2gMGG&t=0s&index=15",
    "https://www.youtube.com/watch?v=Fbf9YUyDFww&list=PLlMkM4tgfjnKsCWav-Z2F-MMFRx-2gMGG&t=0s&index=16",
    "https://www.youtube.com/watch?v=ByB49iDMiZE&list=PLlMkM4tgfjnKsCWav-Z2F-MMFRx-2gMGG&t=0s&index=17",
    "https://www.youtube.com/watch?v=TdA0APWRCx0&list=PLlMkM4tgfjnKsCWav-Z2F-MMFRx-2gMGG&t=0s&index=18",
    "https://www.youtube.com/watch?v=SJQEWgkvBvo&list=PLlMkM4tgfjnKsCWav-Z2F-MMFRx-2gMGG&t=0s&index=19",
    "https://www.youtube.com/watch?v=tqrcjHuNdmQ&list=PLlMkM4tgfjnKsCWav-Z2F-MMFRx-2gMGG&t=0s&index=20",
    "https://www.youtube.com/watch?v=M8RfOCYIL8k&list=PLlMkM4tgfjnKsCWav-Z2F-MMFRx-2gMGG&t=0s&index=21"
]

for i in a:
    yt = YouTube(i)

    print(yt.title)
    yt.streams.first().download()