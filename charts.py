"""Generate four sample charts in a 2x2 Matplotlib figure."""
from pathlib import Path
import matplotlib.pyplot as plt


def main():
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
    sales = [12, 18, 15, 24, 30]
    fig, axes = plt.subplots(2, 2, figsize=(11, 8))
    axes[0, 0].plot(months, sales, marker='o')
    axes[0, 0].set_title('Monthly Sales (Line)')
    axes[0, 1].bar(months, sales)
    axes[0, 1].set_title('Monthly Sales (Bar)')
    axes[1, 0].pie([40, 30, 20, 10], labels=['A', 'B', 'C', 'D'], autopct='%1.0f%%')
    axes[1, 0].set_title('Category Share (Pie)')
    axes[1, 1].scatter([1, 2, 3, 4, 5], [2, 5, 4, 8, 7])
    axes[1, 1].set_title('Sample Relationship (Scatter)')
    for ax in (axes[0, 0], axes[0, 1], axes[1, 1]):
        ax.grid(alpha=0.25)
    fig.tight_layout()
    output = Path(__file__).resolve().parent / 'charts.png'
    fig.savefig(output, dpi=150)
    print(f'Saved chart to {output}')
    plt.show()


if __name__ == '__main__':
    main()
