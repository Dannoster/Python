from PIL import Image
#Read the two images
for type in ("avg", "disp", "count"):
    for D_type in ("D_xx", "D_yy", "D_zz"):
        image1 = Image.open(f'/Users/daniil/Downloads/{type}_D_heatmaps/{type}_{D_type}_positive_B_z_heatmap.png')
        image2 = Image.open(f'/Users/daniil/Downloads/{type}_D_heatmaps/{type}_{D_type}_negative_B_z_heatmap.png')
        #resize, first image
        # image1 = image1.resize((426, 240))
        image1_size = image1.size
        image2_size = image2.size
        new_image = Image.new('RGB',(2*image1_size[0], image1_size[1]), (250,250,250))
        new_image.paste(image1,(0,0))
        new_image.paste(image2,(image1_size[0],0))
        new_image.save(f"/Users/daniil/Downloads/{type}_D_heatmaps/merged_{type}_{D_type}_neg_pos_B_z_heatmap.png","PNG")
        # new_image.show()
    for i in range(2):
        if i == 0:
            first_img = f'/Users/daniil/Downloads/{type}_D_heatmaps/merged_{type}_D_xx_neg_pos_B_z_heatmap.png'
            second_img = f'/Users/daniil/Downloads/{type}_D_heatmaps/merged_{type}_D_yy_neg_pos_B_z_heatmap.png'
        else:
            first_img = f"/Users/daniil/Downloads/{type}_D_heatmaps/final_0.png"
            second_img = f'/Users/daniil/Downloads/{type}_D_heatmaps/merged_{type}_D_zz_neg_pos_B_z_heatmap.png'
        image1 = Image.open(first_img)
        image2 = Image.open(second_img)
        #resize, first image
        # image1 = image1.resize((426, 240))
        image1_size = image1.size
        image2_size = image2.size
        new_image = Image.new('RGB',(image1_size[0], int(2*(4-i)/4 * image1_size[1])), (250,250,250))
        new_image.paste(image1,(0,0))
        new_image.paste(image2,(0,image1_size[1]))
        new_image.save(f"/Users/daniil/Downloads/{type}_D_heatmaps/final_{i}.png","PNG")