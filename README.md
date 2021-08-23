# Subtitle Automation

Get all videos from a directory and subtitle them.

## Parameters

```
Usage: subtitle-automation.py [OPTIONS]

Options:
  --directory TEXT            The directory where there are the video files   
                              and the srt files  [required]
  --video-format TEXT         The video format that you want to the automation
                              find all videos, default: mp4
  --output-format TEXT        The format that you want automation to output, default: mp4   
  --output-sufix TEXT         The output sufix that you want on output, default: -subtitled        
  --subtitle-sufix TEXT       The sufix of the subtitle file, default: srt
  --remove-file [true|false]  Remove file after subtitled, the old video and  
                              the subtitle file, default: false
  --help                      Show this message and exit.
```

## Installation

### Linux

**Install:**
```shell
pip install -r requirements.txt
apt update
apt install -y ffmpeg
```

**Make symbolic link and add interpretor in the first line:**
> Before execute the command below, replace `/local/to/subtitle-automation.py` with the path to your `subtitle-automation.py`
```shell
sed -i '1i #!/usr/bin/python3' subtitle-automation.py
ln -sv /local/to/subtitle-automation.py /usr/local/bin/subtitle-automation 
chmod +x subtitle-automation.py
```

## Run command
```
subtitle-automation --help
```