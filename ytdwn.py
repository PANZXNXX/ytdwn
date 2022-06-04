import youtube_dl
import os,sys,time
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
def run():
    os.system("clear")
    print (f"{bcolors.FAIL}██╗   ██╗████████╗██████╗ ██╗    ██╗███╗   ██╗")
    print (f"{bcolors.FAIL}╚██╗ ██╔╝╚══██╔══╝██╔══██╗██║    ██║████╗  ██║")
    print (f"{bcolors.FAIL} ╚████╔╝    ██║   ██║  ██║██║ █╗ ██║██╔██╗ ██║")
    print (f"{bcolors.ENDC}  ╚██╔╝     ██║   ██║  ██║██║███╗██║██║╚██╗██║")
    print (f"{bcolors.ENDC}   ██║      ██║   ██████╔╝╚███╔███╔╝██║ ╚████║")
    print (f"{bcolors.ENDC}   ╚═╝      ╚═╝   ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝")
    print (f"{bcolors.FAIL}        ALAT BUAT CONVERT"f"{bcolors.ENDC} VIDIO YT TO MP3")               
    print ("                 Author : Panz       ")
    print ("")
    print ("Script Ini di buat untuk Convert Vidio youtube To Mp3")
    print ("Kenapa Saya buat Script ini? Karena Script ini sangat Simpel danmudah")
    print ("Kan bisa di chrome bang? Nah Kalo di chrome itu banyak iklan ")
    print ("Gak Kayak Script yang saya Buat simpel mudah dan tanpa iklan ")
    print ("")
    video_url = input(f"{bcolors.OKGREEN}Url Youtube ==> : ")
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    print ("")
    print("DOWNLOAD SELESAI DENGAN JUDUL {}".format(filename))

if __name__=='__main__':
    run()
