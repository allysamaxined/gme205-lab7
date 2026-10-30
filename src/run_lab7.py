
import json
from pathlib import Path

from database import check_connection, fetch_parcels_by_land_use
from spatial import Parcel
from exchange import build_feature_collection, validate_feature_collection

OUTPUT_PATH = Path("output/residential_parcels.geojson")


def main():
    # 1. Check database connection
    if not check_connection():
        return

    # 2. Retrieve database rows
    rows = fetch_parcels_by_land_use("Residential")

    print("Rows returned:", len(rows))

    if rows:
        print("First database row:", rows[0])

    # 3. Convert rows to Parcel objects
    parcels = [
        Parcel.from_row(row)
        for row in rows
    ]

    print("Parcel objects created:", len(parcels))

    if parcels:
        first = parcels[0]
        print(
            "First Parcel object:",
            first.parcel_id,
            first.land_use,
        )

    # 4. Build GeoJSON FeatureCollection
    collection = build_feature_collection(parcels)

    print("GeoJSON type:", collection["type"])
    print("Feature count:", len(collection["features"]))

    if collection["features"]:
        print(
            "First feature:",
            json.dumps(collection["features"][0], indent=2)
        )

    # 5. Validate GeoJSON
    validate_feature_collection(collection)
    print("GeoJSON contract check: PASSED")

    # 6. Save GeoJSON file
    OUTPUT_PATH.parent.mkdir(exist_ok=True)

    OUTPUT_PATH.write_text(
        json.dumps(collection, indent=2),
        encoding="utf-8",
    )

    print("Output written:", OUTPUT_PATH)
    print("File exists:", OUTPUT_PATH.exists())


if __name__ == "__main__":
    main()
