import moviepy.editor as mp

def extract_audio(videos_file_path):
    my_clip = mp.AudioFileClip(videos_file_path)
    return my_clip


if __name__ == "__main__":
    file_path = r'./m3u8Download/testVideovideo.mp4'
    my_clip = extract_audio(file_path)
    my_clip.write_audiofile(f'01 新冠疫情让世界经济发生了什么变化.mp3')
