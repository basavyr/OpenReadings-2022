from matplotlib import pyplot as plt, style


def plot_data(x_data, y_data, plotfile, plot_label):
    plot_file_location = f'../plots/{plotfile}.pdf'

    plt.style.use('science')

    plt.plot(x_data, y_data, '-or', linewidth=2,
             markersize=4, label=plot_label, markerfacecolor='black', markeredgecolor='black')
    plt.legend(loc='best')
    plt.tight_layout()
    plt.xlabel(r'I [$\hbar$]')
    plt.ylabel(r'E [MeV]')
    plt.savefig(plot_file_location, dpi=300, bbox_inches='tight')
    plt.close()


def main():
    plot_data([1, 2, 3], [1, 2, 3], 'test', 'test_data')


if __name__ == '__main__':
    main()
