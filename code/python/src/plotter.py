from matplotlib import pyplot as plt, style


plot_file_location = lambda plot_file: f'../plots/{plot_file}.pdf'


plot_styles = ['-or', '-*b', '-k']


def plot_data(x_data, y_data, plot_file, plot_label):
    plt.style.use('science')

    plt.plot(x_data, y_data, '-or', linewidth=2,
             markersize=4, label=plot_label, markerfacecolor='black', markeredgecolor='black')
    plt.legend(loc='best')
    plt.tight_layout()
    plt.xlabel(r'I [$\hbar$]')
    plt.ylabel(r'E [MeV]')

    # save the bands to a local file
    plt.savefig(plot_file_location(plot_file), dpi=300, bbox_inches='tight')
    plt.close()


def plot_bands(bands, band_labels, plot_file):
    plt.style.use('science')

    idx = 0
    for band in bands:
        # unpack the bands into separate data sets
        x_data, y_data = band
        plt.plot(x_data, y_data, plot_styles[idx], label=band_labels[idx])
        idx = idx + 1

    plt.legend(loc='best')
    plt.tight_layout()
    plt.xlabel(r'I [$\hbar$]')
    plt.ylabel(r'E [MeV]')

    # save the bands to a local file
    plt.savefig(plot_file_location(plot_file), dpi=300, bbox_inches='tight')
    plt.close()


def main():
    plot_data([1, 2, 3], [1, 2, 3], 'test', 'test_data')


if __name__ == '__main__':
    main()
