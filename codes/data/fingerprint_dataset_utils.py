import os


def get_fingerprint_images_list(base_path):
    HR_images = []
    LR_images = []
    for f in os.listdir(base_path):
        vol_path = os.path.join(base_path, f, 'sd09', f)
        for person_folder in os.listdir(vol_path):
            for i in range(1, 11):
                HR_file_path = os.path.join(vol_path, person_folder,
                                            '{}_{:02d}_cropped_resized_HR.png'.format(person_folder, i))
                if os.path.exists(HR_file_path):
                    HR_images.append(HR_file_path)
                    LR_file_path = os.path.join(vol_path, person_folder,
                                                '{}_{:02d}_cropped_resized_LR.png'.format(person_folder, i))
                    LR_images.append(LR_file_path)
    return HR_images, LR_images
