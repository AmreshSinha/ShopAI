import os
import sys
from google.cloud import vision
import io

def extract_captions(image_path):
    client = vision.ImageAnnotatorClient()

    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    reponse = client.label_detection(image=image)
    labels = reponse.label_annotations

    captions = [label.description for label in labels]

    return captions

def main(folder_path, google_credentials):
    # Process each image in the folder
    with open ("./captions.txt", "w") as file:
        for filename in os.listdir(folder_path):
            if filename.endswith(('.jpg', '.jpeg', '.png')):
                image_path = os.path.join(folder_path, filename)
                
                # Describe the image
                # description = describe_image(image_path, google_credentials, openai_api_key)
                captions = extract_captions(image_path)

                # Print the description
                print(f'Image: {filename}')
                print('Description:')
                print(captions)
                print('---------------------')
                for caption in captions:
                    file.write(caption + "\n")


if __name__ == "__main__":
    # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./backend/gcpconfig.json"
    if len(sys.argv) != 4:
        print("Usage: python generate.py <folder_path> <google_credentials>")
    else:
        main(sys.argv[1], sys.argv[2])