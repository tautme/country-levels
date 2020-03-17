# Country Level ID
### Summary

Country Level IDs are short codes used to identify country polygons and other administrative areas in [Natural Earth](https://www.naturalearthdata.com/) datasets.

This repository also contains each individual shape exported as GeoJSON files.

Data licensed as public domain, code is MIT License.



### Why is it needed?

I developed this library when trying to make a map from COVID-19 datasets and realized that there is no way to refer to a piece of land in a short and unique way. 

When someone refers to `Italy`, does it include Sardinia? What about Sicily? Is it fun to parse `Korea, South`?

Country Level ID was developed to have a standard way of referring to all kind of administrative areas down to state / province / county level in all countries.



### License

The source code of this project is under MIT License.

Natural Earth's data is in public domain. You are free to use it in any way, including for personal, educational, and commercial purposes. [Terms of Use](https://www.naturalearthdata.com/about/terms-of-use/).

Everything inside `export/` folder is public domain. 



### Development

If you would like to develop or contribute, you'll need Python 3.7+ and Node with yarn.

Steps:

1. run `source prepare-virtualenv.sh`
2. run `./process_all.sh`

If you have [direnv](https://direnv.net/) installed, the virtualenv will activate/deactivate automatically upon entering/exiting this project.

