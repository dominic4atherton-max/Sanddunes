import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm


def plot_dune(dune_map, title="Dune height", figsize=(6, 6), show=True):
    """
    Plot a 2D dune/sand array with discrete colours.
    Default mapping: 0 white, 1 green, 2 yellow, 3 orange, 4 red.
    """

    cmap = ListedColormap(["white", "green", "yellow", "orange", "red"])
    norm = BoundaryNorm([-0.5, 0.5, 1.5, 2.5, 3.5, 4.5], cmap.N)

    plt.figure(figsize=figsize)
    plt.imshow(dune_map, cmap=cmap, norm=norm, interpolation="nearest")
    plt.axis("off")
    plt.title(title)

    if show:
        plt.show()
