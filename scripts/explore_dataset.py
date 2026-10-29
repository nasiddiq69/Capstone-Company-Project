import matplotlib.pyplot as plt
from datasets import load_dataset


def main() -> None:
    print("Loading the CardiacUDC annotated dataset...")
    dataset = load_dataset("MedOtter/CardiacUDC", "annotated", split="train")

    print("\nDataset loaded successfully!")
    print("Number of rows:", len(dataset))
    print("Column names:", dataset.column_names)

    sample = dataset[0]
    print("\nFirst record:")
    for column, value in sample.items():
        if column not in ("image", "mask"):
            print(f"{column}: {value}")

    print("\nImage size:", sample["image"].size)
    print("Mask size:", sample["mask"].size)

    figure, axes = plt.subplots(1, 2, figsize=(12, 5))
    axes[0].imshow(sample["image"], cmap="gray")
    axes[0].set_title("Heart Ultrasound Image")
    axes[0].axis("off")

    axes[1].imshow(sample["mask"])
    axes[1].set_title("Segmentation Mask")
    axes[1].axis("off")

    figure.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
