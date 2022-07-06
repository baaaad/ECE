# Explicit Caption Editing (ECE) Datasets
The ECE datasets include the **COCO-EE** and **Flickr30K-EE**, which are prposed for the ECE task investigated in Explicit Image Caption Editing accpeted to ECCV 2022. Refer to our full paper for detailed intructions and analysis.
![Example](https://github.com/baaaad/ECE-dataset/blob/main/images/image_1.png)

## Overview  
The ECE task is defined as follows. Given an **image** and a **reference caption (Ref-Cap)**, ECE models aim to explicitly predict a sequence of edit operations (e.g., KEEP/DELETE/ADD) on the Ref-Cap, which can translate the Ref-Cap close to the **ground-truth caption (GT-Cap)**. Typically, Ref-Cap is lightly misaligned with the image. 

Specifically, the COCO-EE was built based on dataset [MSCOCO](https://cocodataset.org/), the Flikr30K-EE was built based on the dataset [SNLI-VE](https://github.com/necla-ml/SNLI-VE) and [Flickr30K](http://shannon.cs.illinois.edu/DenotationGraph).

Each ECE instance contains three main information:
- `image_id`, the original image ID of the given image in the MSCOCO or Flikr30K-EE.
- `Ref-Cap`, the reference caption which needs to be edited.
- `GT-Cap`, the ground-truth caption of the given image and also the editing target.

### Examples from COCO-EE and Flickr30K-EE 
