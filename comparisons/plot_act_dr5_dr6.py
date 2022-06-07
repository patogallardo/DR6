from iskay import JK
import matplotlib.pyplot as plt


fnames_gt6p1 = ['/home/pag227/iskay_runs/20220526_DR6_SDSS_widerCoverage_outliercut/results_bsdt/DR6_SDSS_WIDERAREA_lum_gt_06p1_bs_dt.pck',  # noqa
                '/home/pag227/iskay_runs/20220519_DR6_SDSS/results_bsdt/DR6_SDSS_lum_gt_06p1_bs_dt.pck',  # noqa
                '/home/pag227/iskay_runs/202012_S18_coadd_150GHz/results_bsdt/S18_coadd_150GHz_V20DR15_V3_lum_gt_06p1_bs_dt.pck']  # noqa

fnames_gt7p9 = ['/home/pag227/iskay_runs/20220526_DR6_SDSS_widerCoverage_outliercut/results_bsdt/DR6_SDSS_WIDERAREA_lum_gt_07p9_bs_dt.pck',  # noqa
                '/home/pag227/iskay_runs/20220519_DR6_SDSS/results_bsdt/DR6_SDSS_lum_gt_07p9_bs_dt.pck',  # noqa
                '/home/pag227/iskay_runs/202012_S18_coadd_150GHz/results_bsdt/S18_coadd_150GHz_V20DR15_V3_lum_gt_07p9_bs_dt.pck']  # noqa

fnames_gt4p3 = ['/home/pag227/iskay_runs/20220526_DR6_SDSS_widerCoverage_outliercut/results_bsdt/DR6_SDSS_WIDERAREA_lum_gt_04p3_bs_dt.pck',  # noqa
                '/home/pag227/iskay_runs/20220519_DR6_SDSS/results_bsdt/DR6_SDSS_lum_gt_04p3_bs_dt.pck',  # noqa
                '/home/pag227/iskay_runs/202012_S18_coadd_150GHz/results_bsdt/S18_coadd_150GHz_V20DR15_V3_lum_gt_04p3_bs_dt.pck']  # noqa


colors = ['tab:orange', 'tab:red', 'tab:blue', 'tab:cyan']

labels = ['DR6 wide', 'DR6 C21 cat', 'DR5 C21 cat']
show = False


def plot_cats(fnames, colors, labels, plotname, show):

    plt.figure(figsize=[8, 4.5])
    for j, fname in enumerate(fnames):
        jk = JK.load_JK(fname)
        plt.errorbar(x=jk.rsep + 2*j,
                     y=jk.kSZ_curveFullDataset,
                     yerr=jk.errorbars,
                     label=labels[j] + "N:%i" % jk.N_objects_in_this_run,
                     marker='o',
                     ls='',
                     color=colors[j])
    plt.axhline(0, color='black')
    plt.legend()
    plt.ylim([-0.25, 0.2])
    plt.title(plotname)
    if show:
        plt.show()
    else:
        plt.savefig('compare_ksz_DR6_%s.pdf' % plotname)
        plt.savefig('compare_ksz_DR6_%s.png' % plotname)
        plt.close()

    plt.figure()
    for j, fname in enumerate(fnames):
        jk = JK.load_JK(fname)
        plt.scatter(jk.rsep + 2*j,
                    jk.errorbars,
                    label=labels[j])
    plt.title(plotname)
    plt.legend()
    if show:
        plt.show()
    else:
        plt.savefig('errorbars_%s.pdf' % plotname)
        plt.savefig('errorbars_%s.png' % plotname)
        plt.close()

    plt.figure()
    jk_norm = JK.load_JK(fnames[2])
    for j, fname in enumerate(fnames):
        jk = JK.load_JK(fname)
        plt.scatter(jk.rsep + 2*j,
                    jk.errorbars/jk_norm.errorbars,
                    label=labels[j])
    plt.title(plotname)
    plt.legend()
    if show:
        plt.show()
    else:
        plt.savefig('errorbars_fraction_%s.pdf' % plotname)
        plt.savefig('errorbars_fraction_%s.png' % plotname)
        plt.close()


plot_cats(fnames_gt4p3, colors, labels, 'lum_gt_4p3', show=show)
plot_cats(fnames_gt6p1, colors, labels, 'lum_gt_6p1', show=show)
plot_cats(fnames_gt7p9, colors, labels, 'lum_gt_7p9', show=show)
