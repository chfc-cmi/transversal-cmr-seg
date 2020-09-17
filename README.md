# Transversal CMR Segmentation
Experiments into segmentation of transversal slices of cardiac MR images

## Initial model
Trained using fastai v1 on 138 images (90 training, 48 validation) from 6 volunteers. Classes to predict were left ventricular cavity and left ventricular myocardium.

The provided model file (see release page) `b0_transversal_5_5.pth` is the base model from
> A Deep Learning Based Cardiac Cine Segmentation Framework for Clinicians - Transfer Learning Application to 7T Markus J Ankenbrand, David Lohr, Wiebke Schlötelburg, Theresa Reiter, Tobias Wech, Laura Maria Schreiber medRxiv 2020.06.15.20131656; doi: https://doi.org/10.1101/2020.06.15.20131656

trained for 5 epochs frozen (max_lr=1e-3) and 5 epochs unfrozen (max_lr=1e-4)
