# Country Level ID
### Summary

Country Level IDs are short codes used to identify country polygons and other administrative areas in [Natural Earth](https://www.naturalearthdata.com/) datasets.

This repository also contains each polygon exported as a GeoJSON file.

Data is licensed as public domain, code has MIT License.



### Why is it needed?

I developed this library when trying to make a map from COVID-19 datasets and realized that there is no way to refer to a piece of land reliably.

When a dataset refers to "Italy", does it include Sicily? Is it fun to parse "Korea, South"?

Country Level ID was developed to have a reliable way of referring to all kinds of administrative areas down to state / province / county levels in all countries.



### Examples

**id0:IT** refers to Italy including islands. [GeoJSON](export/geojson/id0/it.geojson)

![id0_it](docs/id0_it.png)

**id2:ITX** refers to mainland Italy. [GeoJSON](export/geojson/id2/itx.geojson)

![id2_itx](docs/id2_itx.png)

**id3:US-CA** refers to the state of California, USA. [GeoJSON](export/geojson/id3/us/ca.geojson)

![id3_us-ca](docs/id3_us-ca.png)

**id0:GG+id0:JE** refers to the Channel Islands.

![channel_islands](docs/channel_islands.png)



### Specs

Country Level IDs start with one of `id0:` `id1:` `id2:` `id3:` + a code.

id0, id1, id2's code has 2 or 3 uppercase letters (ISO codes).

id3's code is the country's id0 ISO code + a dash `-`  + 1-3 uppercase letters or numbers.

As a special case, about 1% of id3 has an underscore + number postfix, to avoid duplicates. For example

- **id3:AU-NSW_1159313299** refers to New South Wales, Australia
- **id3:AU-NSW_1159313269** refers to Lord Howe Island.

id0, id1, id2 have a tree-like hierarchy. You can see that in [export/id/id012.json](export/id/id012.json). This file also contains population estimates.

id3 means states / provinces / counties, one layer for each country. id3 jsons are split per country, you can find them in the [export/id/id3](export/id/id3) folder.

The source data for each level in the Natural Earth dataset is the following:

- id0: Admin 0 – Countries
- id1: Admin 0 - Map Units
- id2: Admin 0 - Map Subunits
- id3: Admin 1 - States, Provinces



#### Combining codes

Some areas might not be described with a simple ID. For example, Channel Islands doesn't have a matching polygon in the NE dataset. These special cases can be described using the plus `+` sign. You can combine as many IDs as needed.

For example **id0:GG+id0:JE** refers to the Channel Islands.

These combinations are not exported to this repository, you need to combine them with your own scripts. Have a look at [docs/channel_islands.geojson](docs/channel_islands.geojson) to see how you can do it.



### License

The source code of this project is under MIT License.

Natural Earth's data is in the public domain. You are free to use it in any way, including for personal, educational, and commercial purposes. Natural Earth's [Terms of Use](https://www.naturalearthdata.com/about/terms-of-use/).

Everything inside `export/` folder is in the public domain.

The map screenshots in this readme [© Mapbox](https://www.mapbox.com/about/maps/) [© OpenStreetMap](https://openstreetmap.org/about/).

### Development

If you would like to develop or contribute, you'll need Python 3.7+ and Node with yarn.

Steps:

1. run `source prepare-virtualenv.sh`
2. run `./process_all.sh`

If you have [direnv](https://direnv.net/) installed, the virtualenv will activate/deactivate automatically upon entering/exiting this project.





## Reference list

___REPLACE_TEMPLATE___



