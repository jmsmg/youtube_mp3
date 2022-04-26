from pytube import YouTube

while True:
    url = input('추출할 URL을 입력하세요. ')
    #유튜브 전용 인스턴스 생성
    yt = YouTube(url)

    print(yt.streams.filter(only_audio=True).all())

    # 특정영상 다운로드
    yt.streams.filter(only_audio=True).first().download()

    print('추출 완료')