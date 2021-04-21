# How to participate in the Horse-10 benchmark?

1) download the data and unzip:
'''
wget http://deeplabcut.rowland.harvard.edu/datasets/horse10.tar.gz
tar -xvf horse10.tar.gz
'''

2) Train your model for the three splits!

The downloaded data is in DeepLabCut format with information regarding the splits stored in "/training-datasets/iteration-0/UnaugmentedDataSet_HorsesMay8". We also provide COCO format... TBD!

3) Evaluate each split on ??

--> put normalizing code

More infomation and nice pictures can be found at [the horse-10 site!](http://www.mackenziemathislab.org/horse10)

# References

For more details check out the paper: [Pretraining boosts out-of-domain robustness for pose estimation](https://openaccess.thecvf.com/content/WACV2021/html/Mathis_Pretraining_Boosts_Out-of-Domain_Robustness_for_Pose_Estimation_WACV_2021_paper.html) published in the IEEE Winter Conference on Applications of Computer Vision 2021.
