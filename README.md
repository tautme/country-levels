# Country Level ID
Country Level IDs are short codes used to identify country polygons and other administrative areas in [Natural Earth](https://www.naturalearthdata.com/) datasets.

This repository also contains each individual shape exported as a GeoJSON file.



## Why is it needed?

I developed this library when trying to parse COVID-19 datasets and realized that there is no way to refer to a piece of land in a short and unique way. 

When someone refers to `Italy`, does it include Sardinia? What about Sicily? Is it fun to parse `Korea, South`?

This was developed to visualize Covid-19 datasets

This was developed to have a standard way of referring to all kind of administrative areas in Covid-19 maps and datasets, but it is t can be used in all projects 

Natural Earth's data is in [public domain](https://www.naturalearthdata.com/about/terms-of-use/), you are free to use it in any way, including for personal, educational, and commercial purposes.





### Development

This project does not need to be set up locally, as the processed level JSON and shape GeoJSON files are committed in the Git the repo. 

If you would like to develop or contribute, you'll need Python 3.7+ and Node with yarn.

Steps:

1. run `source prepare-virtualenv.sh`
2. run `./process_all.sh`

If you have [direnv](https://direnv.net/) installed, the virtualenv will activate/deactivate automatically upon entering/exiting this project.

