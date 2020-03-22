# Country Level ID
Country Levels IDs are short codes based on the ISO country codes. They uniquely identify country polygons and smaller administrative regions.

This repository contains GeoJSONs for each areas, with up-to-date population information.

### [Country List](docs/country_list.md)

For example, **id0:IT** refers to Italy including islands.

![id0_it](docs/id0_it.png)

**id2:ITX** refers to mainland Italy

![id2_itx](docs/id2_itx.png)

**id3:US-CA** refers to the state of California, USA.

![id3_us-ca](docs/id3_us-ca.png)



### [Country List](docs/country_list.md)



### Why is it needed?

I developed this library when trying to make a map from COVID-19 datasets and realized that there is no way to refer to a piece of administrative region reliably.

When a dataset refers to "Italy", does it include Sicily? Is it fun to parse "Korea, South"?

Country Level ID was developed to have a reliable way of referring to all kinds of administrative regions around the world.



### Specs

Country Level IDs start with one of `id0:` `id1:` `id2:` `id3:` + a code.

id0, id1, id2's code has 2 or 3 uppercase letters (ISO codes).

id3's code is the country's id0 ISO code + a dash `-`  + 1-3 uppercase letters or numbers.

As a special case, about 1% of id3 has an underscore + number postfix, to avoid duplicates. For example

- **id3:AU-NSW** refers to New South Wales, Australia
- **id3:AU-NSW_1159313269** refers to Lord Howe Island.



id0, id1, id2 have a tree-like hierarchy. You can see that in [export/id/id012.json](export/id/id012.json).

Population data is included for id0, id1 and id2 levels.



id3 means states / provinces / counties, a single level for each country.

id3 jsons are split per country, you can find them in the [export/id/id3](export/id/id3) folder.



The source data for each level in the Natural Earth dataset is the following:

- id0: Admin 0 – Countries
- id1: Admin 0 - Map Units
- id2: Admin 0 - Map Subunits
- id3: Admin 1 - States, Provinces



#### Combining codes

Some areas might not be described with a simple ID. For example, Channel Islands doesn't have a matching polygon in the NE dataset. These special cases can be described using the plus `+` sign. You can combine as many IDs as needed.

For example **id0:GG+id0:JE** refers to the Channel Islands.

![](docs/channel_islands.png)

These combinations are not exported to this repository, you need to combine them with your own scripts.

### License

The source code of this project is under MIT License.

Natural Earth's data is in the public domain. You are free to use it in any way, including for personal, educational, and commercial purposes. Natural Earth's [Terms of Use](https://www.naturalearthdata.com/about/terms-of-use/).

Everything inside `export/` folder is in the public domain.

The map screenshots in this readme [© Mapbox](https://www.mapbox.com/about/maps/) [© OpenStreetMap](https://openstreetmap.org/about/).

### Development

If you would like to develop or contribute, you'll need Python 3.7+ and Node with yarn.

Steps:

1. run `source prepare_virtualenv.sh`
2. run `./process_all.sh`

If you have [direnv](https://direnv.net/) installed, the virtualenv will activate/deactivate automatically upon entering/exiting this project.



### [Country List](docs/country_list.md)

