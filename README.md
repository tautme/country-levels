# Country Level ID
### Summary

Country Level IDs are short codes used to identify country polygons and other administrative areas in [Natural Earth](https://www.naturalearthdata.com/) datasets.

This repository also contains each individual shape exported as GeoJSON files.

Data licensed as public domain, code has MIT License.



### Why is it needed?

I developed this library when trying to make a map from COVID-19 datasets and realized that there is no way to refer to a piece of land in a short and unique way. 

When someone refers to "Italy", does it include Sardinia? What about Sicily? Is it fun to parse "Korea, South"?

Country Level ID was developed to have a standard way of referring to all kind of administrative areas down to state / province / county level in all countries.



### Examples

**[id0:IT](export/geojson/id0/it.geojson)** refers to Italy including islands.

![id0_it](docs/id0_it.png)

**[id2:ITX](export/geojson/id2/itx.geojson)** refers to mainland Italy.

![id2_itx](docs/id2_itx.png)

**id3:US-CA** refers to the state of California, USA.





**[id0:GG+id0:JE](docs/channel_islands.geojson)** refers to Channel Islands.



### Reference

Country Level IDs start with one of `id0:` `id1:` `id2:` `id3:` + a code.

id0, id1, id2's code has 2 or 3 uppercase letters (ISO codes).

id3's code is the country's id0 ISO code + a dash `-`  + 1-3 letters or numbers.

As a special case, about 1% of id3 has an underscore + number postfix, to avoid duplicates. For example 

- **id3:AU-NSW_1159313299** refers to New South Wales, Australia while
- **id3:AU-NSW_1159313269** refers to Lord Howe Island.

id0, id1, id2 have a tree-like hierarchy. You can see it in [id012.json](export/id/id012.json)

id3 contains states / provinces / counties, one layer for each country.

[id012.json](export/id/id012.json) contains population estimates from the Natural Earth dataset, as well as the source's ne_id.

The source data for each level in the Natural Earth dataset:

- id0: Admin 0 – Countries
- id1: Admin 0 - Map Units
- id2: Admin 0 - Map Subunits
- id3: Admin 1- States, Provinces



#### Combining codes

Some areas might not be described with a simple code. For example, Channel Islands doesn't have a matching polygon in the NE dataset. These cases can be described using the plus `+` sign. 

For example **[id0:GG+id0:JE](docs/channel_islands.geojson)** refers to Channel Islands.



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



---

The map screenshots [© Mapbox](https://www.mapbox.com/about/maps/) [© OpenStreetMap](http://www.openstreetmap.org/copyright)

