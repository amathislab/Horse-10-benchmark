# How to participate in the Horse-10 benchmark?

More infomation and nice pictures can be found at [the horse-10 site!](http://www.mackenziemathislab.org/horse10)

1) download the data and unzip:

THe data is available from: https://huggingface.co/datasets/mwmathis/Horse-30

```
tar -xvf horse10.tar.xz
```

2) Train your model for the three splits!

The downloaded data is in DeepLabCut format with information regarding the splits stored in "/training-datasets/iteration-0/UnaugmentedDataSet_HorsesMay8". 

3) Evaluate each split. To normalize the different horse sizes, we normalize to the nose-eye distance for each horse. Here is some example [code](https://github.com/amathislab/Horse-10-benchmark/blob/master/normalize_errors.py) as well as the relevant distances are stored in this [file](https://github.com/amathislab/Horse-10-benchmark/blob/master/Horsescale.h5).


# References

For more details check out the paper: [Pretraining boosts out-of-domain robustness for pose estimation](https://openaccess.thecvf.com/content/WACV2021/html/Mathis_Pretraining_Boosts_Out-of-Domain_Robustness_for_Pose_Estimation_WACV_2021_paper.html) published in the IEEE Winter Conference on Applications of Computer Vision 2021.
