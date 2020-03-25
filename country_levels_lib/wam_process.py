import shutil

from country_levels_lib.config import geojson_dir, export_dir
from country_levels_lib.utils import read_json, osm_url, write_json
from country_levels_lib.wam_download import wam_data_dir
from country_levels_lib.wam_iso import validate_iso1, validate_iso2

wam_geojson_simp_dir = geojson_dir / 'wam' / 'simp'


def process_geojson_wam():
    shutil.rmtree(export_dir / 'iso1', ignore_errors=True)
    shutil.rmtree(export_dir / 'iso2', ignore_errors=True)

    for simp in [5, 7, 8]:
        split_geojson(1, simp, debug=False, write_json_file=simp == 5)
        split_geojson(2, simp, debug=False, write_json_file=simp == 5)


def split_geojson(iso_level: int, simp_level, *, debug=False, write_json_file=False):
    assert iso_level in [1, 2]

    print(f'Splitting iso{iso_level} to level: q{simp_level}')
    file_path = wam_geojson_simp_dir / f'iso{iso_level}-{simp_level}.geojson'

    features = read_json(file_path)['features']
    features_sorted = sorted(features, key=lambda i: i['properties']['admin_level'])

    level_subdir = export_dir / f'iso{iso_level}' / f'q{simp_level}'
    level_subdir.mkdir(parents=True)

    population_map = read_json(wam_data_dir / 'population.json')

    json_data = dict()
    seen = dict()

    for feature in features_sorted:
        prop = feature['properties']

        name = prop['name']
        osm_id = int(prop['id'])
        iso = prop[f'iso{iso_level}']
        admin_level = int(prop['admin_level'])
        wikidata_id = prop.get('wikidata_id')
        countrylevel_id = f'iso{iso_level}:{iso}'
        population = population_map.get(wikidata_id)

        prop['countrylevel_id'] = countrylevel_id
        prop['population'] = population
        prop['admin_level'] = admin_level
        prop['osm_id'] = osm_id

        seen.setdefault(iso, list())
        if seen[iso] and not debug:
            # print(f'  duplicate {iso}, skipping')
            continue

        data = {
            'name': name,
            'admin_level': admin_level,
            'osm_id': osm_id,
            'wikidata_id': wikidata_id,
            'countrylevel_id': countrylevel_id,
            'population': population,
            f'iso{iso_level}': iso,
        }

        seen[iso].append(data)
        json_data[iso] = data

        if iso_level == 1:
            if not validate_iso1(iso):
                print(f'invalid iso1: {iso}')
                continue
            write_json(level_subdir / f'{iso}.geojson', feature)
        else:
            if not validate_iso2(iso):
                print(f'invalid iso2: {iso}')
                continue
            iso2_start, iso2_end = iso.split('-')
            iso2_subdir = level_subdir / iso2_start
            iso2_subdir.mkdir(exist_ok=True)
            write_json(level_subdir / iso2_start / f'{iso}.geojson', feature)

    if write_json_file:
        write_json(export_dir / f'iso{iso_level}.json', json_data, indent=2, sort_keys=True)

    #
    #
    if debug:  # debug duplicates, fixed by sorting by admin_level
        debug_dir = geojson_dir / 'wam' / 'debug' / f'iso{iso_level}'
        shutil.rmtree(debug_dir, ignore_errors=True)
        debug_dir.mkdir(parents=True)

        # choose lowest admin level from available ones
        for iso, iso_matches in seen.items():
            if len(iso_matches) != 1:
                matches_sorted = sorted(iso_matches, key=lambda i: i['admin_level'])

                print(f'duplicate iso{iso_level}: {iso}')
                for match in matches_sorted:
                    name = match['name']
                    osm_id = match['osm_id']
                    url = osm_url(osm_id)
                    admin_level = match['admin_level']
                    print(f'  {name} {admin_level} {url}')

                    # file_path = debug_dir / f'{iso} {admin_level} {osm_id}.geojson'
                    # write_json(file_path, match)
