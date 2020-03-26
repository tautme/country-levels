# Country Levels

Country Levels are GeoJSON extracts from OpenStreetMap, based on ISO codes.

It builds on data from both OpenStreetMap and Wikidata, allowing up-to-date population information.

ISO1 is referring to [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1) country codes, for example `ES` for Spain.

<img src="docs/assets/es_resize.jpg" width="400">

ISO2 is referring to [ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2) country codes, for example `ES-CL` for Castilla y León, Spain.

<img src="docs/assets/cl_resize.jpg" width="400">

GeoJSON files are served in different quality levels, *q5* refers to smallest, *q7* to medium and *q8* to higher quality extracts. 

GeoJSON files and JSON catalogs are provided in the [export](export) folder.



## [Country code list](docs/iso1_list.md)



### Country Level IDs

Country level IDs are optional and are included with each GeoJSON. They simply concatenate the level + the ISO code with `:`

For example, Spain's country level ID is `iso1:ES`, Castilla y León's country level ID is `iso2:ES-CL`.



### License

The source code of this project is licensed under the MIT License.

The GeoJSON files are from OpenStreetMap, [© OpenStreetMap contributors](https://www.openstreetmap.org/copyright).

Population information and corrections are from [Wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page), under Public Domain [Creative Commons CC0 License](https://creativecommons.org/publicdomain/zero/1.0/).



The map screenshots in this readme [© Mapbox](https://www.mapbox.com/about/maps/) [© OpenStreetMap](https://openstreetmap.org/about/).



#### Thanks

The land polygons are from Wambacher's [OSM Admin Boundaries Map](https://wambachers-osm.website/boundaries/).



### Development

If you would like to develop or contribute, you'll need Python 3.7+ and Node with yarn.

Note: this process will start a slow and delayed download from the OSM Admin map. It will take many hours, to make sure we are not overloading the server.

Steps:

1. Get a CLI key from [OSM Admin Boundaries Map](https://wambachers-osm.website/boundaries/) and replace `__CLI__KEY__` in `country_levels_lib/wam_download.py`.

1. run `source prepare_virtualenv.sh`
2. run `./process_all.sh`

If you have [direnv](https://direnv.net/) installed, the virtualenv will activate/deactivate automatically upon entering/exiting this project.



## [Country code list](docs/iso1_list.md)
