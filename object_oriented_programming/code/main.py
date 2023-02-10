import particles as prt
import os
import imageio.v2 as imageio


vol = prt.Volume(delta_p=1)
vol.start_modeling(seconds=12000, visualisation_step=600)

vol = prt.LeftOpenedVolume(delta_p=1, number_of_particles=1000)
vol.start_modeling(seconds=12000, visualisation_step=600)

vol = prt.VolumeWithCenters(delta_p=1, number_of_particles=300)
vol.start_modeling(seconds=12000, visualisation_step=600)

vol = prt.VolumeWithRandomCenters(delta_p=1, number_of_particles=300)
vol.start_modeling(seconds=12000, visualisation_step=600)

vol = prt.LeftOpenedVolumeWithRandomCenters(delta_p=1, number_of_particles=300)
vol.start_modeling(seconds=12000, visualisation_step=600)

vol = prt.UltimateVolumeWithEnergyLoss(delta_p=1, number_of_particles=300)
vol.start_modeling(seconds=12000, visualisation_step=600)


# Создание гифок из графиков
for folder in ("1_simple_volume","2_left_opened_volume","3_volume_with_centers",\
        "4_volume_with_random_centers","5_left_opened_volume_with_random_centers","6_volume_with_energy loss"):
    frames = []
    for file in os.listdir(folder):
        if file.endswith(".png"):
            frames.append(file)
    frames.sort(key=lambda str: int(str.replace(".png","").replace("dist","")))
    images = [imageio.imread(folder+"/"+frame) for frame in frames]
    for _ in range(4):
        images.append(imageio.imread(folder+"/"+frames[-1]))
    imageio.mimsave(f'{folder}.gif', images, format='GIF', duration=0.5)