import os
import subprocess
import argparse

# Check if 'ffmpeg' is installed
def check_ffmpeg():
    try:
        # Run a simple command to check the ffmpeg version
        result = subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # If the command returns the code 0, then ffmpeg is installed.
        if result.returncode == 0:
            print("ffmpeg is installed.")
            print(result.stdout.split('\n')[0])
            return True
        # If the return code is not 0, either ffmpeg is not installed or it cannot be accessed
        else:
            print("ffmpeg is not installed or not working properly.")
            return False
    except Exception as e:
        print("ffmpeg is not installed or not accessible.")
        print(str(e))
        return False

# Function that takes an input file, an output path and a target FPS and convers the input file into a GIF
def convert_video_to_gif(input_file, output_file, fps=30):
    cmd = ["ffmpeg", "-i", input_file, "-filter_complex", f"[0:v] fps={fps},scale=-1:-1,split [a][b];[a] palettegen [p];[b][p] paletteuse", "-y", output_file]
    subprocess.run(cmd)
    
def main(args):
    files_to_convert = os.listdir("./input")
    accepted_extensions = ["mp4", "mov"]
    for file_name in files_to_convert:
        name = file_name.split(".")[0]
        extension = file_name.split(".")[1]
        if extension.lower() not in accepted_extensions:
            print(f"{file_name} is not supported. Make sure it is an MP4 or MOV file.")
            continue
        
        convert_video_to_gif(os.path.join(args.input_directory, file_name), os.path.join(args.output_directory, name + ".gif"), fps=args.fps)
        if args.cleanup:
            os.remove("./input/" + file_name)
    
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-directory", "-i", type=str, required=True, help="Path to the input files")
    parser.add_argument("--output-directory", "-o", type=str, required=True, help="Path to where the output files should be written")
    parser.add_argument("--cleanup", "-c", action="store_true", help="Delete input files after conversion.")
    parser.add_argument("--fps", type=int, default=30, help="Frames per second for the output GIF.")
    args = parser.parse_args()
    if check_ffmpeg():
        main(args)