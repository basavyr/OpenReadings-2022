from matplotlib import pyplot as plt


def plot_data(x_data, y_data, plotfile):
    plot_file_location = f'../plots/{plotfile}.pdf'

    plt.plot(x_data, y_data, '-or', linewidth=2, markersize=4, label='data')
    plt.legend(loc='best')
    plt.tight_layout()
    plt.savefig(plot_file_location, dpi=300, bbox_inches='tight')
    plt.close()


def main():
    plot_data([1, 2, 3], [1, 2, 3], 'test')


if __name__ == '__main__':
    main()
