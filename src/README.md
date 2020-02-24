# Smart-Img-Miner
-

#### What is this document? 
A service for quickly (and intelligently) sourcing labeled data for supervised ML projects.


#### The Basic Idea

1. Set up data labels (lion, sealion, lionfish; we're detecting 'variations' of lions!)
2. Get an image from a img-search provider (lion.jpg from GCP etc.)
3. Label the img and upload it automatically to a given storage (e.g. S3, or GCP bucket)
4. After n-mined images, train a baseline model to estimate "low"-quality data (as low prob of belonging to any class). Indicate these and serve them for inspection.
5. Repeat at given interval

<b>Result:</b> Intelligently sourced and labeled img-data.

-
## Contents
-

- Getting Started 
- Examples
- Storage & Customization
- Model Tuning & Customization

#### Getting Started

-
#### Examples

-
#### Storage & Customization

-
#### Baseline Model