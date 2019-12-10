"""
This module has a function called "resize". See the description of the "resize" function about use.
"""
import cv2
import os


def resize(image_path, output_width="", output_height="", output_path=""):
    """
        PARAMETERS or ARGUMENTS
            -- 'image_path'   -> (required) Input image path. This value can be absolute path or relative path.
            -- 'output_width' -> (optional) Intended width of resized image.
            -- 'output_height'-> (optional) Intended height of resized image.
            -- 'output_path'  -> (optional) Directory of new resized image. New image send to this directory.

        WARNING
            -- Also at least one of the 'output_width' or 'output_height' data must be entered. If only one is entered,
            the other will be changed at the same rate.
            -- The 'Output Path' value can be either the absolute file path or the directory path or empty. If left empty,
            output to the same directory with Input Image.
    """

    if output_height == output_width == "":
        print("At least one of the 'Output Width' or 'Output Height' values must be entered!")
    elif output_width is not "" and not output_width.isnumeric():
        print("Output Width must be numeric")
    elif output_height is not "" and not output_height.isnumeric():
        print("Output Height must be numeric")
    else:
        image_path = os.path.abspath(image_path)
        img = cv2.imread(image_path)

        input_height, input_width = img.shape[:2]
        print("width: " + str(input_width) + " x height: " + str(input_height))

        output_width = int(output_width)

        if output_height is "":
            output_height = round(output_width / input_width * input_height)
        else:
            output_height = int(output_height)

        if output_path is "":
            output_path_splitext = os.path.splitext(image_path)
            output_path = output_path_splitext[0] + str(output_width) + "*" + str(output_height) + output_path_splitext[1]
        elif os.path.isdir(output_path):
            output_path = output_path + str(output_width) + "*" + str(output_height) + os.path.basename(image_path)

        resized_image = cv2.resize(img, (output_width, output_height))
        cv2.imwrite(output_path, resized_image)


if __name__ == '__main__':
    while True:
        print("""
            -- 4 different inputs will be asked in the order below.
            -- 'Input Image Path' is required. This value can be absolute path or relative path.
            -- Also at least one of the 'Output Width' or 'Output Height' data must be entered. If only one is entered,
            the other will be changed at the same rate.
            -- The 'Output Path' value can be either the absolute file path or the directory path or empty. If left empty,
            output to the same directory with Input Image.
        """)
        input_image_path = input("Input image path(required): ")
        input_output_width = input("Output Width(optional): ")
        input_output_height = input("Output Height(optional): ")
        input_output_path = input("Output Path(optional): ")

        resize(input_image_path, input_output_width, input_output_height, input_output_path)
