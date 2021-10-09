import os
import glob
import imageio


def create_gif(match_string, duration=0.1, output_filename="movie.gif"):
    """
    Can be used to create a GIF file from images.

    Parameters
    ==========
    match_string : str 
        For example - 'image.*.jpg'.
    duration : float, optional
    output_filename : str, optional
    """
    images = []
    
    for image in glob.glob(match_string):
        images.append(image)

    with imageio.get_writer(output_filename, mode="I", duration=0.1) as writer:
        for image in images:
            writer.append_data(imageio.imread(image))
