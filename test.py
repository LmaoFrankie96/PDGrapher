import anndata as ad
adata = ad.read_h5ad(r"D:\Ramish\PDFGrapher\data\ready.h5ad")
print(adata)
print(adata.obs.head())
print(adata.var.head())
print(adata.X.shape)
