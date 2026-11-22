import os

TEXT = (
    "Late light falls through the kitchen window and rests on the table in "
    "a warm square. Your hands hold a chipped blue mug, its steam rising "
    "slow. Outside, someone sweeps the step — brush, pause, brush. For "
    "now, nothing else needs doing."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
