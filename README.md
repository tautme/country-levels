# Country Levels
Country Levels project provides GeoJSON extracts from OpenStreetMap, for each ISO country and subdivision code (like provinces or states).

It builds on information from both OpenStreetMap and Wikidata, giving up-to-date population information.

ISO1 is referring to [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1) country codes, like `ES` for Spain.

ISO2 is referring to [ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2) country codes, like `ES-CL` for Castilla y León.

GeoJSON files are served in different quality levels, q5 refers to smallest, q7 to medium and q8 to higher quality extracts. All exported GeoJSON and JSON files are found in the "[export](export)" folder.



### [Country code list](docs/iso1_list.md)

JSONs: [iso1.json](../export/iso1.json) [iso2.json](../export/iso2.json)



### Country Level IDs

Country Level IDs are optional and included in each GeoJSON.

They simply concatenate the level + the ISO code.

For example, Spain's country level ID is: `iso1:ES`. Castilla y León's country level ID is `iso2:ES-CL`.



### License

The source code of this project is under MIT License.

The GeoJSON files are from OpenStreetMap, [© OpenStreetMap contributors](https://www.openstreetmap.org/copyright).

Population information and corrections are from Wikidata, under Public Domain [Creative Commons CC0 License](https://creativecommons.org/publicdomain/zero/1.0/).



The map screenshots in this readme [© Mapbox](https://www.mapbox.com/about/maps/) [© OpenStreetMap](https://openstreetmap.org/about/).



#### Thanks

The land polygons are from [OSM Admin Boundaries Map](https://wambachers-osm.website/boundaries/), provided by Wambachers. 



### Development

If you would like to develop or contribute, you'll need Python 3.7+ and Node with yarn.

Note: this process will start a slow and delayed download from the OSM Admin map. It will take many hours, to make sure we are not overloading the server.

Steps:

1. run `source prepare_virtualenv.sh`
2. run `./process_all.sh`

If you have [direnv](https://direnv.net/) installed, the virtualenv will activate/deactivate automatically upon entering/exiting this project.



### [Country code list](docs/iso1_list.md)

JSONs: [iso1.json](../export/iso1.json) [iso2.json](../export/iso2.json)




