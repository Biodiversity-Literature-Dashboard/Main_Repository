# Instructions and Documentation of the Creation of the Map Files

## The Data

The `master_countries.csv` and `small_countries.csv` files were compiled from public sources, and a list of Plotly countries and their ISO codes. There is a chance they are not perfect, but they seem to work for now. 

The marine borders data is the Flanders Marine Institute (2023), Maritime Boundaries Geodatabase, v12 -dataset. The source is cited and linked under the map. [Link to the Dataset](https://doi.org/10.14284/632)

## Creating the `eez_v12.json` File for the Marine Layer

1. From the dataset the following files were used `eez_v12.dbf`, `eez_v12.prj`, `eez_v12.shp`, and `eez_v12.shx`.
2. These files were taken to [mapshaper.org](mapshaper.org).
3. In the console the command `dissolve SOVEREIGN1` was run to merge different areas belonging to one country together. This should return `[dissolve] Dissolved 285 features into 157 features`. Alternatively, the command `dissolve ISO_SOV1` could be run, but doing so means the maps.py file would also need to be edited to use ISO data instead of country names. The `master_countries.csv` file should be ready to accomodate this, if needed.
4. In the simplify options the `prevent shape removal` should be ticked before applying the simplification.
5. After applying the simplification, it would be good to set it to a lower percent. 5-1% was still too detailed, so something closer to 0.1% is probably the best compromise between file size (and in turn loading time of the app,) and the quality of the shapes. However, this percentage can be tweaked and tested for a more optimal value.
6. This file can be then exported as a `GeoJSON` file, named `eez_v12.json`, and put into the same folder as the `maps.py` file.
