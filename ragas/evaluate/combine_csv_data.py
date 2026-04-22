import csv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
OUTPUT = BASE_DIR / "combined_data.csv"
FILES = [
    "sample-bgem3-samples-001-005.csv",
    "sample-bgem3-samples-006-010.csv",
    "sample-bgem3-samples-011-015.csv",
    "sample-bgem3-samples-016-020.csv",
    "sample-bgem3-samples-021-025.csv",
    "sample-bgem3-samples-026-030.csv",
    "sample-bgem3-samples-031-035.csv",
    "sample-bgem3-samples-036-040.csv",
    "sample-bgem3-samples-041-045.csv",
    "sample-bgem3-samples-046-050.csv",
    "sample-bgem3-samples-051-055.csv",
    "sample-bgem3-samples-056-059.csv",
    "sample-conv6-samples-001-005.csv",
    "sample-conv6-samples-006-010.csv",
    "sample-conv6-samples-011-015.csv",
    "sample-conv6-samples-016-020.csv",
    "sample-conv6-samples-021-025.csv",
    "sample-conv6-samples-026-030.csv",
    "sample-conv6-samples-031-035.csv",
    "sample-conv6-samples-036-036.csv",
    "sample-conv7-samples-001-005.csv",
    "sample-conv7-samples-006-010.csv",
    "sample-conv7-samples-011-015.csv",
    "sample-conv7-samples-016-020.csv",
    "sample-conv7-samples-021-025.csv",
    "sample-conv7-samples-026-030.csv",
    "sample-conv7-samples-031-035.csv",
]


def read_csv(path: Path):
    with path.open("r", newline="", encoding="utf-8-sig") as handle:
        reader = csv.reader(handle)
        header = next(reader)
        rows = list(reader)
    return header, rows


def combine():
    expected_header = None
    all_rows = []
    counts = []

    for name in FILES:
        path = BASE_DIR / name
        if not path.exists():
            raise FileNotFoundError(path)

        header, rows = read_csv(path)
        if expected_header is None:
            expected_header = header
        elif header != expected_header:
            raise ValueError(f"Header mismatch in {name}")

        all_rows.extend(rows)
        counts.append((name, len(rows)))

    with OUTPUT.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.writer(handle)
        writer.writerow(expected_header)
        writer.writerows(all_rows)

    return expected_header, counts, len(all_rows)


def verify(expected_header, expected_total):
    header, rows = read_csv(OUTPUT)
    if header != expected_header:
        raise ValueError("Output header mismatch")
    if len(rows) != expected_total:
        raise ValueError(f"Expected {expected_total} rows, got {len(rows)}")
    return rows


if __name__ == "__main__":
    header, counts, total = combine()
    rows = verify(header, total)
    print(f"created={OUTPUT}")
    print(f"files={len(counts)}")
    print(f"rows={len(rows)}")
    print(f"columns={len(header)}")
    print(f"first_source={rows[0][0] if rows else ''}")
    print(f"last_source={rows[-1][0] if rows else ''}")
    print("source_counts=" + "; ".join(f"{name}:{count}" for name, count in counts))
