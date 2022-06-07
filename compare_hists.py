from iskay import paramTools
from iskay import catalogTools

pars1 = paramTools.params('params_lum_gt_06p1_bs_dt.ini')
pars2 = paramTools.params('../20220519_DR6_SDSS/params_lum_gt_06p1_bs_dt.ini')

df1 = catalogTools.preProcessedCat(howMany=None,
                                   query=pars1.CAT_QUERY).df
df2 = catalogTools.preProcessedCat(howMany=None,
                                   query=pars2.CAT_QUERY).df
