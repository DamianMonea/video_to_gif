import os
import subprocess
import argparse

def check_ffmpeg():
    try:
        # Run the ffmpeg command with '-version' to check if ffmpeg is installed
        result = subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # Check if the call was successful
        if result.returncode == 0:
            print("ffmpeg is installed.")
            print(result.stdout.split('\n')[0])  # Print the version line of ffmpeg output
            return True
        else:
            print("ffmpeg is not installed or not working properly.")
            return False
    except Exception as e:
        print("ffmpeg is not installed or not accessible.")
        print(str(e))
        return False


def convert_video_to_gif(input_file, output_file, fps=30):
    # cmd = ["ffmpeg", "-i", input_file, "-vf", "scale=720:1280", "-r", "30", output_file]
    cmd = ["ffmpeg", "-i", input_file, "-filter_complex", f"[0:v] fps={fps},scale=-1:-1,split [a][b];[a] palettegen [p];[b][p] paletteuse", "-y", output_file]
    subprocess.run(cmd)
    
def main(args):
    files_to_convert = os.listdir("./input")
    for file_name in files_to_convert:
        name = file_name.split(".")[0]
        convert_video_to_gif("./input/" + file_name, "./output/" + name + ".gif", fps=args.fps)
        if args.cleanup:
            os.remove("./input/" + file_name)
    
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--cleanup", "-c", action="store_true", help="Delete input files after conversion.")
    parser.add_argument("--fps", type=int, default=30, help="Frames per second for the output GIF.")
    args = parser.parse_args()
    if check_ffmpeg():
        main(args)