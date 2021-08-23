from subprocess import run
from glob import glob
import click
from os import remove

@click.command()
@click.option('--directory', required=True, help="The directory where there are the video files and the srt files")
@click.option('--video-format', default="mp4" ,required=False, help="The video format that you want to the automation find all videos")
@click.option('--output-format', default="mp4" ,required=False, help="The format that you want automation to output")
@click.option('--output-sufix', default="-subtitled" ,required=False, help="The output sufix that you want on output")
@click.option('--subtitle-sufix', default="srt" ,required=False, help="The sufix of the subtitle file")
@click.option('--remove-file',  type=click.Choice(["true", "false"]), default="false", required=False, help="Remove file after subtitled, the old video and the subtitle file")
def main(directory,video_format, output_format, output_sufix, subtitle_sufix ,remove_file):
    videos = glob(f"{directory}/*.{video_format}")
    subtitles = glob(f"{directory}/*.{subtitle_sufix}")
    for file in videos:
        filename = file.split('.')[0]
        if f"{filename}.{subtitle_sufix}" in subtitles:
            print(run(f"ffmpeg -y -i '{file}' -vf subtitles='{filename}.{subtitle_sufix}' '{filename+output_sufix}.{output_format}'", shell=True))
            if remove_file == "true":
                print("Removing files...")
                remove(file)
                remove(f"{filename}.{subtitle_sufix}")
        else:
            print(f"The video {file} don't have subtitle, put the subtitle with same name as the video file.")

if __name__ == '__main__':
    main()