import os.path
import glob
import ntpath

video_paths = (glob.glob("/home/durgesh/PycharmProjects/video_to_frame_script/videos_input/*.avi"))


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

j=0
for i in video_paths:
    name_of_video = path_leaf(i)

    name_of_folder= name_of_video.split('.')
    os.system("mkdir /home/durgesh/PycharmProjects/video_to_frame_script/script_output/%s" %(name_of_folder[0]))
    os.system("ffmpeg -i %s -vf fps=1 %s%s/thumb%%04d.jpg -hide_banner" % (video_paths[j], "/home/durgesh/PycharmProjects/video_to_frame_script/script_output/", name_of_folder[0]))
    j=j+1

